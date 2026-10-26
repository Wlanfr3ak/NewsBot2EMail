"""Seiten-Modul: PHP – https://www.php.net/

Überwacht die vier aktiv gepflegten Hauptversionen 8.5/8.4/8.3/8.2
gemeinsam (GitHub-Issue #3): der Vergleichswert ist kombiniert
('8.5=8.5.12;8.4=8.4.27;8.3=8.3.36;8.2=8.2.35') - eine neue Version in
irgendeinem Zweig löst EINE Benachrichtigung für alle Zweige aus.

Quelle ist die offizielle Release-JSON
(php.net/releases/index.php?json&version=8&max=300): sie liefert alle
8.x-Releases mit Datum, Security-Tag und Quell-Archiven.

Historie: alle Releases der überwachten Zweige mit Datum.
Changelog: ChangeLog-8.php wird in Markdown-Abschnitte
'## <version> – <datum>' überführt (Unterpunkte je Komponente,
Links bleiben klickbar); Security-Releases sind markiert.
Archiv: archive/php_changelog.md.

BRANCHES lässt sich in config.json überschreiben:

  "site_options": { "php": { "branches": ["8.5", "8.4"] } }

Keine Downloads (Quell-Tarballs; Windows-Builds liegen auf
windows.php.net).
"""

import html as _html
import json
import re
import urllib.request
from pathlib import Path

NAME = "PHP"
URL = "https://www.php.net/releases/index.php?json&version=8&max=300"
NOTES = "Downloads: https://www.php.net/downloads.php"
SLUG = "php"
CHANGELOG_URL = "https://www.php.net/ChangeLog-8.php"


def _options() -> dict:
    """site_options.php aus config.json (optional)."""
    try:
        cfg = Path(__file__).resolve().parent.parent / "config.json"
        data = json.loads(cfg.read_text(encoding="utf-8"))
        return data.get("site_options", {}).get("php", {})
    except Exception:
        return {}


_OPTS = _options()

# Überwachte Hauptversionen (Issue #3: 8.5, 8.4, 8.3, 8.2).
BRANCHES = _OPTS.get("branches") or ["8.5", "8.4", "8.3", "8.2"]

_UA = "NewsBot/1.18"
_SECTION_RE = re.compile(
    r'<section class="version" id="([\d.]+)">(.*?)</section>', re.S)
_DATE_RE = re.compile(r"<time[^>]*datetime='(\d{4}-\d{2}-\d{2})'")
_UL_LI_RE = re.compile(r"</?(?:ul|li)\b[^>]*>", re.I)
_UL_RE = re.compile(r"<ul\b[^>]*>", re.I)
_A_RE = re.compile(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S)
_CODE_RE = re.compile(r"<code>(.*?)</code>", re.S)
_STRIP_RE = re.compile(r"<[^>]+>")
_HEAD_RE = re.compile(r"^## (\S+) – (\S+)", re.M)
_STABLE_RE = re.compile(r"^\d+\.\d+\.\d+$")   # RCs/Betas aussortieren
_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
           "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def _ver_key(version: str) -> tuple:
    return tuple(int(p) for p in version.split("."))


def _branch(version: str) -> str:
    """'8.4.27' -> '8.4'."""
    return version.rsplit(".", 1)[0]


def _latest_per_branch(data: dict) -> dict[str, str]:
    """Höchste Versionsnummer je überwachtem Zweig."""
    latest = {}
    for version in data:
        if not _STABLE_RE.match(version):
            continue
        branch = _branch(version)
        if branch in BRANCHES and (
                branch not in latest
                or _ver_key(version) > _ver_key(latest[branch])):
            latest[branch] = version
    return latest


def extract(text: str) -> str:
    """Kombinierter Wert '8.5=8.5.12;8.4=8.4.27;...'."""
    latest = _latest_per_branch(json.loads(text))
    if not latest:
        raise ValueError("Keine PHP-Versionen der Zweige "
                         f"{BRANCHES} im Release-JSON gefunden")
    return ";".join(f"{b}={latest[b]}" for b in BRANCHES if b in latest)


def _iso_date(raw: str | None) -> str | None:
    """'21 Oct 2026' -> '2026-10-21'."""
    match = re.match(r"\s*(\d{1,2})\s+([A-Za-z]{3})\s+(\d{4})",
                     raw or "")
    if not match or match.group(2).lower() not in _MONTHS:
        return None
    return (f"{match.group(3)}-{_MONTHS[match.group(2).lower()]:02d}"
            f"-{int(match.group(1)):02d}")


def extract_history(text: str) -> list[dict]:
    """Alle Releases der überwachten Zweige (JSON ist neueste zuerst)."""
    return [{"version": v, "date": _iso_date(info.get("date"))}
            for v, info in json.loads(text).items()
            if _STABLE_RE.match(v) and _branch(v) in BRANCHES]


def _md(frag: str) -> str:
    """HTML-Fragment -> Markdown-Text (Links, Code, Entities)."""
    frag = _A_RE.sub(lambda m: f"[{_STRIP_RE.sub('', m.group(2))}]"
                             f"({m.group(1)})", frag)
    frag = _CODE_RE.sub(r"`\1`", frag)
    return _html.unescape(_STRIP_RE.sub("", frag)).strip()


def _list_inner(html: str) -> str:
    """Inhalt der ersten <ul> im Block (balanciert, inkl. Tiefe)."""
    m = _UL_RE.search(html)
    if not m:
        return ""
    depth = 1
    for t in _UL_LI_RE.finditer(html, m.end()):
        tag = t.group(0).lower()
        if tag.startswith("<ul"):
            depth += 1
        elif tag.startswith("</ul"):
            depth -= 1
            if depth == 0:
                return html[m.end():t.start()]
    return html[m.end():]


def _lis(inner: str) -> list[str]:
    """Roh-HTML der Top-Level-<li>-Einträge einer Listen-Innenseite."""
    items, depth, cur = [], 0, None
    for t in _UL_LI_RE.finditer(inner):
        tag = t.group(0).lower()
        if tag.startswith("<ul"):
            depth += 1
        elif tag.startswith("</ul"):
            depth -= 1
        elif tag.startswith("<li") and depth == 0:
            cur = t.end()
        elif tag.startswith("</li") and depth == 0 and cur is not None:
            items.append(inner[cur:t.start()])
            cur = None
    if cur is not None:
        items.append(inner[cur:])
    return items


def _version_md(block: str) -> str:
    """ChangeLog-8.php-Abschnitt -> Markdown.

    Struktur upstream: '<li>Komponente:<ul><li>Eintrag</li>…</ul></li>'
    wird zu '- **Komponente:**' mit eingerückten Unterpunkten."""
    lines = []
    for item in _lis(_list_inner(block)):
        m = _UL_RE.search(item)
        if not m:
            text = _md(item)
            if text:
                lines.append(f"- {text}")
            continue
        label = _md(item[:m.start()]).rstrip(":").strip()
        lines.append(f"- **{label}:**" if label else "-")
        for sub in _lis(_list_inner(item)):
            text = _md(sub)
            if text:
                lines.append(f"  - {text}")
    return "\n".join(lines)


def _security_versions() -> set[str]:
    """Versionen mit 'security'-Tag aus dem Release-JSON."""
    try:
        data = json.loads(_fetch(URL))
    except Exception:
        return set()
    return {v for v, info in data.items()
            if "security" in (info.get("tags") or [])}


def update_changelog(existing: str | None) -> str | None:
    """Archiv inkrementell: fehlende Versionsabschnitte aus
    ChangeLog-8.php als '## <version> – <datum>' oben einfügen.
    Rückgabe: kompletter neuer Inhalt oder None (unverändert)."""
    page = _fetch(CHANGELOG_URL)
    security = _security_versions()
    have = {m[0] for m in _HEAD_RE.findall(existing or "")}
    parts = [p.strip() for p in re.split(r"(?m)^(?=## )", existing or "")
             if p.strip()]
    new_sections = []
    for version, block in _SECTION_RE.findall(page):
        if _branch(version) not in BRANCHES or version in have:
            continue
        m = _DATE_RE.search(block)
        date = m.group(1) if m else "n/a"
        suffix = " (Security Release)" if version in security else ""
        body = _version_md(block) or "_Keine Einträge._"
        new_sections.append(f"## {version} – {date}{suffix}\n\n{body}")
    if not new_sections:
        return None
    return "\n\n".join(new_sections + parts)
