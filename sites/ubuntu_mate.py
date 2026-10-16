"""Seiten-Modul: Ubuntu MATE – https://ubuntu-mate.org/download/

Überwacht beide angebotenen Releases kombiniert (Interim + LTS):
eine neue Version in einem der beiden Zweige löst eine Mail aus.
Keine Downloads (wie gewünscht).

extract_history() holt echte Veröffentlichungsdaten der
Point-Releases aus dem cdimage-Verzeichnis (Dateidatum des ISO).

update_changelog() archiviert die Release-Notes-Artikel des Blogs
(ubuntu-mate.org/blog/*-release-notes/) unter
archive/ubuntu-mate_changelog.md – für alle Versionen, nicht nur
die aktuellen. Für aktuelle Releases ohne Notes-Artikel (z. B.
25.10) wird ein kurzer Platzhalter-Abschnitt geschrieben.
"""

import gzip
import html
import re
import urllib.request

NAME = "Ubuntu MATE"
URL = "https://ubuntu-mate.org/download/"
NOTES = "Keine Downloads. Download: https://ubuntu-mate.org/download/"
SLUG = "ubuntu-mate"
CHANGELOG_URL = "https://ubuntu-mate.org/blog/"

_UA = "NewsBot/1.5"
_BLOG = "https://ubuntu-mate.org"

_ITEM_RE = re.compile(r'<div class="row release-item[^"]*">')
_VER_RE = re.compile(r"Ubuntu MATE\s+([\d.]+)\s*(LTS)?")
_CODENAME_RE = re.compile(r'release-codename">[^<]*?([A-Z][a-z]+\s+[A-Z][a-z]+)')
_LABEL_RE = re.compile(r'release-label[^>]*>([^<]+)<')
_NOTES_RE = re.compile(r'href="(/blog/ubuntu-mate-[\w-]+-release-notes/)"')
_ISO_RE = re.compile(
    r'href="(https://cdimage\.ubuntu\.com/[^"]+?-desktop-amd64\.iso)"')
_ISOROW_RE = re.compile(
    r'ubuntu-mate-([\d.]+)-desktop-amd64\.iso</a></td>'
    r'<td[^>]*>(\d{4}-\d{2}-\d{2})')
_HEAD_RE = re.compile(r"^## (\S+) – ", re.M)
_NOTESLINK_RE = re.compile(r'/blog/ubuntu-mate-([\w-]+)-release-notes/')
_TITLE_RE = re.compile(r'<h1 class="page-title">([^<]+)</h1>')
_DATE_RE = re.compile(r'post-date.*?(\d{4}-\d{2}-\d{2})', re.S)
_ARTICLE_RE = re.compile(r'<article[^>]*>(.*?)</article>', re.S)
_MONTHS = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5,
           "june": 6, "july": 7, "august": 8, "september": 9,
           "october": 10, "november": 11, "december": 12}


def _fetch(url: str) -> str:
    req = urllib.request.Request(
        url, headers={"User-Agent": _UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read()
        if "gzip" in (resp.headers.get("Content-Encoding") or ""):
            body = gzip.decompress(body)
        return body.decode("utf-8", "replace")


def _releases(text: str) -> list[dict]:
    """Die Release-Blöcke der Download-Seite (Interim + LTS)."""
    releases = []
    for block in _ITEM_RE.split(text)[1:]:
        ver = _VER_RE.search(block)
        if not ver:
            continue
        label = _LABEL_RE.search(block)
        key = "lts" if (label and "LTS" in label.group(1)) else "interim"
        codename = _CODENAME_RE.search(block)
        notes = _NOTES_RE.search(block)
        iso = _ISO_RE.search(block)
        releases.append({
            "key": key,
            "version": ver.group(1),
            "codename": codename.group(1) if codename else "",
            "notes_url": _BLOG + notes.group(1) if notes else None,
            "iso_dir": iso.group(1).rsplit("/", 1)[0] + "/" if iso else None,
        })
    return releases


def extract(text: str) -> str:
    """Kombinierter Status: 'interim=25.10;lts=24.04.5'."""
    releases = _releases(text)
    if not releases:
        raise ValueError("Keine Release-Blöcke gefunden")
    return ";".join(f"{r['key']}={r['version']}" for r in releases)


def extract_history(text: str) -> list[dict]:
    """Eine Zeile je Release; für LTS zusätzlich alle Point-Releases
    mit echtem ISO-Datum aus dem cdimage-Verzeichnis."""
    rows = []
    for rel in _releases(text):
        dated = {}
        if rel["iso_dir"]:
            try:
                for ver, date in _ISOROW_RE.findall(_fetch(rel["iso_dir"])):
                    dated.setdefault(ver, date)
            except Exception:
                pass
        if rel["version"] not in dated:
            dated[rel["version"]] = None
        for ver, date in dated.items():
            rows.append({"version": f"{rel['key']}={ver}", "date": date})
    rows.sort(key=lambda r: (r["date"] or "", r["version"]), reverse=True)
    return rows


def _to_markdown(fragment: str) -> str:
    """Artikel-HTML -> Markdown (Überschriften, Listen, Links)."""
    fragment = re.sub(r'<div class="blog-metadata">.*?</div>', "",
                      fragment, flags=re.S)
    fragment = re.sub(r"<(script|svg|hr)[^>]*>.*?</\1>", "", fragment,
                      flags=re.S)
    fragment = re.sub(r"<hr[^>]*>", "", fragment)

    def _link(match):
        href, label = match.group(1), match.group(2).strip()
        if href.startswith("/"):
            href = _BLOG + href
        return f"[{label}]({href})" if label else href

    fragment = re.sub(
        r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', _link, fragment,
        flags=re.S)
    fragment = re.sub(r"<h1[^>]*>.*?</h1>", "", fragment, flags=re.S)
    fragment = re.sub(r"<h2[^>]*>(.*?)</h2>", r"### \1", fragment,
                      flags=re.S)
    fragment = re.sub(r"<h3[^>]*>(.*?)</h3>", r"#### \1", fragment,
                      flags=re.S)
    fragment = re.sub(r"<h[4-6][^>]*>(.*?)</h[4-6]>", r"##### \1",
                      fragment, flags=re.S)
    fragment = re.sub(r"<li[^>]*>(.*?)</li>", r"\n- \1", fragment,
                      flags=re.S)
    fragment = re.sub(r"<br[^>]*>", "\n", fragment)
    fragment = re.sub(r"</(p|div|ul|ol|blockquote|pre|table|tr)>", "\n\n",
                      fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = html.unescape(fragment)
    fragment = re.sub(r"[ \t]+\n", "\n", fragment)
    fragment = re.sub(r"\n{3,}", "\n\n", fragment)
    return fragment.strip()


def update_changelog(existing: str | None) -> str | None:
    """Archiviert alle Release-Notes-Artikel des Blogs inkrementell.
    Schlüssel pro Abschnitt: der Codename-Slug aus der Notes-URL.
    Rückgabe: neuer Inhalt oder None (unverändert)."""
    seen = set(_HEAD_RE.findall(existing or ""))
    index = _fetch(_BLOG + "/blog/")
    slugs = list(dict.fromkeys(_NOTESLINK_RE.findall(index)))
    new_sections = []
    for slug in slugs:
        if slug in seen:
            continue
        try:
            page = _fetch(
                f"{_BLOG}/blog/ubuntu-mate-{slug}-release-notes/")
            title = _TITLE_RE.search(page)
            date = _DATE_RE.search(page)
            article = _ARTICLE_RE.search(page)
            body = _to_markdown(article.group(1)) if article else ""
        except Exception:
            continue
        header = title.group(1).strip() if title else slug
        stamp = date.group(1) if date else "n/a"
        new_sections.append(
            f"## {slug} – {stamp}\n\n**{header}**\n\n{body}")
    # Platzhalter für aktuelle Releases ohne Notes-Artikel; eigener
    # Schlüssel ('-hinweis'), damit später echte Notes trotzdem landen.
    try:
        for rel in _releases(_fetch(URL)):
            slug = rel["codename"].lower().replace(" ", "-")
            if slug and slug not in slugs and \
                    f"{slug}-hinweis" not in seen and slug not in seen:
                new_sections.append(
                    f"## {slug}-hinweis – n/a\n\n"
                    f"*Keine Release Notes auf ubuntu-mate.org für "
                    f"{rel['key']}={rel['version']} gefunden.*")
    except Exception:
        pass
    if not new_sections:
        return None
    new = "\n\n".join(new_sections)
    return f"{new}\n\n{existing}" if existing else new
