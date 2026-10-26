"""Seiten-Modul: GitLab – https://gitlab.com/gitlab-org/gitlab

Überwacht die drei neuesten Minor-Zweige (aktuell 19.5/19.4/19.3)
über die öffentliche Tags-API von gitlab.com. GitLab liefert Patches
jeweils für den aktuellen und die zwei vorherigen Minor-Zweige - der
kombinierte Vergleichswert '19.5=19.5.1;19.4=19.4.3;19.3=19.3.6'
meldet jedes neue Release, auch Backports auf ältere Zweige, und
löst EINE Benachrichtigung für alle Zweige aus (wie beim PHP-Modul).

Hinweis: die Releases-API von gitlab.com ist anonym gesperrt (403),
die Tags-API liefert aber Version + committed_date problemlos.

Historie: alle stabilen '-ee'-Tags mit Datum (RCs werden gefiltert).
Changelog: die Feature-Notes der Minor-Releases kommen aus dem
Atom-Feed docs.gitlab.com/releases/releases.xml; Patch-Releases
bekommen einen Verweis auf die Release-Posts. Archiv:
archive/gitlab_changelog.md.

Anzahl der überwachten Zweige in config.json überschreibbar:

  "site_options": { "gitlab": { "branches": 4 } }

Keine Downloads.
"""

import html as _html
import json
import re
import urllib.request
from pathlib import Path

NAME = "GitLab"
URL = ("https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab/"
       "repository/tags?per_page=100&order_by=updated&sort=desc")
NOTES = "Releases: https://docs.gitlab.com/releases/"
SLUG = "gitlab"
CHANGELOG_URL = "https://docs.gitlab.com/releases/"


def _options() -> dict:
    """site_options.gitlab aus config.json (optional)."""
    try:
        cfg = Path(__file__).resolve().parent.parent / "config.json"
        data = json.loads(cfg.read_text(encoding="utf-8"))
        return data.get("site_options", {}).get("gitlab", {})
    except Exception:
        return {}


_OPTS = _options()

# Anzahl der überwachten Minor-Zweige (GitLab patcht aktuell + 2 zurück).
BRANCHES = int(_OPTS.get("branches") or 3)

_UA = "NewsBot/1.18"
_FEED_URL = "https://docs.gitlab.com/releases/releases.xml"
_TAG_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)-ee$")   # '-rc…' fällt weg
_ENTRY_RE = re.compile(r"<entry>(.*?)</entry>", re.S)
_TITLE_RE = re.compile(r"<title[^>]*>\s*GitLab (\d+\.\d+) release notes")
_LINK_RE = re.compile(r'<link[^>]*href="([^"]+)"')
_UPDATED_RE = re.compile(r"<updated>([\d-]+)T")
_H3_RE = re.compile(r"<h3[^>]*>(.*?)</h3>", re.S)
_STRIP_RE = re.compile(r"<[^>]+>")
_HEAD_RE = re.compile(r"^## (\S+) – (\S+)", re.M)


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def _ver_key(version: str) -> tuple:
    return tuple(int(p) for p in version.split("."))


def _stable(text: str) -> list[dict]:
    """Stabile Tags des Tag-API-JSON: {version, date}, RCs gefiltert."""
    out = []
    for tag in json.loads(text):
        m = _TAG_RE.match(tag.get("name") or "")
        if not m:
            continue
        date = ((tag.get("commit") or {}).get("committed_date")
                or tag.get("created_at") or "")[:10] or None
        out.append({"version": m.group(0)[1:-3], "date": date})
    return out


def _latest_per_branch(stable: list[dict]) -> dict[tuple, str]:
    """Höchste Patch-Version je Minor-Zweig {(19, 5): '19.5.1'}."""
    latest = {}
    for r in stable:
        branch = _ver_key(r["version"])[:2]
        if branch not in latest or _ver_key(r["version"]) > _ver_key(latest[branch]):
            latest[branch] = r["version"]
    return latest


def extract(text: str) -> str:
    """Kombinierter Wert '19.5=19.5.1;19.4=19.4.3;19.3=19.3.6'."""
    latest = _latest_per_branch(_stable(text))
    if not latest:
        raise ValueError("Keine stabilen GitLab-Tags gefunden")
    top = sorted(latest, reverse=True)[:BRANCHES]
    return ";".join(f"{b[0]}.{b[1]}={latest[b]}" for b in top)


def extract_history(text: str) -> list[dict]:
    """Alle stabilen Tags, neueste Version zuerst."""
    return sorted(_stable(text),
                  key=lambda r: _ver_key(r["version"]), reverse=True)


def _release_notes() -> dict[str, dict]:
    """Minor-Release-Notes aus dem Atom-Feed:
    {'19.5': {'date', 'link', 'features': [...]}}."""
    notes = {}
    for entry in _ENTRY_RE.findall(_fetch(_FEED_URL)):
        m = _TITLE_RE.search(entry)
        if not m:
            continue
        link = _LINK_RE.search(entry)
        date = _UPDATED_RE.search(entry)
        content = (entry.split("<content", 1)[1].split(">", 1)[1]
                   .split("</content>", 1)[0]
                   if "<content" in entry else "")
        content = content.replace("<![CDATA[", "").replace("]]>", "")
        features = [_html.unescape(_STRIP_RE.sub("", h)).strip()
                    for h in _H3_RE.findall(content)]
        notes[m.group(1)] = {
            "date": date.group(1) if date else None,
            "link": link.group(1) if link else "",
            "features": [f for f in features if f],
        }
    return notes


def update_changelog(existing: str | None) -> str | None:
    """Archiv inkrementell: fehlende Versionen als Abschnitt
    '## <version> – <datum>' oben einfügen. Minor-Releases (X.Y.0)
    bekommen die Feature-Liste aus dem Release-Post, Patch-Releases
    einen Verweis auf die Release-Übersicht.
    Rückgabe: kompletter neuer Inhalt oder None (unverändert)."""
    stable = extract_history(_fetch(URL))
    notes = _release_notes()
    have = {m[0] for m in _HEAD_RE.findall(existing or "")}
    parts = [p.strip() for p in re.split(r"(?m)^(?=## )", existing or "")
             if p.strip()]
    new_sections = []
    for r in stable:
        version = r["version"]
        if version in have:
            continue
        branch = ".".join(version.split(".")[:2])
        note = notes.get(branch) or {}
        if version.endswith(".0") and note:
            body = "\n".join(f"- {f}" for f in note["features"])
            if note.get("link"):
                body += f"\n\nRelease Notes: {note['link']}"
        else:
            body = ("Patch-Release (Security-/Bugfixes) - Details: "
                    f"{CHANGELOG_URL} (Tag v{version}-ee)")
        new_sections.append(
            f"## {version} – {r['date'] or 'n/a'}\n\n{body}")
    if not new_sections:
        return None
    return "\n\n".join(new_sections + parts)
