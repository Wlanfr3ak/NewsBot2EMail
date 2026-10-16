"""Tests für das Web-Dashboard (webui.py) - inkl. echtem HTTP-Server.

Der Server läuft auf 127.0.0.1 mit Port 0 (freier Ephemeral-Port);
alle Verzeichnisse werden auf ein Temp-Dir umgebogen.

Aufruf aus dem Projektverzeichnis:
    python -m unittest discover -s tests -v
"""

import json
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import webui


class TestFormatierung(unittest.TestCase):
    def test_fmt_size(self):
        self.assertEqual(webui._fmt_size(512), "512 B")
        self.assertEqual(webui._fmt_size(2048), "2.0 KB")
        self.assertEqual(webui._fmt_size(5 * 1024**3), "5.0 GB")
        self.assertEqual(webui._fmt_size(3 * 1024**4), "3.0 TB")

    def test_fmt_time(self):
        self.assertEqual(webui._fmt_time(None), "–")
        self.assertEqual(webui._fmt_time("2026-10-16T13:27:54"),
                         "16.10.2026 13:27")
        self.assertEqual(webui._fmt_time("quatsch"), "quatsch")

    def test_esc(self):
        self.assertEqual(webui._esc("<b>&'"), "&lt;b&gt;&amp;&#x27;")


class TestWebServer(unittest.TestCase):
    """End-to-End: Handler + ThreadingHTTPServer auf Ephemeral-Port."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        tmp = Path(cls.tmp.name)
        (tmp / "history").mkdir()
        (tmp / "archive").mkdir()
        (tmp / "downloads" / "myslug").mkdir(parents=True)
        (tmp / "history" / "myslug.md").write_text(
            "# Historie\n| 1.0 | 2026-01-01 |", encoding="utf-8")
        (tmp / "downloads" / "myslug" / "f.bin").write_bytes(b"0123456789")
        (tmp / "newsbot.log").write_text("zeile1\nzeile2\n",
                                         encoding="utf-8")
        (tmp / "state.json").write_text(json.dumps({
            "sites": {"Meine Seite": {"value": "1.0",
                                      "last_checked": "2026-10-16T10:00:00"}}
        }), encoding="utf-8")

        for attr, val in (("STATE_PATH", tmp / "state.json"),
                          ("LOG_PATH", tmp / "newsbot.log"),
                          ("HISTORY_DIR", tmp / "history"),
                          ("ARCHIVE_DIR", tmp / "archive"),
                          ("DOWNLOAD_DIR", tmp / "downloads")):
            p = mock.patch.object(webui, attr, val)
            p.start()
            cls.addClassCleanup(p.stop)

        cls.cfg = {"_version": "test"}
        cls.sites = [{"name": "Meine Seite", "url": "https://x.test/",
                      "slug": "myslug"}]
        cls.trigger_calls = []
        handler = webui.make_handler(
            cls.cfg, lambda cfg: cls.sites,
            lambda slug=None: cls.trigger_calls.append(slug) or True)
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        cls.port = cls.server.server_address[1]
        threading.Thread(target=cls.server.serve_forever,
                         daemon=True).start()
        cls.addClassCleanup(cls.server.server_close)
        cls.addClassCleanup(cls.server.shutdown)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def _get(self, path, headers=None):
        req = urllib.request.Request(
            f"http://127.0.0.1:{self.port}{path}", headers=headers or {})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                return resp.status, dict(resp.headers), resp.read()
        except urllib.error.HTTPError as e:
            e.close()
            return e.code, dict(e.headers), e.read()

    def _post_no_follow(self, path):
        opener = urllib.request.build_opener(_NoRedirect)
        req = urllib.request.Request(
            f"http://127.0.0.1:{self.port}{path}", data=b"", method="POST")
        try:
            with opener.open(req, timeout=10) as resp:
                return resp.status, dict(resp.headers)
        except urllib.error.HTTPError as e:
            e.close()
            return e.code, dict(e.headers)

    def test_dashboard(self):
        status, _, body = self._get("/")
        self.assertEqual(status, 200)
        self.assertIn(b"Meine Seite", body)
        self.assertIn(b"1.0", body)

    def test_history_seite(self):
        status, _, body = self._get("/history/myslug")
        self.assertEqual(status, 200)
        self.assertIn(b"Historie", body)

    def test_history_fehlt(self):
        status, _, _ = self._get("/history/gibtsnicht")
        self.assertEqual(status, 404)

    def test_dl_listing_und_datei(self):
        status, _, body = self._get("/dl/myslug/")
        self.assertEqual(status, 200)
        self.assertIn(b"f.bin", body)
        status, hdrs, body = self._get("/dl/myslug/f.bin")
        self.assertEqual(status, 200)
        self.assertEqual(body, b"0123456789")
        self.assertIn("attachment", hdrs.get("Content-Disposition", ""))

    def test_dl_range(self):
        status, hdrs, body = self._get(
            "/dl/myslug/f.bin", headers={"Range": "bytes=2-5"})
        self.assertEqual(status, 206)
        self.assertEqual(body, b"2345")
        self.assertEqual(hdrs.get("Content-Range"), "bytes 2-5/10")

    def test_dl_traversal(self):
        status, _, _ = self._get("/dl/myslug/..%2F..%2Fstate.json")
        self.assertEqual(status, 404)
        status, _, _ = self._get("/dl/..%2F..%2F/")
        self.assertEqual(status, 404)

    def test_log(self):
        status, _, body = self._get("/log")
        self.assertEqual(status, 200)
        self.assertIn(b"zeile2", body)

    def test_post_check(self):
        status, hdrs = self._post_no_follow("/check")
        self.assertEqual(status, 303)
        self.assertIn("/?msg=", hdrs.get("Location", ""))
        self.assertIn(None, self.trigger_calls)

    def test_post_check_slug(self):
        status, _ = self._post_no_follow("/check/myslug")
        self.assertEqual(status, 303)
        self.assertIn("myslug", self.trigger_calls)

    def test_post_check_besetzt(self):
        handler = webui.make_handler(self.cfg, lambda c: [],
                                     lambda slug=None: False)
        server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            opener = urllib.request.build_opener(_NoRedirect)
            req = urllib.request.Request(
                f"http://127.0.0.1:{server.server_address[1]}/check",
                data=b"", method="POST")
            try:
                opener.open(req, timeout=10)
                self.fail("303 erwartet")
            except urllib.error.HTTPError as e:
                self.assertEqual(e.code, 303)
                self.assertIn("bereits", urllib.parse.unquote(
                    e.headers.get("Location", "")))
                e.close()
        finally:
            server.shutdown()
            server.server_close()

    def test_unbekannte_route(self):
        status, _, _ = self._get("/nichts")
        self.assertEqual(status, 404)


import urllib.parse


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


if __name__ == "__main__":
    unittest.main()
