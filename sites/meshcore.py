"""Seiten-Modul: MeshCore – https://meshcore.io/

Überwacht neue MeshCore-Firmware-Releases über zwei Quellen:

1. GitHub-Releases-API (ripplebiz/MeshCore): die Firmware erscheint
   in drei getaggten Varianten - 'companion-vX.Y.Z' (Companion-Radio
   BLE/USB/WiFi), 'repeater-vX.Y.Z' und 'room-server-vX.Y.Z'.
   extract() kombiniert die jeweils neueste Version je Variante -
   ein neues Release in einer Variante löst eine Mail aus.
2. blog.meshcore.io/feed.xml (Jekyll-Atom-Feed): Release-Posts
   (Slug 'release-X-Y-Z') und sonstige Ankündigungen werden dem
   Changelog-Abschnitt der passenden Version zugeordnet bzw. als
   eigener 'Blog'-Abschnitt archiviert.

Downloads: kein direkter Datei-Download - jedes Release bringt
~150-340 gerätespezifische Firmware-Binaries mit (unpraktikabel);
die Assets bleiben über den Release-Link erreichbar, der
Web-Flasher steht unter https://flasher.meshcore.dev/.

Historie + Changelog: echte published_at-Daten der Releases;
Release-Bodies sind Markdown und werden inkrementell nach
archive/meshcore_changelog.md geschrieben.
"""

import json
import re
import urllib.request
import xml.etree.ElementTree as ET

NAME = "MeshCore"
URL = ("https://api.github.com/repos/ripplebiz/MeshCore/"
       "releases?per_page=100")
NOTES = ("Flasher: https://flasher.meshcore.dev/ – "
         "Blog: https://blog.meshcore.io/")
SLUG = "meshcore"
CHANGELOG_URL = "https://github.com/ripplebiz/MeshCore/releases"

_UA = "NewsBot/1.24"
_FEED_URL = "https://blog.meshcore.io/feed.xml"
# Tag-Familie + Version: 'companion-v1.18.0' -> ('companion','1.18.0')
_TAG_RE = re.compile(r"^([a-z][a-z0-9-]*)-v(\d[\d.]*)$", re.I)
_HEAD_RE = re.compile(r"^## (\S+) – (\d{4}-\d{2}-\d{2})", re.M)
_ATOM = "{http://www.w3.org/2005/Atom}"


def _fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    return urllib.request.urlopen(req, timeout=30).read().decode(
        "utf-8", errors="replace")


def _releases():
    """Liste stabiler Releases: [(familie, version, datum, body, url)]."""
    data = json.loads(_fetch(URL))
    out = []
    for rel in data:
        if rel.get("draft") or rel.get("prerelease"):
            continue
        m = _TAG_RE.match(rel.get("tag_name") or "")
        if not m:
            continue
        out.append((m.group(1).lower(), m.group(2),
                    (rel.get("published_at") or "")[:10],
                    rel.get("body") or "", rel.get("html_url") or ""))
    return out


def _ver_key(v):
    try:
        return [int(p) for p in v.split(".")]
    except ValueError:
        return [0]


def _latest_per_family(releases=None):
    """{familie: (version, datum)} – jeweils höchste Version."""
    best = {}
    for fam, ver, date, _body, _url in (releases or _releases()):
        if fam not in best or _ver_key(ver) > _ver_key(best[fam][0]):
            best[fam] = (ver, date)
    return dict(sorted(best.items()))


def _blog_entries():
    """Atom-Feed -> [{'title','link','date','ver'}] (ver = erkannte
    Release-Version aus Slug 'release-X-Y-Z' oder Titel)."""
    out = []
    try:
        root = ET.fromstring(_fetch(_FEED_URL))
    except Exception:
        return out
    for e in root.findall(f"{_ATOM}entry"):
        title = (e.findtext(f"{_ATOM}title") or "").strip()
        link = ""
        for l in e.findall(f"{_ATOM}link"):
            if l.get("rel") in (None, "alternate") and l.get("href"):
                link = l.get("href").strip()
                break
        date = (e.findtext(f"{_ATOM}updated") or
                e.findtext(f"{_ATOM}published") or "")[:10]
        ver = ""
        m = re.search(r"release-(\d+)-(\d+)(?:-(\d+))?", link)
        if m:
            ver = ".".join(g for g in m.groups() if g)
        else:
            m = re.search(r"\bv?(\d+\.\d+(?:\.\d+)?)\b", title)
            if m:
                ver = m.group(1)
        out.append({"title": title, "link": link, "date": date,
                    "ver": ver})
    return out


def extract(text):
    """Vergleichswert: 'companion=1.18.0;repeater=1.18.0;
    room-server=1.18.0' (je Familie die neueste Version)."""
    latest = _latest_per_family()
    if not latest:
        raise RuntimeError("MeshCore: keine Releases erkannt")
    return ";".join(f"{fam}={ver}" for fam, (ver, _d)
                    in latest.items())


def extract_history(text):
    """Alle stabilen Releases mit echtem Datum, neueste zuerst."""
    rels = _releases()
    rels.sort(key=lambda r: (r[2], _ver_key(r[1])), reverse=True)
    return [{"version": f"{fam}-v{ver}", "date": date}
            for fam, ver, date, _b, _u in rels]


def update_changelog(existing):
    """Neue Release-Abschnitte '## <tag> – <datum>' (GitHub-Body +
    passender Blog-Post) voranstellen; danach neue Blog-Posts ohne
    Release-Bezug unter '## Blog – <datum>'."""
    rels = _releases()
    rels.sort(key=lambda r: (r[2], _ver_key(r[1])), reverse=True)
    known = {m[0] for m in _HEAD_RE.findall(existing or "")}
    blog = _blog_entries()
    by_ver = {}
    for b in blog:
        if b["ver"]:
            by_ver.setdefault(b["ver"], b)

    sections = []
    for fam, ver, date, body, url in rels:
        tag = f"{fam}-v{ver}"
        if tag in known:
            continue
        parts = [f"## {tag} – {date}", ""]
        b = by_ver.get(ver)
        if b:
            parts += [f"Blog: [{b['title']}]({b['link']})", ""]
        if body.strip():
            parts += [body.strip(), ""]
        parts += [f"Release: {url}", ""]
        sections.append("\n".join(parts).rstrip())

    # Blog-Posts ohne Versionsbezug (Ankuendigungen, News)
    known_blog = set(re.findall(r"^## Blog: (.+)$", existing or "",
                                re.M))
    for b in blog:
        if not b["ver"] and b["title"] and b["title"] not in known_blog:
            sections.append(f"## Blog: {b['title']}\n\n{b['date']} – "
                            f"{b['link']}")

    if not sections:
        return None
    parts = [p.strip() for p in
             re.split(r"(?m)^(?=## )", existing or "") if p.strip()]
    if not parts or not parts[0].startswith("#"):
        parts.insert(0, "# MeshCore – Changelog")
    return "\n\n".join([parts[0]] + sections + parts[1:]) + "\n"
