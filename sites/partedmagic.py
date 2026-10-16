"""Seiten-Modul: Parted Magic – https://partedmagic.com/news/

Die News-Seite enthält alle Release-Ankündigungen als
<h2>Parted Magic VERSION</h2>-Überschriften (neueste zuerst), mit
<h3>-Feature-Sektionen und Fließtext darunter. Parted Magic ist
kostenpflichtig – keine Downloads.

Versionsschema: 'YYYY_MM_DD[_N]' (alt) bzw. 'YY.MM[_N]' (neu ab 26.09).
"""

import html
import re

NAME = "Parted Magic"
URL = "https://partedmagic.com/news/"
NOTES = "Kauf/Download über Account: https://partedmagic.com/store/"
SLUG = "parted-magic"

CHANGELOG_URL = URL  # News-Seite enthält die Changelog-Texte gleich mit

_H2_RE = re.compile(r"<h2[^>]*>(.*?)</h2>", re.S)
_H3_RE = re.compile(r"<h3[^>]*>(.*?)</h3>", re.S)
_TAG_RE = re.compile(r"<[^>]+>")
_BR_RE = re.compile(r"<br\s*/?>", re.I)
_BLOCK_RE = re.compile(r"</(?:p|div|ul|ol|table|figure|blockquote)>", re.I)
_LI_RE = re.compile(r"<li[^>]*>", re.I)
_RELEASE_RE = re.compile(r"Parted Magic\s+([\d._]+)", re.I)

# Marker, ab denen nur noch Kommentare/Footer kommen
_CUTOFF_RE = re.compile(
    r'id="comments"|class="comment|Leave a Reply|<footer', re.I)


def _clean(html_text: str) -> str:
    text = _TAG_RE.sub("", html_text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def _release_date(version: str) -> str | None:
    """Leitet das Datum aus dem Versionsschema ab."""
    m = re.fullmatch(r"(\d{4})_(\d{2})_(\d{2})(?:_\d+)?", version)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.fullmatch(r"(\d{2})\.(\d{2})(?:_\d+)?", version)
    if m:
        return f"20{m.group(1)}-{m.group(2)}"
    return None


def _sections(text: str):
    """Alle <h2>-Abschnitte: (heading, version|None, body)."""
    matches = list(_H2_RE.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = _CUTOFF_RE.split(text[m.end():end], maxsplit=1)[0]
        heading = _clean(m.group(1))
        rel = _RELEASE_RE.search(heading)
        yield heading, rel.group(1) if rel else None, body


def extract(text: str) -> str:
    """Neueste Parted-Magic-Version (erste Release-Überschrift)."""
    for _heading, version, _body in _sections(text):
        if version:
            return version
    raise ValueError("Keine Release-Überschrift auf der News-Seite gefunden")


def extract_history(text: str) -> list[dict]:
    """Alle Releases [{version, date}, ...], neueste zuerst."""
    releases, seen = [], set()
    for _heading, version, _body in _sections(text):
        if version and version not in seen:
            seen.add(version)
            releases.append({"version": version,
                             "date": _release_date(version)})
    return releases


def _body_to_md(body: str) -> str:
    """Abschnitts-HTML -> Markdown-Fließtext (h3 -> ###, li -> -)."""
    body = _H3_RE.sub(lambda m: f"\n### {_clean(m.group(1))}\n", body)
    body = _LI_RE.sub("\n- ", body)
    body = _BR_RE.sub("\n", body)
    body = _BLOCK_RE.sub("\n", body)
    body = _TAG_RE.sub("", body)
    body = html.unescape(body)
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in body.splitlines()]
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
    """Alle News-Abschnitte -> Markdown (Releases + sonstige Meldungen)."""
    lines = []
    for heading, version, body in _sections(text):
        date = f" – {_release_date(version)}" if version else ""
        lines += [f"## {heading}{date}", "", _body_to_md(body), ""]
    return "\n".join(lines).strip()
