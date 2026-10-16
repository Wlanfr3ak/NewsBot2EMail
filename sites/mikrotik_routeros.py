"""Seiten-Modul: MikroTik RouterOS – https://mikrotik.com/download

Versionslisten pro Kanal (serverseitig gerendert):
  https://mikrotik.com/download/changelogs/<kanal>
Changelog-Text pro Version (offizieller Update-Endpoint):
  https://upgrade.mikrotik.com/routeros/<version>/CHANGELOG

CHANNELS wählt, bei welchen Kanälen eine neue Version eine
Benachrichtigung auslöst. ARCHIVE_CHANNELS wählt, welche Kanäle im
Changelog-Archiv (archive/mikrotik-routeros_changelog.md) landen.
Beides lässt sich in config.json überschreiben:

  "site_options": {
    "mikrotik_routeros": {
      "channels": ["stable", "long-term"],
      "archive_channels": ["stable", "long-term", "development"]
    }
  }

Keine Downloads (wie gewünscht).
"""

import gzip
import json
import re
import urllib.request
from pathlib import Path

NAME = "MikroTik RouterOS"
URL = "https://mikrotik.com/download/changelogs/stable"
NOTES = "Download: https://mikrotik.com/download"
SLUG = "mikrotik-routeros"
CHANGELOG_URL = "https://mikrotik.com/download/changelogs"

def _options() -> dict:
    """site_options.mikrotik_routeros aus config.json (optional)."""
    try:
        cfg = Path(__file__).resolve().parent.parent / "config.json"
        data = json.loads(cfg.read_text(encoding="utf-8"))
        return data.get("site_options", {}).get("mikrotik_routeros", {})
    except Exception:
        return {}


_OPTS = _options()

# Benachrichtigung bei neuer Version in diesen Kanälen.
# Optionen: "stable", "long-term", "testing", "development"
CHANNELS = _OPTS.get("channels") or ["stable"]

# Kanäle, deren Changelog archiviert wird (None = wie CHANNELS).
ARCHIVE_CHANNELS = _OPTS.get(
    "archive_channels", ["stable", "long-term", "testing", "development"])

_UA = "NewsBot/1.5"
_CHANNEL_URL = "https://mikrotik.com/download/changelogs/{}"
_CHANGELOG_URL = "https://upgrade.mikrotik.com/routeros/{}/CHANGELOG"
_VERSION_RE = re.compile(r'data-changelog-version="([^"]+)"')
_TITLE_RE = re.compile(
    r"(?:What's new in|New RouterOS)\s+(\S+)\s*\(([^)]*)\)")
_HEAD_RE = re.compile(r"^## (\S+) – (\S+) – (\S+)", re.M)
# "arp" ist ein Upstream-Tippfehler für April (7.23beta5-Changelog)
_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "arp": 4, "may": 5,
           "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11,
           "dec": 12}
_URL_CHANNEL = URL.rsplit("/", 1)[-1]


def _fetch(url: str) -> str:
    req = urllib.request.Request(
        url, headers={"User-Agent": _UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read()
        if "gzip" in (resp.headers.get("Content-Encoding") or ""):
            body = gzip.decompress(body)
        return body.decode("utf-8", "replace")


def _channel_versions(channel: str, text: str | None = None) -> list[str]:
    """Versionsliste eines Kanals (neueste zuerst)."""
    if text is None:
        text = _fetch(_CHANNEL_URL.format(channel))
    return _VERSION_RE.findall(text)


def _current_versions(text: str) -> dict[str, str]:
    """Aktuelle Version je Kanal in CHANNELS."""
    versions = {}
    for channel in CHANNELS:
        page = text if channel == _URL_CHANNEL else None
        found = _channel_versions(channel, page)
        if not found:
            raise ValueError(f"Keine Versionen für Kanal '{channel}' gefunden")
        versions[channel] = found[0]
    return versions


def extract(text: str) -> str:
    """Aktuelle Version(en) der überwachten Kanäle.

    Ein Kanal: nur die Versionsnummer ('7.24.4').
    Mehrere:   'stable=7.24.4;long-term=7.23.7'.
    """
    versions = _current_versions(text)
    if len(versions) == 1:
        return next(iter(versions.values()))
    return ";".join(f"{ch}={ver}" for ch, ver in versions.items())


def _parse_date(raw: str) -> str | None:
    """Bekannte Datumsformate -> 'YYYY-MM-DD'.

    MikroTik nutzt je nach Ära: '2026-09-16', '2026-Aug-21 16:06'
    (RouterOS 7), 'Dec/22/2021 13:49:22' (RouterOS 6) und
    'Aug.25.15-12:59:46' (RouterOS 6, zweistelliges Jahr).
    """
    match = re.match(r"\s*(\d{4})-(\d{2})-(\d{2})", raw)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    match = re.match(r"\s*(\d{4})-([A-Za-z]{3})-(\d{1,2})", raw)
    if match and match.group(2).lower() in _MONTHS:
        return (f"{match.group(1)}-{_MONTHS[match.group(2).lower()]:02d}"
                f"-{int(match.group(3)):02d}")
    match = re.match(r"\s*([A-Za-z]{3})[./](\d{1,2})[./](\d{2,4})", raw)
    if match and match.group(1).lower() in _MONTHS:
        year = int(match.group(3))
        year = 2000 + year if year < 100 else year
        return (f"{year}-{_MONTHS[match.group(1).lower()]:02d}"
                f"-{int(match.group(2)):02d}")
    return None


def extract_history(text: str) -> list[dict]:
    """Eine Zeile je Kanal: aktuelle Version mit Release-Datum."""
    releases = []
    for channel, version in _current_versions(text).items():
        date = None
        try:
            match = _TITLE_RE.search(_fetch(_CHANGELOG_URL.format(version)))
            if match:
                date = _parse_date(match.group(2))
        except Exception:
            pass
        label = version if len(CHANNELS) == 1 else f"{channel}={version}"
        releases.append({"version": label, "date": date})
    if len(releases) > 1:
        # Für die Historien-Tabelle: kombinierte Version als eine Zeile
        combined = ";".join(r["version"] for r in releases)
        newest = max((r["date"] or "" for r in releases), default="")
        return [{"version": combined, "date": newest or None}]
    return releases


def _changelog(version: str) -> tuple[str, str]:
    """(Datum, Text) eines Versions-Changelogs.

    Datum 'n/a', wenn die Kopfzeile fehlt oder das Format unbekannt
    ist – 'n/a'-Abschnitte werden nicht erneut geholt (im Gegensatz
    zu älteren '?'-Abschnitten, siehe update_changelog).
    """
    text = _fetch(_CHANGELOG_URL.format(version))
    match = _TITLE_RE.search(text)
    if match:
        return _parse_date(match.group(2)) or "n/a", text[match.end():].strip()
    return "n/a", text.strip()


def update_changelog(existing: str | None) -> str | None:
    """Baut das Archiv inkrementell auf: für jede Version in
    ARCHIVE_CHANNELS, die noch nicht im Archiv steht, wird das
    CHANGELOG geholt und als Abschnitt oben eingefügt.
    Abschnitte mit altem '?'-Datum werden einmalig neu geholt und
    an ihrer Position ersetzt (Selbstreparatur nach Parser-Fix).
    Rückgabe: kompletter neuer Inhalt oder None (unverändert)."""
    parts = [p.strip() for p in re.split(r"(?m)^(?=## )", existing or "")
             if p.strip()]
    sections, have = [], set()
    for part in parts:
        match = _HEAD_RE.match(part)
        if match:
            key = (match.group(1), match.group(2))
            if match.group(3) == "?":
                sections.append([key, part])   # neu holen, Position behalten
                continue
            have.add(key)
        sections.append([None, part])
    new_sections, changed = [], False
    for channel in (ARCHIVE_CHANNELS or CHANNELS):
        for version in _channel_versions(channel):
            key = (channel, version)
            if key in have:
                continue
            try:
                date, body = _changelog(version)
            except Exception:
                continue
            have.add(key)
            section = f"## {channel} – {version} – {date}\n\n{body}"
            for entry in sections:
                if entry[0] == key:
                    entry[0], entry[1] = None, section
                    break
            else:
                new_sections.append(section)
            changed = True
    if not changed:
        return None
    return "\n\n".join(new_sections + [text for _k, text in sections])
