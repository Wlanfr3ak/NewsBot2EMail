"""Seiten-Modul: BlossomOS (Online-Edition) – https://blossom.computer/downloads

Die Download-Seite ist eine SvelteKit-App, deren Karten ihre Daten
clientseitig von https://cdn.blossomos.org/iso/isodata.json laden:

    {"name": "BlossomOS-2026.09.18-x86_64.iso", "sha256": "..."}

Überwacht wird genau diese Datei (winzig, enthält Dateiname +
SHA256 der aktuellen Online-ISO). Version = Datum im Dateinamen
(YYYY.MM.DD). Der eigentliche Download-Button der Webseite ist mit
Cloudflare-Turnstile geschützt - die ISO liegt aber offen am CDN.

Download: die Online-ISO (~8,4 GB) plus isodata.json als
Hash-Beleg, versioniert als BlossomOS-<version>.isodata.json.

Es gibt keine öffentliche Release-Historie - die Historie
(history/blossomos.md) wächst mit jedem erkannten Release.
"""

import json
import re

NAME = "BlossomOS Online"
URL = "https://cdn.blossomos.org/iso/isodata.json"
NOTES = "Download: https://blossom.computer/downloads (Online-Edition)"
SLUG = "blossomos"

DOWNLOADS = [
    # isodata.json zuerst (versionierter Hash-Beleg) - verifiziert
    # die ISO beim Download
    {"url": "https://cdn.blossomos.org/iso/isodata.json",
     "filename": "BlossomOS-{version}-x86_64.isodata.json"},
    "https://cdn.blossomos.org/iso/BlossomOS-{version}-x86_64.iso",
]

_NAME_RE = re.compile(r"BlossomOS-(\d{4}\.\d{2}\.\d{2})-x86_64\.iso")


def extract(text: str) -> str:
    """isodata.json -> Version (Datum im Dateinamen)."""
    name = json.loads(text).get("name", "")
    match = _NAME_RE.search(name)
    if not match:
        raise ValueError(f"Kein ISO-Name in isodata.json: {name!r}")
    return match.group(1)


def extract_history(text: str) -> list[dict]:
    """Die Version IST das Datum (YYYY.MM.DD) -> direkt ableitbar."""
    ver = extract(text)
    return [{"version": ver, "date": ver.replace(".", "-")}]
