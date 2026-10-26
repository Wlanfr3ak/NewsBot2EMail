"""Seiten-Modul: VeraCrypt – https://veracrypt.fr/

Überwacht das neueste stabile Release über die GitHub-Releases-API
(veracrypt/VeraCrypt, Tag = VeraCrypt_X.Y.Z) und lädt den
Windows-Installer sowie die sha256sum-Datei (Hash-Verifikation
beim Download) nach downloads/veracrypt/. Linux- (deb/rpm/
AppImage), macOS- (dmg) und Quell-Pakete werden nicht geladen;
.sig-Signaturen werden nicht geladen (die sha256sum-Datei
reicht zur Integritätsprüfung).

Historie + Changelog: die GitHub-Releases liefern tag_name,
published_at und den Changelog-Text (body) bereits als Markdown -
update_changelog() holt fehlende Abschnitte inkrementell nach
archive/veracrypt_changelog.md.
"""

import json
import re
import urllib.request

NAME = "VeraCrypt"
URL = ("https://api.github.com/repos/veracrypt/VeraCrypt/"
       "releases/latest")
NOTES = "Download: https://veracrypt.fr/en/Downloads.html"
SLUG = "veracrypt"
CHANGELOG_URL = "https://github.com/veracrypt/VeraCrypt/releases"

_UA = "NewsBot/1.22"
_RELEASES_API = ("https://api.github.com/repos/veracrypt/VeraCrypt/"
                 "releases?per_page=100")
_HEAD_RE = re.compile(r"^## (\S+) – (\S+)", re.M)
_TAG_RE = re.compile(r"^VeraCrypt_(.+)$")
# Hash-Datei muss VOR den Nutzdaten laden (Reihenfolge!), damit
# _verify_download die Prüfung direkt durchführen kann.
_SUM_RE = re.compile(r"^veracrypt-[\d.]+-sha256sum\.txt$")
# Windows-Installer: bevorzugt 'VeraCrypt Setup x.y.exe', sonst das
# portable exe. Keine .sig-Dateien.
_SETUP_RE = re.compile(r"^VeraCrypt Setup [\d.]+\.exe$")
_PORTABLE_RE = re.compile(r"^VeraCrypt\.Portable\.[\d.]+\.exe$")


def _github_releases() -> list[dict]:
    """Alle stabilen Releases (keine Drafts/Prereleases), neueste zuerst."""
    releases = []
    for page in (1, 2):
        req = urllib.request.Request(
            f"{_RELEASES_API}&page={page}",
            headers={"User-Agent": _UA,
                     "Accept": "application/vnd.github+json"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            rels = json.loads(resp.read().decode("utf-8", "replace"))
        if not rels:
            break
        releases.extend(
            r for r in rels
            if not r.get("draft") and not r.get("prerelease"))
        if len(rels) < 100:
            break
    return releases


def extract(text: str) -> str:
    """Latest-Release-JSON -> Versionsnummer (Tag 'VeraCrypt_X.Y.Z')."""
    tag = json.loads(text).get("tag_name", "")
    match = _TAG_RE.match(tag)
    if not match:
        raise ValueError(f"Kein VeraCrypt-Tag im Release-JSON: {tag!r}")
    return match.group(1)


def extract_history(text: str) -> list[dict]:
    """Alle stabilen GitHub-Releases mit Veröffentlichungsdatum."""
    out = []
    for r in _github_releases():
        m = _TAG_RE.match(r.get("tag_name") or "")
        if m:
            out.append({"version": m.group(1),
                        "date": (r.get("published_at") or "")[:10] or None})
    return out


def update_changelog(existing: str | None) -> str | None:
    """Archiv inkrementell: die Release-Bodies sind bereits Markdown
    und werden als Abschnitt '## <version> – <datum>' oben eingefügt.
    Rückgabe: kompletter neuer Inhalt oder None (unverändert)."""
    have = {m[0] for m in _HEAD_RE.findall(existing or "")}
    parts = [p.strip() for p in re.split(r"(?m)^(?=## )", existing or "")
             if p.strip()]
    new_sections = []
    for rel in _github_releases():
        m = _TAG_RE.match(rel.get("tag_name") or "")
        if not m or m.group(1) in have:
            continue
        date = (rel.get("published_at") or "")[:10] or "n/a"
        body = (rel.get("body") or "").strip() or "_Kein Changelog-Text._"
        new_sections.append(f"## {m.group(1)} – {date}\n\n{body}")
    if not new_sections:
        return None
    return "\n\n".join(new_sections + parts)


def list_downloads(text: str, have: set, target_dir) -> list[dict]:
    """Aus dem Release-JSON: sha256sum.txt (zuerst, fuer die
    Hash-Verifikation) + Windows-Installer (Setup bevorzugt, sonst
    Portable)."""
    assets = json.loads(text).get("assets") or []
    by_name = {a["name"]: a["browser_download_url"] for a in assets}
    items = []
    for name, url in by_name.items():
        if _SUM_RE.match(name) and name not in have:
            items.append({"url": url, "filename": name})
    setup = next((n for n in by_name if _SETUP_RE.match(n)), None)
    portable = next((n for n in by_name if _PORTABLE_RE.match(n)), None)
    installer = setup or portable
    if installer and installer not in have:
        items.append({"url": by_name[installer], "filename": installer})
    return items
