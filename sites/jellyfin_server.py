"""Seiten-Modul: Jellyfin Server – https://jellyfin.org/

Überwacht das neueste stabile Release über die GitHub-Releases-API
(jellyfin/jellyfin, Tag = vX.Y) und lädt den Windows-x64-Installer
(jellyfin_X.Y_windows-x64.exe, ~200 MB) von repo.jellyfin.org nach
downloads/jellyfin-server/. Die portablen Zips und ARM64-Builds
werden nicht geladen.

Historie + Changelog: die GitHub-Releases liefern tag_name,
published_at und den Changelog-Text (body) bereits als Markdown -
update_changelog() holt fehlende Abschnitte inkrementell nach
archive/jellyfin-server_changelog.md.
"""

import json
import re
import urllib.request

NAME = "Jellyfin Server"
URL = "https://api.github.com/repos/jellyfin/jellyfin/releases/latest"
NOTES = "Download: https://jellyfin.org/downloads/server"
SLUG = "jellyfin-server"
CHANGELOG_URL = "https://github.com/jellyfin/jellyfin/releases"

# Nur der Windows-x64-Installer (wie gewünscht); Zip/ARM64 werden
# nicht geladen. Versionierter Pfad: /files/server/windows/stable/
# v<version>/amd64/. Es gibt keine Hash-Dateien auf dem Repo-Server.
DOWNLOADS = [
    "https://repo.jellyfin.org/files/server/windows/stable/"
    "v{version}/amd64/jellyfin_{version}_windows-x64.exe",
]

_UA = "NewsBot/1.17"
_RELEASES_API = ("https://api.github.com/repos/jellyfin/jellyfin/"
                 "releases?per_page=100")
_HEAD_RE = re.compile(r"^## (\S+) – (\S+)", re.M)


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
