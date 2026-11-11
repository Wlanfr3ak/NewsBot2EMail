"""Seiten-Modul: GitLab – https://gitlab.com/gitlab-org/gitlab

Überwacht die drei neuesten Minor-Zweige (aktuell 19.5/19.4/19.3)
über die öffentliche Tags-API von gitlab.com. GitLab liefert Patches
jeweils für den aktuellen und die zwei vorherigen Minor-Zweige - der
kombinierte Vergleichswert '19.5=19.5.1;19.4=19.4.3;19.3=19.3.6'
meldet jedes neue Release, auch Backports auf ältere Zweige, und
löst EINE Benachrichtigung für alle Zweige aus (wie beim PHP-Modul).

Hinweis: die Releases-API von gitlab.com ist anonym gesperrt (403),
die Tags-API liefert aber Version + committed_date problemlos.

Historie: alle stabilen '-ee'-Tags mit Datum (RCs werden gefiltert).
Changelog: die Feature-Notes der Minor-Releases kommen aus dem
Atom-Feed docs.gitlab.com/releases/releases.xml; Patch-Releases
verlinken ihren Release-Post und listen dessen Security-Fixes.
Archiv: archive/gitlab_changelog.md.

CVE-Filter (site_options.gitlab.cve_only = true): meldet nur
Releases mit nachgewiesenen Security-Fixes. Seit April 2024 legt
GitLab Patch- und Security-Releases zusammen - jede Release-Welle
bekommt einen Post unter
  docs.gitlab.com/releases/patches/patch-release-gitlab-<höchste
  Version der Welle>-released/
Enthält der Post CVE-Einträge (Sektion 'Security fixes'/'Security
update' mit Tabelle + CVE-IDs), zählt die Welle als CVE-Release.
Der Vergleichswert zeigt dann je Zweig die NEUESTE CVE-bestaetigte
Version - reine Bugfix-Releases (~24 % der Wellen) veraendern den
Wert nicht und loesen keine Mail aus. Minor-Releases (X.Y.0)
zaehlen immer: sie enthalten alle akkumulierten Fixes des Zweigs.
Posts erscheinen oft erst Stunden nach den Tags - ein Post, der
(404) noch fehlt oder die Version nicht abdeckt, gilt als
'unbekannt' und wird spaeter erneut geprueft; deshalb traegt die
Tags-URL im CVE-Modus einen Zeitparameter, der den ETag-304-
Fastpath umgeht (Module werden pro Check-Zyklus neu geladen).

Optionen in config.json:

  "site_options": { "gitlab": { "branches": 3, "cve_only": true } }

Keine Downloads.
"""

import html as _html
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

NAME = "GitLab"
URL = ("https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab/"
       "repository/tags?per_page=100&order_by=updated&sort=desc")
NOTES = "Releases: https://docs.gitlab.com/releases/"
SLUG = "gitlab"
CHANGELOG_URL = "https://docs.gitlab.com/releases/"


def _options() -> dict:
    """site_options.gitlab aus config.json (optional)."""
    try:
        cfg = Path(__file__).resolve().parent.parent / "config.json"
        data = json.loads(cfg.read_text(encoding="utf-8"))
        return data.get("site_options", {}).get("gitlab", {})
    except Exception:
        return {}


_OPTS = _options()

# Anzahl der überwachten Minor-Zweige (GitLab patcht aktuell + 2 zurück).
BRANCHES = int(_OPTS.get("branches") or 3)

# True = nur Releases mit CVE-Fixes melden.
CVE_ONLY = bool(_OPTS.get("cve_only"))

if CVE_ONLY:
    # Zeitparameter umgeht den ETag-304-Fastpath, damit ein noch
    # fehlender Patch-Post beim nächsten Lauf erneut geprüft wird.
    URL += f"&_cve={int(time.time())}"
    NOTES += " (nur CVE-Releases)"

_UA = "NewsBot/1.25"
_FEED_URL = "https://docs.gitlab.com/releases/releases.xml"
_SITEMAP_URL = "https://docs.gitlab.com/en-us/sitemap.xml"
_PATCH_URL = ("https://docs.gitlab.com/releases/patches/"
              "patch-release-gitlab-{}-released/")
_CVE_SCAN = 8       # Rueckwaerts-Fenster pro Zweig (cve_only)
_SITEMAP_SCAN = 8   # neueste Patch-Posts im Sitemap-Fallback

_TAG_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)-ee$")   # '-rc…' fällt weg
_ENTRY_RE = re.compile(r"<entry>(.*?)</entry>", re.S)
_TITLE_RE = re.compile(r"<title[^>]*>\s*GitLab (\d+\.\d+) release notes")
_LINK_RE = re.compile(r'<link[^>]*href="([^"]+)"')
_UPDATED_RE = re.compile(r"<updated>([\d-]+)T")
_H3_RE = re.compile(r"<h3[^>]*>(.*?)</h3>", re.S)
_STRIP_RE = re.compile(r"<[^>]+>")
_HEAD_RE = re.compile(r"^## (\S+) – (\S+)", re.M)
_H2_RE = re.compile(r"<h2")
_VERS_RE = re.compile(r"\d+\.\d+\.\d+")
_CVE_RE = re.compile(r"CVE-\d{4}-\d{4,}")
_SEC_RE = re.compile(r"<h2[^>]*id=[\"']?security", re.I)
_SEC_ROW_RE = re.compile(
    r"<tr[^>]*>\s*<td[^>]*><a href=([^ >]+)[^>]*>(.*?)</a></td>\s*"
    r"<td[^>]*>([^<]*)</td>\s*</tr>", re.S)
_PATCH_SLUG_RE = re.compile(
    r"patch-release-gitlab-(\d+-\d+-\d+)-released")


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def _ver_key(version: str) -> tuple:
    return tuple(int(p) for p in version.split("."))


def _stable(text: str) -> list[dict]:
    """Stabile Tags des Tag-API-JSON: {version, date}, RCs gefiltert."""
    out = []
    for tag in json.loads(text):
        m = _TAG_RE.match(tag.get("name") or "")
        if not m:
            continue
        date = ((tag.get("commit") or {}).get("committed_date")
                or tag.get("created_at") or "")[:10] or None
        out.append({"version": m.group(0)[1:-3], "date": date})
    return out


def _latest_per_branch(stable: list[dict]) -> dict[tuple, str]:
    """Höchste Patch-Version je Minor-Zweig {(19, 5): '19.5.1'}."""
    latest = {}
    for r in stable:
        branch = _ver_key(r["version"])[:2]
        if branch not in latest or _ver_key(r["version"]) > _ver_key(latest[branch]):
            latest[branch] = r["version"]
    return latest


def _parse_post(page: str) -> dict:
    """Patch-Release-Post -> {title, versions, cves, fixes}.
    'versions' = alle im Titel genannten Versionen (die Welle),
    'fixes' = Zeilen der Security-Tabelle (cve/severity/title)."""
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", page, re.S)
    title = (_html.unescape(_STRIP_RE.sub("", h1.group(1))).strip()
             if h1 else "")
    text = _html.unescape(_STRIP_RE.sub(" ", page))
    fixes = []
    sec = _SEC_RE.search(page)
    if sec:
        seg = page[sec.end():]
        nxt = _H2_RE.search(seg)
        if nxt:
            seg = seg[:nxt.start()]
        for href, t, sev in _SEC_ROW_RE.findall(seg):
            m = re.search(r"(cve-\d{4}-\d+)", href)
            fixes.append({
                "cve": m.group(1).upper() if m else None,
                "severity": _html.unescape(sev).strip(),
                "title": _html.unescape(_STRIP_RE.sub("", t)).strip()})
    return {"title": title,
            "versions": _VERS_RE.findall(title),
            "cves": sorted(set(_CVE_RE.findall(text))),
            "fixes": fixes}


def _patch_post(version: str, cache: dict) -> dict | None:
    """Post-Page zur Slug-Version (z. B. '19.5.4' oder '19-5-4');
    None bei 404 (Post noch nicht online), Cache je Slug."""
    slug = version.replace(".", "-")
    if slug not in cache:
        try:
            cache[slug] = _parse_post(_fetch(_PATCH_URL.format(slug)))
        except urllib.error.HTTPError as exc:
            exc.close()   # HTTPError ist file-like (ResourceWarning)
            if exc.code != 404:
                raise
            cache[slug] = None
    return cache[slug]


def _sitemap_slugs(cache: dict) -> list:
    """Neueste Patch-Post-Slugs aus dem Sitemap (Fallback, wenn der
    Post einer Welle nicht nach der hoechsten Tag-Version benannt
    ist - z. B. verspaetet nachgetaggte Versionen)."""
    if "sitemap" not in cache:
        try:
            text = _fetch(_SITEMAP_URL)
            slugs = sorted(set(_PATCH_SLUG_RE.findall(text)),
                           key=lambda s: _ver_key(s.replace("-", ".")),
                           reverse=True)
            cache["sitemap"] = slugs[:_SITEMAP_SCAN]
        except Exception:
            cache["sitemap"] = []
    return cache["sitemap"]


def _post_for(version: str, stable: list[dict], cache: dict):
    """Patch-Post der Release-Welle, die 'version' abdeckt.
    Rückgabe (post|None, url|None); Netzfehler gehen durch.
    Kandidaten: hoechste am selben Tag getaggte Version (Wellen
    werden gemeinsam getaggt), dann die Version selbst, zuletzt
    die juengsten Posts aus dem Sitemap (Titel-Versionsliste)."""
    date = next((r["date"] for r in stable
                 if r["version"] == version), None)
    candidates = [version]
    if date:
        wave = [r["version"] for r in stable if r["date"] == date]
        top = max(wave, key=_ver_key, default=None)
        if top:
            candidates.insert(0, top)
    for cand in dict.fromkeys(candidates):
        post = _patch_post(cand, cache)
        if post and (cand == version or version in post["versions"]):
            slug = cand.replace(".", "-")
            return post, _PATCH_URL.format(slug)
    for slug in _sitemap_slugs(cache):
        post = _patch_post(slug, cache)
        if post and version in post["versions"]:
            return post, _PATCH_URL.format(slug)
    return None, None


def _release_security(version: str, stable: list[dict],
                      cache: dict) -> bool | None:
    """True = Release mit CVE-Fixes, False = reines Bugfix-Release,
    None = Post (noch) nicht auffindbar/bestimmbar.
    Minor-Releases (X.Y.0) zaehlen als CVE-Release: sie enthalten
    alle bis dahin veroeffentlichten Fixes ihres Zweigs."""
    if version.endswith(".0"):
        return True
    post, _ = _post_for(version, stable, cache)
    if post is None:
        return None
    return bool(post["cves"] or post["fixes"])


def extract(text: str) -> str:
    """Kombinierter Wert '19.5=19.5.1;19.4=19.4.3;19.3=19.3.6'.
    Mit cve_only wird je Zweig die neueste Version gemeldet, die
    nachweislich Security-Fixes enthaelt - reine Bugfix-Releases
    veraendern den Wert dann nicht und bleiben still."""
    stable = _stable(text)
    latest = _latest_per_branch(stable)
    if not latest:
        raise ValueError("Keine stabilen GitLab-Tags gefunden")
    top = sorted(latest, reverse=True)[:BRANCHES]
    if not CVE_ONLY:
        return ";".join(f"{b[0]}.{b[1]}={latest[b]}" for b in top)
    by_branch = {}
    for r in stable:
        by_branch.setdefault(_ver_key(r["version"])[:2],
                             []).append(r["version"])
    cache = {}
    parts = []
    for b in top:
        reported = None
        recent = sorted(by_branch.get(b, []), key=_ver_key,
                        reverse=True)[:_CVE_SCAN]
        for v in recent:
            if _release_security(v, stable, cache):
                reported = v
                break
        parts.append(f"{b[0]}.{b[1]}={reported or '?'}")
    return ";".join(parts)


def extract_history(text: str) -> list[dict]:
    """Alle stabilen Tags, neueste Version zuerst."""
    return sorted(_stable(text),
                  key=lambda r: _ver_key(r["version"]), reverse=True)


def _release_notes() -> dict[str, dict]:
    """Minor-Release-Notes aus dem Atom-Feed:
    {'19.5': {'date', 'link', 'features': [...]}}."""
    notes = {}
    for entry in _ENTRY_RE.findall(_fetch(_FEED_URL)):
        m = _TITLE_RE.search(entry)
        if not m:
            continue
        link = _LINK_RE.search(entry)
        date = _UPDATED_RE.search(entry)
        content = (entry.split("<content", 1)[1].split(">", 1)[1]
                   .split("</content>", 1)[0]
                   if "<content" in entry else "")
        content = content.replace("<![CDATA[", "").replace("]]>", "")
        features = [_html.unescape(_STRIP_RE.sub("", h)).strip()
                    for h in _H3_RE.findall(content)]
        notes[m.group(1)] = {
            "date": date.group(1) if date else None,
            "link": link.group(1) if link else "",
            "features": [f for f in features if f],
        }
    return notes


def update_changelog(existing: str | None) -> str | None:
    """Archiv inkrementell: fehlende Versionen als Abschnitt
    '## <version> – <datum>' oben einfügen. Minor-Releases (X.Y.0)
    bekommen die Feature-Liste aus dem Release-Post; Patch-Releases
    verlinken ihren Wellen-Post und listen dessen Security-Fixes
    (CVE + Severity + Titel), reine Bugfix-Releases sind als solche
    markiert. Rückgabe: kompletter neuer Inhalt oder None."""
    stable = extract_history(_fetch(URL))
    notes = _release_notes()
    have = {m[0] for m in _HEAD_RE.findall(existing or "")}
    parts = [p.strip() for p in re.split(r"(?m)^(?=## )", existing or "")
             if p.strip()]
    cache = {}
    new_sections = []
    for r in stable:
        version = r["version"]
        if version in have:
            continue
        branch = ".".join(version.split(".")[:2])
        note = notes.get(branch) or {}
        if version.endswith(".0") and note:
            body = "\n".join(f"- {f}" for f in note["features"])
            if note.get("link"):
                body += f"\n\nRelease Notes: {note['link']}"
        else:
            post, purl = _post_for(version, stable, cache)
            if post and (post["cves"] or post["fixes"]):
                lines = []
                listed = set()
                for f in post["fixes"]:
                    listed.add(f["cve"])
                    label = " ".join(
                        p for p in (f["cve"], f"({f['severity']})"
                                    if f["severity"] else "") if p)
                    lines.append(f"- {label + ': ' if label else ''}"
                                 f"{f['title']}")
                for cve in post["cves"]:
                    if cve not in listed:
                        lines.append(f"- {cve}")
                body = (f"Patch-Release: {purl} (Tag v{version}-ee)\n\n"
                        "Security-Fixes:\n" + "\n".join(lines))
            elif post is not None:
                body = (f"Patch-Release (nur Bugfixes): {purl} "
                        f"(Tag v{version}-ee)")
            else:
                body = ("Patch-Release (Security-/Bugfixes) - Details: "
                        f"{CHANGELOG_URL} (Tag v{version}-ee)")
        new_sections.append(
            f"## {version} – {r['date'] or 'n/a'}\n\n{body}")
    if not new_sections:
        return None
    return "\n\n".join(new_sections + parts)
