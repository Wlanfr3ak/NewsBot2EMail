"""Seiten-Modul: Proxmox VE – https://www.proxmox.com/en/downloads

Quelle ist das ISO-Verzeichnis enterprise.proxmox.com/iso/ (dahin
verlinkt die Download-Seite): jede Karte enthält Dateiname, Größe,
Datum und SHA256. Es werden nur die Proxmox-VE-ISOs der x86-Edition
betrachtet (kein ARM64, kein PBS/PMG/PDM).

Lädt ISO (~1,7 GB) + .sha256 + .asc nach downloads/proxmox-ve/.

Changelog: die Roadmap-Wiki-Seite enthält ALLE Release-Sektionen
(„Proxmox VE X.Y" mit „Released DD. Month YYYY") bis zurück zu 0.9 –
wird nach archive/proxmox-ve_changelog.md gespiegelt.
"""

import gzip
import html
import re
import urllib.request

NAME = "Proxmox VE"
URL = "https://enterprise.proxmox.com/iso/"
NOTES = ("Nur Proxmox VE (amd64). Übersicht: "
         "https://www.proxmox.com/en/downloads")
SLUG = "proxmox-ve"
CHANGELOG_URL = "https://pve.proxmox.com/wiki/Roadmap"

DOWNLOADS = [
    # Hash-Datei zuerst - sie verifiziert die ISO
    "https://enterprise.proxmox.com/iso/proxmox-ve_{version}.iso.sha256",
    "https://enterprise.proxmox.com/iso/proxmox-ve_{version}.iso.asc",
    "https://enterprise.proxmox.com/iso/proxmox-ve_{version}.iso",
]

_UA = "NewsBot/1.7"
_ISO_RE = re.compile(
    r'<span class="filename">proxmox-ve_(\d+\.\d+-\d+)\.iso</span>'
    r'.*?(\d{4}-\d{2}-\d{2})', re.S)
_WIKI = "https://pve.proxmox.com"
_SEC_RE = re.compile(
    r'<h2[^>]*>\s*<span class="mw-headline" id="Proxmox_VE_([^"]+)">'
    r"(.*?)</span></h2>(.*?)(?=<h2|\Z)",
    re.S)
_DATE_RE = re.compile(
    r"Released\s+(\d{1,2})\.?\s+([A-Za-z]+)\s+(\d{4})")
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


def _isos(text: str) -> list[tuple[str, str]]:
    """(Version, Datum)-Paare aller amd64-VE-ISOs, neueste zuerst."""
    pairs = _ISO_RE.findall(text)
    pairs.sort(
        key=lambda p: [int(x) for x in re.split(r"[.-]", p[0])],
        reverse=True)
    return pairs


def extract(text: str) -> str:
    pairs = _isos(text)
    if not pairs:
        raise ValueError("Kein Proxmox-VE-ISO gefunden")
    return pairs[0][0]


def extract_history(text: str) -> list[dict]:
    return [{"version": v, "date": d} for v, d in _isos(text)]


def _release_date(section: str) -> str:
    match = _DATE_RE.search(section)
    if match and match.group(2).lower() in _MONTHS:
        return (f"{match.group(3)}-{_MONTHS[match.group(2).lower()]:02d}"
                f"-{int(match.group(1)):02d}")
    return "n/a"


def _to_markdown(fragment: str) -> str:
    """Wiki-Abschnitt -> Markdown."""

    def _link(match):
        href, label = match.group(1), match.group(2).strip()
        if href.startswith("/"):
            href = _WIKI + href
        return f"[{label}]({href})" if label else href

    fragment = re.sub(r"<(script|style|svg)[^>]*>.*?</\1>", "",
                      fragment, flags=re.S)
    fragment = re.sub(
        r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', _link, fragment,
        flags=re.S)
    fragment = re.sub(r"<h3[^>]*>(.*?)</h3>", r"### \1", fragment,
                      flags=re.S)
    fragment = re.sub(r"<h4[^>]*>(.*?)</h4>", r"#### \1", fragment,
                      flags=re.S)
    fragment = re.sub(r"<li[^>]*>(.*?)</li>", r"\n- \1", fragment,
                      flags=re.S)
    fragment = re.sub(r"<br[^>]*>", "\n", fragment)
    fragment = re.sub(r"</(p|div|ul|ol|blockquote|pre|table|tr)>",
                      "\n\n", fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = html.unescape(fragment)
    fragment = re.sub(r"[ \t]+\n", "\n", fragment)
    fragment = re.sub(r"\n{3,}", "\n\n", fragment)
    return fragment.strip()


def extract_changelog(text: str) -> str:
    """Alle 'Proxmox VE X.Y'-Release-Sektionen der Roadmap-Seite
    als Markdown (die Seite enthält die komplette Historie)."""
    sections = []
    for sec_id, heading, body in _SEC_RE.findall(text):
        title = html.unescape(re.sub(r"<[^>]+>", "", heading)).strip()
        if title.startswith("Proxmox VE "):
            title = title[len("Proxmox VE "):]  # '9.2', '9.0 BETA 1', ...
        date = _release_date(body)
        sections.append(
            f"## {title} – {date}\n\n{_to_markdown(body)}")
    return "\n\n".join(sections)
