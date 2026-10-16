"""Seiten-Modul: CAINE – https://www.caine-live.net/

Überwacht wird die Release-Kategorie des News-Blogs
(page6/files/category-release.html): Dort steht pro Release
"CAINE X.Y Codename released DD/Mon/YYYY" mit dem kompletten
Changelog im Blog-Body – neueste zuerst.

Zusätzlich:
- extract_changelog(): archiviert alle Release-Einträge als Markdown
  unter archive/caine_changelog.md.
- DOWNLOADS: ISO (~4,2 GB) + SHA256-Datei vom cfitaly-Mirror nach
  downloads/caine/. Der Mirror wird genutzt, weil caine-live.net eine
  unvollständige TLS-Zertifikatskette ausliefert; falls die Hauptseite
  auch betroffen ist: VERIFY_TLS = False setzen.
"""

import html
import re
from datetime import datetime

NAME = "CAINE"
URL = "https://www.caine-live.net/page6/files/category-release.html"
NOTES = "Download: https://www.caine-live.net/page5/page5.html"
SLUG = "caine"

# caine-live.net liefert zeitweise eine unvollständige Zertifikatskette
# (fehlendes Intermediate). Bei SSL-Fehlern auf False setzen:
VERIFY_TLS = True

CHANGELOG_URL = URL  # Release-Liste enthält die Changelog-Texte gleich mit

DOWNLOADS = [
    # Hash-Datei zuerst - sie verifiziert die ISO
    "https://cfitaly.net/caine/caine{version}_sha256.txt",
    # ~4,2 GB ISO - auskommentieren, falls nicht gewünscht:
    "https://cfitaly.net/caine/caine{version}.iso",
]

# Marker: "CAINE 14.0 Lightstream released <font...>24/Mar/2025 </font>"
_MARKER_RE = re.compile(
    r"<div>\s*CAINE\s+(\d+\.\d+)\s+([^<]*?)\s+released\s*"
    r"<font[^>]*>\s*(\d{1,2})/(\w{3})/(\d{4})",
    re.I,
)
_TAG_RE = re.compile(r"<[^>]+>")
_BR_RE = re.compile(r"<br\s*/?>", re.I)
_BLOCK_RE = re.compile(r"</(?:p|div|li|ul|ol|h[1-6])>", re.I)

_MONTHS = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05",
    "jun": "06", "jul": "07", "aug": "08", "sep": "09", "oct": "10",
    "nov": "11", "dec": "12",
}


def _iso_date(day: str, month: str, year: str) -> str:
    return f"{year}-{_MONTHS.get(month.lower(), '01')}-{int(day):02d}"


def _entries(text: str):
    """Alle Release-Marker + zugehöriger Body-Text (neueste zuerst)."""
    matches = list(_MARKER_RE.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        yield m, text[m.end():end]


def extract(text: str) -> str:
    """Neueste CAINE-Version (erster Release-Eintrag)."""
    match = _MARKER_RE.search(text)
    if not match:
        raise ValueError("Kein Release-Eintrag auf der CAINE-Seite gefunden")
    return match.group(1)


def extract_history(text: str) -> list[dict]:
    """Alle Releases [{version, date}, ...], neueste zuerst."""
    releases, seen = [], set()
    for m, _body in _entries(text):
        version = m.group(1)
        if version in seen:
            continue
        seen.add(version)
        releases.append({
            "version": version,
            "date": _iso_date(m.group(3), m.group(4), m.group(5)),
        })
    return releases


def _body_to_text(body: str) -> str:
    """Blog-Body-HTML -> lesbarer Fließtext mit Zeilenumbrüchen."""
    text = _BR_RE.sub("\n", body)
    text = _BLOCK_RE.sub("\n", text)
    text = _TAG_RE.sub("", text)
    text = html.unescape(text)
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines()]
    # Leerzeilen auf max. eine reduzieren
    out, blank = [], False
    for line in lines:
        if not line:
            if not blank:
                out.append("")
            blank = True
        else:
            out.append(line)
            blank = False
    return "\n".join(out).strip()


def extract_changelog(text: str) -> str:
    """Alle Release-Einträge -> Markdown-Changelog."""
    lines = []
    for m, body in _entries(text):
        version, codename = m.group(1), m.group(2).strip()
        date = _iso_date(m.group(3), m.group(4), m.group(5))
        title = f"## {version} {codename} – {date}".strip()
        lines += [title, "", _body_to_text(body), ""]
    return "\n".join(lines).strip()
