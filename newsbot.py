#!/usr/bin/env python3
"""
NewsBot - prüft Webseiten regelmäßig auf neue Versionen und sendet E-Mails.

Aufruf:
    python newsbot.py              Dauerschleife (Intervall aus config.json)
    python newsbot.py --once       Einmaliger Check (für cron/Aufgabenplanung)
    python newsbot.py --dry-run    Check ohne E-Mail und ohne State-Update
    python newsbot.py --test-mail  Test-E-Mail an die konfigurierte Adresse
    python newsbot.py --status     Zeigt überwachte Seiten und letzte Werte
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import logging
import os
import re
import shutil
import smtplib
import ssl
import sys
import threading
import time
import urllib.error
import urllib.request
import zipfile
import zlib
from datetime import datetime
from email.message import EmailMessage
from logging.handlers import RotatingFileHandler
from pathlib import Path

__version__ = "1.23.0"

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.json"
STATE_PATH = BASE_DIR / "state.json"
ENV_PATH = BASE_DIR / ".env"
LOG_PATH = BASE_DIR / "newsbot.log"
SITES_DIR = BASE_DIR / "sites"
HISTORY_DIR = BASE_DIR / "history"
ARCHIVE_DIR = BASE_DIR / "archive"
DOWNLOAD_DIR = BASE_DIR / "downloads"

log = logging.getLogger("newsbot")


# ---------------------------------------------------------------------------
# Konfiguration & Umgebung
# ---------------------------------------------------------------------------

def load_env_file(path: Path) -> None:
    """Lädt KEY=VALUE-Zeilen aus einer .env-Datei (überschreibt nichts)."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key.strip(), value)


def resolve_env(value):
    """Ersetzt Strings der Form 'env:VARIABLE' durch den Umgebungswert."""
    if isinstance(value, str) and value.startswith("env:"):
        env_value = os.environ.get(value[4:], "")
        if not env_value:
            log.warning("Umgebungsvariable %s ist nicht gesetzt!", value[4:])
        return env_value
    return value


def load_config(path: Path) -> dict:
    if not path.exists():
        sys.exit(
            f"Konfigurationsdatei fehlt: {path}\n"
            "Bitte config.example.json nach config.json kopieren und anpassen."
        )
    try:
        cfg = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(f"config.json ist kein gültiges JSON: {exc}")

    cfg.setdefault("check_interval_minutes", 60)
    cfg.setdefault("request_timeout_seconds", 30)
    cfg.setdefault("user_agent", f"NewsBot/{__version__}")
    cfg.setdefault("sites", [])
    return cfg


def slugify(name: str) -> str:
    """Macht aus einem Seitennamen einen dateitauglichen Slug."""
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "seite"


def load_site_modules() -> list[dict]:
    """Lädt alle Seiten-Module aus dem sites/-Verzeichnis.

    Jedes Modul definiert NAME und URL (Pflicht), optional METHOD,
    PATTERN, NOTES, SLUG sowie die Funktionen extract(text) und
    extract_history(text). Kaputte Module werden geloggt und übersprungen.
    """
    modules = []
    if not SITES_DIR.is_dir():
        return modules
    for path in sorted(SITES_DIR.glob("*.py")):
        if path.name.startswith("_"):
            continue
        try:
            spec = importlib.util.spec_from_file_location(f"newsbot_site_{path.stem}", path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
        except Exception as exc:
            log.error("Seiten-Modul %s konnte nicht geladen werden: %s", path.name, exc)
            continue
        if not getattr(mod, "NAME", None) or not getattr(mod, "URL", None):
            log.error("Seiten-Modul %s ohne NAME/URL - übersprungen.", path.name)
            continue
        modules.append({
            "name": mod.NAME,
            "url": mod.URL,
            "method": getattr(mod, "METHOD", "regex"),
            "pattern": getattr(mod, "PATTERN", None),
            "notes": getattr(mod, "NOTES", ""),
            "slug": getattr(mod, "SLUG", "") or slugify(mod.NAME),
            "extract": getattr(mod, "extract", None),
            "extract_history": getattr(mod, "extract_history", None),
            "changelog_url": getattr(mod, "CHANGELOG_URL", None),
            "extract_changelog": getattr(mod, "extract_changelog", None),
            "update_changelog": getattr(mod, "update_changelog", None),
            "downloads": list(getattr(mod, "DOWNLOADS", None) or []),
            "list_downloads": getattr(mod, "list_downloads", None),
            "verify_tls": getattr(mod, "VERIFY_TLS", True),
        })
    return modules


def collect_sites(cfg: dict) -> list[dict]:
    """Alle überwachten Seiten: config.json-Einträge + sites/-Module."""
    sites = []
    for site in cfg["sites"]:
        site = dict(site)
        site.setdefault("slug", slugify(site.get("name") or site.get("url", "")))
        sites.append(site)
    sites.extend(load_site_modules())
    if not sites:
        log.warning("Keine Seiten konfiguriert (config.json 'sites' und sites/-Module sind leer).")
    return sites


def load_state(path: Path) -> dict:
    if not path.exists():
        return {"sites": {}}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        log.warning("state.json beschädigt - starte mit leerem Zustand.")
        return {"sites": {}}


def save_state(path: Path, state: dict) -> None:
    path.write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# HTTP & Versionsermittlung
# ---------------------------------------------------------------------------

def _ssl_context(site: dict):
    """None = Standard-Verifikation; sonst unverifizierter Kontext
    (für Seiten mit unvollständiger Zertifikatskette)."""
    if site.get("verify_tls", True):
        return None
    return ssl._create_unverified_context()


def fetch(site: dict, cfg: dict, entry: dict):
    """Lädt eine Seite. Gibt (status, headers_klein, body_bytes) zurück.

    Sendet If-None-Match/If-Modified-Since mit, sofern bekannt - ein 304
    bedeutet 'keine Änderung' und spart die weitere Auswertung.
    """
    if not site.get("verify_tls", True):
        log.warning("TLS-Verifikation deaktiviert für %s", site["url"])
    headers = {
        "User-Agent": cfg["user_agent"],
        "Accept-Encoding": "gzip, deflate",
    }
    if entry.get("etag"):
        headers["If-None-Match"] = entry["etag"]
    if entry.get("last_modified"):
        headers["If-Modified-Since"] = entry["last_modified"]

    req = urllib.request.Request(site["url"], headers=headers)
    timeout = cfg["request_timeout_seconds"]
    context = _ssl_context(site)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=context) as resp:
            body = resp.read()
            hdrs = {k.lower(): v for k, v in resp.headers.items()}
            body = decompress_body(body, hdrs)
            return resp.status, hdrs, body
    except urllib.error.HTTPError as exc:
        if exc.code == 304:
            return 304, {k.lower(): v for k, v in exc.headers.items()}, b""
        raise


def decompress_body(body: bytes, headers: dict) -> bytes:
    """Dekomprimiert die Antwort anhand des Content-Encoding-Headers.

    Manche Server liefern gzip auch ohne angefragtes Accept-Encoding -
    urllib dekomprimiert nicht automatisch, daher hier manuell.
    """
    encoding = (headers.get("content-encoding") or "").lower()
    if "gzip" in encoding:
        return gzip.decompress(body)
    if "deflate" in encoding:
        try:
            return zlib.decompress(body)
        except zlib.error:
            # Manche Server schicken rohe Deflate-Daten ohne zlib-Header.
            return zlib.decompress(body, -zlib.MAX_WBITS)
    return body


def decode_body(body: bytes, headers: dict) -> str:
    content_type = headers.get("content-type", "")
    match = re.search(r"charset=([\w.-]+)", content_type)
    charset = match.group(1) if match else "utf-8"
    return body.decode(charset, errors="replace")


def extract_value(site: dict, headers: dict, body: bytes) -> str:
    """Ermittelt den Vergleichswert je nach Methode der Seite.

    extract : Falls das Seiten-Modul eine extract(text)-Funktion
              mitbringt, hat diese Vorrang vor allem anderen.
    regex   : site["pattern"] wird auf den Seitentext angewendet,
              Gruppe 1 (oder der gesamte Treffer) ist die Version.
    hash    : SHA-256 des kompletten Antwort-Bodys (jede Änderung zählt).
    etag    : ETag- bzw. Last-Modified-Header des Servers.
    """
    if callable(site.get("extract")):
        return site["extract"](decode_body(body, headers))
    method = site.get("method", "regex")
    if method == "regex":
        text = decode_body(body, headers)
        match = re.search(site["pattern"], text)
        if not match:
            raise ValueError(
                f"Pattern {site['pattern']!r} nicht auf {site['url']} gefunden"
            )
        return match.group(1) if match.groups() else match.group(0)
    if method == "hash":
        return hashlib.sha256(body).hexdigest()
    if method == "etag":
        return headers.get("etag") or headers.get("last-modified") or ""
    raise ValueError(f"Unbekannte Methode: {method!r}")


# ---------------------------------------------------------------------------
# Versionshistorie
# ---------------------------------------------------------------------------

def history_path(site: dict) -> Path:
    return HISTORY_DIR / f"{site['slug']}.md"


def init_history(site: dict, new_value: str, releases: list | None) -> None:
    """Legt die Historiendatei einer Seite an.

    Liefert das Modul extract_history(), werden alle bekannten Releases
    mit ihren echten Veröffentlichungsdaten eingetragen (Baseline).
    """
    HISTORY_DIR.mkdir(exist_ok=True)
    path = history_path(site)
    if path.exists():
        return
    today = datetime.now().strftime("%d.%m.%Y")
    lines = [
        f"# Versionshistorie: {site['name']}",
        "",
        f"Quelle: {site['url']}",
        f"Erstellt: {today}",
        "",
        "| Version | Veröffentlicht | Erkannt am | Anmerkung |",
        "|---------|----------------|------------|-----------|",
    ]
    if releases:
        for release in releases:
            version = release.get("version", "?")
            date = release.get("date") or "–"
            note = "Baseline" if version == new_value else ""
            lines.append(f"| {version} | {date} | {today} | {note} |")
    else:
        lines.append(f"| {new_value} | – | {today} | Baseline |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log.info("Historie angelegt: %s", path.name)


def append_history(site: dict, result: dict) -> None:
    """Trägt eine neu erkannte Version oben in die Historiendatei ein
    (neueste zuerst, konsistent zur Baseline-Reihenfolge)."""
    release_date = None
    for release in result.get("releases") or []:
        if release.get("version") == result["new"]:
            release_date = release.get("date")
            break
    today = datetime.now().strftime("%d.%m.%Y")
    path = history_path(site)
    if not path.exists():
        init_history(site, result["new"], result.get("releases"))
        return
    note = f"vorher: {result['old']}" if result.get("old") else ""
    row = f"| {result['new']} | {release_date or '–'} | {today} | {note} |"
    lines = path.read_text(encoding="utf-8").splitlines()
    # Direkt unter der Tabellen-Trennzeile einfügen; Fallback: ans Ende.
    for i, line in enumerate(lines):
        if line.startswith("|-"):
            lines.insert(i + 1, row)
            break
    else:
        lines.append(row)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log.info("Historie ergänzt: %s -> %s", path.name, result["new"])


# ---------------------------------------------------------------------------
# Modul-Hooks: Changelog-Archiv & Release-Downloads
# ---------------------------------------------------------------------------

def _archive_body(path: Path) -> str | None:
    """Inhalt eines Changelog-Archivs ohne Kopfzeile (None wenn nicht da)."""
    if not path.exists():
        return None
    old = path.read_text(encoding="utf-8")
    return old.partition("---\n\n")[2].rstrip("\n")


def update_changelog_archive(site: dict, cfg: dict) -> None:
    """Aktualisiert archive/<slug>_changelog.md.

    Zwei Modul-Varianten:
    - extract_changelog(text) + CHANGELOG_URL: NewsBot lädt die Seite,
      das Modul wandelt sie in Markdown um.
    - update_changelog(existing): Das Modul macht alle Requests selbst
      (für Quellen mit mehreren URLs). 'existing' ist der aktuelle
      Archiv-Inhalt ohne Kopf oder None; Rückgabe None = unverändert.

    Die Datei wird nur neu geschrieben, wenn sich der Inhalt geändert
    hat (der Stand-Zeitstempel im Kopf wird vom Vergleich ausgenommen).
    """
    ARCHIVE_DIR.mkdir(exist_ok=True)
    path = ARCHIVE_DIR / f"{site['slug']}_changelog.md"

    if callable(site.get("update_changelog")):
        content = site["update_changelog"](_archive_body(path))
        if content is None:
            return
    else:
        status, headers, body = fetch({"url": site["changelog_url"]}, cfg, {})
        if status == 304:
            return
        content = site["extract_changelog"](decode_body(body, headers))
        if not content:
            return
        if _archive_body(path) == content.rstrip("\n"):
            return

    header = (
        f"# Changelog: {site['name']}\n\n"
        f"Quelle: {site.get('changelog_url') or site['url']}\n"
        f"Stand: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n\n---\n\n"
    )
    path.write_text(header + content.rstrip("\n") + "\n", encoding="utf-8")
    log.info("Changelog-Archiv aktualisiert: %s", path.name)


def download_filename(url: str) -> str:
    """Dateiname aus einer URL; behandelt SourceForge-/download-Endungen."""
    parts = url.split("?")[0].rstrip("/").split("/")
    if parts[-1] == "download" and len(parts) > 1:
        return parts[-2]
    return parts[-1]


_HASH_LINE = re.compile(r"^([0-9a-fA-F]{32,128})\s+\*?(\S+)\s*$", re.M)
_HASH_ALGOS = {32: "md5", 40: "sha1", 64: "sha256", 128: "sha512"}
# Dateien, die Hash-Listen anderer Downloads enthalten
_CHECKSUM_NAME = re.compile(r"(?i)(sha\d|hash|checksum|sum)")


def _checksum_map(target_dir: Path) -> dict:
    """Dateiname -> erwarteter Hash, aus den Hash-Dateien im
    Download-Ordner (sha256sum.txt, SHA256SUMS, signed-hashes.txt,
    *.iso.sha256, *.isodata.json ...). Zeilen im Format
    '<hexhash>  <name>'; Pfade in Namen werden auf den Basename
    gekürzt. Pro Datei gewinnt der längste Hash (sha512 > md5)."""
    out = {}
    if not target_dir.is_dir():
        return out
    for p in target_dir.iterdir():
        if not p.is_file():
            continue
        if p.name.endswith(".isodata.json"):
            try:
                d = json.loads(p.read_text(encoding="utf-8"))
                if d.get("name") and d.get("sha256"):
                    out[d["name"]] = d["sha256"].lower()
            except Exception:
                pass
            continue
        if not _CHECKSUM_NAME.search(p.name):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for h, fn in _HASH_LINE.findall(text):
            fn = fn.rsplit("/", 1)[-1]   # 'v8.10/foo.zip' -> 'foo.zip'
            if fn not in out or len(h) > len(out[fn]):
                out[fn] = h.lower()
    return out


def _verify_download(site: dict, tmp: Path, url_name: str,
                     target_dir: Path) -> bool:
    """Prüft die geladene Datei gegen publizierte Hashes.

    True = ok oder kein Hash vorhanden; False = Mismatch (Datei wird
    verworfen und beim nächsten Lauf erneut geladen)."""
    expected = _checksum_map(target_dir).get(url_name)
    if not expected:
        return True
    algo = _HASH_ALGOS.get(len(expected), "sha256")
    digest = hashlib.new(algo)
    with tmp.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            digest.update(chunk)
    got = digest.hexdigest()
    if got != expected:
        log.error("%-30s HASH-MISMATCH bei %s (%s): erwartet %s, "
                  "bekommen %s - Download verworfen, Retry nächster "
                  "Lauf", site["name"], url_name, algo, expected, got)
        return False
    log.info("%-30s Hash verifiziert: %s (%s)", site["name"], url_name,
             algo)
    return True


def _download_one(site: dict, cfg: dict, url: str, target: Path,
                  unzip: bool = False) -> bool:
    """Lädt eine Datei herunter (Stream in .part-Datei, dann Rename).

    unzip=True: die geladene Zip wird nicht behalten - das erste
    .iso-Mitglied (sonst erstes Mitglied) wird als 'target'
    geschrieben, die Zip verworfen."""
    if target.exists():
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_name(target.name + ".part")
    out = target.with_name(target.name + ".out")
    try:
        log.info("%-30s lade %s herunter...", site["name"], target.name)
        req = urllib.request.Request(
            url, headers={"User-Agent": cfg["user_agent"]})
        with urllib.request.urlopen(
                req, timeout=cfg["request_timeout_seconds"],
                context=_ssl_context(site)) as resp:
            with tmp.open("wb") as f:
                shutil.copyfileobj(resp, f)
        # Gegen publizierte Hashes prüfen (vor dem Entpacken -
        # der Hash bezieht sich auf die Zip, nicht die ISO).
        if not _verify_download(site, tmp, download_filename(url),
                                target.parent):
            tmp.unlink(missing_ok=True)
            return False
        if unzip:
            with zipfile.ZipFile(tmp) as zf:
                names = [n for n in zf.namelist() if not n.endswith("/")]
                member = next(
                    (n for n in names if n.lower().endswith(".iso")),
                    names[0])
                with zf.open(member) as src, out.open("wb") as dst:
                    shutil.copyfileobj(src, dst)
            tmp.unlink()
            out.rename(target)
            log.info("%-30s entpackt: %s (%s, %.1f MB)",
                     site["name"], target.name, member,
                     target.stat().st_size / 1_000_000)
        else:
            tmp.rename(target)
            log.info("%-30s gespeichert: %s (%.1f MB)",
                     site["name"], target.name,
                     target.stat().st_size / 1_000_000)
        return True
    except Exception as exc:
        tmp.unlink(missing_ok=True)
        out.unlink(missing_ok=True)
        log.warning("Download %s fehlgeschlagen: %s", target.name, exc)
        return False


def _download_target(entry) -> tuple[str, bool, str | None]:
    """Normalisiert einen DOWNLOADS-Eintrag -> (url_template, unzip,
    filename|None). Strings sind einfache URL-Templates; Dicts können
    'unzip' (Zip nach dem Laden entpacken) und 'filename' setzen."""
    if isinstance(entry, dict):
        return entry["url"], bool(entry.get("unzip")), entry.get("filename")
    return entry, False, None


def download_releases(site: dict, cfg: dict, version: str) -> None:
    """Lädt die in DOWNLOADS definierten Dateien der aktuellen Version
    nach downloads/<slug>/ herunter. Vorhandene Dateien werden
    übersprungen - fehlende werden bei jedem Lauf nachgeladen."""
    target_dir = DOWNLOAD_DIR / site["slug"]
    for entry in site["downloads"]:
        template, unzip, filename = _download_target(entry)
        url = template.format(version=version)
        name = (filename or download_filename(url)).format(version=version)
        if unzip and name.lower().endswith(".zip"):
            name = name[:-4]  # Zip wird entpackt, Ziel ist der Inhalt
        _download_one(site, cfg, url, target_dir / name, unzip=unzip)


def run_dynamic_downloads(site: dict, cfg: dict, text: str) -> None:
    """Dynamische Download-Liste des Moduls abarbeiten.

    Das Modul bekommt den Seitentext, die Menge bereits vorhandener
    Dateinamen und das Zielverzeichnis; es liefert
    [{"url", "filename"}, ...] für fehlende Dateien zurück.
    """
    target_dir = DOWNLOAD_DIR / site["slug"]
    have = ({p.name for p in target_dir.iterdir()}
            if target_dir.is_dir() else set())
    items = site["list_downloads"](text, have, target_dir) or []
    for item in items:
        _download_one(site, cfg, item["url"], target_dir / item["filename"],
                      unzip=bool(item.get("unzip")))


def run_site_hooks(site: dict, cfg: dict, state: dict,
                   version: str | None = None,
                   text: str | None = None) -> None:
    """Optionale Seiten-Hooks nach erfolgreichem Check ausführen.

    'version' ist die aktuell gültige Version (bei frisch erkannten
    Änderungen die neue, sonst der gespeicherte Stand).
    'text' ist der Seiteninhalt, soweit beim Check schon geladen -
    Module mit list_downloads bekommen ihn sonst nachgeladen.
    """
    version = version or state["sites"].get(site["name"], {}).get("value")
    if not version:
        return
    if site.get("changelog_url") and callable(site.get("extract_changelog")) \
            or callable(site.get("update_changelog")):
        try:
            update_changelog_archive(site, cfg)
        except Exception as exc:
            log.warning("Changelog-Archiv für %s fehlgeschlagen: %s",
                        site["name"], exc)
    if site.get("downloads"):
        try:
            download_releases(site, cfg, version)
        except Exception as exc:
            log.warning("Downloads für %s fehlgeschlagen: %s", site["name"], exc)
    if callable(site.get("list_downloads")):
        try:
            if text is None:
                # Seite unverändert (304) oder kein Body da - für
                # Nachladen gelöschter Dateien trotzdem einmal holen.
                status, headers, body = fetch(site, cfg, {})
                if status != 304:
                    text = decode_body(body, headers)
            if text is not None:
                run_dynamic_downloads(site, cfg, text)
        except Exception as exc:
            log.warning("Dynamische Downloads für %s fehlgeschlagen: %s",
                        site["name"], exc)


# ---------------------------------------------------------------------------
# E-Mail
# ---------------------------------------------------------------------------

def send_email(cfg: dict, subject: str, body: str) -> None:
    mail = cfg.get("email")
    if not mail:
        raise RuntimeError("Kein 'email'-Abschnitt in config.json")

    recipients = mail.get("to", [])
    if isinstance(recipients, str):
        recipients = [recipients]
    if not recipients:
        raise RuntimeError("Keine Empfänger ('to') in config.json")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = resolve_env(mail.get("from", ""))
    msg["To"] = ", ".join(recipients)
    msg.set_content(body)

    host = resolve_env(mail.get("smtp_host", ""))
    port = int(mail.get("smtp_port", 465))
    user = resolve_env(mail.get("username", ""))
    password = resolve_env(mail.get("password", ""))
    context = ssl.create_default_context()

    if mail.get("use_ssl", True):
        with smtplib.SMTP_SSL(host, port, context=context, timeout=30) as smtp:
            if user:
                smtp.login(user, password)
            smtp.send_message(msg)
    else:
        with smtplib.SMTP(host, port, timeout=30) as smtp:
            if mail.get("use_starttls"):
                smtp.starttls(context=context)
            if user:
                smtp.login(user, password)
            smtp.send_message(msg)


def _released_on(c: dict) -> str:
    """Veröffentlichungsdatum der neuen Version(en) aus
    extract_history().

    Bei kombinierten Werten ('8.4=8.4.27;8.3=8.3.36;…') werden nur
    die Teilversionen gezeigt, die gegenüber 'old' neu sind - so ist
    klar, welcher Zweig gepatcht wurde. Ohne extract_history:
    'unbekannt'."""
    new = c.get("new") or ""
    old = c.get("old") or ""
    found = []
    for rel in c.get("releases") or []:
        version, date = rel.get("version"), rel.get("date")
        if not version or not date:
            continue
        if version in new and version not in old:
            found.append(date if version == new else f"{version}: {date}")
    return ", ".join(dict.fromkeys(found)) or "unbekannt"


def build_change_mail(changes: list[dict]) -> tuple[str, str]:
    if len(changes) == 1:
        c = changes[0]
        subject = f"[NewsBot] Neue Version: {c['site']['name']} -> {c['new']}"
    else:
        names = ", ".join(c["site"]["name"] for c in changes)
        subject = f"[NewsBot] {len(changes)} Änderungen: {names}"

    lines = [
        "NewsBot hat folgende Änderungen gefunden:",
        "",
    ]
    for c in changes:
        site = c["site"]
        lines += [
            f"  Seite:          {site['name']}",
            f"  URL:            {site['url']}",
            f"  Vorher:         {c['old'] or '(erster Check)'}",
            f"  Jetzt:          {c['new']}",
            f"  Veröffentlicht: {_released_on(c)}",
            f"  Erkannt:        {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}",
        ]
        if site.get("notes"):
            lines.append(f"  Hinweis:        {site['notes']}")
        lines.append("")
    lines += [
        "--",
        f"NewsBot v{__version__}",
        "https://github.com/Wlanfr3ak/NewsBot2EMail",
    ]
    return subject, "\n".join(lines)


# ---------------------------------------------------------------------------
# Check-Zyklus
# ---------------------------------------------------------------------------

def _extract_history(site: dict, text: str) -> list | None:
    """extract_history() des Moduls, fehlertolerant."""
    if callable(site.get("extract_history")):
        try:
            return site["extract_history"](text)
        except Exception as exc:
            log.warning("extract_history für %s fehlgeschlagen: %s",
                        site["name"], exc)
    return None


def check_site(site: dict, cfg: dict, state: dict) -> dict | None:
    """Prüft eine Seite.

    Rückgabe: None (unverändert) oder ein Ergebnis-Dict mit 'kind':
      baseline – erster Check, Referenzwert wurde gesetzt
      change   – neue Version erkannt
      retry    – Version bekannt, aber Benachrichtigung steht noch aus
    """
    name = site["name"]
    entry = state["sites"].setdefault(name, {})
    entry["last_checked"] = datetime.now().isoformat(timespec="seconds")

    status, headers, body = fetch(site, cfg, entry)
    if status == 304:
        log.info("%-30s unverändert (304)", name)
        return None

    if headers.get("etag"):
        entry["etag"] = headers["etag"]
    if headers.get("last-modified"):
        entry["last_modified"] = headers["last-modified"]

    new_value = extract_value(site, headers, body)
    old_value = entry.get("value")
    pending = entry.get("pending_value")

    if new_value == old_value:
        log.info("%-30s unverändert (%s)", name, new_value)
        return None

    text = decode_body(body, headers)

    if pending and new_value == pending:
        # Schon erkannt & in der Historie, aber die Mail steht noch aus.
        # 'releases' mitgeben, damit die Mail das Veröffentlichungsdatum
        # zeigen kann.
        log.info("%-30s Benachrichtigung ausstehend: %s", name, pending)
        return {"site": site, "old": old_value, "new": pending,
                "kind": "retry", "history_done": True,
                "releases": _extract_history(site, text), "text": text}

    releases = _extract_history(site, text)

    if old_value is None and pending is None:
        # Erster Check: Baseline setzen, keine Mail schicken.
        entry["value"] = new_value
        entry["last_changed"] = entry["last_checked"]
        log.info("%-30s Baseline gesetzt: %s", name, new_value)
        return {"site": site, "new": new_value, "text": text,
                "kind": "baseline", "releases": releases}

    log.info("%-30s ÄNDERUNG: %s -> %s", name, pending or old_value, new_value)
    return {"site": site, "old": pending or old_value, "new": new_value,
            "kind": "change", "releases": releases, "text": text}


def run_cycle(cfg: dict, dry_run: bool = False,
              only: str | None = None) -> None:
    state = load_state(STATE_PATH)
    changes = []

    sites = collect_sites(cfg)
    if only:
        sites = [s for s in sites
                 if s.get("slug") == only or s.get("name") == only]
        if not sites:
            log.warning("Manueller Check: Seite '%s' unbekannt.", only)
            return

    for site in sites:
        try:
            result = check_site(site, cfg, state)
        except Exception as exc:  # einzelne Seite darf den Lauf nicht stoppen
            log.error("Fehler bei %s: %s", site.get("name", site.get("url")), exc)
            continue
        if not result:
            if not dry_run:
                run_site_hooks(site, cfg, state)
            continue
        if result["kind"] == "baseline":
            if not dry_run:
                init_history(site, result["new"], result.get("releases"))
            else:
                print(f"[DRY-RUN] {site['name']}: Baseline {result['new']}")
        else:
            changes.append(result)
            # Historie wird bei Erkennung geschrieben - unabhängig davon,
            # ob die Benachrichtigungs-Mail klappt.
            if not dry_run and not result.get("history_done"):
                append_history(site, result)
        if not dry_run:
            # Bei frisch erkannter Version die neue, sonst den Stand laden.
            run_site_hooks(site, cfg, state,
                           version=result["new"], text=result.get("text"))

    if not changes:
        if not dry_run:
            save_state(STATE_PATH, state)
        log.info("Check abgeschlossen: keine Änderungen.")
        return

    if dry_run:
        for c in changes:
            print(f"[DRY-RUN] {c['site']['name']}: {c['old']} -> {c['new']}")
        return

    subject, body = build_change_mail(changes)
    try:
        send_email(cfg, subject, body)
    except Exception as exc:
        # Werte als 'pending' merken, damit die Mail beim nächsten
        # Lauf erneut versucht wird statt dauerhaft verloren zu gehen.
        for c in changes:
            state["sites"][c["site"]["name"]]["pending_value"] = c["new"]
        save_state(STATE_PATH, state)
        log.error("E-Mail-Versand fehlgeschlagen (%s) - Retry beim nächsten Lauf.", exc)
        return

    for c in changes:
        entry = state["sites"][c["site"]["name"]]
        entry["value"] = c["new"]
        entry.pop("pending_value", None)
        entry["last_changed"] = entry["last_checked"]
    save_state(STATE_PATH, state)
    log.info("Check abgeschlossen: %d Änderung(en), E-Mail versendet.", len(changes))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def print_status(cfg: dict) -> None:
    state = load_state(STATE_PATH)
    sites = collect_sites(cfg)
    print(f"NewsBot v{__version__} - {len(sites)} überwachte Seite(n)\n")
    for site in sites:
        entry = state["sites"].get(site["name"], {})
        hist = history_path(site)
        print(f"  {site['name']}")
        print(f"    URL:          {site['url']}")
        print(f"    Methode:      {'extract()' if callable(site.get('extract')) else site.get('method', 'regex')}")
        print(f"    Letzter Wert: {entry.get('value', '-')}")
        print(f"    Letzer Check: {entry.get('last_checked', '-')}")
        print(f"    Historie:     {hist if hist.exists() else '-'}")
        print()


def _run_web_check(cfg: dict, lock: threading.Lock,
                   slug: str | None = None) -> bool:
    """Manueller Check aus dem Web-Dashboard (--web-Modus).

    Läuft in einem Hintergrund-Thread; False, wenn schon ein Check
    läuft. 'slug' begrenzt den Check auf eine Seite (None = alle).
    Im Daemon-Modus stattdessen einfach das Wake-Event setzen.
    """
    if not lock.acquire(blocking=False):
        return False

    def _bg():
        try:
            run_cycle(cfg, only=slug)
        except Exception as exc:
            log.error("Manueller Check fehlgeschlagen: %s", exc)
        finally:
            lock.release()

    threading.Thread(target=_bg, daemon=True).start()
    return True


def main() -> None:
    # UTF-8-Ausgabe erzwingen (Windows-Konsole nutzt sonst cp850/cp1252).
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

    parser = argparse.ArgumentParser(
        description="NewsBot - überwacht Webseiten auf neue Versionen."
    )
    parser.add_argument("--once", action="store_true",
                        help="einmaliger Check, dann beenden")
    parser.add_argument("--dry-run", action="store_true",
                        help="prüfen ohne E-Mail und ohne State-Update")
    parser.add_argument("--test-mail", action="store_true",
                        help="Test-E-Mail senden und beenden")
    parser.add_argument("--status", action="store_true",
                        help="Status der überwachten Seiten anzeigen")
    parser.add_argument("--web", action="store_true",
                        help="nur das Web-Dashboard starten (keine Checks)")
    parser.add_argument("--config", type=Path, default=CONFIG_PATH,
                        help="Pfad zur Konfigurationsdatei")
    parser.add_argument("--version", action="version",
                        version=f"NewsBot {__version__}")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-7s %(message)s",
        handlers=[
            logging.StreamHandler(),
            RotatingFileHandler(LOG_PATH, maxBytes=1_000_000,
                                backupCount=3, encoding="utf-8"),
        ],
    )

    load_env_file(ENV_PATH)
    cfg = load_config(args.config)
    cfg["_version"] = __version__   # fürs Web-Dashboard

    if args.status:
        print_status(cfg)
        return

    if args.test_mail:
        try:
            send_email(
                cfg,
                f"[NewsBot] Testmail v{__version__}",
                "Die E-Mail-Konfiguration funktioniert.\n",
            )
        except Exception as exc:
            sys.exit(f"Test-E-Mail fehlgeschlagen: {exc}")
        print("Test-E-Mail wurde versendet.")
        return

    if args.once or args.dry_run:
        run_cycle(cfg, dry_run=args.dry_run)
        return

    if args.web:
        # Nur das Dashboard ohne Check-Schleife; 'Jetzt prüfen'
        # startet einen Check im Hintergrund-Thread.
        import webui
        lock = threading.Lock()
        webui.start(cfg, collect_sites,
                    lambda slug=None: _run_web_check(cfg, lock, slug))
        print(f"Web-Dashboard läuft (Beenden mit Strg+C).")
        try:
            while True:
                time.sleep(3600)
        except KeyboardInterrupt:
            pass
        return

    interval = max(1, int(cfg["check_interval_minutes"])) * 60
    wake = threading.Event()
    pending = []   # vom Web-Dashboard angeforderte Checks (None = alle)

    def _queue_check(slug: str | None = None) -> bool:
        pending.append(slug)
        wake.set()
        return True

    if (cfg.get("web") or {}).get("enabled", True):
        try:
            import webui
            webui.start(cfg, collect_sites, _queue_check)
        except Exception as exc:
            log.error("Web-Dashboard konnte nicht gestartet werden: %s", exc)
    log.info("NewsBot v%s gestartet - Intervall: %d min", __version__, interval // 60)

    # Schleife: wartet bis 'next_due' (Regel-Check) oder bis das
    # Dashboard einen Check anfordert ('pending'). Manuelle Checks
    # verändern den Regel-Zeitplan nicht.
    next_due = 0.0
    while True:
        remaining = next_due - time.monotonic()
        if not pending and remaining > 0:
            try:
                wake.wait(remaining)
                wake.clear()
            except KeyboardInterrupt:
                log.info("Beendet durch Benutzer.")
                break
            continue
        try:
            if pending:
                run_cycle(cfg, only=pending.pop(0))
            else:
                run_cycle(cfg)
                next_due = time.monotonic() + interval
        except Exception as exc:
            log.error("Unerwarteter Fehler im Check-Zyklus: %s", exc)
            next_due = time.monotonic() + 60


if __name__ == "__main__":
    main()
