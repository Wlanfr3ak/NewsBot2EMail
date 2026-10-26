"""Seiten-Modul: Twitch Drops (GitHub-Issue #1)

Überwacht Drops-Seiten von Spielen auf neue Kampagnen. Twitch
selbst hat keine öffentliche Kampagnen-API und die
Drops-Übersicht braucht einen Login - daher werden die
Drops-Seiten der Spiele direkt beobachtet (Default: Gray Zone
Warfare, twitch.grayzonewarfare.com).

Erkennung (generisch, funktioniert auf beliebigen Seiten):
- alle ISO-Zeitstempel im HTML (z. B. der Kampagnen-Countdown
  'targetDate' im Next.js-Payload),
- sichtbare Sätze mit 'drop'/'campaign'/'twitch' (laufende
  Countdown-Zahlen wie '12 Days 3 Hours' werden dabei neutralisiert,
  sonst würde jeder Check eine Änderung melden).
Aus beidem wird eine Signatur gehasht; der Vergleichswert ist
'<label>=<hash>;...' über alle konfigurierten Seiten - jede
Inhaltsänderung einer Kampagnen-Sektion löst eine Mail aus.

Seiten in config.json wählbar (Dict URL->Label oder Liste von URLs,
Label = Hostname; Default = Gray Zone Warfare):

  "site_options": {
    "twitch_drops": {
      "urls": {"https://twitch.grayzonewarfare.com/": "Gray Zone Warfare"}
    }
  }

Historie: Signatur ohne echtes Datum.
Changelog: je neuer Signatur werden die erkannten Schlusselfragmente
(Text + ISO-Daten) nach archive/twitch-drops_changelog.md
archiviert - so bleibt nachvollziehbar, welche Kampagne wann kam.
"""

import hashlib
import html as _html
import json
import re
import urllib.request
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

def _normalize_urls(raw) -> dict:
    """Liste ['https://…'] oder Dict {url: label} -> {url: label}."""
    if isinstance(raw, dict):
        return {str(u): str(l) for u, l in raw.items()}
    return {str(u): _host_label(str(u)) for u in (raw or [])}


def _host_label(url: str) -> str:
    host = re.sub(r"^https?://|/$", "", url).split("/")[0]
    return host.replace("www.", "")


# URL -> Label; Default: Gray Zone Warfare (Issue #1).
URLS = _normalize_urls(_OPTS.get("urls")) or {URL: "Gray Zone Warfare"}

_UA = "NewsBot/1.20"
_SCRIPT_RE = re.compile(r"<(script|style)\b.*?</\1>", re.S | re.I)
_TAG_RE = re.compile(r"<[^>]+>")
_ISO_RE = re.compile(r"20\d{2}-\d{2}-\d{2}T\d{2}:\d{2}")
_KW_RE = re.compile(r"drop|campaign|kampagne|twitch", re.I)
_COUNTDOWN_RE = re.compile(
    r"\b\d+\s*(?:Days?|Hours?|Minutes?|Min\.?|Secs?\.?|Seconds?)\b", re.I)
_WS_RE = re.compile(r"\s+")
_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+|\n+")
_HEAD_RE = re.compile(r"^## (.+?) – ([0-9a-f]{12}) – ", re.M)


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def _fragments(page: str) -> tuple[list, list]:
    """Relevante Signatur-Fragmente einer Seite:
    (ISO-Zeitstempel, Keyword-Sätze) - beide sortiert, dedupliziert."""
    dates = sorted(set(_ISO_RE.findall(page)))
    body = _SCRIPT_RE.sub(" ", page)
    text = _html.unescape(_WS_RE.sub(" ", _TAG_RE.sub(" ", body)))
    sentences = []
    for part in _SENTENCE_RE.split(text):
        part = part.strip()
        if not _KW_RE.search(part):
            continue
        part = _COUNTDOWN_RE.sub("#", part)   # Countdown-Zahlen neutralisieren
        sentences.append(part)
    return dates, sorted(set(sentences))


def _signature(page: str) -> str:
    """Stabiler Signatur-Hash der Kampagnen-Inhalte einer Seite."""
    dates, sentences = _fragments(page)
    raw = "\n".join(dates) + "\n--\n" + "\n".join(sentences)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]


def _current(text: str | None = None) -> dict[str, str]:
    """{label: signatur} aller konfigurierten Seiten.

    'text' ist die bereits geladene erste Seite (wird wiederverwendet,
    spart einen Request)."""
    out = {}
    first = next(iter(URLS))
    for url, label in URLS.items():
        page = text if url == first and text is not None else _fetch(url)
        out[label] = _signature(page)
    return out


def extract(text: str) -> str:
    """Kombinierter Wert '<label>=<hash>;…' über alle Seiten."""
    return ";".join(f"{label}={sig}"
                    for label, sig in _current(text).items())


def extract_history(text: str) -> list[dict]:
    """Eine Zeile je Seite (kein echtes Upstream-Datum)."""
    return [{"version": f"{label}={sig}", "date": None}
            for label, sig in _current(text).items()]


def update_changelog(existing: str | None) -> str | None:
    """Je neuer Signatur werden die erkannten Fragmente
    (ISO-Daten + Keyword-Sätze) als Abschnitt
    '## <label> – <hash> – <erkannt-am>' oben eingefügt.
    Rückgabe: kompletter neuer Inhalt oder None (unverändert)."""
    have = {m[1] for m in _HEAD_RE.findall(existing or "")}
    parts = [p.strip() for p in re.split(r"(?m)^(?=## )", existing or "")
             if p.strip()]
    new_sections = []
    from datetime import date
    today = date.today().isoformat()
    for url, label in URLS.items():
        page = _fetch(url)
        sig = _signature(page)
        if sig in have:
            continue
        dates, sentences = _fragments(page)
        body = ([f"- `{d}`" for d in dates]
                + ([""] if dates and sentences else [])
                + [f"- {s}" for s in sentences][:40])
        new_sections.append(
            f"## {label} – {sig} – {today}\n\n"
            + ("\n".join(body) or "_Keine Fragmente._"))
    if not new_sections:
        return None
    return "\n\n".join(new_sections + parts)
