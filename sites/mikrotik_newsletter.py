"""Seiten-Modul: MikroTik Newsletter – https://mikrotik.com/

Die Homepage listet die neuesten Newsletter als mt.lv/newsNNN-Links
("Newsletter #133 | June 2026"). mt.lv leitet auf einen Seafile-Share
(box.mikrotik.com) weiter, dessen HTML den direkten PDF-Link
(seafhttp) enthält.

Über list_downloads() werden ALLE Newsletter-PDFs ab OLDEST in
downloads/mikrotik-newsletter/ archiviert - nicht nur die auf der
Startseite verlinkten. Nicht auflösbare Nummern bekommen eine
.news_N.pdf.missing-Markierung und werden nicht erneut versucht.

Neue Newsletter erscheinen mitunter auf mt.lv, BEVOR sie auf der
Homepage verlinkt sind (z. B. ging mt.lv/news135 schon, als die
Seite nur bis #134 verlinkte). Daher probieren extract() und
list_downloads() ab der höchsten verlinkten Nummer weiter, bis der
erste Kurzlink nicht auflöst (404) - höchstens PROBE_LIMIT weit. Im Voraus-Probebereich werden
Fehlschläge NICHT als .missing markiert - die Nummer kann ja später
noch live gehen.

Die mt.lv-Kurzlinks existieren erst ab #77; die Redirect-Ziele
wechseln über die Jahre: direkte PDFs (download2.mikrotik.com,
S3-Bucket) oder Seafile-Shares (box.mikrotik.com, dort liefert
die Share-URL + '?dl=1' die Datei direkt).
"""

import re
import urllib.error
import urllib.request

NAME = "MikroTik Newsletter"
URL = "https://mikrotik.com/"
NOTES = "Archiv: downloads/mikrotik-newsletter/"
SLUG = "mikrotik-newsletter"

OLDEST = 77  # Newsletter ab dieser Nummer archivieren (#1-76 existieren nicht)

# Sicherheitsgrenze für die Voraus-Probe: stoppt die Schleife auch
# dann, wenn mt.lv irgendwann für beliebige Nummern weiterleitet
# (statt 404). So weit springt die Nummerierung real nie.
PROBE_LIMIT = 5

_UA = "NewsBot/1.5"
_LINK_RE = re.compile(r"mt\.lv/news(\d+)")
_TITLE_RE = re.compile(r"Newsletter #(\d+)\s*\|\s*([A-Za-z]+)\s+(\d{4})")

_MONTHS = {
    "january": "01", "february": "02", "march": "03", "april": "04",
    "may": "05", "june": "06", "july": "07", "august": "08",
    "september": "09", "october": "10", "november": "11", "december": "12",
}


def _numbers(text: str) -> list[int]:
    """Alle auf der Seite verlinkten Newsletter-Nummern."""
    return sorted({int(n) for n in _LINK_RE.findall(text)})


def _probe_ahead(linked_max: int) -> int:
    """Höchste auf mt.lv auflösbare Newsletter-Nummer ab linked_max.

    Stoppt beim ersten nicht auflösbaren Kurzlink - spätestens aber
    nach PROBE_LIMIT Nummern (Schutz vor Endlosschleife, falls mt.lv
    künftig für beliebige Nummern weiterleitet statt 404 zu liefern).
    Gibt linked_max zurück, wenn schon die nächste Nummer fehlt.
    """
    latest = linked_max
    while latest - linked_max < PROBE_LIMIT:
        try:
            _resolve_pdf_url(latest + 1)
        except Exception:
            break
        latest += 1
    return latest


def extract(text: str) -> str:
    """Neueste Newsletter-Nummer (z. B. '133'), inkl. Voraus-Probe."""
    numbers = _numbers(text)
    if not numbers:
        raise ValueError("Keine Newsletter-Links auf mikrotik.com gefunden")
    return str(_probe_ahead(numbers[-1]))


def extract_history(text: str) -> list[dict]:
    """Verlinkte Newsletter mit Ausgabemonat [{version, date}]."""
    releases = []
    for num, month, year in _TITLE_RE.findall(text):
        releases.append({
            "version": num,
            "date": f"{year}-{_MONTHS.get(month.lower(), '01')}",
        })
    releases.sort(key=lambda r: int(r["version"]), reverse=True)
    return releases


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def _resolve_pdf_url(number: int) -> str:
    """mt.lv/newsNNN -> Redirect-Ziel -> direkte PDF-URL.

    Ziel-Typen: direkte PDFs (download2/S3), Seafile-Share mit
    '?dl=1' (direkt ladbar) oder Share-Seite (dann '?dl=1' anhängen).
    """
    opener = urllib.request.build_opener(_NoRedirect)
    req = urllib.request.Request(
        f"https://mt.lv/news{number}", headers={"User-Agent": _UA})
    try:
        with opener.open(req, timeout=30) as resp:
            location = resp.headers.get("Location") or ""
    except urllib.error.HTTPError as exc:
        if exc.code in (301, 302, 303, 307, 308):
            location = exc.headers.get("Location") or ""
        else:
            raise ValueError(f"Newsletter #{number}: HTTP {exc.code}")
    if not location:
        raise ValueError(f"Kein Redirect-Ziel für Newsletter #{number}")
    if "box.mikrotik.com/f/" in location and "dl=1" not in location:
        location = location.rstrip("/") + "/?dl=1"
    return location


def list_downloads(text: str, have: set, target_dir) -> list[dict]:
    """Alle Newsletter-PDFs ab OLDEST, die lokal noch fehlen.

    Nicht auflösbare Nummern im verlinkten Bereich werden mit einer
    .missing-Datei markiert, damit sie nicht bei jedem Lauf erneut
    versucht werden. Oberhalb der höchsten verlinkten Nummer wird
    vorgeprobt (s. _probe_ahead); Fehlschläge dort werden nicht
    markiert, sondern beim nächsten Lauf erneut versucht.
    """
    numbers = _numbers(text)
    if not numbers:
        return []
    linked_max = numbers[-1]
    items = []
    for number in range(OLDEST, _probe_ahead(linked_max) + 1):
        filename = f"news_{number}.pdf"
        if filename in have or filename + ".missing" in have:
            continue
        try:
            url = _resolve_pdf_url(number)
        except Exception:
            if number <= linked_max:
                target_dir.mkdir(parents=True, exist_ok=True)
                (target_dir / (filename + ".missing")).touch()
            continue
        items.append({"url": url, "filename": filename})
    return items
