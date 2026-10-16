# NewsBot bei der Anmeldung automatisch starten (Autostart-Ordner).
# Einmalig ausführen:  powershell -ExecutionPolicy Bypass -File install_autostart.ps1
# Entfernen:           .\remove_autostart.ps1
#
# Legt NewsBot.lnk in shell:startup -> pythonw.exe newsbot.py.
# pythonw startet ohne Konsolenfenster; der Bot läuft im
# Hintergrund inkl. Web-Dashboard (http://127.0.0.1:8321).
# Keine Admin-Rechte nötig (im Gegensatz zu schtasks/
# Register-ScheduledTask, die auf dieser Maschine gesperrt sind).

$dir = $PSScriptRoot
$pythonw = (Get-Command pythonw.exe -ErrorAction Stop).Source
$startup = [Environment]::GetFolderPath("Startup")
$lnkPath = Join-Path $startup "NewsBot.lnk"

$wsh = New-Object -ComObject WScript.Shell
$lnk = $wsh.CreateShortcut($lnkPath)
$lnk.TargetPath = $pythonw
$lnk.Arguments = "`"$dir\newsbot.py`""
$lnk.WorkingDirectory = $dir
$lnk.Description = "NewsBot: Versions-Ueberwachung + Web-Dashboard"
$lnk.Save()

Write-Host "Autostart-Verknuepfung erstellt: $lnkPath"
Write-Host "Beim naechsten Login startet NewsBot automatisch."
Write-Host "Entfernen: .\remove_autostart.ps1"
