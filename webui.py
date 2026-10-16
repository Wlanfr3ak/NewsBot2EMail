"""Web-Dashboard für NewsBot – reine Standardbibliothek.

Eingebetteter lokaler Webserver (http.server), der Bot-Status,
Versionshistorien, Changelog-Archive und die geladenen Dateien
darstellt. Aufruf:

    server = webui.start(cfg, trigger)

'trigger' ist ein Callable mit optionalem Argument 'slug' (Check nur
für diese Seite, None = alle); Rückgabe True, wenn ein Check
angestoßen wurde, False, wenn gerade einer läuft
("Jetzt prüfen"-Buttons). Konfiguration in config.json:

    "web": {"enabled": true, "host": "127.0.0.1", "port": 8321}

Bindet standardmäßig nur an localhost – es gibt keine
Authentifizierung, also keinen anderen Host ohne Absicherung
einstellen.
"""

import html
import json
import logging
import mimetypes
import threading
import urllib.parse
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

log = logging.getLogger("newsbot.web")

BASE_DIR = Path(__file__).resolve().parent
STATE_PATH = BASE_DIR / "state.json"
LOG_PATH = BASE_DIR / "newsbot.log"
HISTORY_DIR = BASE_DIR / "history"
ARCHIVE_DIR = BASE_DIR / "archive"
DOWNLOAD_DIR = BASE_DIR / "downloads"

_PAGE = """<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – NewsBot</title>
<style>
:root {{ color-scheme: dark; }}
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: #0f1115;
       color: #d8dee9; margin: 0; padding: 2rem; }}
h1 {{ font-size: 1.4rem; margin: 0 0 .2rem; }}
h2 {{ font-size: 1rem; margin: 1.6rem 0 .5rem; color: #88c0d0; }}
a {{ color: #81a1c1; text-decoration: none; }} a:hover {{ text-decoration: underline; }}
.sub {{ color: #7b88a1; font-size: .85rem; margin-bottom: 1.2rem; }}
table {{ border-collapse: collapse; width: 100%; font-size: .9rem; }}
th, td {{ text-align: left; padding: .45rem .7rem; border-bottom: 1px solid #232a38; }}
th {{ color: #7b88a1; font-weight: 600; font-size: .78rem; text-transform: uppercase;
     letter-spacing: .05em; }}
tr:hover td {{ background: #161a23; }}
.badge {{ display: inline-block; padding: .1rem .45rem; border-radius: .4rem;
         font-size: .75rem; background: #2e3440; color: #a3be8c; }}
.badge.pending {{ background: #5e4128; color: #ebcb8b; }}
pre {{ background: #161a23; border: 1px solid #232a38; border-radius: .5rem;
      padding: 1rem; overflow-x: auto; font-size: .85rem; line-height: 1.45; }}
button, .btn {{ background: #2e3440; color: #d8dee9; border: 1px solid #3b4252;
      border-radius: .45rem; padding: .45rem .9rem; font-size: .85rem;
      cursor: pointer; }}
button:hover, .btn:hover {{ background: #3b4252; text-decoration: none; }}
.msg {{ background: #24303f; border: 1px solid #3b4252; border-radius: .45rem;
       padding: .5rem .9rem; margin-bottom: 1rem; font-size: .85rem; }}
.size {{ color: #7b88a1; }}
code {{ background: #232a38; padding: .1rem .3rem; border-radius: .3rem; }}
</style></head><body>
<h1>NewsBot <span class="size">v{version}</span></h1>
<div class="sub">{sub}</div>
{body}
<div class="sub" style="margin-top:2rem">
  <a href="/">Übersicht</a> · <a href="/log">Log</a> ·
  NewsBot v{version}
</div>
</body></html>"""


def _fmt_size(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or unit == "TB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return f"{n} B"


def _fmt_time(iso: str | None) -> str:
    if not iso:
        return "–"
    try:
        return datetime.fromisoformat(iso).strftime("%d.%m.%Y %H:%M")
    except ValueError:
        return iso


def _esc(text) -> str:
    return html.escape(str(text))


def _page(title: str, sub: str, body: str, version: str) -> bytes:
    return _PAGE.format(title=_esc(title), version=version, sub=sub,
                       body=body).encode("utf-8")


def _load_state() -> dict:
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {"sites": {}}


def _dashboard(cfg: dict, collect_sites, msg: str = "") -> str:
    """Übersichtsseite: alle Seiten mit Stand, Historie, Downloads."""
    state = _load_state()
    sites = collect_sites(cfg)
    version = cfg.get("_version", "?")

    last = max((e.get("last_checked") or "" for e in
                state.get("sites", {}).values()), default="")
    sub = (f"{len(sites)} überwachte Seiten · letzter Check: "
           f"{_fmt_time(last)}")
    if msg:
        sub = f'<div class="msg">{_esc(msg)}</div>' + sub

    rows = []
    for site in sites:
        entry = state.get("sites", {}).get(site["name"], {})
        value = entry.get("value", "–")
        pending = entry.get("pending_value")
        badge = f'<span class="badge">{_esc(value)}</span>'
        if pending:
            badge += (f' <span class="badge pending">Mail ausstehend: '
                      f'{_esc(pending)}</span>')
        links = []
        if (HISTORY_DIR / f"{site['slug']}.md").exists():
            links.append(f'<a href="/history/{site["slug"]}">Historie</a>')
        if (ARCHIVE_DIR / f"{site['slug']}_changelog.md").exists():
            links.append(f'<a href="/archive/{site["slug"]}">Changelog</a>')
        dl = DOWNLOAD_DIR / site["slug"]
        if dl.is_dir():
            files = [p for p in dl.iterdir() if p.is_file()]
            total = sum(p.stat().st_size for p in files)
            links.append(
                f'<a href="/dl/{site["slug"]}/">Downloads</a> '
                f'<span class="size">({len(files)}, {_fmt_size(total)})</span>')
        rows.append(
            f"<tr><td><b>{_esc(site['name'])}</b><br>"
            f'<a href="{_esc(site["url"])}" class="size">{_esc(site["url"])}</a></td>'
            f"<td>{badge}</td>"
            f"<td>{_fmt_time(entry.get('last_checked'))}</td>"
            f"<td>{_fmt_time(entry.get('last_changed'))}</td>"
            f"<td>{' &middot; '.join(links) or '–'}</td>"
            f'<td><form method="post" action="/check/'
            f'{urllib.parse.quote(site["slug"])}">'
            f'<button type="submit">Prüfen</button></form></td></tr>')

    body = f"""
<form method="post" action="/check" style="margin-bottom:1rem">
  <button type="submit">Alle jetzt prüfen</button>
</form>
<table><tr><th>Seite</th><th>Aktuell</th><th>Letzter Check</th>
<th>Letzte Änderung</th><th>Dateien</th><th></th></tr>
{''.join(rows)}</table>"""
    return _page("Übersicht", sub, body, version)


def _markdown_page(title: str, path: Path, version: str) -> bytes:
    text = path.read_text(encoding="utf-8")
    return _page(title, f'<a href="/">← Übersicht</a> · {path.name}',
                 f"<pre>{_esc(text)}</pre>", version)


def _dl_listing(slug: str, version: str) -> bytes | None:
    target = (DOWNLOAD_DIR / slug).resolve()
    if not str(target).startswith(str(DOWNLOAD_DIR.resolve())) \
            or not target.is_dir():
        return None
    rows = []
    for p in sorted(target.iterdir()):
        if not p.is_file():
            continue
        url = urllib.parse.quote(p.name)
        rows.append(
            f'<tr><td><a href="/dl/{_esc(slug)}/{url}">{_esc(p.name)}</a></td>'
            f'<td class="size">{_fmt_size(p.stat().st_size)}</td></tr>')
    body = (f"<table><tr><th>Datei</th><th>Größe</th></tr>{''.join(rows)}"
            f"</table>" if rows else "<p>Keine Dateien.</p>")
    return _page(f"Downloads {slug}",
                 f'<a href="/">← Übersicht</a> · downloads/{_esc(slug)}/',
                 body, version)


def _log_tail(version: str, lines: int = 200) -> bytes:
    try:
        text = "\n".join(
            LOG_PATH.read_text(encoding="utf-8", errors="replace")
            .splitlines()[-lines:])
    except Exception as exc:
        text = f"(Log nicht lesbar: {exc})"
    return _page("Log", '<a href="/">← Übersicht</a> · newsbot.log',
                 f"<pre>{_esc(text)}</pre>", version)


def _send_file(handler: BaseHTTPRequestHandler, path: Path) -> None:
    """Datei ausliefern, inkl. Range-Support (Resume bei großen ISOs)."""
    size = path.stat().st_size
    ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    start, end = 0, size - 1
    status = 200
    rng = handler.headers.get("Range")
    if rng:
        m = re_range.match(rng)
        if m:
            start = int(m.group(1))
            end = int(m.group(2)) if m.group(2) else size - 1
            end = min(end, size - 1)
            status = 206
    length = end - start + 1
    handler.send_response(status)
    handler.send_header("Content-Type", ctype)
    handler.send_header("Content-Length", str(length))
    handler.send_header("Accept-Ranges", "bytes")
    handler.send_header("Content-Disposition",
                        f'attachment; filename="{path.name}"')
    if status == 206:
        handler.send_header("Content-Range",
                            f"bytes {start}-{end}/{size}")
    handler.end_headers()
    if handler.command == "HEAD":
        return
    with path.open("rb") as f:
        f.seek(start)
        remaining = length
        while remaining > 0:
            chunk = f.read(min(1 << 20, remaining))
            if not chunk:
                break
            try:
                handler.wfile.write(chunk)
            except (BrokenPipeError, ConnectionResetError):
                break
            remaining -= len(chunk)


import re
re_range = re.compile(r"bytes=(\d+)-(\d*)")


def make_handler(cfg: dict, collect_sites, trigger):
    """Request-Handler mit Zugriff auf cfg/Module/Trigger."""

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            log.debug("HTTP %s", fmt % args)

        def _html(self, body: bytes, status: int = 200):
            self.send_response(status)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _redirect(self, to: str):
            self.send_response(303)
            self.send_header("Location", to)
            self.end_headers()

        def _download_path(self, slug: str, fname: str) -> Path | None:
            target = (DOWNLOAD_DIR / slug / fname).resolve()
            try:
                target.relative_to(DOWNLOAD_DIR.resolve())
            except ValueError:
                return None
            return target if target.is_file() else None

        def do_GET(self):  # noqa: N802
            parsed = urllib.parse.urlparse(self.path)
            parts = [urllib.parse.unquote(p)
                     for p in parsed.path.split("/") if p]
            q = urllib.parse.parse_qs(parsed.query)
            try:
                if not parts:
                    msg = q.get("msg", [""])[0]
                    self._html(_dashboard(cfg, collect_sites, msg))
                elif parts[0] == "history" and len(parts) == 2:
                    p = (HISTORY_DIR / f"{parts[1]}.md")
                    p = p.resolve()
                    if p.parent != HISTORY_DIR.resolve() or not p.is_file():
                        self._html(b"nicht gefunden", 404)
                    else:
                        self._html(_markdown_page(f"Historie {parts[1]}", p,
                                                  cfg.get("_version", "?")))
                elif parts[0] == "archive" and len(parts) == 2:
                    p = (ARCHIVE_DIR / f"{parts[1]}_changelog.md").resolve()
                    if p.parent != ARCHIVE_DIR.resolve() or not p.is_file():
                        self._html(b"nicht gefunden", 404)
                    else:
                        self._html(_markdown_page(f"Changelog {parts[1]}", p,
                                                  cfg.get("_version", "?")))
                elif parts[0] == "dl" and len(parts) == 2:
                    page = _dl_listing(parts[1], cfg.get("_version", "?"))
                    self._html(page if page else b"nicht gefunden",
                               200 if page else 404)
                elif parts[0] == "dl" and len(parts) == 3:
                    p = self._download_path(parts[1], parts[2])
                    if not p:
                        self._html(b"nicht gefunden", 404)
                    else:
                        _send_file(self, p)
                elif parts[0] == "log":
                    self._html(_log_tail(cfg.get("_version", "?")))
                else:
                    self._html(b"nicht gefunden", 404)
            except (BrokenPipeError, ConnectionResetError):
                pass
            except Exception as exc:
                log.warning("Web-Fehler bei %s: %s", self.path, exc)
                try:
                    self._html(f"<pre>{_esc(exc)}</pre>".encode(), 500)
                except Exception:
                    pass

        def do_HEAD(self):  # noqa: N802
            parts = [urllib.parse.unquote(p)
                     for p in urllib.parse.urlparse(self.path)
                     .path.split("/") if p]
            if len(parts) == 3 and parts[0] == "dl":
                p = self._download_path(parts[1], parts[2])
                if p:
                    _send_file(self, p)
                    return
            self.send_response(404)
            self.end_headers()

        def do_POST(self):  # noqa: N802
            parsed = urllib.parse.urlparse(self.path)
            parts = [urllib.parse.unquote(p)
                     for p in parsed.path.split("/") if p]
            if parts[:1] == ["check"]:
                slug = parts[1] if len(parts) > 1 else None
                ok = trigger(slug) if callable(trigger) else False
                self._redirect("/?msg=" + urllib.parse.quote(
                    (f"Check für '{slug}' gestartet." if slug
                     else "Check gestartet.") if ok
                    else "Ein Check läuft bereits."))
            else:
                self._html(b"nicht gefunden", 404)

    return Handler


def start(cfg: dict, collect_sites, trigger=None) -> ThreadingHTTPServer:
    """Webserver in einem Daemon-Thread starten; gibt den Server zurück."""
    web = cfg.get("web") or {}
    host = web.get("host", "127.0.0.1")
    port = int(web.get("port", 8321))
    handler = make_handler(cfg, collect_sites, trigger)
    server = ThreadingHTTPServer((host, port), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    log.info("Web-Dashboard: http://%s:%d/", host, port)
    return server
