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


class TestJellyfin(unittest.TestCase):
    """Gemeinsame Basis der beiden Jellyfin-Module: Version kommt aus
    dem tag_name des GitHub-Release-JSON."""

    RELEASE_JSON = json.dumps({"tag_name": "v12.3",
                               "published_at": "2026-10-23T00:30:06Z"})

    def test_server_extract(self):
        mod = load_module("jellyfin_server")
        self.assertEqual(mod.extract(self.RELEASE_JSON), "12.3")
        with self.assertRaises(ValueError):
            mod.extract(json.dumps({}))

    def test_desktop_extract(self):
        mod = load_module("jellyfin_desktop")
        self.assertEqual(mod.extract(self.RELEASE_JSON), "12.3")
        with self.assertRaises(ValueError):
            mod.extract(json.dumps({}))

    def test_desktop_list_downloads_nur_x64(self):
        """Nur die normale windows-x64.exe - kein legacy, kein x86."""
        mod = load_module("jellyfin_desktop")
        text = json.dumps({"assets": [
            {"name": "JellyfinMediaPlayer-1.12.0-windows-x64-legacy.exe",
             "browser_download_url": "https://x/legacy.exe"},
            {"name": "JellyfinMediaPlayer-1.12.0-windows-x64.exe",
             "browser_download_url": "https://x/normal.exe"},
            {"name": "JellyfinMediaPlayer-1.12.0-windows-x86.exe",
             "browser_download_url": "https://x/x86.exe"},
            {"name": "JellyfinMediaPlayer-1.12.0.dmg",
             "browser_download_url": "https://x/mac.dmg"}]})
        items = mod.list_downloads(text, set(), None)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["url"], "https://x/normal.exe")
        self.assertEqual(items[0]["filename"],
                         "JellyfinMediaPlayer-1.12.0-windows-x64.exe")

    def test_desktop_list_downloads_have(self):
        """Bereits vorhandene Dateien werden nicht erneut gelistet."""
        mod = load_module("jellyfin_desktop")
        name = "JellyfinMediaPlayer-1.12.0-windows-x64.exe"
        text = json.dumps({"assets": [
            {"name": name, "browser_download_url": "https://x/a.exe"}]})
        self.assertEqual(mod.list_downloads(text, {name}, None), [])


class TestPHP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module("php")

    # Ausschnitt aus php.net/releases/index.php?json&version=8
    FIXTURE = json.dumps({
        "8.5.12": {"date": "21 Oct 2026", "tags": ["security"],
                   "source": [{"filename": "php-8.5.12.tar.gz"}]},
        "8.4.27": {"date": "21 Oct 2026", "tags": ["security"],
                   "source": [{"filename": "php-8.4.27.tar.gz"}]},
        "8.3.36": {"date": "21 Oct 2026", "tags": [],
                   "source": [{"filename": "php-8.3.36.tar.gz"}]},
        "8.2.35": {"date": "21 Oct 2026", "tags": [],
                   "source": [{"filename": "php-8.2.35.tar.gz"}]},
        "8.5.11": {"date": "24 Sep 2026", "tags": ["security"],
                   "source": [{"filename": "php-8.5.11.tar.gz"}]},
        "8.1.33": {"date": "03 Jul 2025", "tags": [],
                   "source": [{"filename": "php-8.1.33.tar.gz"}]},
        "8.6.0RC1": {"date": "30 Oct 2026", "tags": [],
                     "source": [{"filename": "php-8.6.0rc1.tar.gz"}]},
    })

    def test_extract_kombiniert(self):
        self.assertEqual(self.mod.extract(self.FIXTURE),
                         "8.5=8.5.12;8.4=8.4.27;8.3=8.3.36;8.2=8.2.35")

    def test_extract_branch_fehlt(self):
        """Ein Zweig ohne Release fällt raus, killt aber nicht den Rest."""
        data = json.dumps({"8.5.1": {"date": "x"}, "8.4.1": {"date": "x"}})
        self.assertEqual(self.mod.extract(data), "8.5=8.5.1;8.4=8.4.1")

    def test_extract_fehler(self):
        with self.assertRaises(ValueError):
            self.mod.extract(json.dumps({"7.4.33": {"date": "x"}}))

    def test_extract_history(self):
        releases = self.mod.extract_history(self.FIXTURE)
        versions = [r["version"] for r in releases]
        # nur die 4 überwachten Zweige, stabile Versionen
        self.assertNotIn("8.1.33", versions)
        self.assertNotIn("8.6.0RC1", versions)
        self.assertEqual(releases[0],
                         {"version": "8.5.12", "date": "2026-10-21"})

    def test_iso_date(self):
        self.assertEqual(self.mod._iso_date("21 Oct 2026"), "2026-10-21")
        self.assertIsNone(self.mod._iso_date("bald"))
        self.assertIsNone(self.mod._iso_date(None))

    CHANGELOG_FIXTURE = """
<section class="version" id="8.5.12"><!-- {{{ 8.5.12 -->
<h3>Version 8.5.12</h3>
<b><time class='releasedate' datetime='2026-10-22'>22 Oct 2026</time></b>
<ul><li>Core:
<ul>
  <li>Fixed bug <a href="https://github.com/php/php-src/issues/1">GH-1</a> (Beschreibung).</li>
</ul></li>
<li>Standard:
<ul>
  <li>Fix <a href="https://github.com/php/php-src/issues/2">GH-2</a>.</li>
</ul></li></ul>
</section>
<section class="version" id="8.4.27">
<h3>Version 8.4.27</h3>
<b><time class='releasedate' datetime='2026-10-22'>22 Oct 2026</time></b>
<ul><li>Core:
<ul><li>Fixed X.</li></ul></li></ul>
</section>
<section class="version" id="8.1.33">
<h3>Version 8.1.33</h3>
<b><time class='releasedate' datetime='2025-07-03'>03 Jul 2025</time></b>
<ul><li>Core:<ul><li>alt</li></ul></li></ul>
</section>
"""

    def test_update_changelog(self):
        def fake_fetch(url):
            if "ChangeLog" in url:
                return self.CHANGELOG_FIXTURE
            return self.FIXTURE   # Release-JSON für Security-Tags
        with mock.patch.object(self.mod, "_fetch", side_effect=fake_fetch):
            out = self.mod.update_changelog(None)
        self.assertIn("## 8.5.12 – 2026-10-22 (Security Release)", out)
        self.assertIn("## 8.4.27 – 2026-10-22", out)
        self.assertNotIn("## 8.1.33", out)      # nicht überwachter Zweig
        self.assertIn("- **Core:**", out)
        self.assertIn("Fixed bug [GH-1](https://github.com/php/php-src/issues/1)", out)

    def test_update_changelog_inkrementell(self):
        existing = "## 8.5.12 – 2026-10-22\n\nalt\n"
        def fake_fetch(url):
            if "ChangeLog" in url:
                return self.CHANGELOG_FIXTURE
            return self.FIXTURE
        with mock.patch.object(self.mod, "_fetch", side_effect=fake_fetch):
            out = self.mod.update_changelog(existing)
        self.assertTrue(out.startswith("## 8.4.27"))
        self.assertIn("alt", out)
        # schon vorhandene Sektion nicht duplizieren
        self.assertEqual(out.count("## 8.5.12"), 1)

    def test_update_changelog_unveraendert(self):
        existing = ("## 8.5.12 – 2026-10-22\n\nx\n\n"
                    "## 8.4.27 – 2026-10-22\n\ny")
        def fake_fetch(url):
            if "ChangeLog" in url:
                return self.CHANGELOG_FIXTURE
            return self.FIXTURE
        with mock.patch.object(self.mod, "_fetch", side_effect=fake_fetch):
            self.assertIsNone(self.mod.update_changelog(existing))


class TestGitLab(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module("gitlab")

    TAGS_FIXTURE = json.dumps([
        {"name": "v19.5.1-ee",
         "commit": {"committed_date": "2026-10-20T23:00:49.000+00:00"}},
        {"name": "v19.4.3-ee",
         "commit": {"committed_date": "2026-10-20T23:07:57.000+00:00"}},
        {"name": "v19.3.6-ee",
         "commit": {"committed_date": "2026-10-20T23:15:49.000+00:00"}},
        {"name": "v19.2.9-ee",
         "commit": {"committed_date": "2026-10-20T17:18:17.000+00:00"}},
        {"name": "v19.5.0-ee",
         "commit": {"committed_date": "2026-10-15T00:37:08.000+00:00"}},
        {"name": "v19.6.0-rc1-ee",
         "commit": {"committed_date": "2026-10-14T19:43:39.000+00:00"}},
        {"name": "v19.5.0-rc43-ee",
         "commit": {"committed_date": "2026-10-13T12:08:07.000+00:00"}},
    ])

    def test_extract_top3(self):
        """Top-3 Minor-Zweige; 19.2 fällt raus, RCs werden ignoriert."""
        self.assertEqual(self.mod.extract(self.TAGS_FIXTURE),
                         "19.5=19.5.1;19.4=19.4.3;19.3=19.3.6")

    def test_extract_fehler(self):
        with self.assertRaises(ValueError):
            self.mod.extract(json.dumps([]))

    def test_extract_history(self):
        releases = self.mod.extract_history(self.TAGS_FIXTURE)
        versions = [r["version"] for r in releases]
        self.assertNotIn("19.5.0-rc43", versions)
        self.assertEqual(releases[0],
                         {"version": "19.5.1", "date": "2026-10-20"})
        # semver-absteigend sortiert
        self.assertLess(versions.index("19.4.3"), versions.index("19.3.6"))

    FEED_FIXTURE = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
<entry><title>GitLab 19.5 release notes</title>
<link href="https://docs.gitlab.com/releases/19/gitlab-19-5-released/" rel="alternate"/>
<updated>2026-10-15T00:00:00Z</updated>
<content type="html"><![CDATA[<p>Intro</p>
<h3 id="a">Feature A</h3><h3 id="b">Feature B</h3>]]></content></entry>
</feed>"""

    def test_update_changelog(self):
        def fake_fetch(url):
            return self.FEED_FIXTURE if "releases.xml" in url \
                else self.TAGS_FIXTURE
        with mock.patch.object(self.mod, "_fetch", side_effect=fake_fetch):
            out = self.mod.update_changelog(None)
        self.assertIn("## 19.5.0 – 2026-10-15", out)
        self.assertIn("- Feature A", out)
        self.assertIn("gitlab-19-5-released", out)
        self.assertIn("## 19.5.1 – 2026-10-20", out)
        self.assertIn("Patch-Release", out)

    def test_update_changelog_unveraendert(self):
        existing = "\n\n".join(
            f"## {v} – 2026-10-20\n\nx" for v in
            ("19.5.1", "19.4.3", "19.3.6", "19.2.9", "19.5.0"))
        def fake_fetch(url):
            return self.FEED_FIXTURE if "releases.xml" in url \
                else self.TAGS_FIXTURE
        with mock.patch.object(self.mod, "_fetch", side_effect=fake_fetch):
            self.assertIsNone(self.mod.update_changelog(existing))


class TestHPDocks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module("hp_docks")

    OSVER_FIXTURE = json.dumps({"data": {"osAvailablePlatformsAnsOS": {
        "osPlatforms": [{"osVersions": [
            {"id": "ARM_ID", "name": "Windows 11 Version 25H2 auf ARM (64 Bit)"},
            {"id": "GEN_ID", "name": "Windows 11"},
            {"id": "H2_ID", "name": "Windows 11 Version 26H2 (64 Bit)"},
        ]}]}}})

    DRIVERS_FIXTURE = json.dumps({"data": {"softwareTypes": [{
        "accordionName": "Dockingstationen-Firmware und Treiber",
        "softwareDriversList": [
            {"latestVersionDriver": {
                "title": "Alle Dockingstationen - Ethernet-Treiber",
                "version": "11.22"},
             "previousVersionOfDriversList": []},
            {"latestVersionDriver": {
                "title": "HP USB-C Dockingstation G5 - Firmware",
                "version": "1.0.26.0 Rev.A",
                "releaseDateString": "Nov 20, 2025",
                "fileUrl": "https://ftp.hp.com/pub/softpaq/x/sp165907.exe",
                "fileSize": "8.6 MB",
                "detailInformation": {
                    "description": "<p>Paket mit dem Installer.</p>",
                    "fixesAndEnhancements":
                        "<body>- Fix eins. - Fix zwei.</body>"}},
             "previousVersionOfDriversList": [{
                "version": "1.0.25.0 Rev.C",
                "releaseDateString": "Jul 18, 2025",
                "fileUrl": "https://ftp.hp.com/pub/softpaq/x/sp161510.exe",
                "fileSize": "13.7 MB"}]},
        ]}]}})

    def _patch_docks(self, mod):
        """_os_tms_id und _fetch mocken: zwei Docks mit Fixture-Daten."""
        products = {"1": "Dock Eins", "2": "Dock Zwei"}
        def fake_fetch(url, payload=None):
            if "osVersionData" in url:
                return self.OSVER_FIXTURE
            return self.DRIVERS_FIXTURE
        return mock.patch.multiple(
            mod, PRODUCTS=products, _fetch=mock.Mock(side_effect=fake_fetch))

    def test_os_tms_id_generisch_bevorzugt(self):
        mod = self.mod
        with mock.patch.object(mod, "_fetch",
                               return_value=self.OSVER_FIXTURE):
            self.assertEqual(mod._os_tms_id("1"), "GEN_ID")

    def test_os_tms_id_fallback_nicht_arm(self):
        fixture = json.dumps({"data": {"osAvailablePlatformsAnsOS": {
            "osPlatforms": [{"osVersions": [
                {"id": "ARM_ID", "name": "Windows 11 on ARM (64-bit)"},
                {"id": "H2_ID", "name": "Windows 11 Version 26H2"}]}]}}})
        with mock.patch.object(self.mod, "_fetch", return_value=fixture):
            self.assertEqual(self.mod._os_tms_id("1"), "H2_ID")

    def test_extract_kombiniert(self):
        with self._patch_docks(self.mod):
            self.assertEqual(
                self.mod.extract(""),
                "Dock Eins=1.0.26.0 Rev.A;Dock Zwei=1.0.26.0 Rev.A")

    def test_extract_kein_firmware(self):
        """Kein Firmware-Eintrag -> ValueError."""
        leer = json.dumps({"data": {"softwareTypes": []}})
        def fake_fetch(url, payload=None):
            if "osVersionData" in url:
                return self.OSVER_FIXTURE
            return leer
        with mock.patch.multiple(self.mod, PRODUCTS={"1": "Dock"},
                                 _fetch=mock.Mock(side_effect=fake_fetch)):
            with self.assertRaises(ValueError):
                self.mod.extract("")

    def test_extract_history_mit_prev(self):
        with self._patch_docks(self.mod):
            releases = self.mod.extract_history("")
        self.assertIn({"version": "1.0.26.0 Rev.A",
                       "date": "2025-11-20"}, releases)
        self.assertIn({"version": "1.0.25.0 Rev.C",
                       "date": "2025-07-18"}, releases)

    def test_iso_date(self):
        self.assertEqual(self.mod._iso_date("Nov 20, 2025"), "2025-11-20")
        self.assertIsNone(self.mod._iso_date("bald"))

    def test_update_changelog(self):
        with self._patch_docks(self.mod):
            out = self.mod.update_changelog(None)
        self.assertIn("## Dock Eins: 1.0.26.0 Rev.A – 2025-11-20", out)
        self.assertIn("- Fix eins.", out)
        self.assertIn("- Fix zwei.", out)
        self.assertIn("sp165907.exe", out)

    def test_update_changelog_unveraendert(self):
        existing = ("## Dock Eins: 1.0.26.0 Rev.A – 2025-11-20\n\nx\n\n"
                    "## Dock Zwei: 1.0.26.0 Rev.A – 2025-11-20\n\ny")
        with self._patch_docks(self.mod):
            self.assertIsNone(self.mod.update_changelog(existing))

    def test_list_downloads(self):
        with self._patch_docks(self.mod):
            items = self.mod.list_downloads("", set(), None)
        self.assertEqual(len(items), 2)
        self.assertIn("sp165907.exe", items[0]["url"])
        self.assertIn("sp165907", items[0]["filename"])
        with self._patch_docks(self.mod):
            self.assertEqual(
                self.mod.list_downloads(
                    "", {items[0]["filename"], items[1]["filename"]}, None),
                [])


if __name__ == "__main__":
    unittest.main()
