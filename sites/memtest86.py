"""Seiten-Modul: Memtest86+ – https://www.memtest.org/

Überwacht die aktuelle Version (Memtest86+ vX.YZ) und lädt die
drei Linux-Boot-ISOs nach downloads/memtest86/. Sie werden gezippt
ausgeliefert und direkt beim Download entpackt - gespeichert wird
die ISO unter dem Zip-Namen ohne '.zip', die Zip selbst wird
verworfen:

  - mt86plus_X.YZ_i586.iso       (32-bit)
  - mt86plus_X.YZ_x86_64.iso     (64-bit)
  - mt86plus_X.YZ_x86_64.grub.iso (64-bit, GRUB-Variante)

plus sha256sum-{version}.txt als Hash-Beleg (verifiziert die
Zips vor dem Entpacken automatisch).

Historie und Changelog kommen von den GitHub-Releases
(memtest86plus/memtest86plus) – echte Veröffentlichungsdaten und
Release-Notes als Markdown nach archive/memtest86_changelog.md.
"""

import json
import re
import urllib.request

NAME = "Memtest86+"
URL = "https://www.memtest.org/"
NOTES = "Download: https://www.memtest.org/"
SLUG = "memtest86"
CHANGELOG_URL = ("https://api.github.com/repos/memtest86plus/"
                 "memtest86plus/releases?per_page=100")

# Die drei Linux-Boot-ISOs kommen gezippt - "unzip" entpackt sie nach
# dem Laden und speichert sie unter dem Zip-Namen ohne '.zip'
# (z. B. mt86plus_8.10_x86_64.iso). Die Zip selbst wird nicht behalten.
DOWNLOADS = [
    # Hash-Datei zuerst - sie verifiziert die Zips VOR dem
    # Entpacken (der Hash bezieht sich auf die Zip, nicht die ISO).
    # Versionierter Name, damit sie pro Release neu geladen wird.
    {"url": "https://www.memtest.org/download/v{version}/sha256sum.txt",
     "filename": "sha256sum-{version}.txt"},
    {"url": "https://www.memtest.org/download/v{version}/mt86plus_{version}_i586.iso.zip",
     "unzip": True},
    {"url": "https://www.memtest.org/download/v{version}/mt86plus_{version}_x86_64.iso.zip",
     "unzip": True},
    {"url": "https://www.memtest.org/download/v{version}/mt86plus_{version}_x86_64.grub.iso.zip",
     "unzip": True},
]

_UA = "NewsBot/1.8"
_VERSION_RE = re.compile(r"mt86plus_(\d+\.\d+)_x86_64\.iso\.zip")
_API = ("https://api.github.com/repos/memtest86plus/"
        "memtest86plus/releases?per_page=100")


def _releases() -> list[dict]:
    req = urllib.request.Request(
        _API, headers={"User-Agent": _UA,
                       "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))


def extract(text: str) -> str:
    match = _VERSION_RE.search(text)
    if not match:
        raise ValueError("Keine ISO-Version gefunden")
    return match.group(1)


def extract_history(text: str) -> list[dict]:
    """Alle GitHub-Releases mit echten Daten, neueste zuerst."""
    try:
        rows = [{"version": rel["tag_name"].lstrip("v"),
                 "date": (rel.get("published_at") or "")[:10] or None}
                for rel in _releases()]
    except Exception:
        rows = []
    current = extract(text)
    if current not in {r["version"] for r in rows}:
        rows.insert(0, {"version": current, "date": None})
    return rows


def extract_changelog(text: str) -> str:
    """text = JSON der GitHub-Releases-API -> Markdown-Archiv."""
    sections = []
    for rel in json.loads(text):
        version = rel["tag_name"].lstrip("v")
        date = (rel.get("published_at") or "")[:10] or "n/a"
        title = (rel.get("name") or f"Memtest86+ v{version}").strip()
        body = (rel.get("body") or "").replace("\r\n", "\n").strip()
        sections.append(f"## {version} – {date}\n\n**{title}**\n\n{body}")
    return "\n\n".join(sections)
