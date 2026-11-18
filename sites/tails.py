"""Seiten-Modul: Tails – https://tails.net/install/download-iso/

Die Download-Seite verlinkt die kanonische Versionsquelle
`install/v2/Tails/amd64/stable/latest.json`:

    {"installations": [{"version": "7.17.1",
        "installation-paths": [
            {"type": "img", "target-files": [{"url","sha256","size"}]},
            {"type": "iso", "target-files": [{"url","sha256","size"}]}]}]}

Überwacht wird genau diese Datei (enthält Version, ISO/IMG-URLs,
SHA256 + Größe). Release-Daten + Anmerkungen kommen aus dem
Atom-Feed https://tails.net/news/index.en.atom ('Tails X.Y'
Einträge mit <published>).

Downloads: tails-amd64-<v>.iso + .img (+ beide .sig-Signaturen)
nach downloads/tails/; die latest.json wird als
tails-amd64-<v>.latest.json mit abgelegt - newsbot parst sie als
Hash-Quelle (._checksum_map) und lädt sie dank _is_checksum_file
bei jedem Lauf frisch (Respin-sicher).
"""

import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

NAME = "Tails"
URL = ("https://tails.net/install/v2/Tails/amd64/stable/"
       "latest.json")
NOTES = ("Download-Seite: "
         "https://tails.net/install/download-iso/index.en.html")
SLUG = "tails"
CHANGELOG_URL = "https://tails.net/news/index.en.html"

_UA = "NewsBot/1.27"
_FEED_URL = "https://tails.net/news/index.en.atom"
_SIG_BASE = "https://tails.net/torrents/files"
_ATOM = "{http://www.w3.org/2005/Atom}"
_HEAD_RE = re.compile(r"^## (.+?) – \d{4}-\d{2}-\d{2}", re.M)
_TITLE_RE = re.compile(r"^Tails\s+(\d+(?:\.\d+)+)$")


def _fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    return urllib.request.urlopen(req, timeout=30).read()


def _installation(text):
    data = json.loads(text)
    insts = data.get("installations") or []
    if not insts:
        raise ValueError("Tails: keine 'installations' in latest.json")
    return insts[0]


def _target_files(inst):
    """{'iso': {url,sha256,size}, 'img': {...}} aus den
    installation-paths."""
    out = {}
    for path in inst.get("installation-paths") or []:
        files = path.get("target-files") or []
        if files and path.get("type"):
            out[path["type"]] = files[0]
    return out


def _news_entries():
    """Atom-Feed -> [{'version','date','link','title'}], nur
    'Tails X.Y[.Z]'-Release-Einträge."""
    out = []
    try:
        root = ET.fromstring(_fetch(_FEED_URL))
    except Exception:
        return out
    for e in root.findall(f"{_ATOM}entry"):
        m = _TITLE_RE.match(
            (e.findtext(f"{_ATOM}title") or "").strip())
        if not m:
            continue
        link = ""
        for l in e.findall(f"{_ATOM}link"):
            if l.get("href"):
                link = l.get("href")
                break
        date = (e.findtext(f"{_ATOM}published") or
                e.findtext(f"{_ATOM}updated") or "")[:10]
        out.append({"version": m.group(1), "date": date,
                    "link": link,
                    "title": (e.findtext(f"{_ATOM}title") or "")
                             .strip()})
    return out


def extract(text):
    """latest.json -> Versionsnummer."""
    ver = _installation(text).get("version", "")
    if not ver:
        raise ValueError("Tails: kein 'version'-Feld in latest.json")
    return ver


def extract_history(text):
    """Release-Daten aus dem News-Feed (published) - neueste
    zuerst."""
    return [{"version": e["version"], "date": e["date"]}
            for e in _news_entries()]


def list_downloads(text, have, target_dir):
    """ISO + IMG (+ .sig) + latest.json als Hash-Beleg."""
    inst = _installation(text)
    ver = inst["version"]
    base = f"tails-amd64-{ver}"
    items = []
    # Hash-Beleg zuerst (wird bei jedem Lauf erneuert und dient der
    # Verifikation der grossen Dateien).
    items.append({"url": URL, "filename": f"{base}.latest.json"})
    for typ in ("iso", "img"):
        tf = _target_files(inst).get(typ)
        if not tf or not tf.get("url"):
            continue
        fname = urlparse(tf["url"]).path.rsplit("/", 1)[-1]
        items.append({"url": tf["url"], "filename": fname})
        sig = f"{_SIG_BASE}/{fname}.sig"
        items.append({"url": sig, "filename": f"{fname}.sig"})
    return [i for i in items if i["filename"] not in have
            or i["filename"].endswith(".latest.json")]


def update_changelog(existing):
    """News-Feed -> Abschnitte '## Tails <v> – <datum>' mit Link
    auf die Release-Notes; inkrementell, neue oben."""
    known = set(_HEAD_RE.findall(existing or ""))
    sections = []
    for e in _news_entries():
        head = f"Tails {e['version']}"
        if head in known:
            continue
        sections.append(
            f"## {head} – {e['date']}\n\n"
            f"Release-Notes: {e['link']}")
    if not sections:
        return None
    parts = [p.strip() for p in
             re.split(r"(?m)^(?=## )", existing or "") if p.strip()]
    if not parts or not parts[0].startswith("#"):
        parts.insert(0, "# Tails – Changelog")
    return "\n\n".join([parts[0]] + sections + parts[1:]) + "\n"
