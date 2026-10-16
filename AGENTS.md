# AGENTS.md – NewsBot

## Projektübersicht

NewsBot überwacht konfigurierbare Webseiten auf neue Versionen bzw.
Änderungen und benachrichtigt per E-Mail. Reine Python-Standardbibliothek,
plattformübergreifend (Windows/Linux/macOS), keine externen Abhängigkeiten.

**Aktuelle Version: 1.16.0** (siehe `__version__` in `newsbot.py`)

## Projektstruktur

```
newsbot.py           Hauptprogramm (CLI, Check-Logik, E-Mail, Historie, Hooks)
sites/*.py           Seiten-Module: eine Datei pro überwachter Seite
history/*.md         Versionshistorie pro Seite (automatisch gepflegt)
archive/*.md         Changelog-Archive (bei Modulen mit CHANGELOG_URL)
downloads/<slug>/    Heruntergeladene Releases (bei Modulen mit DOWNLOADS)
config.json          Benutzerkonfiguration (SMTP, Optionen) – nicht committen
config.example.json  Vorlage für config.json
state.json           Letzte gesehene Werte pro Seite (Laufzeit) – nicht committen
.env                 SMTP-Passwort – nicht committen
.env.example         Vorlage für .env
newsbot.log          Rotierendes Log (Laufzeit) – nicht committen
requirements.txt     Leer – nur Standardbibliothek
```

## Seiten-Module (Vertrag)

Jede Datei `sites/<name>.py` (nicht mit `_` beginnend) wird automatisch
geladen und muss definieren:

```python
NAME = "..."        # Pflicht: Anzeigename
URL = "..."         # Pflicht: zu prüfende Adresse
METHOD = "regex"    # optional: regex | hash | etag (Default: regex)
PATTERN = r"..."    # bei METHOD="regex"
NOTES = "..."       # optional: erscheint in der Benachrichtigungs-Mail
SLUG = "..."        # optional: Dateiname der Historie (Default: NAME als Slug)

def extract(text) -> str:          # optional, überschreibt METHOD/PATTERN
def extract_history(text) -> list: # optional: [{"version","date"}, ...], neueste zuerst

CHANGELOG_URL = "..."              # optional: URL einer Changelog-/News-Seite
def extract_changelog(text) -> str:# optional: Seite -> Markdown-Text;
                                   #   füllt archive/<slug>_changelog.md
def update_changelog(existing):    # optional, Alternative zu CHANGELOG_URL:
                                   #   bekommt bisherigen Archiv-Text (| None),
                                   #   darf eigene Requests machen;
                                   #   Rückgabe: neuer Inhalt | None
DOWNLOADS = ["https://...{version}...",  # optional: URL-Templates,
             {"url": "...{version}...",  #   oder Dicts: "unzip" entpackt
              "unzip": True}]           #   geladene Zips (erstes .iso-
                                   #   Mitglied) unter dem Dateinamen
                                   #   ohne '.zip' und verwirft die Zip;
                                   #   "filename" überschreibt den Namen.
                                   #   {version} wird ersetzt, Dateien
                                   #   landen in downloads/<slug>/
def list_downloads(text, have, target_dir):  # optional, Alternative zu
                                   #   DOWNLOADS: dynamische Liste,
                                   #   Rückgabe [{"url","name"}] | [url, ...];
                                   #   Items dürfen ebenfalls "unzip" tragen

VERIFY_TLS = True   # optional, Default True. False = TLS-Verifikation
                    # aus (nur bei kaputter Zertifikatskette der Seite)
```

Gleichwertige Einträge sind weiterhin in `config.json` unter `sites`
möglich (für einfache regex/hash/etag-Fälle ohne Modul).

## Regeln für Änderungen (verbindlich)

1. **Versionsnummer hochzählen:** Bei JEDER Änderung am Code oder an den
   Konfigurationsvorlagen `__version__` in `newsbot.py` erhöhen
   (Semantic Versioning: MAJOR.MINOR.PATCH).
2. **Changelog pflegen:** Bei JEDER Änderung einen ausführlichen Eintrag
   im Changelog unten ergänzen – was, warum, betroffene Dateien.
3. **Keine externen Abhängigkeiten** ohne ausdrückliche Freigabe des Users –
   das Projekt soll mit nacktem Python lauffähig bleiben.
4. **Geheimnisse niemals in committete Dateien** schreiben. Passwörter
   ausschließlich über `.env` / `env:VARIABLE`-Referenzen in config.json.
5. **Kommentare und Nutzertexte auf Deutsch** (persönliches Projekt des Users).
6. Nach Codeänderungen `python -m py_compile newsbot.py` und idealerweise
   `python newsbot.py --dry-run` ausführen.

## Testen / Verifizieren

```bash
python -m py_compile newsbot.py   # Syntaxcheck
python newsbot.py --status        # Konfiguration + State anzeigen
python newsbot.py --dry-run       # Check ohne Seiteneffekte
python newsbot.py --once          # echter Check, setzt Baseline
python newsbot.py --test-mail     # SMTP-Zugang prüfen
```

## Changelog

### 1.16.0 – 2026-10-16

**Tests, Git-Repo, CI; Sicherheitsgrenze für die Newsletter-Probe.**

- `tests/` (neu): 108 Tests, reine Standardbibliothek (`unittest` +
  `unittest.mock`), komplett offline - Netzwerk wird gemockt.
  Aufruf: `python -m unittest discover -s tests`.
  - `test_newsbot.py`: Kernlogik - slugify, env-Auflösung,
    State-Roundtrip, gzip/deflate-Dekompression, extract_value
    (regex/hash/etag/extract), `_checksum_map`/`_verify_download`,
    Historie (init/append), Changelog-Archiv beider Hook-Varianten,
    `check_site` (baseline/change/retry/304/etag) und `run_cycle`
    inkl. Pending-Mail-Retry bei SMTP-Fehler.
  - `test_sites.py`: Vertragstest für ALLE Module (NAME/URL/SLUG,
    Pattern kompiliert, Hooks callbar, Downloads-Format,
    Slug-/Name-Eindeutigkeit) plus Parser-Fixture-Tests für
    mikrotik_newsletter (Voraus-Probe, .missing-Logik,
    mt.lv-Redirect-Auflösung), mikrotik_routeros (`_parse_date`
    inkl. 'Arp'-Tippfehler, Kanal-Kombi), ventoy, blossomos,
    memtest86, notepadpp, partedmagic, python_org.
  - `test_webui.py`: Format-Helfer + echter HTTP-Test auf
    Ephemeral-Port (Dashboard, Historie, Download-Listing,
    Range-Request 206, Traversal-Schutz, POST /check + Slug,
    "bereits laufend"-Fall, /log, 404).
- `sites/mikrotik_newsletter.py`: `PROBE_LIMIT = 5` - die
  Voraus-Probe stoppt spätestens nach 5 Nummern. Schutz vor
  Endlosschleife (und Dauer-Beschuss von mt.lv), falls der
  Kurzlink-Dienst künftig für beliebige Nummern weiterleitet
  statt 404. Durch den neuen Test gefunden.
- `.github/workflows/tests.yml` (neu): GitHub-Actions-Workflow,
  `unittest discover` auf Ubuntu + Windows, Python 3.11/3.13/3.15.
- `.gitignore`: + `nul`, `%TEMP%*` (Shell-Artefakte).
- Betroffene Dateien: `tests/` (neu), `sites/mikrotik_newsletter.py`,
  `newsbot.py` (Version), `AGENTS.md`, `README.md`, `.gitignore`,
  `.github/workflows/tests.yml` (neu).
- `__version__` auf 1.16.0.

### 1.15.0 – 2026-10-16

**Feature: MikroTik-Newsletter – Voraus-Probe auf mt.lv.**

- `sites/mikrotik_newsletter.py`: Neue Newsletter erscheinen auf
  mt.lv teils BEVOR sie auf mikrotik.com verlinkt sind ( konkret:
  mt.lv/news135 ging schon, als die Homepage nur bis #134
  verlinkte). Neu `_probe_ahead(linked_max)`: ab der höchsten
  verlinkten Nummer werden `mt.lv/news<N+1>`, `N+2`, … aufgelöst,
  bis der erste Kurzlink fehlschlägt (404).
  - `extract()` liefert jetzt die höchste auflösbare Nummer statt
    nur der höchsten verlinkten – ein noch unverlinkter Newsletter
    löst damit regulär Änderung + Mail aus.
  - `list_downloads()` lädt die PDFs im Probe-Bereich ebenfalls;
    Fehlschläge oberhalb der verlinkten Nummer bekommen KEINE
    `.missing`-Markierung (die Nummer kann später noch live gehen)
    und werden nächsten Lauf erneut versucht. `.missing` nur noch
    bei Lücken ≤ höchster verlinkter Nummer.
  - Kosten: 1–2 Extra-Requests auf mt.lv pro Check (der abschließende
    404). Keine Retry-Schleife nötig: die Probe stoppt am ersten 404,
    übersprungene Nummern dahinter werden nicht gesucht.
- Betroffene Dateien: `sites/mikrotik_newsletter.py`, `newsbot.py`
  (Version), `AGENTS.md`, `README.md`.
- `__version__` auf 1.15.0.

### 1.14.0 – 2026-09-23

**Feature: Hash-Verifikation, Einzelseiten-Checks, 12h-Intervall,
Debian-Autostart.**

- `newsbot.py`: nach jedem Download wird die Datei gegen die
  publizierten Hashes geprüft (`_checksum_map()` sammelt Einträge
  aus allen Hash-Dateien im selben Ordner – sha256sum.txt,
  SHA256SUMS, signed-hashes.txt, *.sha256, *.isodata.json; Format
  `<hexhash>  <name>`, Pfad-Präfixe werden gekürzt, längster Hash
  gewinnt: sha512 > sha256 > md5). Mismatch → Datei wird verworfen
  und beim nächsten Lauf erneut geladen. Die Prüfung läuft VOR dem
  Entpacken (Zip-Hash, nicht ISO-Hash).
- `run_cycle(cfg, only=slug)` prüft optional nur eine Seite;
  `webui.py` hat pro Zeile einen "Prüfen"-Button (POST
  `/check/<slug>`), der globale Button bleibt (POST `/check`).
- Daemon-Schleife neu: wartet auf `next_due` (Timer) ODER Wake-
  Event; vom Dashboard angeforderte Checks landen in `pending` und
  ändern den Regel-Zeitplan nicht (kein Reset des 12h-Intervalls,
  keine Doppel-Checks).
- `check_interval_minutes` auf 720 (12 h) gesetzt
  (config.json + config.example.json); manuelle Checks sind davon
  ausgenommen.
- Module: Hash-Dateien stehen jetzt ERST in `DOWNLOADS` (müssen
  vor den Nutzdaten da sein) und bekommen versionierte Namen, damit
  sie pro Release frisch geladen werden:
  - ventoy.py: + `sha256.txt` (SourceForge) als
    `ventoy-{v}-sha256.txt`
  - kali.py: `SHA256SUMS-{v}` + `.gpg`
  - parrot.py: `signed-hashes-{v}.txt`
  - memtest86.py: `sha256sum-{v}.txt`
  - caine.py, proxmox.py, blossomos.py: nur umgeordnet (schon
    versioniert)
  - notepadpp.py: + `npp.{v}.checksums.sha256` (GitHub)
  - Bestehende Dateien auf die neuen Namen umbenannt.
- `install_autostart.sh` / `remove_autostart.sh` (neu): systemd-
  User-Service für Debian/Linux (`~/.config/systemd/user/`,
  `Restart=on-failure`, Hinweis auf `loginctl enable-linger` für
  Betrieb ohne Login).
- `__version__` auf 1.14.0.

### 1.13.0 – 2026-09-23

**Feature: Web-Dashboard + Autostart.**

- `webui.py` (neu): eingebetteter lokaler Webserver
  (`http.server.ThreadingHTTPServer`, reine Standardbibliothek),
  bindet an `127.0.0.1:8321` (config.json: `"web"`). Seiten:
  - `/` – Dashboard: alle Seiten mit aktuellem Stand,
    letztem Check, letzter Änderung; ausstehende Mails als
    Badge; "Jetzt prüfen"-Button stößt einen Check an
    (POST /check, per Wake-Event bzw. Hintergrund-Thread).
  - `/history/<slug>`, `/archive/<slug>` – Historien- und
    Changelog-Markdown als HTML.
  - `/dl/<slug>/` + `/dl/<slug>/<datei>` – Download-Bereich mit
    Datei-Downloads (Content-Disposition: attachment, Range-
    Requests/206 für Resume bei Multi-GB-ISOs,
    Traversal-Schutz via resolve()+relative_to).
  - `/log` – die letzten 200 Zeilen von newsbot.log.
- `newsbot.py`: Daemon-Modus startet das Dashboard automatisch
  (`web.enabled`, Default an); neuer Flag `--web` startet nur das
  Dashboard ohne Check-Schleife. Die Daemon-Schleife wartet jetzt
  auf ein `threading.Event` statt starr `time.sleep`, damit der
  Web-Button den nächsten Check sofort auslöst.
- `install_autostart.ps1` / `remove_autostart.ps1` (neu):
  Autostart über den Startup-Ordner (`shell:startup` +
  NewsBot.lnk → pythonw.exe). Hintergrund: schtasks.exe und
  Register-ScheduledTask sind auf dieser Maschine ohne Admin
  gesperrt ("Zugriff verweigert"); die .lnk-Lösung braucht keine
  Rechte und zeigt kein Konsolenfenster.
- config.json + config.example.json: `"web"`-Sektion
  (`enabled`, `host`, `port`).
- Betroffene Dateien: `webui.py` (neu), `newsbot.py`,
  `config*.json`, `install_autostart.ps1` (neu),
  `remove_autostart.ps1` (neu), `AGENTS.md`, `README.md`.
- `__version__` auf 1.13.0.

### 1.12.0 – 2026-09-23

**Feature: BlossomOS-Modul (Online-Edition).**

- `sites/blossomos.py` (neu): Überwacht die Online-Edition von
  BlossomOS. Die Webseite (blossom.computer/downloads) ist eine
  SvelteKit-App, deren Download-Karten ihre Metadaten clientseitig
  von `https://cdn.blossomos.org/iso/isodata.json` laden
  (`{"name": "BlossomOS-YYYY.MM.DD-x86_64.iso", "sha256": "…"}`) –
  diese 128-Byte-Datei ist die überwachte URL.
  - `extract()`: Version = Datum im ISO-Namen (aktuell 2026.09.18).
  - `extract_history()`: die Version ist selbst ein Datum
    (`YYYY.MM.DD` → `YYYY-MM-DD`); eine öffentliche Release-Liste
    existiert nicht, die Historie wächst mit jedem Release.
  - `DOWNLOADS`: die Online-ISO direkt vom CDN (~8,4 GB) plus
    `isodata.json` als versionierter Hash-Beleg
    (`BlossomOS-{version}-x86_64.isodata.json`).
  - Hinweis: Der Download-Button der Webseite ist mit
    Cloudflare-Turnstile geschützt (`/api/downloads/verify`), die
    ISO selbst liegt aber offen am CDN.
- `newsbot.py`: `"filename"` in `DOWNLOADS`-Dicts unterstützt jetzt
  ebenfalls den `{version}`-Platzhalter.
- Betroffene Dateien: `sites/blossomos.py` (neu), `newsbot.py`,
  `AGENTS.md`, `README.md`.
- `__version__` auf 1.12.0.

### 1.11.0 – 2026-09-21

**Feature: Notepad++-Modul (x64-Installer + Changelog-Archiv).**

- `sites/notepadpp.py` (neu): Überwacht
  https://notepad-plus-plus.org/downloads/ (`Current Version X.Y.Z`
  → aktuell 8.9.8; Fallback: erster `/downloads/vX/`-Link).
  - `DOWNLOADS`: nur der x64-Installer
    `npp.{version}.Installer.x64.exe` (~7 MB) via GitHub-Releases –
    portable/arm64/x86 werden nicht geladen.
  - `extract_history()`: alle ~113 Versionen aus der
    Download-Übersicht; echte Daten von der GitHub-Releases-API
    (`tag_name` → `published_at`, bis zu 3 API-Seiten). Uralte
    6.x/7.x-Releases ohne GitHub-Tag bekommen 'n/a'.
  - `update_changelog()`: die Änderungsliste steckt je Version auf
    `/downloads/vX.Y.Z/` (`Release Date:` + `<h3 id="notepad-…">` +
    `<ol>`). Fehlende Abschnitte werden inkrementell nachgeholt –
    Erstlauf archivierte 113 Abschnitte bis zurück zu 6.2.3
    (2012-12-16), ~221 KB. Sonderfall: der Scherz-Eintrag '666'
    liefert 404 und wird in `_SKIP` dauerhaft übersprungen.
  - Bug beim Parsen vermieden: die Changelog-`<h3>` wird über
    `id="notepad-…"` identifiziert, damit die Regex nicht die
    Download-`<ul>`-Blöcke (x64/x86/arm64) einsammelt.
- Betroffene Dateien: `sites/notepadpp.py` (neu), `newsbot.py`
  (Version), `AGENTS.md`, `README.md`.
- `__version__` auf 1.11.0.

### 1.10.0 – 2026-09-21

**Feature: Zip-Entpackung für Downloads (Memtest-ISOs).**

- `newsbot.py`: `DOWNLOADS`-Einträge dürfen jetzt Dicts sein –
  `{"url": ..., "unzip": True}` lädt die Zip in eine `.part`-Datei,
  entpackt das erste `.iso`-Mitglied (Fallback: erstes Mitglied) und
  speichert es unter dem Zip-Dateinamen ohne `.zip` (also
  `mt86plus_8.10_x86_64.iso.zip` → `mt86plus_8.10_x86_64.iso`);
  die Zip selbst wird nach erfolgreichem Entpacken verworfen.
  Da der Vorhanden-Check auf die entpackte Datei zeigt, wird die
  gleiche Version nicht erneut geladen. Auch
  `list_downloads()`-Items dürfen `"unzip"` tragen. Optional
  überschreibt `"filename"` den Zielnamen. Neuer Import `zipfile`
  (Standardbibliothek).
- `sites/memtest86.py`: die drei ISO-Downloads auf `unzip: True`
  umgestellt – die Zip-Inhalte hießen generisch `memtest.iso`/
  `grub-memtest.iso` und wären ununterscheidbar; jetzt heißen die
  Dateien wie ihre Quell-Zips. `sha256sum.txt` bleibt.
- Bestehende Zips einmalig migriert: drei ISOs entpackt
  (`mt86plus_8.10_i586.iso` 6,2 MB, `mt86plus_8.10_x86_64.iso`
  6,2 MB, `mt86plus_8.10_x86_64.grub.iso` 20,2 MB), Zips gelöscht.
- Betroffene Dateien: `newsbot.py`, `sites/memtest86.py`,
  `downloads/memtest86/`, `AGENTS.md`, `README.md`.
- `__version__` auf 1.10.0.

### 1.9.0 – 2026-09-21

**Feature: Memtest86+-Modul (3 Linux-ISOs + GitHub-Changelog).**

- `sites/memtest86.py` (neu): Überwacht https://www.memtest.org/
  (`mt86plus_X.YZ_x86_64.iso.zip` auf der Seite → aktuell 8.10).
  - `DOWNLOADS`: die drei Linux-Boot-ISOs als Zip
    (`_i586`, `_x86_64`, `_x86_64.grub` – 0,2/0,2/6,6 MB, enthalten
    `memtest.iso` bzw. `grub-memtest.iso`) plus `sha256sum.txt`;
    alle drei Zips gegen die Checksummen verifiziert (Hinweis:
    die sum-Datei listet Pfade mit `vX.YZ/`-Präfix).
  - `extract_history()` + `extract_changelog()`: die Seite selbst
    hat keine Release-Historie – beides kommt von der
    GitHub-Releases-API (`memtest86plus/memtest86plus`), 7 Releases
    seit v6.01 mit `published_at`-Daten und Markdown-Notes. Das
    Changelog-Archiv nutzt den einfachen Hook:
    `CHANGELOG_URL` zeigt direkt auf die API und
    `extract_changelog()` rendert das JSON zu Markdown.
- `__version__` auf 1.9.0.
- Betroffene Dateien: `sites/memtest86.py` (neu), `newsbot.py`,
  `AGENTS.md`, `README.md`. Neue Laufzeit-Artefakte:
  `history/memtest86.md`, `archive/memtest86_changelog.md`,
  `downloads/memtest86/*`.

### 1.8.0 – 2026-09-21

**Feature: Proxmox-VE-Modul (nur PVE, mit ISO-Download).**

- `sites/proxmox.py` (neu): Überwacht Proxmox VE. Quelle ist
  `enterprise.proxmox.com/iso/` (das Ziel der Download-Links von
  proxmox.com/en/downloads; `download.proxmox.com` hat derzeit ein
  ungültiges Zertifikat – Hostname-Mismatch). Jede Karte enthält
  Dateiname, Größe, Datum und SHA256 inline. Nur amd64-PVE-ISOs
  (`proxmox-ve_X.Y-Z.iso`), kein ARM64/PBS/PMG/PDM.
  - `extract()`: neueste Version `9.2-1` (inkl. Respins über den
    `-Z`-Build-Suffix), sortiert per Versionstupel.
  - `extract_history()`: 4 VE-ISOs mit echten Daten
    (9.2-1/2026-05-21 … 7.4-1/2023-03-23).
  - `DOWNLOADS`: ISO (~1,7 GB) + `.sha256` + `.asc`.
  - `extract_changelog()` + `CHANGELOG_URL`: die Wiki-Seite
    `pve.proxmox.com/wiki/Roadmap` enthält ALLE Release-Sektionen
    (`<h2><span class="mw-headline" id="Proxmox_VE_X">`) inkl.
    `Released DD. Month YYYY`-Datum – wird komplett archiviert
    (59 Sektionen bis zurück zu 0.9, ~450 KB).
- ISO SHA256 gegen die geladene .sha256-Datei verifiziert.
- `__version__` auf 1.8.0.
- Betroffene Dateien: `sites/proxmox.py` (neu), `newsbot.py`,
  `AGENTS.md`, `README.md`. Neue Laufzeit-Artefakte:
  `history/proxmox-ve.md`, `archive/proxmox-ve_changelog.md`,
  `downloads/proxmox-ve/*`.

### 1.7.0 – 2026-09-21

**Feature: Parrot-Security- und Kali-Linux-Module (mit Downloads).**

- `sites/parrot.py` (neu): Überwacht
  https://parrotsec.org/download/ – Version aus dem
  `Parrot-security-X.Y_amd64.iso`-Link (aktuell 7.3).
  - `DOWNLOADS`: Security-ISO (~8,5 GB) + `signed-hashes.txt`
    von deb.parrot.sh.
  - `extract_history()`: Release-Daten aus den Blog-Slug-Daten
    (`/blog/YYYY-MM-DD-parrot-X.Y-release-notes`).
  - `update_changelog()`: Release-Notes-Posts liefern ihren Inhalt
    als fertiges Markdown im `__NEXT_DATA__`-JSON (Next.js-CSR) –
    kein HTML-Umbau nötig. Archiv-Schlüssel `parrot-X.Y`.
    ACHTUNG: Post-URLs brauchen abschließenden `/` – sonst
    Redirect-Schleife (301 http ↔ 308 https).
- `sites/kali.py` (neu): Überwacht
  https://www.kali.org/get-kali/ – Version aus
  `kali-linux-YYYY.W-installer-amd64.iso` (aktuell 2026.2).
  - `DOWNLOADS`: Standard-Installer-ISO (~4,8 GB) +
    `SHA256SUMS`/`SHA256SUMS.gpg` + das Everything-Offline-ISO als
    `.torrent` (das Everything-ISO existiert nur via Torrent –
    auf cdimage.kali.org und kali.download kein Direkt-ISO).
  - `extract_history()`/`update_changelog()`: Release-Posts auf
    kali.org/blog/ über paginierte Index-Seiten (`/blog/page/N/`,
    max. 6); Datum aus `<time datetime>` im Index, Artikel-HTML
    (`<article>`) wird zu Markdown – Achtung: Kali nutzt
    unquotierte HTML-Attribute (`href=https://...`).
  - Archiv: 25 Release-Posts 2020.2–2026.2 (~490 KB).
- `__version__` auf 1.7.0.
- Betroffene Dateien: `sites/parrot.py` (neu), `sites/kali.py`
  (neu), `newsbot.py`, `AGENTS.md`, `README.md`. Neue
  Laufzeit-Artefakte: `history/parrot-security.md`,
  `history/kali-linux.md`, `archive/parrot-security_changelog.md`,
  `archive/kali-linux_changelog.md`,
  `downloads/parrot-security/*`, `downloads/kali-linux/*`.

### 1.6.0 – 2026-09-21

**Feature: Ubuntu-MATE-Modul (beide Release-Zweige + Release-Notes-Archiv).**

- `sites/ubuntu_mate.py` (neu): Überwacht
  https://ubuntu-mate.org/download/. Die Seite bietet zwei Releases
  (`release-item`-Blöcke): Interim (25.10 „Questing Quokka") und
  LTS (24.04.5 „Noble Numbat"). Keine Downloads (User-Wunsch).
  - `extract()`: kombinierter Status `interim=25.10;lts=24.04.5` –
    die Mail geht raus, sobald EIN Zweig eine neue Version bekommt.
  - `extract_history()`: echte Veröffentlichungsdaten aus dem
    cdimage-Verzeichnis (`releases/<codename|version>/release/`,
    Dateidatum des Desktop-ISO) – für LTS inkl. aller Point-Releases
    (24.04.3/.4/.5), sortiert nach Datum.
  - `update_changelog()`: archiviert ALLE Release-Notes-Artikel aus
    dem Blog-Index (`/blog/*-release-notes/`, 9 Artikel seit 20.04)
    unter `archive/ubuntu-mate_changelog.md`; `_to_markdown()`
    wandelt Artikel-HTML in Markdown um (h2–h6, Listen, Links mit
    absoluten URLs, Metadaten/SVG entfernt). Schlüssel pro Abschnitt:
    Codename-Slug (`## noble-numbat – 2024-04-23`).
  - Für aktuelle Releases OHNE Notes-Artikel (25.10 hat keine im
    Blog) wird ein `## <slug>-hinweis`-Platzhalter geschrieben –
    eigener Schlüssel, damit später erscheinende Notes trotzdem
    als eigener Abschnitt ergänzt werden.
- `__version__` auf 1.6.0.
- Betroffene Dateien: `sites/ubuntu_mate.py` (neu), `newsbot.py`,
  `AGENTS.md`, `README.md`. Neue Laufzeit-Artefakte:
  `history/ubuntu-mate.md`, `archive/ubuntu-mate_changelog.md`.

### 1.5.1 – 2026-09-21

**Bugfix: RouterOS-Changelog-Datumsformate + Archiv-Selbstreparatur.**

- `sites/mikrotik_routeros.py`: Die CHANGELOG-Texte nutzen je nach
  Ära unterschiedliche Kopfzeilen/Datumsformate – bisher wurde nur
  `What's new in X (YYYY-MM-DD)` erkannt, wodurch 611 von 623
  Archiv-Abschnitten `?` als Datum bekamen. Neu:
  - `_TITLE_RE` akzeptiert auch `New RouterOS X (...)` (RouterOS-6-Ära).
  - `_parse_date()` normalisiert vier Formate zu `YYYY-MM-DD`:
    `2026-09-16`, `2026-Aug-21 16:06`, `Dec/22/2021 13:49:22`,
    `Aug.25.15-12:59:46` (zweistelliges Jahr). `_MONTHS` enthält
    zusätzlich `arp`→April – Upstream-Tippfehler im
    7.23beta5-Changelog (`2026-Arp-01`).
  - `update_changelog()` repariert sich selbst: Abschnitte mit
    `?`-Datum werden einmalig neu geholt und an ihrer Position
    ersetzt; unlesbare Daten werden als `n/a` geschrieben (final,
    kein Endlos-Retry). Ergebnis: 621/623 Abschnitte mit echtem
    Datum; `n/a` nur bei 3.30 (Changelog enthält kein Datum) und
    6.33.6 (Eintrag ohne Kopfzeile).
- `__version__` auf 1.5.1.
- Betroffene Dateien: `sites/mikrotik_routeros.py`, `newsbot.py`,
  `AGENTS.md`. Laufzeit-Artefakt: repariertes
  `archive/mikrotik-routeros_changelog.md`.

### 1.5.0 – 2026-09-21

**Feature: MikroTik-Module (Newsletter-PDF-Archiv + RouterOS-Kanäle) +
zwei neue Hook-Typen.**

- `sites/mikrotik_newsletter.py` (neu): Überwacht
  https://mikrotik.com/ auf die neueste Newsletter-Nummer
  (`Newsletter #133 | June 2026` → Version `133`,
  `extract_history()` liefert Monat/Jahr der letzten Ausgaben).
  - `list_downloads()`: archiviert ALLE Newsletter-PDFs ab #77 unter
    `downloads/mikrotik-newsletter/news_<nr>.pdf`. Die Kurzlinks
    `mt.lv/news<nr>` existieren erst ab #77 (ältere → 404);
    Redirect-Ziele variieren je Ära: direkte PDFs
    (download2.mikrotik.com, S3) oder Seafile-Shares
    (box.mikrotik.com, `?dl=1` liefert die Datei direkt).
    `_resolve_pdf_url()` liest den Location-Header ohne Redirect zu
    folgen und hängt bei Shares `?dl=1` an.
  - Nicht auflösbare Nummern bekommen eine `<name>.missing`-Markierung
    und werden nicht erneut versucht; Download-Fehler dagegen werden
    beim nächsten Lauf nachgeholt. Erstlauf lud 44 PDFs (~300 MB),
    12 Lücken (81–87, 94, 106–109) existieren upstream nicht.
- `sites/mikrotik_routeros.py` (neu): Überwacht die RouterOS-
  Release-Kanäle. Versionslisten kommen aus den serverseitig
  gerenderten Seiten `mikrotik.com/download/changelogs/<kanal>`
  (`data-changelog-version`-Attribute), Changelog-Texte vom offiziellen
  Update-Endpoint `upgrade.mikrotik.com/routeros/<version>/CHANGELOG`.
  - `CHANNELS` wählt die benachrichtigten Kanäle (stable/long-term/
    testing/development); bei mehreren Kanälen wird ein kombinierter
    Statuswert `stable=7.24.4;long-term=7.23.7` geführt – die Mail
    geht raus, sobald EIN überwachter Kanal eine neue Version hat.
  - `update_changelog()` baut `archive/mikrotik-routeros_changelog.md`
    inkrementell für `ARCHIVE_CHANNELS` auf (Default: alle vier
    Kanäle; Erstlauf 623 Abschnitte, ~5 MB, Folgeläufe nur neue).
  - `site_options.mikrotik_routeros` in config.json überschreibt
    `channels`/`archive_channels` ohne Codeänderung (`_options()`
    liest config.json relativ zum Modulpfad).
  - Keine Downloads – RouterOS-Dateien werden nie geladen (expliziter
    User-Wunsch).
- `newsbot.py`: zwei neue Hook-Typen im Modul-Vertrag:
  - `list_downloads(text, have, target_dir)` als dynamische Alternative
    zu `DOWNLOADS`-Templates (`run_site_hooks()` bevorzugt sie,
    `download_releases()` akzeptiert Dicts `{url, name}` neben Strings).
  - `update_changelog(existing)` als Alternative zu
    `CHANGELOG_URL`+`extract_changelog()` für Module, die ihr Archiv
    aus mehreren Requests selbst aufbauen
    (`update_changelog_archive()`, `_archive_body()`).
  - `check_site()` reicht den Seitentext im Ergebnis durch
    (`result["text"]`), damit `list_downloads`/`extract_history` ihn
    wiederverwenden können. `__version__` auf 1.5.0.
- `config.example.json`/`config.json`: neuer Schlüssel `site_options`.
- Betroffene Dateien: `newsbot.py`, `sites/mikrotik_newsletter.py`
  (neu), `sites/mikrotik_routeros.py` (neu), `config.json`,
  `config.example.json`, `README.md`, `AGENTS.md`. Neue
  Laufzeit-Artefakte: `history/mikrotik-newsletter.md`,
  `history/mikrotik-routeros.md`,
  `archive/mikrotik-routeros_changelog.md`,
  `downloads/mikrotik-newsletter/*.pdf` (+ `.missing`-Marker).

### 1.4.0 – 2026-09-21

**Feature: Parted-Magic-Modul + Bugfix Changelog-Vergleich.**

- `sites/partedmagic.py` (neu): Überwacht
  https://partedmagic.com/news/. Die Seite enthält alle
  Release-Ankündigungen als `<h2>Parted Magic VERSION</h2>`
  (neueste zuerst) mit `<h3>`-Feature-Sektionen darunter.
  - `extract()`: neueste Version (aktuell 26.09_2 – neues Schema
    `YY.MM[_N]`, davor `YYYY_MM_DD`).
  - `extract_history()`: alle Releases; `_release_date()` leitet das
    Datum aus dem Schema ab (`2026_06_04` → `2026-06-04`,
    `26.09` → `2026-09` ohne Tag).
  - `extract_changelog()`: alle News-Abschnitte (Releases + sonstige
    Meldungen) als Markdown (~40 KB); h3 → `###`, Listen → Bullets,
    Abschnitt endet vor Kommentar-/Footer-Bereich (`_CUTOFF_RE`).
  - Keine Downloads (kostenpflichtige Software), `NOTES` verweist
    auf den Store.
- Bugfix `update_changelog_archive()`: `rpartition` → `partition`
  beim Inhaltsvergleich. Der Changelog-Text selbst kann `---\n\n`
  enthalten; rpartition schnitt am letzten Vorkommnis und verglich
  nur den Schwanz – die Datei wurde dadurch bei jedem Lauf neu
  geschrieben obwohl unverändert.
- Betroffene Dateien: `sites/partedmagic.py` (neu), `newsbot.py`,
  `AGENTS.md`. Neue Laufzeit-Artefakte: `history/parted-magic.md`,
  `archive/parted-magic_changelog.md`.

### 1.3.0 – 2026-09-21

**Feature: CAINE-Modul + VERIFY_TLS-Option + Streaming-Downloads.**

- `sites/caine.py` (neu): Überwacht die Release-Kategorie des
  CAINE-News-Blogs (page6/files/category-release.html). Eintrag-Format:
  `CAINE X.Y Codename released DD/Mon/YYYY` + Blog-Body mit Changelog.
  - `extract()`: neueste Version (aktuell 14.0).
  - `extract_history()`: alle Releases mit echten Daten
    (14.0/2025-03-24, 13.0/2023-03-16, 12.4/2021-12-10, 11.0/2019-12-01).
  - `extract_changelog()`: alle Blog-Bodies als Markdown
    (~12 KB, `archive/caine_changelog.md`); HTML-Tags werden entfernt,
    Entities aufgelöst, Leerzeilen normalisiert.
  - `DOWNLOADS`: `caine{version}.iso` (~4,2 GB) + `{version}_sha256.txt`
    vom cfitaly-Mirror (valide TLS; caine-live.net liefert zeitweise
    eine unvollständige Zertifikatskette).
- `VERIFY_TLS` als neues Modul-Attribut (Default True): Bei `False`
  nutzt `fetch()` und `download_releases()` einen unverifizierten
  SSL-Kontext (`_ssl_context()`) und loggt eine Warnung – für Seiten
  mit kaputter Zertifikatskette.
- `download_releases()` streamt jetzt mit `shutil.copyfileobj` in die
  `.part`-Datei statt die Antwort komplett in den RAM zu laden –
  wichtig für Multi-GB-Images wie das CAINE-ISO.
- Hook-Reihenfolge korrigiert: `run_site_hooks()` läuft jetzt NACH der
  Ergebnisverarbeitung (Historie/State) statt davor und bekommt die
  aktuell gültige Version als Parameter – eine frisch erkannte Version
  wird so im selben Zyklus heruntergeladen statt erst beim nächsten.
- Betroffene Dateien: `newsbot.py`, `sites/caine.py` (neu),
  `AGENTS.md`, `README.md`. Neue Laufzeit-Artefakte:
  `history/caine.md`, `archive/caine_changelog.md`,
  `downloads/caine/*`.

### 1.2.0 – 2026-09-21

**Feature: Changelog-Archiv und Release-Downloads (Modul-Hooks).**

- Neue optionale Modul-Hooks, ausgeführt nach jedem erfolgreichen
  Seiten-Check (`run_site_hooks()`), unabhängig von Versionsänderungen:
  - `CHANGELOG_URL` + `extract_changelog(text)`: Die Funktion wandelt
    eine News-/Changelog-Seite in Markdown um; NewsBot schreibt sie nach
    `archive/<slug>_changelog.md` (`update_changelog_archive()`). Die
    Datei wird nur neu geschrieben, wenn sich der Inhalt ändert – der
    Stand-Zeitstempel im Kopf wird vom Vergleich ausgenommen.
  - `DOWNLOADS`: Liste von URL-Templates mit `{version}`-Platzhalter.
    `download_releases()` lädt fehlende Dateien nach
    `downloads/<slug>/` – vorhandene werden übersprungen, gelöschte
    beim nächsten Lauf erneut geholt („immer bereithalten").
    Download über `.part`-Tempdatei mit atomarem Rename;
    `download_filename()` behandelt SourceForge-`/download`-Endungen.
- `sites/ventoy.py`: `CHANGELOG_URL` auf doc_news.html gesetzt;
  `extract_changelog()` parst die News-Einträge
  (`<li class='news'>DATUM --- VERSION release` + `<ol>`-Listen) in
  Markdown – 104 Release-Abschnitte werden archiviert. `DOWNLOADS`
  enthält das Windows-ZIP via SourceForge (Linux/LiveCD als
  auskommentierte Templates). `html.unescape` + Tag-Stripping für
  saubere Listeneinträge.
- `newsbot.py`: Konstanten `ARCHIVE_DIR`, `DOWNLOAD_DIR`;
  `load_site_modules()` liest die neuen Modul-Attribute;
  Hooks laufen nicht im `--dry-run`-Modus.
- `.gitignore`: `downloads/` ergänzt (Binärdateien).
- Betroffene Dateien: `newsbot.py`, `sites/ventoy.py`, `.gitignore`,
  `README.md`, `AGENTS.md`. Neue Laufzeit-Artefakte:
  `archive/ventoy_changelog.md`, `downloads/ventoy/*.zip`.

### 1.1.0 – 2026-09-21

**Feature: Seiten-Module und Versionshistorie.**

- `sites/`-Verzeichnis eingeführt: Jede überwachte Seite ist ein eigenes
  Python-Modul. Module werden automatisch per `importlib` geladen
  (`load_site_modules()`); kaputte Module werden geloggt und übersprungen.
  Modul-Vertrag: `NAME`/`URL` pflicht, optional `METHOD`, `PATTERN`,
  `NOTES`, `SLUG`, `extract(text)`, `extract_history(text)` – siehe
  Abschnitt „Seiten-Module (Vertrag)".
- `sites/ventoy.py`: Überwacht https://www.ventoy.net/en/download.html.
  Die Seite enthält ein JavaScript-Array `ReleaseList` mit allen
  Versionen und echten Veröffentlichungsdaten; `extract()` liefert die
  neueste (ReleaseList[0]), `extract_history()` die komplette Liste
  (dedupliziert, neueste zuerst).
- `sites/python_org.py`: Bisheriger config.json-Eintrag „Python Releases"
  als Modul überführt (METHOD/PATTERN ohne eigenen Code).
- Versionshistorie: Pro Seite wird `history/<slug>.md` gepflegt
  (`init_history()`, `append_history()`). Beim Baseline-Check wird die
  Datei angelegt – mit `extract_history()` werden alle bekannten Releases
  samt echter Veröffentlichungsdaten eingetragen, sonst nur der
  gefundene Wert. Neue Versionen werden mit Erkennungsdatum, Upstream-
  Datum (falls bekannt) und Vorgängerversion direkt unter dem
  Tabellenkopf eingefügt (neueste zuerst). Die Historie wird bei
  Erkennung geschrieben – unabhängig vom Mailversand.
- Bugfix: `check_site()` liefert nun Ergebnis-Dicts mit `kind`
  (baseline/change/retry). Zuvor blockierte `pending_value` den
  Mail-Retry dauerhaft (erkannte Version == pending → „unverändert",
  Mail ging nie raus). Jetzt wird `kind="retry"` erzeugt und die Mail
  erneut versucht, ohne die Historie zu duplizieren (`history_done`).
- `collect_sites()` fasst config.json-`sites` und `sites/`-Module
  zusammen; `run_cycle()` und `print_status()` nutzen die gemeinsame
  Liste. `print_status` zeigt Methode (inkl. `extract()`) und
  Historienpfad an.
- `extract_value()`: `extract()`-Funktion eines Moduls hat Vorrang vor
  METHOD/PATTERN.
- `config.json`: `sites` geleert (Python-Releases ist jetzt ein Modul),
  `user_agent` auf NewsBot/1.1.
- Betroffene Dateien: `newsbot.py`, `sites/ventoy.py` (neu),
  `sites/python_org.py` (neu), `config.json`, `config.example.json`,
  `README.md`, `AGENTS.md`.

### 1.0.1 – 2026-09-21

**Bugfix: Gzip-komprimierte Antworten und Konsolen-Encoding.**

- `newsbot.py`:
  - Neue Funktion `decompress_body()`: Dekomprimiert Antwort-Bodies
    anhand des `Content-Encoding`-Headers (`gzip`, `deflate` inkl.
    Raw-Deflate-Fallback). `urllib.request` dekomprimiert nicht
    automatisch – Server wie python.org liefern gzip auch ohne explizites
    `Accept-Encoding`, wodurch Regex-Muster ins Leere liefen.
  - `fetch()` sendet nun explizit `Accept-Encoding: gzip, deflate` und
    ruft `decompress_body()` vor der Weiterverarbeitung auf. Damit
    funktionieren alle drei Methoden (`regex`, `hash`, `etag`) auch mit
    komprimierten Antworten.
  - `main()` rekonfiguriert `stdout`/`stderr` auf UTF-8, damit Umlaute
    in der Windows-Konsole korrekt dargestellt werden.
  - `__version__` auf `1.0.1` erhöht.
- Betroffene Dateien: `newsbot.py`, `AGENTS.md`.

### 1.0.0 – 2026-09-21

**Initiale Version.** Kompletter Neuaufbau des Projekts.

- `newsbot.py`: Kernprogramm mit drei Überwachungsmethoden:
  - `regex`: Versionsstring per regulärem Ausdruck aus dem Seitentext
    extrahieren (unempfindlich gegen dynamische Seiteninhalte).
  - `hash`: SHA-256 über den kompletten Antwort-Body (jede Änderung).
  - `etag`: Vergleich von `ETag`-/`Last-Modified`-Headern.
- HTTP-Client mit `urllib.request`: sendet `If-None-Match` /
  `If-Modified-Since` für konditionelle Requests (304 = unverändert),
  konfigurierbarer User-Agent und Timeout.
- Änderungserkennung mit Baseline-Logik: Der erste Check speichert den
  gefundenen Wert still als Referenz, erst spätere Änderungen lösen eine
  Benachrichtigung aus.
- E-Mail-Versand via `smtplib`: SSL (Port 465) oder STARTTLS (Port 587),
  Digest-E-Mail bei mehreren gleichzeitigen Änderungen, deutsches Format
  mit altem/neuem Wert, URL, Zeitpunkt und optionalem Hinweis.
- Fehlertoleranz: Schlägt der Versand fehl, wird der neue Wert als
  `pending_value` in `state.json` gemerkt und beim nächsten Lauf erneut
  benachrichtigt (kein verlorener Alarm, kein Spam).
- Zustandspersistenz in `state.json` (Wert, ETag, Last-Modified,
  Zeitstempel der letzten Prüfung/Änderung).
- CLI: `--once` (Einmalcheck für Scheduler), `--dry-run` (ohne
  Seiteneffekte), `--test-mail`, `--status`, `--config`, `--version`.
  Ohne Flags läuft eine Dauerschleife mit `check_interval_minutes`.
- Logging auf Konsole und rotierend in `newsbot.log` (1 MB × 3).
- `.env`-Loader (KEY=VALUE) plus `env:`-Präfix-Auflösung in config.json,
  damit das SMTP-Passwort nicht in der Konfiguration steht.
- `config.example.json` / `config.json`: Vorlage mit Beispiel-Seite
  (Python-Releases auf python.org via Regex).
- `.gitignore`: schließt `.env`, `state.json`, `config.json`, Logs aus.
- `README.md`: Einrichtung, Methoden-Doku, Aufgabenplanung/cron,
  Hinweise zu Gmail/GMX/Outlook.
