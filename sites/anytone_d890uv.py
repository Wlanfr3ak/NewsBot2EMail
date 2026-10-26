"""Seiten-Modul: Anytone AT-D890UV – Firmware & Zubehoer

Überwacht zwei Seiten gemeinsam:
- wouxun.us Kategorie 'AT-D890UV Firmware Updates' (Firmware-Zips
  V1.0x, NX-DMR-Varianten, Change-Log-PDFs, Anleitungen,
  Firmware-Update-Tool) - hier steht die eigentliche Versionsliste.
- anytone.net Produktseite / Download-Liste (data-open-download
  Eintraege mit file_url; D890UV-Treffer werden mitgeladen).

Vergleichswert: hoechste gefundene Firmware-Version ('1.05') aus
Dateinamen 'D890UV_V1.05.zip' / 'AT-D890UV-V1.03.zip' /
'FW-v1.05' ueber beide Seiten - ein neues Release loest eine
Mail aus.

Downloads (downloads/anytone-d890uv/): ALLE verlinkten Dateien
beider Seiten - Firmware, Change-Log-PDFs, Tools, Anleitungen
('alle weiteren Sachen'). Vorhandene Dateien werden uebersprungen.

Archiv (archive/anytone-d890uv_changelog.md): bei jeder Aenderung
der verlinkten Datei-/Version-Liste wird ein Snapshot-Abschnitt
'## Stand <datum> – <kurz-hash>' abgelegt - enthaelt die komplette
Linkliste UND den sichtbaren Seitentext (die 'Webseite selbst'
bleibt so archiviert erhalten).
"""

import html as _html
import json
import re
import urllib.request
from datetime import date
from pathlib import Path

NAME = "Anytone D890UV"
URL = "https://www.wouxun.us/category.php?category_id=112"
NOTES = ("Firmware: https://www.wouxun.us/category.php?category_id=112 "
         "| Produkt: https://www.anytone.net/"
         "multi-procotol-digital-and-analog-radio.html")
SLUG = "anytone-d890uv"
CHANGELOG_URL = URL

SOURCES = {
    URL: "wouxun",
    "https://www.anytone.net/download": "anytone",
    "https://www.anytone.net/"
    "multi-procotol-digital-and-analog-radio.html": "anytone-product",
}

_UA = "NewsBot/1.23"   # wouxun.us blockiert Browser-UAs (406), nicht NewsBot
_LINK_RE = re.compile(r'href="(https?://[^"]+|/[^"]+)"')
_FILE_URL_RE = re.compile(r'file_url="([^"]+)"')
_TITLE_RE = re.compile(r'<div class="title">([^<]+)</div>')
_TAG_RE = re.compile(r"<[^>]+>")
_SCRIPT_RE = re.compile(r"<(script|style)\b.*?</\1>", re.S | re.I)
_WS_RE = re.compile(r"\s+")
_VER_RE = re.compile(r"[Vv](?:er\.? ?)?(\d+\.\d+(?:\.\d+)?)")
_FW_FILE_RE = re.compile(
    r"(?:D890UV|D890)[^/]*?[Vv](\d+\.\d+(?:\.\d+)?)|"
    r"FW-v(\d+\.\d+(?:\.\d+)?)", re.I)
_FILE_EXT_RE = re.compile(
    r"\.(zip|rar|7z|exe|pdf|bin|dmg|apk|docx?|xlsx?)(\?|$)", re.I)
_HEAD_RE = re.compile(r"^## Stand (\S+) – ([0-9a-f]{8})", re.M)


def _options() -> dict:
    try:
        cfg = Path(__file__).resolve().parent.parent / "config.json"
        data = json.loads(cfg.read_text(encoding="utf-8"))
        return data.get("site_options", {}).get("anytone_d890uv", {})
    except Exception:
        return {}


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def _pages(text: str | None = None) -> dict[str, str]:
    """{quelle: html} - 'text' ist die bereits geladene URL-Seite."""
    return {src: (text if src == URL and text is not None else _fetch(src))
            for src in SOURCES}


def _links(url: str, page: str) -> list[str]:
    """Alle Datei-Links einer Seite (absolut, dedupliziert)."""
    out = []
    for href in _LINK_RE.findall(page) + _FILE_URL_RE.findall(page):
        if href.startswith("/"):
            host = url.split("/")[2]
            href = f"https://{host}{href}"
        if not _FILE_EXT_RE.search(href):
            continue
        if href not in out:
            out.append(href)
    return out


def _versions(links: list[str]) -> list[str]:
    """Firmware-Versionen aus Dateinamen (nur FW-/D890-Dateien)."""
    out = []
    for link in links:
        name = link.rsplit("/", 1)[-1]
        if "fw" not in name.lower() and "d890" not in name.lower():
            continue
        for m in _FW_FILE_RE.finditer(name):
            ver = m.group(1) or m.group(2)
            if ver and ver not in out:
                out.append(ver)
    return out


def _ver_key(v: str) -> tuple:
    return tuple(int(p) for p in v.split("."))


def _latest(text: str | None = None) -> str:
    """Hoechste Firmware-Version ueber alle Quellen."""
    best = None
    for url, page in _pages(text).items():
        for ver in _versions(_links(url, page)):
            if best is None or _ver_key(ver) > _ver_key(best):
                best = ver
    if not best:
        raise ValueError("Keine D890UV-Firmware-Version gefunden")
    return best


def extract(text: str) -> str:
    return _latest(text)


def extract_history(text: str) -> list[dict]:
    """Alle gefundenen FW-Versionen (kein echtes Datum vorhanden)."""
    versions = []
    for url, page in _pages(text).items():
        for ver in _versions(_links(url, page)):
            if ver not in versions:
                versions.append(ver)
    return [{"version": v, "date": None}
            for v in sorted(versions, key=_ver_key, reverse=True)]


def _snapshot(url: str, page: str) -> str:
    """Sichtbarer Text + Linkliste einer Seite (fuer das Archiv)."""
    body = _SCRIPT_RE.sub(" ", page)
    text = _html.unescape(_WS_RE.sub(" ", _TAG_RE.sub(" ", body))).strip()
    files = "\n".join(f"- {l}" for l in _links(url, page))
    return (f"### Datei-Links\n\n{files or '_keine_'}\n\n"
            f"### Seiten-Snapshot\n\n{text[:8000]}")


def _sig(url: str, page: str) -> str:
    """Kurz-Hash ueber die verlinkten Dateien + Versionen."""
    import hashlib
    raw = "\n".join(sorted(_links(url, page)))
    return hashlib.sha256(raw.encode()).hexdigest()[:8]


def update_changelog(existing: str | None) -> str | None:
    """Neuer Abschnitt '## Stand <datum> – <hash>', wenn sich die
    verlinkten Dateien einer Quelle geaendert haben; enthaelt
    Linkliste + Seiten-Snapshot ('Webseite selbst' im Archiv)."""
    have = {m[1] for m in _HEAD_RE.findall(existing or "")}
    parts = [p.strip() for p in re.split(r"(?m)^(?=## )", existing or "")
             if p.strip()]
    today = date.today().isoformat()
    new_sections = []
    for url, src in SOURCES.items():
        page = _fetch(url)
        sig = _sig(url, page)
        if sig in have:
            continue
        new_sections.append(
            f"## Stand {today} – {sig} ({src})\n\nQuelle: {url}\n\n"
            + _snapshot(url, page))
    if not new_sections:
        return None
    return "\n\n".join(new_sections + parts)


def list_downloads(text: str, have: set, target_dir) -> list[dict]:
    """Alle Datei-Links beider Seiten ('Firmwares und alle weiteren
    Sachen'); target_name = URL-Basename."""
    items = []
    for url, page in _pages(text).items():
        for link in _links(url, page):
            name = link.split("?")[0].rsplit("/", 1)[-1] or "datei"
            if name not in have:
                items.append({"url": link, "filename": name})
    return items
