# NewsBot

Überwacht Webseiten regelmäßig auf neue Versionen und schickt eine E-Mail,
sobald sich etwas ändert. Reines Python (Standardbibliothek) – läuft auf
Windows, Linux und macOS ohne zusätzliche Pakete.

Jede überwachte Seite ist ein eigenes **Modul** im Ordner `sites/`. Für jede
Seite führt der Bot eine **Versionshistorie** in `history/` mit – bei Seiten
wie Ventoy mit echten Veröffentlichungsdaten.

## Schnellstart

1. **Konfiguration anlegen**

   `config.example.json` nach `config.json` kopieren und den `email`-Block
   ausfüllen. Das Passwort gehört **nicht** in die config.json – stattdessen
   `.env.example` nach `.env` kopieren und dort `NEWSBOT_SMTP_PASSWORD`
   setzen. In config.json steht dann nur `"password": "env:NEWSBOT_SMTP_PASSWORD"`.

2. **Testen**

   ```bash
   python newsbot.py --status      # überwachte Seiten + Historie anzeigen
   python newsbot.py --once        # einmaliger Check
   python newsbot.py --test-mail   # Test-E-Mail senden
   python newsbot.py --dry-run     # Check ohne Mail/State/Historie
   ```

3. **Dauerbetrieb**

   ```bash
   python newsbot.py
   ```

   …oder besser per Aufgabenplanung/cron (siehe unten).

## Seiten-Module (`sites/`)

Jede Datei `sites/<name>.py` ist eine überwachte Seite. Minimales Modul:

```python
NAME = "Mein Tool"
URL = "https://example.org/download"
METHOD = "regex"                      # regex | hash | etag
PATTERN = r"Version\s+(\d+\.\d+)"     # bei METHOD = "regex"
```

Optional mit eigener Logik und echter Release-Historie:

```python
NAME = "Ventoy"
URL = "https://www.ventoy.net/en/download.html"
NOTES = "..."                          # optional, erscheint in der Mail
SLUG = "ventoy"                        # optional, Dateiname der Historie

def extract(text):
    ...                                # gibt den aktuellen Versionsstring zurück

def extract_history(text):
    ...                                # optional: [{"version": "1.1.17",
                                       #            "date": "2026-07-24"}, ...]
                                       # neueste zuerst

CHANGELOG_URL = "https://..."          # optional: Changelog-/News-Seite
def extract_changelog(text):
    ...                                # optional: HTML -> Markdown;
                                       # füllt archive/<slug>_changelog.md

def update_changelog(existing):
    ...                                # optional, Alternative zu
                                       # CHANGELOG_URL: bekommt den
                                       # bisherigen Archiv-Text (oder
                                       # None), darf selbst Requests
                                       # machen; Rückgabe: neuer
                                       # Inhalt oder None (unverändert)

DOWNLOADS = [                          # optional: Release-Dateien laden
    "https://.../tool-{version}.zip",  # {version} wird ersetzt
    {"url": ".../img-{version}.iso.zip",  # oder Dict: "unzip" entpackt
     "unzip": True},                   # die Zip (erstes .iso-Mitglied),
                                       # speichert unter dem Zip-Namen
                                       # ohne '.zip', verwirft die Zip;
                                       # "filename" setzt den Namen
]

def list_downloads(text, have, target_dir):
    ...                                # optional, Alternative zu
                                       # DOWNLOADS: dynamische Liste;
                                       # Rückgabe: [{"url": ..., "name": ...}]
                                       # oder URL-Strings; Items dürfen
                                       # ebenfalls "unzip": True tragen

VERIFY_TLS = True                      # optional, Default True.
                                       # False = TLS-Prüfung aus (nur
                                       # bei kaputter Zertifikatskette)
```

Module, die mit `_` beginnen, werden ignoriert. Kaputte Module werden
geloggt und übersprungen, ohne den Lauf abzubrechen.

### Aktuell mitgelieferte Module

| Modul | Überwacht | Historie | Changelog | Download |
|-------|-----------|----------|-----------|----------|
| `ventoy.py` | neueste Version | echte Daten | News-Archiv | Windows-ZIP |
| `caine.py` | neueste Version | echte Daten | Release-Texte | ISO + SHA256 |
| `partedmagic.py` | neueste Version | Schema-Daten | News-Archiv | – |
| `mikrotik_newsletter.py` | Newsletter-Nr. | Monat/Jahr | – | alle PDFs |
| `mikrotik_routeros.py` | Kanal-Versionen | Kanal-Status | alle Kanäle | – |
| `ubuntu_mate.py` | Interim + LTS | ISO-Daten | Release Notes | – |
| `parrot.py` | Security-Edition | Blog-Daten | Release Notes | ISO + Hashes |
| `kali.py` | neueste Version | Blog-Daten | Release Notes | ISO + Torrent + Hashes |
| `proxmox.py` | PVE (amd64) | ISO-Daten | Roadmap-Wiki | ISO + sha256 + asc |
| `memtest86.py` | neueste Version | GitHub-Daten | GitHub-Releases | 3 ISOs (entzippt) + sha256 |
| `notepadpp.py` | neueste Version | GitHub-Daten | Versionsseiten | x64-Installer |
| `blossomos.py` | Online-Edition | Datum = Version | – | ISO + Hash-JSON |
| `python_org.py` | neueste Version | – | – | – |
| `jellyfin_server.py` | neueste Version | GitHub-Daten | GitHub-Releases | Windows-x64-Installer |
| `jellyfin_desktop.py` | neueste Version | GitHub-Daten | GitHub-Releases | Windows-x64-.exe |
| `php.py` | 4 Zweige kombiniert (8.5/8.4/8.3/8.2) | echte Daten | ChangeLog-8.php | – |
| `gitlab.py` | 3 Zweige kombiniert (Top-3 Minors) | Tag-Daten | Release-Notes-Feed | – |
| `hp_docks.py` | 2 Docks kombiniert (G5 + G6) | echte Daten | Treiberseiten-API | Firmware-.exe |
| `twitch_drops.py` | Drops-Kampagnen (konfigurierbare Links) | Kampagnen-Start | Zeitraum + Status | – |

## Überwachungsmethoden

| Methode | Bedeutung |
|---------|-----------|
| `extract()` | Eigene Python-Funktion im Modul – volle Kontrolle, Vorrang vor allem. |
| `regex` | Sucht `PATTERN` im Seitentext; Gruppe 1 `(...)` ist die Version. Unempfindlich gegen Werbung/Zeitstempel. |
| `hash` | SHA-256 über den kompletten Seiteninhalt. Meldet **jede** Änderung. |
| `etag` | Vergleicht `ETag`/`Last-Modified`-Header (nur wenn der Server sie sendet). |

## Versionshistorie (`history/`)

Pro Seite eine Markdown-Datei `history/<slug>.md`:

| Version | Veröffentlicht | Erkannt am | Anmerkung |
|---------|----------------|------------|-----------|
| 1.1.17 | 2026-07-24 | 21.09.2026 | Baseline |
| 1.1.18 | 2026-10-01 | 03.10.2026 | vorher: 1.1.17 |

- **Veröffentlicht:** echtes Upstream-Datum, wenn das Modul
  `extract_history()` liefert (z. B. Ventoy), sonst `–`.
- **Erkannt am:** wann NewsBot die Version zuerst gesehen hat.
- Der erste Check setzt nur die Baseline (keine Mail) und legt die
  Historie an; danach wird jede Änderung oben eingefügt – auch wenn der
  Mailversand gerade fehlschlägt.

## Changelog-Archiv und Downloads

Module können zwei weitere optionale Hooks nutzen (Beispiel: Ventoy):

- **Changelog-Archiv** (`CHANGELOG_URL` + `extract_changelog()`):
  NewsBot wandelt die News-Seite in Markdown um und legt sie unter
  `archive/<slug>_changelog.md` ab – aktualisiert automatisch, sobald
  sich der Inhalt ändert. Du hast so immer den kompletten Changelog
  lokal, ohne die Webseite aufzurufen.
- **Release-Downloads** (`DOWNLOADS`): URL-Templates mit `{version}`
  werden nach `downloads/<slug>/` geladen. Vorhandene Dateien werden
  übersprungen, fehlende bei jedem Lauf nachgeladen – die aktuelle
  Version liegt so immer griffbereit auf der Platte. Einträge mit
  `"unzip": True` werden nach dem Laden entpackt (z. B. Memtest-ISOs):
  gespeichert wird der Inhalt unter dem Zip-Namen ohne `.zip`, die
  Zip wird verworfen und nicht erneut geladen. Nach jedem Download
  wird die Datei gegen publizierte Hashes geprüft (sha256sum.txt,
  SHA256SUMS, signed-hashes.txt, *.sha256, *.isodata.json – md5 bis
  sha512); bei einem Mismatch wird sie verworfen und nächsten Lauf
  erneut geladen.

Beides läuft nach jedem Check automatisch mit (nicht im `--dry-run`).

## MikroTik

Zwei Module:

- **MikroTik Newsletter** (`sites/mikrotik_newsletter.py`): erkennt die
  neueste Newsletter-Nummer auf mikrotik.com und archiviert **alle**
  PDFs ab #77 (ältere existieren nicht als Kurzlink) unter
  `downloads/mikrotik-newsletter/news_<nr>.pdf`. Nummern, die nicht
  auflösbar sind, bekommen eine `.missing`-Markierung und werden nicht
  erneut versucht. Download-Fehler (Timeout o. ä.) dagegen schon –
  die Datei fehlt dann einfach und wird beim nächsten Lauf nachgeholt.
  Da neue Newsletter auf `mt.lv` mitunter schon existieren, bevor sie
  auf der Homepage verlinkt sind, wird ab der höchsten verlinkten
  Nummer vorgeprobt (`mt.lv/news<N+1>`, `N+2`, … bis zum ersten 404) –
  so wird auch ein noch unverlinkter Newsletter erkannt und geladen.
- **MikroTik RouterOS** (`sites/mikrotik_routeros.py`): prüft die
  Versionsliste der Release-Kanäle, benachrichtigt bei neuen Versionen
  und archiviert die offiziellen Changelog-Texte unter
  `archive/mikrotik-routeros_changelog.md`. **Es werden keine
  RouterOS-Dateien heruntergeladen.**

  Kanal-Auswahl in `config.json` (Default: nur `stable`):

  ```json
  "site_options": {
    "mikrotik_routeros": {
      "channels": ["stable", "long-term", "development"],
      "archive_channels": ["stable", "long-term", "testing", "development"]
    }
  }
  ```

  - `channels`: bei welchen Kanälen eine neue Version eine Mail auslöst
    (`stable`, `long-term`, `testing`, `development`). Mehrere Kanäle
    ergeben einen kombinierten Statuswert `stable=7.24.4;long-term=7.23.7`.
  - `archive_channels`: welche Kanäle im Changelog-Archiv landen
    (`null` = wie `channels`).

  Wer nur im Modul arbeiten will: `CHANNELS`/`ARCHIVE_CHANNELS` oben in
  `sites/mikrotik_routeros.py` sind die Defaults, `site_options` hat Vorrang.

## Web-Dashboard

Der Bot bringt ein lokales Web-Dashboard mit (reine
Standardbibliothek). Im Dauerbetrieb (`python newsbot.py`) startet
es automatisch, sonst separat:

```
python newsbot.py --web          # nur Dashboard, keine Checks
```

Dann **http://127.0.0.1:8321/** im Browser öffnen:

- **Übersicht:** alle Seiten mit aktuellem Stand, letztem Check und
  letzter Änderung; ausstehende Mails werden markiert
- **Jetzt prüfen:** globaler Button für alle Seiten, plus ein
  "Prüfen"-Button pro Zeile für Einzel-Checks (auch im
  Daemon-Betrieb – der Timer wird aufgeweckt, der 12h-Rhythmus
  bleibt unverändert)
- **Historie / Changelog:** die `history/`- und `archive/`-Dateien
  direkt lesbar
- **Downloads:** alle geladenen Releases als Liste, Dateien per
  Klick herunterladbar (Resume-fähig, auch für die großen ISOs)
- **Log:** die letzten 200 Zeilen von `newsbot.log`

Konfiguration in `config.json`:

```json
"web": { "enabled": true, "host": "127.0.0.1", "port": 8321 }
```

**Achtung:** Es gibt keine Authentifizierung – `host` nur ändern,
wenn der Rechner in einem vertrauten Netz hängt (die Downloads sind
dann für andere im Netz erreichbar).

## Autostart (Windows)

Damit der Bot bei jedem Rechnerstart mitläuft:

```
powershell -ExecutionPolicy Bypass -File install_autostart.ps1
```

Legt `NewsBot.lnk` im Autostart-Ordner an → `pythonw.exe` startet
den Bot unsichtbar im Hintergrund (Daemon + Dashboard). Entfernen
mit `remove_autostart.ps1` oder die Verknüpfung in `shell:startup`
löschen. Task-Scheduler/sktasks wären eleganter, brauchen auf
dieser Maschine aber Admin-Rechte – die Verknüpfung nicht.

**Debian/Linux (systemd-User-Service):**

```
bash install_autostart.sh
```

Legt `~/.config/systemd/user/newsbot.service` an und startet es.
Entfernen mit `bash remove_autostart.sh`. Damit der Dienst auch
**ohne** aktive Session läuft (echter Serverbetrieb):
`loginctl enable-linger $USER`

## Regelmäßiger Betrieb

Alternativ zum Dauerbetrieb: zeitgesteuerte Einzel-Checks.

**Windows (Aufgabenplanung):** Aufgabe anlegen, z. B. stündlich:

```
Programm:   C:\Program Files\Python314\python.exe
Argumente:  newsbot.py --once
Starten in: C:\Users\HP-Pavilion\Desktop\2026-09-21 - News Bot
```

**Linux/macOS (cron):**

```
0 * * * *  cd /pfad/zum/newsbot && python3 newsbot.py --once
```

## Tests

```bash
python -m unittest discover -s tests        # alle Tests
python -m unittest discover -s tests -v     # ausführlich
python -m unittest tests.test_newsbot       # nur eine Datei
```

Die Tests unter `tests/` nutzen nur die Standardbibliothek
(`unittest`, `unittest.mock`) und laufen komplett offline –
Netzwerkzugriffe werden gemockt. Abgedeckt sind die Kernlogik
(`test_newsbot.py`), der Modul-Vertrag aller `sites/`-Module plus
Parser-Fixtures (`test_sites.py`) und das Web-Dashboard inkl.
echtem HTTP-Server auf Ephemeral-Port (`test_webui.py`).
Bei jedem Push laufen sie zusätzlich per GitHub Actions
(`.github/workflows/tests.yml`, Ubuntu + Windows).

## Dateien

| Pfad | Zweck |
|------|-------|
| `newsbot.py` | Das Programm |
| `webui.py` | Web-Dashboard (http://127.0.0.1:8321) |
| `sites/*.py` | Seiten-Module (eine Datei pro überwachter Seite) |
| `tests/` | Unit-Tests (`python -m unittest discover -s tests`) |
| `history/*.md` | Versionshistorie pro Seite (automatisch) |
| `archive/*.md` | Changelog-Archive (bei Modulen mit `CHANGELOG_URL`) |
| `downloads/<slug>/` | Geladene Releases (bei Modulen mit `DOWNLOADS`) |
| `config.json` | Deine Konfiguration (nicht committen!) |
| `state.json` | Zuletzt gesehene Werte (automatisch) |
| `.env` | SMTP-Passwort (nicht committen!) |
| `newsbot.log` | Logdatei, rotiert automatisch |
| `AGENTS.md` | Projekt-Regeln, Version und Changelog |

## Hinweise zu E-Mail-Anbietern

- **Gmail:** normales Passwort funktioniert nicht – ein
  [App-Passwort](https://myaccount.google.com/apppasswords) erstellen
  (2FA nötig). `smtp.gmail.com`, Port 465, `use_ssl: true`.
- **GMX/Web.de/Outlook:** SMTP-Zugang ggf. erst in den Account-Einstellungen
  aktivieren; die dort genannten Server/Ports verwenden.
