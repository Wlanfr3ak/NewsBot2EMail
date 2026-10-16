#!/usr/bin/env bash
# Entfernt den NewsBot systemd-User-Service.
set -e
systemctl --user disable --now newsbot.service 2>/dev/null || true
rm -f "$HOME/.config/systemd/user/newsbot.service"
systemctl --user daemon-reload
echo "newsbot.service entfernt."
