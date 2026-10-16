"""Tests für die Seiten-Module unter sites/ (offline, Netzwerk gemockt).

Aufruf aus dem Projektverzeichnis:
    python -m unittest discover -s tests -v
"""

import importlib.util
import json
import re
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import newsbot


def load_module(name: str):
    """Lädt sites/<name>.py als Modul-Objekt (wie newsbot es tut)."""
    path = ROOT / "sites" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(f"test_site_{name}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestModulVertrag(unittest.TestCase):
    """Jedes Modul erfüllt den dokumentierten Vertrag aus AGENTS.md."""

    @classmethod
    def setUpClass(cls):
        cls.sites = newsbot.load_site_modules()

    def test_module_werden_geladen(self):
        self.assertGreaterEqual(len(self.sites), 10)

    def test_pflichtfelder(self):
        for site in self.sites:
            with self.subTest(site=site["name"]):
                self.assertIsInstance(site["name"], str)
                self.assertTrue(site["name"].strip())
                self.assertTrue(site["url"].startswith("https://"))
                self.assertRegex(site["slug"], r"^[a-z0-9][a-z0-9-]*$")
                self.assertIn(site["method"], ("regex", "hash", "etag"))

    def test_eindeutige_slugs_und_namen(self):
        slugs = [s["slug"] for s in self.sites]
        names = [s["name"] for s in self.sites]
        self.assertEqual(len(slugs), len(set(slugs)))
        self.assertEqual(len(names), len(set(names)))

    def test_pattern_kompiliert(self):
        for site in self.sites:
            if site["pattern"] is None:
                continue
            with self.subTest(site=site["name"]):
                re.compile(site["pattern"])

    def test_regex_braucht_pattern_oder_extract(self):
        for site in self.sites:
            if site["method"] == "regex" and not callable(site["extract"]):
                with self.subTest(site=site["name"]):
                    self.assertIsNotNone(site["pattern"])

    def test_changelog_paarung(self):
        for site in self.sites:
            with self.subTest(site=site["name"]):
                # CHANGELOG_URL braucht einen Hook, der das Archiv füllt:
                # extract_changelog (NewsBot lädt die URL) ODER
                # update_changelog (Modul lädt selbst, URL ist dann
                # nur die Quellenangabe im Archiv-Kopf).
                if site["changelog_url"]:
                    self.assertTrue(
                        callable(site["extract_changelog"])
                        or callable(site["update_changelog"]))

    def test_hooks_callbar(self):
        for site in self.sites:
            for key in ("extract", "extract_history", "extract_changelog",
                        "update_changelog", "list_downloads"):
                hook = site[key]
                with self.subTest(site=site["name"], hook=key):
                    self.assertTrue(hook is None or callable(hook))

    def test_downloads_format(self):
        for site in self.sites:
            for entry in site["downloads"]:
                with self.subTest(site=site["name"], entry=entry):
                    if isinstance(entry, dict):
                        self.assertIn("url", entry)
                    else:
                        self.assertIsInstance(entry, str)


class TestMikroTikNewsletter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module("mikrotik_newsletter")

    FIXTURE = """
    <a href="https://mt.lv/news132">Newsletter #132 | April 2026</a>
    <a href="https://mt.lv/news133">Newsletter #133 | June 2026</a>
    <a href="https://mt.lv/news134">Newsletter #134 | July 2026</a>
    """

    def test_numbers(self):
        self.assertEqual(self.mod._numbers(self.FIXTURE), [132, 133, 134])

    def test_extract_verlinkt(self):
        """Ohne vorgelagerte Nummern bleibt es beim verlinkten Maximum."""
        with mock.patch.object(self.mod, "_resolve_pdf_url",
                               side_effect=ValueError("404")):
            self.assertEqual(self.mod.extract(self.FIXTURE), "134")

    def test_extract_voraus_probe(self):
        """Ein existierender, aber unverlinkter Kurzlink wird gefunden."""
        def fake(number):
            if number == 135:
                return "https://box.mikrotik.com/f/abc/?dl=1"
            raise ValueError("404")
        with mock.patch.object(self.mod, "_resolve_pdf_url", fake):
            self.assertEqual(self.mod.extract(self.FIXTURE), "135")

    def test_probe_mehrere_voraus(self):
        def fake(number):
            if number in (135, 136):
                return "https://x/"
            raise ValueError("404")
        with mock.patch.object(self.mod, "_resolve_pdf_url", fake):
            self.assertEqual(self.mod.extract(self.FIXTURE), "136")

    def test_extract_keine_links(self):
        with self.assertRaises(ValueError):
            self.mod.extract("<p>keine Newsletter</p>")

    def test_extract_history(self):
        releases = self.mod.extract_history(self.FIXTURE)
        self.assertEqual(releases[0], {"version": "134", "date": "2026-07"})
        self.assertEqual(releases[-1], {"version": "132", "date": "2026-04"})

    def test_list_downloads_missing_logik(self):
        """.missing nur im verlinkten Bereich, Probe-Bereich nicht."""
        calls = []
        def fake(number):
            calls.append(number)
            if number == 99:
                raise ValueError("404")          # Lücke im verlinkten Bereich
            if number == 101:
                # Beim Proben ok, beim Download-Lauf defekt -> kein .missing
                if calls.count(101) > 1:
                    raise ValueError("flaky")
                return "https://x/news101.pdf"
            if number > 101:
                raise ValueError("404")
            return f"https://x/news{number}.pdf"

        old_oldest = self.mod.OLDEST
        self.mod.OLDEST = 98
        try:
            with tempfile.TemporaryDirectory() as d, \
                 mock.patch.object(self.mod, "_resolve_pdf_url", fake):
                items = self.mod.list_downloads(self.FIXTURE_100, set(),
                                                Path(d))
                names = {i["filename"] for i in items}
                self.assertIn("news_98.pdf", names)
                self.assertIn("news_100.pdf", names)
                self.assertNotIn("news_99.pdf", names)     # .missing stattdessen
                self.assertNotIn("news_101.pdf", names)    # flaky, kein item
                self.assertTrue((Path(d) / "news_99.pdf.missing").exists())
                self.assertFalse((Path(d) / "news_101.pdf.missing").exists())
        finally:
            self.mod.OLDEST = old_oldest

    FIXTURE_100 = """
    <a href="https://mt.lv/news98">x</a>
    <a href="https://mt.lv/news99">x</a>
    <a href="https://mt.lv/news100">x</a>
    """

    def test_list_downloads_have_gesetzt(self):
        def fake(number):
            if number > 101:
                raise ValueError("404")
            return f"https://x/news{number}.pdf"
        old_oldest = self.mod.OLDEST
        self.mod.OLDEST = 98
        try:
            with tempfile.TemporaryDirectory() as d, \
                 mock.patch.object(self.mod, "_resolve_pdf_url", fake):
                have = {"news_98.pdf", "news_99.pdf.missing"}
                items = self.mod.list_downloads(self.FIXTURE_100, have,
                                                Path(d))
                self.assertEqual([i["filename"] for i in items],
                                 ["news_100.pdf", "news_101.pdf"])
        finally:
            self.mod.OLDEST = old_oldest

    def test_probe_limit_bremst(self):
        """Endlos auflösbare Nummern werden durch PROBE_LIMIT gestoppt."""
        with mock.patch.object(self.mod, "_resolve_pdf_url",
                               return_value="https://x/"):
            self.assertEqual(self.mod._probe_ahead(100),
                             100 + self.mod.PROBE_LIMIT)

    def _opener_raising(self, exc=None, headers=None):
        """Mock-Opener: open() wirft exc oder liefert Response mit headers."""
        opener = mock.Mock()
        if exc is not None:
            opener.open.side_effect = exc
        else:
            resp = mock.MagicMock()
            resp.__enter__.return_value.headers = headers or {}
            opener.open.return_value = resp
        return opener

    def test_resolve_redirect(self):
        err = urllib.error.HTTPError(
            "https://mt.lv/news1", 302, "Found",
            {"Location": "https://cdn.mt.lv/news1.pdf"}, None)
        with mock.patch("urllib.request.build_opener",
                        return_value=self._opener_raising(exc=err)):
            self.assertEqual(self.mod._resolve_pdf_url(1),
                             "https://cdn.mt.lv/news1.pdf")
        err.close()

    def test_resolve_seafile_dl1(self):
        """box.mikrotik.com/f/-Share ohne dl=1 bekommt '/?dl=1' angehängt."""
        err = urllib.error.HTTPError(
            "https://mt.lv/news1", 302, "Found",
            {"Location": "https://box.mikrotik.com/f/abc/"}, None)
        with mock.patch("urllib.request.build_opener",
                        return_value=self._opener_raising(exc=err)):
            self.assertEqual(self.mod._resolve_pdf_url(1),
                             "https://box.mikrotik.com/f/abc/?dl=1")
        err.close()

    def test_resolve_404(self):
        err = urllib.error.HTTPError("https://mt.lv/news999", 404,
                                     "Not Found", {}, None)
        with mock.patch("urllib.request.build_opener",
                        return_value=self._opener_raising(exc=err)):
            with self.assertRaises(ValueError):
                self.mod._resolve_pdf_url(999)
        err.close()

    def test_resolve_kein_redirect(self):
        with mock.patch("urllib.request.build_opener",
                        return_value=self._opener_raising(headers={})):
            with self.assertRaises(ValueError):
                self.mod._resolve_pdf_url(1)


class TestMikroTikRouterOS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module("mikrotik_routeros")

    def test_parse_date_iso(self):
        self.assertEqual(self.mod._parse_date("2026-09-16"), "2026-09-16")

    def test_parse_date_ros7(self):
        self.assertEqual(self.mod._parse_date("2026-Aug-21 16:06"),
                         "2026-08-21")

    def test_parse_date_ros6(self):
        self.assertEqual(self.mod._parse_date("Dec/22/2021 13:49:22"),
                         "2021-12-22")

    def test_parse_date_kurzes_jahr(self):
        self.assertEqual(self.mod._parse_date("Aug.25.15-12:59:46"),
                         "2015-08-25")

    def test_parse_date_upstream_tippfehler(self):
        """'Arp' statt 'Apr' im 7.23beta5-Changelog."""
        self.assertEqual(self.mod._parse_date("2026-Arp-01"), "2026-04-01")

    def test_parse_date_unbekannt(self):
        self.assertIsNone(self.mod._parse_date("irgendwas"))
        self.assertIsNone(self.mod._parse_date("2026-Xxx-01"))

    def test_channel_versions(self):
        text = ('<a data-changelog-version="7.24.4">x</a>'
                '<a data-changelog-version="7.24.3">y</a>')
        self.assertEqual(self.mod._channel_versions("stable", text),
                         ["7.24.4", "7.24.3"])

    def test_extract_kombiniert(self):
        fake = {"stable": ["7.24.4"], "testing": ["7.25beta1"]}
        with mock.patch.object(self.mod, "CHANNELS",
                               ["stable", "testing"]), \
             mock.patch.object(self.mod, "_channel_versions",
                               lambda ch, text=None: fake[ch]):
            self.assertEqual(self.mod.extract(""),
                             "stable=7.24.4;testing=7.25beta1")

    def test_extract_einzelkanal(self):
        with mock.patch.object(self.mod, "CHANNELS", ["stable"]), \
             mock.patch.object(self.mod, "_channel_versions",
                               lambda ch, text=None: ["7.24.4"]):
            self.assertEqual(self.mod.extract(""), "7.24.4")


class TestVentoy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module("ventoy")

    FIXTURE = ('ReleaseList = [{"version":"1.1.07","date":"2026-09-20"},'
               '{"version":"1.1.06","date":"2026-05-01"},'
               '{"version":"1.1.06","date":"2026-05-01"}]')

    def test_extract(self):
        self.assertEqual(self.mod.extract(self.FIXTURE), "1.1.07")

    def test_extract_history_dedup(self):
        releases = self.mod.extract_history(self.FIXTURE)
        self.assertEqual([r["version"] for r in releases],
                         ["1.1.07", "1.1.06"])
        self.assertEqual(releases[0]["date"], "2026-09-20")

    def test_extract_fehler(self):
        with self.assertRaises(ValueError):
            self.mod.extract("<html>nichts</html>")

    def test_extract_changelog(self):
        news = ('<li class="news">2026/09/20 --- 1.1.07 release hotfix</li>'
                '</ul><ol class="LL"><li class="N1">Fixed bug<br>details</li>'
                '<li class="N1">Second item</li></ol>')
        md = self.mod.extract_changelog(news)
        self.assertIn("## 1.1.07 – 2026-09-20 (hotfix)", md)
        self.assertIn("- Fixed bug details", md)
        self.assertIn("- Second item", md)


class TestBlossomOS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module("blossomos")

    def test_extract(self):
        text = json.dumps({"name": "BlossomOS-2026.09.18-x86_64.iso",
                           "sha256": "abc"})
        self.assertEqual(self.mod.extract(text), "2026.09.18")

    def test_extract_history(self):
        text = json.dumps({"name": "BlossomOS-2026.09.18-x86_64.iso"})
        self.assertEqual(self.mod.extract_history(text),
                         [{"version": "2026.09.18", "date": "2026-09-18"}])

    def test_extract_fehler(self):
        with self.assertRaises(ValueError):
            self.mod.extract(json.dumps({"name": "was-anderes.iso"}))


class TestDiverseModule(unittest.TestCase):
    def test_python_org_pattern(self):
        mod = load_module("python_org")
        m = re.search(mod.PATTERN, "Download Python 3.13.7 now")
        self.assertEqual(m.group(1), "3.13.7")

    def test_memtest86_extract(self):
        mod = load_module("memtest86")
        self.assertEqual(
            mod.extract('<a href="v8.10/mt86plus_8.10_x86_64.iso.zip">'),
            "8.10")
        with self.assertRaises(ValueError):
            mod.extract("<html>kein iso</html>")

    def test_memtest86_changelog(self):
        mod = load_module("memtest86")
        api = json.dumps([{"tag_name": "v8.10",
                           "published_at": "2025-06-01T10:00:00Z",
                           "name": "Memtest86+ v8.10",
                           "body": "Neue Features"}])
        md = mod.extract_changelog(api)
        self.assertIn("## 8.10 – 2025-06-01", md)
        self.assertIn("Neue Features", md)

    def test_notepadpp_extract(self):
        mod = load_module("notepadpp")
        self.assertEqual(mod.extract("Current Version 8.9.8"), "8.9.8")
        # Fallback: erster /downloads/vX/-Link
        self.assertEqual(mod.extract('<a href="/downloads/v8.9.7/">x</a>'),
                         "8.9.7")
        with self.assertRaises(ValueError):
            mod.extract("nichts")

    def test_partedmagic_extract(self):
        mod = load_module("partedmagic")
        text = "<h2>Parted Magic 2026_09_17</h2><p>Neu: alles besser</p>"
        self.assertEqual(mod.extract(text), "2026_09_17")
        with self.assertRaises(ValueError):
            mod.extract("<h2>Kein Release</h2>")

    def test_partedmagic_release_date(self):
        mod = load_module("partedmagic")
        self.assertEqual(mod._release_date("2026_09_17"), "2026-09-17")
        self.assertEqual(mod._release_date("2026_09_17_2"), "2026-09-17")
        self.assertIsNone(mod._release_date("keinschema"))


if __name__ == "__main__":
    unittest.main()
