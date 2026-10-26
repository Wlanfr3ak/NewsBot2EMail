"""Tests für die Kernlogik von newsbot.py (reine Standardbibliothek).

Aufruf aus dem Projektverzeichnis:
    python -m unittest discover -s tests -v

Alle Tests laufen offline - Netzwerkzugriffe werden gemockt.
"""

import gzip
import hashlib
import json
import os
import sys
import tempfile
import unittest
import zlib
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import newsbot


def _site(**kw):
    site = {"name": "Testseite", "url": "https://example.test/",
            "slug": "testseite", "method": "regex",
            "pattern": r"v(\d+\.\d+)"}
    site.update(kw)
    return site


class TestSlugify(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(newsbot.slugify("MikroTik RouterOS"),
                         "mikrotik-routeros")

    def test_sonderzeichen(self):
        self.assertEqual(newsbot.slugify("  Foo / Bar_Baz  "), "foo-bar-baz")

    def test_fallback(self):
        self.assertEqual(newsbot.slugify("###"), "seite")


class TestEnv(unittest.TestCase):
    def test_resolve_env_gesetzt(self):
        os.environ["NB_TEST_VAR"] = "geheim"
        try:
            self.assertEqual(newsbot.resolve_env("env:NB_TEST_VAR"), "geheim")
        finally:
            del os.environ["NB_TEST_VAR"]

    def test_resolve_env_fehlt(self):
        os.environ.pop("NB_TEST_FEHLT", None)
        self.assertEqual(newsbot.resolve_env("env:NB_TEST_FEHLT"), "")

    def test_resolve_env_normaler_string(self):
        self.assertEqual(newsbot.resolve_env("klartext"), "klartext")
        self.assertEqual(newsbot.resolve_env(42), 42)

    def test_load_env_file(self):
        with tempfile.TemporaryDirectory() as d:
            env = Path(d) / ".env"
            env.write_text(
                "# Kommentar\n"
                "NB_T1=wert1\n"
                "NB_T2=\"mit quotes\"\n"
                "NB_T3='single'\n"
                "kaputt ohne gleich\n"
                "\n",
                encoding="utf-8")
            os.environ["NB_T1"] = "schon da"  # darf nicht überschrieben werden
            try:
                newsbot.load_env_file(env)
                self.assertEqual(os.environ["NB_T1"], "schon da")
                self.assertEqual(os.environ["NB_T2"], "mit quotes")
                self.assertEqual(os.environ["NB_T3"], "single")
            finally:
                for k in ("NB_T1", "NB_T2", "NB_T3"):
                    os.environ.pop(k, None)

    def test_load_env_file_fehlt(self):
        newsbot.load_env_file(Path("/gibts/nicht/.env"))  # kein Fehler


class TestState(unittest.TestCase):
    def test_load_state_fehlt(self):
        self.assertEqual(newsbot.load_state(Path("/gibts/nicht.json")),
                         {"sites": {}})

    def test_load_state_kaputt(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "state.json"
            p.write_text("{kein json", encoding="utf-8")
            self.assertEqual(newsbot.load_state(p), {"sites": {}})

    def test_state_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "state.json"
            state = {"sites": {"A": {"value": "1.0", "umlaut": "äöü"}}}
            newsbot.save_state(p, state)
            self.assertEqual(newsbot.load_state(p), state)


class TestBodyDecoding(unittest.TestCase):
    def test_decompress_gzip(self):
        raw = gzip.compress(b"hallo welt")
        self.assertEqual(
            newsbot.decompress_body(raw, {"content-encoding": "gzip"}),
            b"hallo welt")

    def test_decompress_deflate_zlib(self):
        raw = zlib.compress(b"abc")
        self.assertEqual(
            newsbot.decompress_body(raw, {"content-encoding": "deflate"}),
            b"abc")

    def test_decompress_deflate_roh(self):
        comp = zlib.compressobj(wbits=-15)
        raw = comp.compress(b"roh") + comp.flush()
        self.assertEqual(
            newsbot.decompress_body(raw, {"content-encoding": "deflate"}),
            b"roh")

    def test_decompress_plain(self):
        self.assertEqual(newsbot.decompress_body(b"nix", {}), b"nix")

    def test_decode_charset(self):
        body = "ümläut".encode("latin-1")
        headers = {"content-type": "text/html; charset=latin-1"}
        self.assertEqual(newsbot.decode_body(body, headers), "ümläut")

    def test_decode_default_utf8(self):
        self.assertEqual(newsbot.decode_body("hällö".encode(), {}), "hällö")

    def test_decode_kaputte_bytes(self):
        out = newsbot.decode_body(b"\xff\xfe<x>", {})
        self.assertIn("<x>", out)  # errors="replace" statt Absturz


class TestExtractValue(unittest.TestCase):
    def test_regex_gruppe(self):
        site = _site()
        self.assertEqual(newsbot.extract_value(site, {}, b"Release v2.5"),
                         "2.5")

    def test_regex_ohne_gruppe(self):
        site = _site(pattern=r"v\d+\.\d+")
        self.assertEqual(newsbot.extract_value(site, {}, b"v3.1"), "v3.1")

    def test_regex_kein_treffer(self):
        site = _site()
        with self.assertRaises(ValueError):
            newsbot.extract_value(site, {}, b"nichts drin")

    def test_hash(self):
        site = _site(method="hash")
        self.assertEqual(newsbot.extract_value(site, {}, b"inhalt"),
                         hashlib.sha256(b"inhalt").hexdigest())

    def test_etag(self):
        site = _site(method="etag")
        self.assertEqual(newsbot.extract_value(site, {"etag": '"abc"'}, b""),
                         '"abc"')
        self.assertEqual(
            newsbot.extract_value(site, {"last-modified": "Mo, 1.1."}, b""),
            "Mo, 1.1.")
        self.assertEqual(newsbot.extract_value(site, {}, b""), "")

    def test_extract_hat_vorrang(self):
        site = _site(extract=lambda text: "aus-extract")
        self.assertEqual(
            newsbot.extract_value(site, {}, b"v9.9"), "aus-extract")

    def test_unbekannte_methode(self):
        site = _site(method="rauch")
        with self.assertRaises(ValueError):
            newsbot.extract_value(site, {}, b"")


class TestDownloadHelfer(unittest.TestCase):
    def test_download_filename(self):
        self.assertEqual(newsbot.download_filename(
            "https://x/y/datei.iso"), "datei.iso")
        self.assertEqual(newsbot.download_filename(
            "https://x/v1.0/datei.zip/download"), "datei.zip")
        self.assertEqual(newsbot.download_filename(
            "https://x/f.iso?token=abc"), "f.iso")

    def test_download_target(self):
        self.assertEqual(newsbot._download_target("https://x/f"),
                         ("https://x/f", False, None))
        self.assertEqual(
            newsbot._download_target({"url": "u", "unzip": True,
                                      "filename": "n"}),
            ("u", True, "n"))


class TestChecksum(unittest.TestCase):
    def _dir(self, files: dict) -> Path:
        d = Path(tempfile.mkdtemp())
        for name, content in files.items():
            (d / name).write_text(content, encoding="utf-8")
        return d

    def test_sha256_format(self):
        h = "a" * 64
        d = self._dir({"sha256sum.txt": f"{h}  mt86plus_8.10_x86_64.iso.zip\n"})
        self.assertEqual(newsbot._checksum_map(d),
                         {"mt86plus_8.10_x86_64.iso.zip": h})

    def test_pfadprefix_wird_gekürzt(self):
        h = "b" * 64
        d = self._dir({"SHA256SUMS": f"{h}  v8.10/foo.iso\n"})
        self.assertEqual(newsbot._checksum_map(d), {"foo.iso": h})

    def test_laengster_hash_gewinnt(self):
        md5, sha = "c" * 32, "d" * 64
        d = self._dir({"hashes.txt": f"{md5}  f.iso\n{sha}  f.iso\n"})
        self.assertEqual(newsbot._checksum_map(d), {"f.iso": sha})

    def test_isodata_json(self):
        h = "E" * 64
        d = self._dir({"BlossomOS-1.isodata.json":
                       json.dumps({"name": "B.iso", "sha256": h})})
        self.assertEqual(newsbot._checksum_map(d), {"B.iso": h.lower()})

    def test_unbeteiligte_dateien_ignoriert(self):
        d = self._dir({"readme.txt": "a" * 64 + "  f.iso\n"})
        self.assertEqual(newsbot._checksum_map(d), {})

    def test_verify_ok_und_mismatch(self):
        site = _site()
        with tempfile.TemporaryDirectory() as d:
            target = Path(d)
            payload = b"payload"
            sha = hashlib.sha256(payload).hexdigest()
            (target / "SHA256SUMS").write_text(f"{sha}  f.iso\n")
            tmp = target / "f.iso.part"
            tmp.write_bytes(payload)
            self.assertTrue(
                newsbot._verify_download(site, tmp, "f.iso", target))
            tmp.write_bytes(b"anders")
            self.assertFalse(
                newsbot._verify_download(site, tmp, "f.iso", target))
            # Kein Hash vorhanden -> ok
            self.assertTrue(
                newsbot._verify_download(site, tmp, "andere.iso", target))


class TestHistory(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.hist = Path(self.tmp.name)
        patcher = mock.patch.object(newsbot, "HISTORY_DIR", self.hist)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_init_history_mit_releases(self):
        site = _site()
        releases = [{"version": "2.0", "date": "2026-02-01"},
                    {"version": "1.0", "date": "2025-01-01"}]
        newsbot.init_history(site, "2.0", releases)
        text = newsbot.history_path(site).read_text(encoding="utf-8")
        self.assertIn("| 2.0 | 2026-02-01 |", text)
        self.assertIn("Baseline", text)
        self.assertIn("| 1.0 | 2025-01-01 |", text)

    def test_init_history_ueberschreibt_nicht(self):
        site = _site()
        newsbot.init_history(site, "1.0", None)
        path = newsbot.history_path(site)
        path.write_text("manuell", encoding="utf-8")
        newsbot.init_history(site, "2.0", None)
        self.assertEqual(path.read_text(encoding="utf-8"), "manuell")

    def test_append_history(self):
        site = _site()
        newsbot.init_history(site, "1.0",
                             [{"version": "1.0", "date": "2025-01-01"}])
        newsbot.append_history(site, {
            "new": "2.0", "old": "1.0",
            "releases": [{"version": "2.0", "date": "2026-02-02"}]})
        text = newsbot.history_path(site).read_text(encoding="utf-8")
        self.assertIn("| 2.0 | 2026-02-02 |", text)
        self.assertIn("vorher: 1.0", text)
        # Neuester Eintrag steht über dem älteren
        self.assertLess(text.index("| 2.0 |"), text.index("| 1.0 |"))

    def test_append_history_legt_datei_an(self):
        site = _site()
        newsbot.append_history(site, {"new": "1.0", "old": None,
                                      "releases": []})
        self.assertTrue(newsbot.history_path(site).exists())


class TestChangelogArchiv(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.arch = Path(self.tmp.name)
        patcher = mock.patch.object(newsbot, "ARCHIVE_DIR", self.arch)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_update_changelog_hook(self):
        site = _site(update_changelog=lambda existing: "neuer Inhalt"
                     if existing is None else None)
        newsbot.update_changelog_archive(site, {})
        path = self.arch / "testseite_changelog.md"
        self.assertTrue(path.exists())
        self.assertIn("neuer Inhalt", path.read_text(encoding="utf-8"))
        # Zweiter Lauf: Hook liefert None -> keine Änderung
        newsbot.update_changelog_archive(site, {})
        self.assertIn("neuer Inhalt", path.read_text(encoding="utf-8"))

    def test_extract_changelog_mit_fetch(self):
        site = _site(changelog_url="https://example.test/cl",
                     extract_changelog=lambda text: "markdown-body")
        with mock.patch.object(newsbot, "fetch",
                               return_value=(200, {}, b"seite")):
            newsbot.update_changelog_archive(site, {})
        path = self.arch / "testseite_changelog.md"
        self.assertIn("markdown-body", path.read_text(encoding="utf-8"))

    def test_304_kein_update(self):
        site = _site(changelog_url="https://example.test/cl",
                     extract_changelog=lambda t: "x")
        with mock.patch.object(newsbot, "fetch",
                               return_value=(304, {}, b"")):
            newsbot.update_changelog_archive(site, {})
        self.assertFalse((self.arch / "testseite_changelog.md").exists())


class TestCheckSite(unittest.TestCase):
    """check_site mit gemocktem fetch - die zentrale Vergleichslogik."""

    def _run(self, body=b"v1.0", status=200, headers=None, state=None):
        site = _site()
        state = state if state is not None else {"sites": {}}
        with mock.patch.object(newsbot, "fetch",
                               return_value=(status, headers or {}, body)):
            return newsbot.check_site(site, {}, state), state

    def test_baseline(self):
        result, state = self._run()
        self.assertEqual(result["kind"], "baseline")
        self.assertEqual(result["new"], "1.0")
        self.assertEqual(state["sites"]["Testseite"]["value"], "1.0")

    def test_unveraendert(self):
        state = {"sites": {"Testseite": {"value": "1.0"}}}
        result, _ = self._run(state=state)
        self.assertIsNone(result)

    def test_aenderung(self):
        state = {"sites": {"Testseite": {"value": "1.0"}}}
        result, _ = self._run(body=b"v2.0", state=state)
        self.assertEqual(result["kind"], "change")
        self.assertEqual(result["old"], "1.0")
        self.assertEqual(result["new"], "2.0")

    def test_retry_bei_pending(self):
        state = {"sites": {"Testseite": {"value": "1.0",
                                        "pending_value": "2.0"}}}
        result, _ = self._run(body=b"v2.0", state=state)
        self.assertEqual(result["kind"], "retry")
        self.assertTrue(result["history_done"])

    def test_304(self):
        state = {"sites": {"Testseite": {"value": "1.0"}}}
        result, _ = self._run(status=304, state=state)
        self.assertIsNone(result)

    def test_etag_wird_gespeichert(self):
        _, state = self._run(headers={"etag": '"e1"',
                                      "last-modified": "x"})
        entry = state["sites"]["Testseite"]
        self.assertEqual(entry["etag"], '"e1"')
        self.assertEqual(entry["last_modified"], "x")


class TestRunCycle(unittest.TestCase):
    """Ganzer Check-Zyklus: fetch/send_email gemockt, State in tmp."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.state_path = Path(self.tmp.name) / "state.json"
        self.hist = Path(self.tmp.name) / "history"
        for attr, val in (("STATE_PATH", self.state_path),
                          ("HISTORY_DIR", self.hist)):
            p = mock.patch.object(newsbot, attr, val)
            p.start()
            self.addCleanup(p.stop)
        self.sites = [_site()]
        p = mock.patch.object(newsbot, "collect_sites",
                              return_value=self.sites)
        p.start()
        self.addCleanup(p.stop)

    def _cycle(self, body, mail_error=None):
        sent = []
        def fake_mail(cfg, subject, text):
            if mail_error:
                raise mail_error
            sent.append(subject)
        with mock.patch.object(newsbot, "fetch",
                               return_value=(200, {}, body)), \
             mock.patch.object(newsbot, "send_email", fake_mail):
            newsbot.run_cycle({})
        return sent

    def test_aenderung_mail_und_state(self):
        newsbot.save_state(self.state_path,
                           {"sites": {"Testseite": {"value": "1.0"}}})
        sent = self._cycle(b"v2.0")
        self.assertEqual(len(sent), 1)
        self.assertIn("Testseite", sent[0])
        state = newsbot.load_state(self.state_path)
        self.assertEqual(state["sites"]["Testseite"]["value"], "2.0")
        self.assertNotIn("pending_value", state["sites"]["Testseite"])
        # Historie wurde geschrieben
        self.assertTrue((self.hist / "testseite.md").exists())

    def test_mail_fehler_setzt_pending_und_retry(self):
        newsbot.save_state(self.state_path,
                           {"sites": {"Testseite": {"value": "1.0"}}})
        self._cycle(b"v2.0", mail_error=RuntimeError("smtp down"))
        state = newsbot.load_state(self.state_path)
        entry = state["sites"]["Testseite"]
        self.assertEqual(entry["value"], "1.0")          # noch nicht umgestellt
        self.assertEqual(entry["pending_value"], "2.0")  # Retry markiert
        # Nächster Lauf: gleiche Version -> retry, Mail geht durch
        sent = self._cycle(b"v2.0")
        self.assertEqual(len(sent), 1)
        entry = newsbot.load_state(self.state_path)["sites"]["Testseite"]
        self.assertEqual(entry["value"], "2.0")
        self.assertNotIn("pending_value", entry)

    def test_keine_aenderung_keine_mail(self):
        newsbot.save_state(self.state_path,
                           {"sites": {"Testseite": {"value": "1.0"}}})
        sent = self._cycle(b"v1.0")
        self.assertEqual(sent, [])


class TestChangeMail(unittest.TestCase):
    def test_einzeln(self):
        c = {"site": _site(notes="Hinweis"), "old": "1.0", "new": "2.0"}
        subject, body = newsbot.build_change_mail([c])
        self.assertIn("Testseite", subject)
        self.assertIn("2.0", subject)
        self.assertIn("Vorher:         1.0", body)
        self.assertIn("Hinweis", body)

    def test_mehrere(self):
        c1 = {"site": _site(), "old": "1.0", "new": "2.0"}
        c2 = {"site": _site(name="Andere", url="https://b.test/"),
              "old": None, "new": "9.9"}
        subject, body = newsbot.build_change_mail([c1, c2])
        self.assertIn("2 Änderungen", subject)
        self.assertIn("(erster Check)", body)

    def test_veroeffentlicht_und_erkannt(self):
        """Die Mail zeigt das Release-Datum, nicht die Scriptlaufzeit."""
        c = {"site": _site(), "old": "1.0", "new": "2.0",
             "releases": [{"version": "2.0", "date": "2026-10-20"},
                          {"version": "1.0", "date": "2026-01-01"}]}
        subject, body = newsbot.build_change_mail([c])
        self.assertIn("Veröffentlicht: 2026-10-20", body)
        self.assertIn("Erkannt:", body)
        self.assertNotIn("Zeitpunkt", body)
        self.assertIn("https://github.com/Wlanfr3ak/NewsBot2EMail", body)
        self.assertIn(f"NewsBot v{newsbot.__version__}", body)

    def test_veroeffentlicht_kombiniert(self):
        """Kombinierter Wert (PHP/GitLab): nur die geänderten Zweige."""
        c = {"site": _site(),
             "old": "8.5=8.5.11;8.4=8.4.27",
             "new": "8.5=8.5.12;8.4=8.4.27",
             "releases": [{"version": "8.5.12", "date": "2026-10-21"},
                          {"version": "8.4.27", "date": "2026-10-21"},
                          {"version": "8.5.11", "date": "2026-09-24"}]}
        subject, body = newsbot.build_change_mail([c])
        self.assertIn("Veröffentlicht: 8.5.12: 2026-10-21", body)
        self.assertNotIn("8.5.11: 2026-09-24", body)
        # 8.4.27 unverändert -> nicht nochmal datiert
        self.assertNotIn("8.4.27:", body)

    def test_veroeffentlicht_unbekannt(self):
        c = {"site": _site(), "old": "a", "new": "b"}
        subject, body = newsbot.build_change_mail([c])
        self.assertIn("Veröffentlicht: unbekannt", body)


if __name__ == "__main__":
    unittest.main()
