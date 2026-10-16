"""Seiten-Modul: Ventoy – https://www.ventoy.net/en/download.html

Die Download-Seite enthält ein JavaScript-Array 'ReleaseList' mit allen
Versionen und Veröffentlichungsdaten. ReleaseList[0] ist die neueste.

Zusätzlich:
- CHANGELOG_URL + extract_changelog(): archiviert die komplette
  News-Seite (doc_news.html) als Markdown unter archive/.
- DOWNLOADS: lädt das Windows-ZIP der aktuellen Version nach
  downloads/ventoy/ herunter (weitere Templates bei Bedarf ergänzen).
"""

import html
import re

NAME = "Ventoy"
URL = "https://www.ventoy.net/en/download.html"
NOTES = "Download: https://sourceforge.net/projects/ventoy/files/"
SLUG = "ventoy"

CHANGELOG_URL = "https://www.ventoy.net/en/doc_news.html"

DOWNLOADS = [
    # Hash-Datei zuerst - sie verifiziert die nachfolgenden Downloads
    {"url": "https://sourceforge.net/projects/ventoy/files/v{version}/sha256.txt/download",
     "filename": "ventoy-{version}-sha256.txt"},
    "https://sourceforge.net/projects/ventoy/files/v{version}/ventoy-{version}-windows.zip/download",
    # Bei Bedarf weitere Pakete:
    # "https://sourceforge.net/projects/ventoy/files/v{version}/ventoy-{version}-linux.tar.gz/download",
    # "https://sourceforge.net/projects/ventoy/files/v{version}/ventoy-{version}-livecd.iso/download",
]

_ENTRY_RE = re.compile(
    r'"version"\s*:\s*"(\d+\.\d+\.\d+)"\s*,\s*"date"\s*:\s*"(\d{4}-\d{2}-\d{2})"'
)

_NEWS_RE = re.compile(
    r"<li class=[\"']news[\"']>\s*(\d{4}/\d{2}/\d{2})\s*---\s*([\d.]+)\s*release([^<]*)</li>"
    r"\s*</ul>\s*<ol class=[\"']LL[\"']>(.*?)</ol>",
    re.S,
)
_ITEM_RE = re.compile(r"<li class=[\"']N1[\"']>(.*?)</li>", re.S)
_TAG_RE = re.compile(r"<[^>]+>")
_BR_RE = re.compile(r"<br\s*/?>", re.I)


def extract(text: str) -> str:
    """Gibt die neueste Ventoy-Version zurück (erster ReleaseList-Eintrag)."""
    match = _ENTRY_RE.search(text)
    if not match:
        raise ValueError("Keine ReleaseList-Version auf der Ventoy-Seite gefunden")
    return match.group(1)


def extract_history(text: str) -> list[dict]:
    """Komplette Releaseliste [{version, date}, ...], neueste zuerst."""
    releases, seen = [], set()
    for version, date in _ENTRY_RE.findall(text):
        if version not in seen:
            seen.add(version)
            releases.append({"version": version, "date": date})
    return releases


def _clean_item(html_text: str) -> str:
    """HTML-Eintrag -> Fließtext (Tags raus, Entities auflösen)."""
    text = _BR_RE.sub(" ", html_text)
    text = _TAG_RE.sub(" ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def extract_changelog(text: str) -> str:
    """Ventoy-News-Seite -> Markdown-Changelog aller Versionen."""
    lines = []
    for date, version, extra, items_html in _NEWS_RE.findall(text):
        title = f"## {version} – {date.replace('/', '-')}"
        if extra.strip():
            title += f" ({extra.strip()})"
        lines += [title, ""]
        for item in _ITEM_RE.findall(items_html):
            lines.append(f"- {_clean_item(item)}")
        lines.append("")
    return "\n".join(lines).strip()
