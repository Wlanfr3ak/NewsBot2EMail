"""Seiten-Modul: Jellyfin Desktop – https://jellyfin.org/

Überwacht das neueste Release des Desktop-Clients (früher 'Jellyfin
Media Player', Repo jellyfin/jellyfin-desktop) über die
GitHub-Releases-API. Geladen wird nur die normale Windows-x64-.exe
(*-windows-x64.exe) - weder das '-legacy'-Build (alte Windows-
Versionen) noch x86, macOS oder Linux. Landet in
downloads/jellyfin-desktop/.

Die Asset-Namen werden aus dem Release-JSON gelesen statt hart
kodiert: das Projekt hat das Repo einmal umbenannt (media-player ->
desktop), künftige Assets könnten daher 'JellyfinDesktop-*.exe'
heißen - das Muster auf '-windows-x64.exe' deckt beides ab.

Historie + Changelog: GitHub-Releases (tag_name, published_at,
body als Markdown) -> archive/jellyfin-desktop_changelog.md.
"""

import json
import re
import urllib.request

NAME = "Jellyfin Desktop"
URL = ("https://api.github.com/repos/jellyfin/jellyfin-desktop/"
       "releases/latest")
NOTES = "Download: https://jellyfin.org/downloads/clients"
SLUG = "jellyfin-desktop"
CHANGELOG_URL = "https://github.com/jellyfin/jellyfin-desktop/releases"

_UA = "NewsBot/1.17"
_RELEASES_API = ("https://api.github.com/repos/jellyfin/"
                 "jellyfin-desktop/releases?per_page=100")
_HEAD_RE = re.compile(r"^## (\S+) – (\S+)", re.M)
# Normale Windows-Installer enden auf '-windows-x64.exe'; das
# Legacy-Build ('-windows-x64-legacy.exe') und x86 fallen raus.
_EXE_SUFFIX = "-windows-x64.exe"


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
    """Latest-Release-JSON -> Versionsnummer ohne führendes 'v'."""
    version = json.loads(text).get("tag_name", "").lstrip("v")
    if not version:
        raise ValueError("Kein tag_name im Release-JSON gefunden")
    return version


def extract_history(text: str) -> list[dict]:
    """Alle stabilen GitHub-Releases mit Veröffentlichungsdatum."""
    return [{"version": r["tag_name"].lstrip("v"),
             "date": (r.get("published_at") or "")[:10] or None}
            for r in _github_releases()]


def list_downloads(text: str, have: set, target_dir) -> list:
    """Normale Windows-x64-.exe des Releases (i. d. R. genau eine)."""
    items = []
    for asset in json.loads(text).get("assets", []):
        name = asset.get("name", "")
        if name.endswith(_EXE_SUFFIX) and name not in have:
            items.append({"url": asset["browser_download_url"],
                          "filename": name})
    return items


def update_changelog(existing: str | None) -> str | None:
    """Archiv inkrementell: die Release-Bodies sind bereits Markdown
    und werden als Abschnitt '## <version> – <datum>' oben eingefügt.
    Rückgabe: kompletter neuer Inhalt oder None (unverändert)."""
    have = {m[0] for m in _HEAD_RE.findall(existing or "")}
    parts = [p.strip() for p in re.split(r"(?m)^(?=## )", existing or "")
             if p.strip()]
    new_sections = []
    for rel in _github_releases():
        version = rel["tag_name"].lstrip("v")
        if version in have:
            continue
        date = (rel.get("published_at") or "")[:10] or "n/a"
        body = (rel.get("body") or "").strip() or "_Kein Changelog-Text._"
        new_sections.append(f"## {version} – {date}\n\n{body}")
    if not new_sections:
        return None
    return "\n\n".join(new_sections + parts)
