# Entfernt die NewsBot-Autostart-Verknüpfung aus dem
# Autostart-Ordner (shell:startup).
$lnk = Join-Path ([Environment]::GetFolderPath("Startup")) "NewsBot.lnk"
if (Test-Path $lnk) {
    Remove-Item $lnk
    Write-Host "Autostart-Verknuepfung entfernt: $lnk"
} else {
    Write-Host "Keine NewsBot-Verknuepfung im Autostart gefunden."
}
