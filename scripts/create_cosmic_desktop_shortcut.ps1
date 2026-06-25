param(
    [string]$BatchPath = "C:\Users\themi\projects\prtoe_class\prtoe_class\launch_windows_wsl.bat",
    [string]$IconPath = "C:\Users\themi\CosmicDashboardAssets\galaxy_icon_v3.ico",
    [string]$DesktopPath = ""
)

if (-not $DesktopPath) {
    $DesktopPath = [Environment]::GetFolderPath('Desktop')
}

$shortcutFile = Join-Path $DesktopPath "CosmicDashboard.lnk"

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutFile)
$Shortcut.TargetPath = "$env:SystemRoot\System32\cmd.exe"
$Shortcut.Arguments = "/k `"$BatchPath`""
$Shortcut.WorkingDirectory = "C:\Users\themi"
$Shortcut.WindowStyle = 1
$Shortcut.Description = "Launch CosmicDashboard (opens WSL terminal with backend + tunnel)"
if (Test-Path $IconPath) {
    $Shortcut.IconLocation = $IconPath
}
$Shortcut.Save()

Write-Host "Desktop shortcut created at: $shortcutFile"
