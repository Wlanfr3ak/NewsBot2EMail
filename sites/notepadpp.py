"""Seiten-Modul: Notepad++ – https://notepad-plus-plus.org/downloads/

Überwacht die aktuelle Version und lädt den x64-Installer
(npp.X.Y.Z.Installer.x64.exe) nach downloads/notepad-plus-plus/.

Historie: alle Versionen der Download-Übersicht; echte
Veröffentlichungsdaten kommen von der GitHub-Releases-API
(notepad-plus-plus/notepad-plus-plus, Tag = vX.Y.Z).

Changelog: die Änderungsliste steht jeweils auf der Versionsseite
/downloads/vX.Y.Z/ ('Release Date' + nummerierte Liste).
update_changelog() holt fehlende Abschnitte inkrementell nach
archive/notepad-plus-plus_changelog.md.
"""

import html as _html
import json
import re
import urllib.request

NAME = "Notepad++"
URL = "https://notepad-plus-plus.org/downloads/"
NOTES = "Download: https://notepad-plus-plus.org/downloads/"
SLUG = "notepad-plus-plus"
CHANGELOG_URL = URL

# Nur der x64-Installer (wie gewünscht); portable/arm64/x86 werden
# nicht geladen. ~5 MB pro Release.
DOWNLOADS = [
    # Hash-Datei zuerst - sie verifiziert den Installer
    "https://github.com/notepad-plus-plus/notepad-plus-plus/"
    "releases/download/v{version}/npp.{version}.checksums.sha256",
    "https://github.com/notepad-plus-plus/notepad-plus-plus/"
    "releases/download/v{version}/npp.{version}.Installer.x64.exe",
]

_UA = "NewsBot/1.10"
_GITHUB_API = ("https://api.github.com/repos/notepad-plus-plus/"
               "notepad-plus-plus/releases?per_page=100")
_CURRENT_RE = re.compile(r"Current Version\s*([\d.]+)")
_VLINK_RE = re.compile(r"/downloads/v([\d.]+)/")
_DATE_RE = re.compile(r"Release Date:\s*(\d{4}-\d{2}-\d{2})")
# Changelog-Block: <h3 id="notepad-v…">Titel</h3> gefolgt von <ol>.
# (Die Download-Listen davor stehen in <ul>, deren h3-IDs mit
# 'download-' beginnen.)
_CL_RE = re.compile(
    r'<h3[^>]*id="notepad[^"]*"[^>]*>((?:(?!</h3>).)*?)</h3>'
    r"\s*<ol>(.*?)</ol>", re.S)
_LI_RE = re.compile(r"<li>(.*?)</li>", re.S)
_A_RE = re.compile(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S)
_CODE_RE = re.compile(r"<code>(.*?)</code>", re.S)
_TAG_RE = re.compile(r"<[^>]+>")
_HEAD_RE = re.compile(r"^## (\S+) – (\S+)", re.M)
# '/downloads/v666/' ist ein Scherz-Eintrag in der Übersicht und
# liefert 404 - nicht jeden Lauf erneut versuchen.
_SKIP = {"666"}


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def _github_dates() -> dict[str, str]:
    """Tag-Version -> Veröffentlichungsdatum (YYYY-MM-DD).
    Bis zu 3 API-Seiten (ältere Releases liegen teils vor GitHub)."""
    dates = {}
    try:
        for page in (1, 2, 3):
            req = urllib.request.Request(
                f"{_GITHUB_API}&page={page}",
                headers={"User-Agent": _UA,
                         "Accept": "application/vnd.github+json"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                rels = json.loads(resp.read().decode("utf-8", "replace"))
            if not rels:
                break
            dates.update(
                {r["tag_name"].lstrip("v"): (r.get("published_at") or "")[:10]
                 for r in rels})
            if len(rels) < 100:
                break
    except Exception:
        pass
    return dates


def _versions(text: str) -> list[str]:
    """Alle Versionen der Übersicht, neueste zuerst, dedupliziert."""
    seen, out = set(), []
    for ver in _VLINK_RE.findall(text):
        if ver not in seen:
            seen.add(ver)
            out.append(ver)
    return out


def extract(text: str) -> str:
    match = _CURRENT_RE.search(text)
    if match:
        return match.group(1)
    versions = _versions(text)
    if not versions:
        raise ValueError("Keine Version gefunden")
    return versions[0]


def extract_history(text: str) -> list[dict]:
    """Alle gelisteten Versionen; Datum aus der GitHub-API, sonst n/a."""
    dates = _github_dates()
    return [{"version": ver, "date": dates.get(ver) or None}
            for ver in _versions(text)]


def _md(frag: str) -> str:
    """HTML-Fragment -> Markdown-Text (Links, Code, Entities)."""
    frag = _A_RE.sub(lambda m: f"[{_TAG_RE.sub('', m.group(2))}]"
                             f"({m.group(1)})", frag)
    frag = _CODE_RE.sub(r"`\1`", frag)
    return _html.unescape(_TAG_RE.sub("", frag)).strip()


def _changelog(version: str) -> tuple[str, str]:
    """(Datum, Markdown-Text) der Versionsseite /downloads/vX/."""
    page = _fetch(f"https://notepad-plus-plus.org/downloads/v{version}/")
    m = _DATE_RE.search(page)
    date = m.group(1) if m else "n/a"
    cl = _CL_RE.search(page)
    if not cl:
        return date, "_Keine Changelog-Liste auf der Seite._"
    title = _md(cl.group(1)).rstrip(":")
    items = [f"- {_md(li)}" for li in _LI_RE.findall(cl.group(2))]
    return date, f"**{title}**\n\n" + "\n".join(items)


def update_changelog(existing: str | None) -> str | None:
    """Archiv inkrementell: fehlende Versionsseiten holen und als
    Abschnitt '## <version> – <datum>' oben einfügen.
    Rückgabe: kompletter neuer Inhalt oder None (unverändert)."""
    have = {m[0] for m in _HEAD_RE.findall(existing or "")}
    parts = [p.strip() for p in re.split(r"(?m)^(?=## )", existing or "")
             if p.strip()]
    new_sections, changed = [], False
    for version in _versions(_fetch(URL)):
        if version in have or version in _SKIP:
            continue
        try:
            date, body = _changelog(version)
        except Exception:
            continue
        new_sections.append(f"## {version} – {date}\n\n{body}")
        changed = True
    if not changed:
        return None
    return "\n\n".join(new_sections + parts)
