"""Seiten-Modul: Kali Linux – https://www.kali.org/get-kali/

Überwacht die Installer-Images (quartalsweise Releases, Schema
YYYY.W). Lädt nach downloads/kali-linux/:

  - das Standard-Installer-ISO (~4,8 GB, direkter Download)
  - das "everything"-Offline-ISO als .torrent-Datei – das ISO
    selbst gibt es nur via Torrent (kein Direkt-Download)
  - SHA256SUMS + SHA256SUMS.gpg zur Verifikation

Changelog: die Release-Posts auf kali.org/blog/ (paginiert)
werden unter archive/kali-linux_changelog.md archiviert.
"""

import gzip
import html
import re
import urllib.request

NAME = "Kali Linux"
URL = "https://www.kali.org/get-kali/#kali-installer-images"
NOTES = ("Standard-Installer-ISO + Everything-ISO als .torrent "
         "(Everything gibt es nicht als Direkt-Download). "
         "https://www.kali.org/get-kali/")
SLUG = "kali-linux"
CHANGELOG_URL = "https://www.kali.org/blog/"

DOWNLOADS = [
    # Hash-Dateien zuerst - sie verifizieren die nachfolgenden
    # Downloads; versionierte Namen, damit sie pro Release neu
    # geladen werden statt ewig "vorhanden" zu sein.
    {"url": "https://cdimage.kali.org/kali-{version}/SHA256SUMS",
     "filename": "SHA256SUMS-{version}"},
    {"url": "https://cdimage.kali.org/kali-{version}/SHA256SUMS.gpg",
     "filename": "SHA256SUMS-{version}.gpg"},
    "https://cdimage.kali.org/kali-{version}/kali-linux-{version}-installer-amd64.iso",
    "https://cdimage.kali.org/kali-{version}/kali-linux-{version}-installer-everything-amd64.iso.torrent",
]

_UA = "NewsBot/1.6"
_BLOG = "https://www.kali.org"
_MAX_PAGES = 6  # Blog-Seiten für Historie/Archiv (1 Seite ≈ 4 Releases)

_VERSION_RE = re.compile(r"kali-linux-(\d{4}\.\d+)-installer-amd64\.iso")
_POST_RE = re.compile(
    r"href=[\"']?(?:https://www\.kali\.org)?"
    r"(/blog/kali-linux-(\d{4})-(\d+)-release/)")
_DATE_RE = re.compile(
    r'<time[^>]*datetime="(\d{4}-\d{2}-\d{2})', re.S)
_HEAD_RE = re.compile(r"^## (\S+) – ", re.M)
_ARTICLE_RE = re.compile(r"<article>(.*?)</article>", re.S)
_TITLE_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)


def _fetch(url: str) -> str:
    req = urllib.request.Request(
        url, headers={"User-Agent": _UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read()
        if "gzip" in (resp.headers.get("Content-Encoding") or ""):
            body = gzip.decompress(body)
        return body.decode("utf-8", "replace")


def extract(text: str) -> str:
    match = _VERSION_RE.search(text)
    if not match:
        raise ValueError("Keine Installer-Version gefunden")
    return match.group(1)


def _blog_releases() -> list[dict]:
    """Release-Posts über alle Blog-Seiten:
    [{'slug', 'version' ('2026.2'), 'date', 'url'}, ...] neueste zuerst."""
    releases, seen = [], set()
    for page in range(1, _MAX_PAGES + 1):
        url = _BLOG + "/blog/" if page == 1 else f"{_BLOG}/blog/page/{page}/"
        try:
            text = _fetch(url)
        except Exception:
            break
        found = list(_POST_RE.finditer(text))
        new = []
        for m in found:
            if m.group(1) not in seen:
                seen.add(m.group(1))
                new.append(m)
        if not new:
            break
        for m in new:
            # Datum steht im <time datetime> direkt nach dem Post-Link
            date = _DATE_RE.search(text, m.end())
            releases.append({
                "slug": m.group(1),
                "version": f"{m.group(2)}.{m.group(3)}",
                "date": date.group(1) if date else None,
                "url": _BLOG + m.group(1),
            })
    return releases


def extract_history(text: str) -> list[dict]:
    rows, seen = [], set()
    for rel in _blog_releases():
        if rel["version"] not in seen:
            seen.add(rel["version"])
            rows.append({"version": rel["version"], "date": rel["date"]})
    current = extract(text)
    if current not in seen:
        rows.insert(0, {"version": current, "date": None})
    return rows


def _to_markdown(fragment: str) -> str:
    """Kali-Artikel-HTML -> Markdown (Attributes teils unquotiert)."""
    fragment = re.sub(r"<(script|style|svg|time|img|nav)[^>]*>.*?</\1>",
                      "", fragment, flags=re.S)
    fragment = re.sub(r"<(img|time|hr)[^>]*>", "", fragment)

    def _link(match):
        href = match.group(1) or match.group(2)
        label = re.sub(r"<[^>]+>", "", match.group(3)).strip()
        if href.startswith("/"):
            href = _BLOG + href
        return f"[{label}]({href})" if label else href

    fragment = re.sub(
        r'<a[^>]*href=(?:"([^"]+)"|([^\s>]+))[^>]*>(.*?)</a>',
        _link, fragment, flags=re.S)
    fragment = re.sub(r"<h1[^>]*>.*?</h1>", "", fragment, flags=re.S)
    for tag, mark in (("h2", "###"), ("h3", "####"), ("h4", "#####")):
        fragment = re.sub(
            rf"<{tag}[^>]*>(.*?)</{tag}>", rf"{mark} \1", fragment,
            flags=re.S)
    fragment = re.sub(r"<li[^>]*>(.*?)</li>", r"\n- \1", fragment,
                      flags=re.S)
    fragment = re.sub(r"<br[^>]*>", "\n", fragment)
    fragment = re.sub(r"</(p|div|ul|ol|blockquote|pre|table|tr|figure)>",
                      "\n\n", fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = html.unescape(fragment)
    fragment = re.sub(r"[ \t]+\n", "\n", fragment)
    fragment = re.sub(r"\n{3,}", "\n\n", fragment)
    return fragment.strip()


def update_changelog(existing: str | None) -> str | None:
    """Archiviert alle Release-Posts inkrementell.
    Schlüssel pro Abschnitt: die Version ('2026.2')."""
    seen = set(_HEAD_RE.findall(existing or ""))
    new_sections = []
    for rel in _blog_releases():
        if rel["version"] in seen:
            continue
        try:
            page = _fetch(rel["url"])
            article = _ARTICLE_RE.search(page)
            body = _to_markdown(article.group(1)) if article else ""
            title = _TITLE_RE.search(article.group(1)) if article else None
        except Exception:
            continue
        header = re.sub(r"<[^>]+>", "", title.group(1)).strip() \
            if title else f"Kali Linux {rel['version']}"
        new_sections.append(
            f"## {rel['version']} – {rel['date'] or 'n/a'}\n\n"
            f"**{header}**\n\n{body}")
    if not new_sections:
        return None
    new = "\n\n".join(new_sections)
    return f"{new}\n\n{existing}" if existing else new
