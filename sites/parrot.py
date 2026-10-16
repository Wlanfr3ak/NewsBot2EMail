"""Seiten-Modul: Parrot Security – https://parrotsec.org/download/

Überwacht die Security-Edition. Lädt das aktuelle ISO (~8,5 GB)
und die signierte Hash-Datei nach downloads/parrot-security/.

Changelog: Die Release-Notes-Posts unter parrotsec.org/blog/
liefern ihren Inhalt als fertiges Markdown im __NEXT_DATA__-JSON
(client-seitig gerenderte Next.js-Seite). Archiv:
archive/parrot-security_changelog.md.
"""

import gzip
import json
import re
import urllib.request

NAME = "Parrot Security"
URL = "https://parrotsec.org/download/"
NOTES = "Security-Edition. Download: https://parrotsec.org/download/"
SLUG = "parrot-security"
CHANGELOG_URL = "https://parrotsec.org/blog/"

DOWNLOADS = [
    # Hash-Datei zuerst - verifiziert die ISO (enthält md5/sha256/
    # sha512-Sektionen; der längste Hash pro Datei gewinnt)
    {"url": "https://deb.parrot.sh/parrot/iso/{version}/signed-hashes.txt",
     "filename": "signed-hashes-{version}.txt"},
    "https://deb.parrot.sh/parrot/iso/{version}/Parrot-security-{version}_amd64.iso",
]

_UA = "NewsBot/1.6"
_BLOG = "https://parrotsec.org"
_VERSION_RE = re.compile(r"Parrot-security-(\d+\.\d+)_amd64\.iso")
_SLUG_RE = re.compile(
    r"/blog/(\d{4}-\d{2}-\d{2})-parrot-([\d.]+)-release-notes")
_HEAD_RE = re.compile(r"^## (\S+) – ", re.M)
_NEXTDATA_RE = re.compile(r'__NEXT_DATA__[^>]*>(.*?)</script>', re.S)
_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
           "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}


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
        raise ValueError("Keine Security-ISO-Version gefunden")
    return match.group(1)


def extract_history(text: str) -> list[dict]:
    """Release-Daten stehen im Blog-Slug (YYYY-MM-DD-parrot-X.Y)."""
    index = _fetch(_BLOG + "/blog/")
    rows = [{"version": v, "date": d}
            for d, v in _SLUG_RE.findall(index)]
    # aktuelle Version sicher aufnehmen, falls noch kein Post existiert
    current = extract(text)
    if current not in {r["version"] for r in rows}:
        rows.insert(0, {"version": current, "date": None})
    return rows


def _post_date(raw: str) -> str:
    """'Jun 29, 2026' -> '2026-06-29' (Fallback: Originalstring)."""
    match = re.match(r"(\w{3})\w*\s+(\d{1,2}),\s*(\d{4})", raw.strip())
    if match and match.group(1).lower()[:3] in _MONTHS:
        return (f"{match.group(3)}-{_MONTHS[match.group(1).lower()[:3]]:02d}"
                f"-{int(match.group(2)):02d}")
    return raw.strip() or "n/a"


def update_changelog(existing: str | None) -> str | None:
    """Archiviert alle Release-Notes-Posts inkrementell.

    Wichtig: Post-URL braucht den abschließenden '/' – ohne ihn
    liefert der Server eine Redirect-Schleife (301 http->308 https).
    """
    seen = set(_HEAD_RE.findall(existing or ""))
    index = _fetch(_BLOG + "/blog/")
    slugs = list(dict.fromkeys(
        m.group(0).split("/blog/")[1] for m in _SLUG_RE.finditer(index)))
    new_sections = []
    for slug in slugs:
        key = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug).replace(
            "-release-notes", "")
        if key in seen:
            continue
        try:
            page = _fetch(f"{_BLOG}/blog/{slug}/")
            data = json.loads(_NEXTDATA_RE.search(page).group(1))
            post = data["props"]["pageProps"]["post"]
        except Exception:
            continue
        new_sections.append(
            f"## {key} – {_post_date(post.get('date', ''))}\n\n"
            f"**{post.get('title', key)}**\n\n{post.get('content', '').strip()}")
    if not new_sections:
        return None
    new = "\n\n".join(new_sections)
    return f"{new}\n\n{existing}" if existing else new
