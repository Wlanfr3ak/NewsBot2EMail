#!/usr/bin/env bash
# NewsBot-Autostart für Debian/Linux via systemd-User-Service.
# Einmalig ausführen:   bash install_autostart.sh
# Entfernen:          bash remove_autostart.sh
#
# Legt ~/.config/systemd/user/newsbot.service an und aktiviert es.
# Der Dienst startet bei der Anmeldung; mit
#   loginctl enable-linger "$USER"
# läuft er sogar ohne aktive Session (richtiger Dauerbetrieb).

set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="$(command -v python3)"
UNIT_DIR="$HOME/.config/systemd/user"
UNIT="$UNIT_DIR/newsbot.service"

mkdir -p "$UNIT_DIR"
cat > "$UNIT" <<EOF
[Unit]
Description=NewsBot - Versions-Ueberwachung + Web-Dashboard
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=$PY "$DIR/newsbot.py"
WorkingDirectory=$DIR
Restart=on-failure
RestartSec=60

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable --now newsbot.service

echo "newsbot.service installiert und gestartet."
echo "Status:  systemctl --user status newsbot"
echo "Logs:    journalctl --user -u newsbot -f"
echo "Tipp:    loginctl enable-linger \"$USER\"  -> laeuft auch ohne Login"
