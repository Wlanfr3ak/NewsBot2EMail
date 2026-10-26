"""Seiten-Modul: Twitch Drops (GitHub-Issue #1)

Überwacht Drops-Seiten von Spielen auf neue Kampagnen. Twitch hat
keine öffentliche Kampagnen-API (die Drops-Übersicht braucht Login) -
daher werden die Drops-Seiten der Spiele direkt beobachtet.
Default: Gray Zone Warfare (twitch.grayzonewarfare.com).

Erkennung (generisch): die Seiten nennen den Kampagnen-Zeitraum im
Text ('campaign, running from October 22 to November 6', dt.
'22.10.-06.11.') und/oder als ISO-Countdown-Datum im Seiten-Payload.
Aus allen gefundenen Zeiträumen wird ein Status gebaut:
  aktiv       – heute liegt in einem Zeitraum (oder Countdown-Ende
                in der Zukunft),
  angekündigt – ein Zeitraum liegt komplett in der Zukunft,
  keine       – kein (mehr aktueller) Zeitraum gefunden.
Der Vergleichswert ist '<label>=<status>:<name> (<start>..<end>);…'
über alle konfigurierten Seiten - Kampagnenstart, -ende und neue
Ankündigungen lösen jeweils EINE Mail aus. Als
Veröffentlichungsdatum in der Mail gilt der Kampagnen-START.

Seiten in config.json wählbar (Dict URL->Label oder Liste von URLs,
Label = Hostname; Default = Gray Zone Warfare):

  "site_options": {
    "twitch_drops": {
      "urls": {"https://twitch.grayzonewarfare.com/": "Gray Zone Warfare"}
    }
  }

Changelog: pro Kampagne ein Abschnitt
'## <label> – <name> (<start>..<end>)' mit Status und den erkannten
Schlusselfragmenten in archive/twitch-drops_changelog.md.
"""

import html as _html
import json
import re
import urllib.request
from datetime import date, timedelta
from pathlib import Path

NAME = "Twitch Drops"
URL = "https://twitch.grayzonewarfare.com/"
NOTES = "Beispiel: https://twitch.grayzonewarfare.com/"
SLUG = "twitch-drops"
CHANGELOG_URL = "https://www.twitch.tv/drops/campaigns"


def _options() -> dict:
    """site_options.twitch_drops aus config.json (optional)."""
    try:
        cfg = Path(__file__).resolve().parent.parent / "config.json"
        data = json.loads(cfg.read_text(encoding="utf-8"))
        return data.get("site_options", {}).get("twitch_drops", {})
    except Exception:
        return {}


_OPTS = _options()


def _host_label(url: str) -> str:
    host = re.sub(r"^https?://|/$", "", url).split("/")[0]
    return host.replace("www.", "")


def _normalize_urls(raw) -> dict:
    """Liste ['https://…'] oder Dict {url: label} -> {url: label}."""
    if isinstance(raw, dict):
        return {str(u): str(l) for u, l in raw.items()}
    return {str(u): _host_label(str(u)) for u in (raw or [])}


# URL -> Label; Default: Gray Zone Warfare (Issue #1).
URLS = _normalize_urls(_OPTS.get("urls")) or {URL: "Gray Zone Warfare"}

_UA = "NewsBot/1.21"
_SCRIPT_RE = re.compile(r"<(script|style)\b.*?</\1>", re.S | re.I)
_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")
_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+|\n+")
_KW_RE = re.compile(r"drop|campaign|kampagne|twitch", re.I)
_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
           "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
_MON = ("jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun[ei]?"
        "|jul[y]?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?"
        "|nov(?:ember)?|dec(?:ember)?")
# optionaler Uhrzeit-Anhang hinter einem Datum (' at 18:00 CEST')
_TIME_TAIL = r"(?:\s+at\s+\d{1,2}:\d{2}(?::\d{2})?(?:\s+[A-Za-z]{2,6})?)?"
# 'October 22 to November 6' / 'Oct 22nd – Nov 6th'
_RANGE_EN_RE = re.compile(
    rf"({_MON})\s+(\d{{1,2}})(?:st|nd|rd|th)?{_TIME_TAIL}"
    rf"\s*(?:to|until|bis|–|-)\s*"
    rf"({_MON})\s+(\d{{1,2}})(?:st|nd|rd|th)?", re.I)
# '22nd October 2026 at 18:00 CEST until 6th November 2026'
_RANGE_EN2_RE = re.compile(
    rf"(\d{{1,2}})(?:st|nd|rd|th)?\s+({_MON})(?:\s+(\d{{4}}))?{_TIME_TAIL}"
    rf"\s*(?:to|until|bis|–|-)\s*"
    rf"(\d{{1,2}})(?:st|nd|rd|th)?\s+({_MON})(?:\s+(\d{{4}}))?", re.I)
# '22.10.-06.11.' oder '22.10.2026-06.11.2026'
_RANGE_DE_RE = re.compile(
    r"\b(\d{1,2})\.(\d{1,2})\.(?:(\d{4}))?\s*(?:–|-|bis)\s*"
    r"(\d{1,2})\.(\d{1,2})\.(?:(\d{4}))?")
_ISO_RE = re.compile(r"(20\d{2})-(\d{2})-(\d{2})")
# Kampagnenname: 'the Rogue Ops (Twitch Drops) campaign' oder dt.
# 'die X Kampagne'. Der Artikel ist Pflicht, sonst griffe der lazy
# Namensteil den Satzanfang mit ('During the Rogue Ops').
_NAME_RE = re.compile(
    r"(?:the |der |die |das )([A-ZÄÖÜ][\w&' -]{2,40}?)\s+"
    r"(?:Twitch )?(?:Drops )?(?:campaign|kampagne)", re.I)
_HEAD_RE = re.compile(
    r"^## (.+?) – (.+?) \((?:(\d{4}-\d{2}-\d{2})|bis)", re.M)
_TOL = timedelta(days=3)   # ISO-Datum ~ Zeitraum-Ende = gleiche Kampagne


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def _month(name: str) -> int:
    return _MONTHS[name[:3].lower()]


def _mkdate(year: int, mon: int, day: int) -> date | None:
    try:
        return date(year, mon, day)
    except ValueError:
        return None


def _ranges_en(text: str) -> list[tuple[date, date]]:
    """'October 22 to November 6' bzw. '22nd October ... until 6th
    November 2026' -> (start, end); Jahr = aktuelles (oder explizit),
    end < start -> Folgejahr."""
    year = date.today().year
    out = []
    for m in _RANGE_EN_RE.finditer(text):
        start = _mkdate(year, _month(m.group(1)), int(m.group(2)))
        end = _mkdate(year, _month(m.group(3)), int(m.group(4)))
        if start and end:
            if end < start:
                end = date(end.year + 1, end.month, end.day)
            out.append((start, end))
    for m in _RANGE_EN2_RE.finditer(text):
        sy, ey = int(m.group(3) or year), int(m.group(6) or year)
        start = _mkdate(sy, _month(m.group(2)), int(m.group(1)))
        end = _mkdate(ey, _month(m.group(5)), int(m.group(4)))
        if start and end:
            if end < start:
                end = date(end.year + 1, end.month, end.day)
            out.append((start, end))
    return out


def _ranges_de(text: str) -> list[tuple[date, date]]:
    """'22.10.-06.11.2026' -> (start, end)."""
    year = date.today().year
    out = []
    for m in _RANGE_DE_RE.finditer(text):
        sy, ey = int(m.group(3) or year), int(m.group(6) or year)
        start = _mkdate(sy, int(m.group(2)), int(m.group(1)))
        end = _mkdate(ey, int(m.group(5)), int(m.group(4)))
        if start and end:
            if end < start:
                end = date(end.year + 1, end.month, end.day)
            out.append((start, end))
    return out


def _iso_dates(page: str) -> list[date]:
    return [d for y, m, dd in _ISO_RE.findall(page)
            if (d := _mkdate(int(y), int(m), int(dd)))]


def _visible_text(page: str) -> str:
    body = _SCRIPT_RE.sub(" ", page)
    return _html.unescape(_WS_RE.sub(" ", _TAG_RE.sub(" ", body)))


def _sentences(text: str) -> list[str]:
    """Sätze mit Drops-Keywords."""
    return [p.strip() for p in _SENTENCE_RE.split(text)
            if _KW_RE.search(p)]


def _campaign_name(sentences: list[str]) -> str | None:
    """'Rogue Ops' aus 'the Rogue Ops Twitch Drops campaign'."""
    for s in sentences:
        m = _NAME_RE.search(s)
        if m:
            name = m.group(1).strip(" -")
            if name.lower() not in ("twitch", "drops"):
                return name
    return None


def detect(page: str) -> dict:
    """Kampagnen-Status einer Seite.

    Liefert {status, name, start, end, sentences} mit
    status in {'aktiv','angekündigt','keine'}. Zeiträume kommen aus
    Text-Ranges (en/de); ISO-Countdown-Daten ergänzen bzw. bilden
    allein ein 'aktiv bis <datum>'-Zeitraum."""
    text = _visible_text(page)
    sentences = _sentences(text)
    context = " ".join(sentences)
    today = date.today()

    periods = _ranges_en(context) + _ranges_de(context)
    for iso in sorted(set(_iso_dates(page))):
        # ISO-Datum ~ bekanntes Zeitraum-Ende -> gleiche Kampagne
        if any(abs(end - iso) <= _TOL or abs(start - iso) <= _TOL
               for start, end in periods):
            continue
        if iso >= today:
            # Countdown-Ende ohne Text-Zeitraum: läuft bis dahin.
            periods.append((today, iso))

    name = _campaign_name(sentences)
    active = [(s, e) for s, e in periods if s <= today <= e]
    upcoming = [(s, e) for s, e in periods if s > today]
    if active:
        start, end = max(active, key=lambda p: p[1])
        status = "aktiv"
    elif upcoming:
        start, end = min(upcoming)
        status = "angekündigt"
    else:
        start = end = None
        status = "keine"
    return {"status": status, "name": name, "start": start,
            "end": end, "sentences": sentences}


def _label_value(url: str, label: str, page: str | None = None) -> str:
    det = detect(page if page is not None else _fetch(url))
    return _value_part(label, det)


def _value_part(label: str, det: dict) -> str:
    """'<label>=<status>:<name> (<start>..<end>)'."""
    if det["status"] == "keine":
        return f"{label}=keine"
    span = (f"{det['start']}..{det['end']}"
            if det["start"] else f"bis {det['end']}")
    return (f"{label}={det['status']}:{det['name'] or 'Kampagne'} "
            f"({span})")


def extract(text: str) -> str:
    """Kombinierter Status aller konfigurierten Seiten
    ('text' = bereits geladene erste Seite)."""
    first = next(iter(URLS))
    parts = []
    for url, label in URLS.items():
        parts.append(_label_value(
            url, label, text if url == first else None))
    return ";".join(parts)


def extract_history(text: str) -> list[dict]:
    """Je Seite eine Zeile; Datum = Kampagnen-Start (echtes Datum)."""
    first = next(iter(URLS))
    releases = []
    for url, label in URLS.items():
        det = detect(text if url == first else _fetch(url))
        releases.append({"version": _value_part(label, det),
                         "date": det["start"].isoformat()
                         if det["start"] else None})
    return releases


def update_changelog(existing: str | None) -> str | None:
    """Pro erkannter Kampagne ein Abschnitt
    '## <label> – <name> (<start>..<end>)' mit Status + den
    erkannten Schlusselfragmenten; neue Zeiträume landen oben.
    Rückgabe: kompletter neuer Inhalt oder None (unverändert)."""
    have = {"|".join(m) for m in _HEAD_RE.findall(existing or "")}
    parts = [p.strip() for p in re.split(r"(?m)^(?=## )", existing or "")
             if p.strip()]
    new_sections = []
    for url, label in URLS.items():
        det = detect(_fetch(url))
        name = det["name"] or "Kampagne"
        span = (f"{det['start']}..{det['end']}" if det["start"]
                else f"bis {det['end'] or '?'}")
        if det["status"] == "keine":
            continue
        key = (f"{label}|{name}|"
               f"{det['start'].isoformat() if det['start'] else ''}")
        if key in have:
            continue
        body = [f"Status: {det['status']} (Zeitraum {span})",
                f"Seite: {url}"]
        body += ["", *[f"- {s}" for s in det["sentences"][:40]]]
        new_sections.append(
            f"## {label} – {name} ({span})\n\n" + "\n".join(body))
    if not new_sections:
        return None
    return "\n\n".join(new_sections + parts)
