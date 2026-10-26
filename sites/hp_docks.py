"""Seiten-Modul: HP USB-C Docks – Firmware (GitHub-Issue #2)

Überwacht die Dock-Firmware beider konfigurierter HP-Produkte
(USB-C Dock G5 + USB-C 100W G6) über die API hinter
support.hp.com (`wcc-services/swd-v2`): zuerst liefert
`osVersionData?productOid=<oid>` die OS-IDs, dann bekommt
`POST driverDetails` mit `productSeriesOid` die Softwareliste -
darin stehen Titel, Version, Datum, Größe und ftp.hp.com-URL
des aktuellen Firmware-Softpaqs sowie die Vorgängerversionen.

Der Vergleichswert ist kombiniert
('HP USB-C Dock G5=1.0.26.0 Rev.A;HP USB-C 100W G6 Dock=1.3.16.0 Rev.A')
- ein neues Release bei irgendeinem Dock löst eine Mail aus.

Hinweis: die SRS-Empfehlungs-API (workforceexperience.hp.com)
hinkt bei Dock-Firmware hinterher (zeigte 1.0.25.0, obwohl
sp165907 mit 1.0.26.0 live war) - daher die Treiberseiten-API.

Historie: neueste + Vorgängerversionen je Dock mit Datum.
Changelog: Beschreibung + fixesAndEnhancements je Version nach
archive/hp-usb-c-docks_changelog.md.
Downloads: das Firmware-.exe (spXXXXXX.exe) je Dock.

Produkte in config.json überschreibbar:

  "site_options": {
    "hp_docks": {"products": {"27767206": "HP USB-C Dock G5"}}
  }
"""

import html as _html
import json
import re
import urllib.request
from pathlib import Path

NAME = "HP USB-C Docks"
# GET-Endpunkt der Produktseite (existiert; der eigentliche
# Treiberabruf läuft per POST in _firmware()).
URL = ("https://support.hp.com/wcc-services/swd-v2/osVersionData"
       "?cc=ch&lc=de&productOid=27767206")
NOTES = "Treiberseiten: https://support.hp.com/ch-de/drivers/usb-c-docking"
SLUG = "hp-usb-c-docks"
CHANGELOG_URL = "https://support.hp.com/ch-de/drivers/usb-c-docking"


def _options() -> dict:
    """site_options.hp_docks aus config.json (optional)."""
    try:
        cfg = Path(__file__).resolve().parent.parent / "config.json"
        data = json.loads(cfg.read_text(encoding="utf-8"))
        return data.get("site_options", {}).get("hp_docks", {})
    except Exception:
        return {}


_OPTS = _options()

# Produkt-OIDs -> Anzeigename (aus Issue #2).
PRODUCTS = _OPTS.get("products") or {
    "27767206": "HP USB-C Dock G5",
    "2102849106": "HP USB-C 100W G6 Dock",
}

_UA = "NewsBot/1.19"
_OSVER_URL = ("https://support.hp.com/wcc-services/swd-v2/osVersionData"
              "?cc=ch&lc=de&productOid={}")
_DRIVERS_URL = ("https://support.hp.com/wcc-services/swd-v2/"
                "driverDetails")
# Kopfzeilenformat '## <dock>: <version> – <datum>' - der Doppelpunkt
# trennt den Dock-Namen, weil Versionen Leerzeichen enthalten
# ('1.0.26.0 Rev.A'); '(.+) – ' ist gierig und greift bis zum letzten
# ' – ' der Zeile (das Datum enthaelt selbst keins).
_HEAD_RE = re.compile(r"^## ([^:]+): (.+) – ", re.M)
_A_RE = re.compile(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S)
_CODE_RE = re.compile(r"<code>(.*?)</code>", re.S)
_STRIP_RE = re.compile(r"<[^>]+>")
_SP_RE = re.compile(r"(sp\d+)\.exe")
_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
           "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}


def _fetch(url: str, payload: dict | None = None) -> str:
    """GET (payload=None) oder JSON-POST."""
    data = json.dumps(payload).encode("utf-8") if payload else None
    headers = {"User-Agent": _UA}
    if data:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def _os_tms_id(oid: str) -> str:
    """OS-ID des Produkts für driverDetails.

    Bevorzugt das generische 'Windows 11' ohne Versionssuffix - nur
    dieses liefert auch die previousVersionOfDriversList mit; die
    konkreten Builds (26H2, 25H2, ...) zeigen oft nur die neueste
    Version. Fallback: erste Nicht-ARM-Version."""
    data = json.loads(_fetch(_OSVER_URL.format(oid)))
    platforms = (data["data"]["osAvailablePlatformsAnsOS"]
                 ["osPlatforms"])
    fallback = None
    for platform in platforms:
        for osver in platform.get("osVersions") or []:
            name = osver.get("name") or ""
            if "ARM" in name.upper():
                continue
            if fallback is None:
                fallback = osver["id"]
            if re.match(r"^Windows \d+$", name):
                return osver["id"]
    if fallback:
        return fallback
    raise ValueError(f"Keine OS-Version für Produkt {oid} gefunden")


def _firmware(oid: str) -> list[dict]:
    """Firmware-Einträge eines Produkts (neueste zuerst):
    {version, date, url, size, description, fixes}."""
    payload = {"lc": "de", "cc": "ch", "osName": "Windows 11",
               "osTMSId": _os_tms_id(oid), "productSeriesOid": int(oid)}
    data = json.loads(_fetch(_DRIVERS_URL, payload))
    out = []
    for stype in (data.get("data") or {}).get("softwareTypes") or []:
        for drv in stype.get("softwareDriversList") or []:
            latest = drv.get("latestVersionDriver") or {}
            if "irmware" not in (latest.get("title") or ""):
                continue
            info = latest.get("detailInformation") or {}
            # fixesAndEnhancements ist ein Fließtext '- Punkt - Punkt'
            fixes = [t.strip().lstrip("-").strip() for t in re.split(
                r"\s+-\s+", _md(info.get("fixesAndEnhancements") or ""))
                if t.strip().lstrip("-").strip()]
            entry = {
                "version": latest.get("version"),
                "date": _iso_date(latest.get("releaseDateString")),
                "url": latest.get("fileUrl"),
                "size": latest.get("fileSize"),
                "description": _md(info.get("description") or ""),
                "fixes": fixes,
            }
            prev = [{"version": p.get("version"),
                     "date": _iso_date(p.get("releaseDateString")),
                     "url": p.get("fileUrl"),
                     "size": p.get("fileSize")}
                    for p in drv.get("previousVersionOfDriversList")
                    or []]
            entry["prev"] = prev
            out.append(entry)
    return out


def _iso_date(raw: str | None) -> str | None:
    """'Nov 20, 2025' -> '2025-11-20'."""
    match = re.match(r"\s*([A-Za-z]{3})[a-z]*\s+(\d{1,2}),?\s+(\d{4})",
                     raw or "")
    if not match or match.group(1).lower()[:3] not in _MONTHS:
        return None
    return (f"{match.group(3)}-{_MONTHS[match.group(1).lower()[:3]]:02d}"
            f"-{int(match.group(2)):02d}")


def _md(frag: str) -> str:
    """HTML-Fragment -> Markdown-Text (Links, Code, Entities)."""
    frag = _A_RE.sub(lambda m: f"[{_STRIP_RE.sub('', m.group(2))}]"
                             f"({m.group(1)})", frag)
    frag = _CODE_RE.sub(r"`\1`", frag)
    return _html.unescape(_STRIP_RE.sub("", frag)).strip()


def extract(text: str) -> str:
    """Kombinierter Wert '<dock>=<version>;...' (text = osVersionData
    des ersten Produkts, die Daten kommen aus driverDetails-POSTs)."""
    parts = []
    for oid, label in PRODUCTS.items():
        fw = _firmware(oid)
        if not fw:
            raise ValueError(f"Keine Firmware für {label} ({oid})")
        parts.append(f"{label}={fw[0]['version']}")
    return ";".join(parts)


def extract_history(text: str) -> list[dict]:
    """Aktuelle + Vorgängerversionen je Dock (mit Datum)."""
    releases = []
    for oid, label in PRODUCTS.items():
        for fw in _firmware(oid):
            releases.append({"version": fw["version"],
                             "date": fw["date"]})
            releases.extend({"version": p["version"],
                             "date": p["date"]}
                            for p in fw["prev"])
    return releases


def update_changelog(existing: str | None) -> str | None:
    """Archiv inkrementell: fehlende Versionen als Abschnitt
    '## <dock> – <version> – <datum>' oben einfügen.
    Rückgabe: kompletter neuer Inhalt oder None (unverändert)."""
    have = set(_HEAD_RE.findall(existing or ""))
    parts = [p.strip() for p in re.split(r"(?m)^(?=## )", existing or "")
             if p.strip()]
    new_sections = []
    for oid, label in PRODUCTS.items():
        for fw in _firmware(oid):
            if (label, fw["version"]) in have:
                continue
            body = []
            if fw["description"]:
                body.append(fw["description"])
            if fw["fixes"]:
                fixes = "\n".join(f"- {f}" for f in fw["fixes"])
                body.append(f"**Fixes/Enhancements:**\n\n{fixes}")
            if fw["url"]:
                body.append(f"Download: {fw['url']} ({fw['size']})")
            new_sections.append(
                f"## {label}: {fw['version']} – "
                f"{fw['date'] or 'n/a'}\n\n" + "\n\n".join(body))
    if not new_sections:
        return None
    return "\n\n".join(new_sections + parts)


def list_downloads(text: str, have: set, target_dir) -> list[dict]:
    """Aktuelles Firmware-.exe je Dock ->
    '<slug>-firmware-<version>-spNNNNNN.exe'."""
    items = []
    for oid, label in PRODUCTS.items():
        for fw in _firmware(oid):
            if not fw.get("url"):
                continue
            sp = _SP_RE.search(fw["url"])
            version = re.sub(r"[^\w.-]+", "-", fw["version"] or "?")
            name = (f"{label.lower().replace(' ', '-')}-firmware-"
                    f"{version}-{sp.group(1) if sp else 'hp'}.exe")
            if name not in have:
                items.append({"url": fw["url"], "filename": name})
    return items
