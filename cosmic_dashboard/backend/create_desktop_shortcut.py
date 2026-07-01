import os
import sys
import shutil
import subprocess
from pathlib import Path

# Paths
project_dir = Path(__file__).resolve().parent.parent.parent
assets_dir = project_dir / "dashboard" / "assets"
assets_dir.mkdir(parents=True, exist_ok=True)

dest_ico = assets_dir / "galaxy_icon.ico"
dest_png = assets_dir / "galaxy_icon.png"

def to_windows_path(linux_path: Path) -> str:
    parts = list(linux_path.parts)
    if len(parts) > 2 and parts[1] == 'mnt' and parts[2] == 'c':
        return "C:\\" + "\\".join(parts[3:])
    return str(linux_path)

# 1. Create Windows Desktop Shortcut (.url file)
# Dynamically query Windows for the active Desktop path (handles OneDrive and custom paths)
windows_desktop = None
try:
    desktop_res = subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command", "[Environment]::GetFolderPath('Desktop')"],
        capture_output=True,
        text=True,
        timeout=10,
    )
    if desktop_res.returncode == 0 and desktop_res.stdout.strip():
        try:
            wsl_res = subprocess.run(
                ["wslpath", "-u", desktop_res.stdout.strip()],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if wsl_res.returncode == 0:
                windows_desktop = Path(wsl_res.stdout.strip())
        except (FileNotFoundError, subprocess.TimeoutExpired):
            # wslpath not available or timed out; leave windows_desktop as None
            windows_desktop = None
except (FileNotFoundError, subprocess.TimeoutExpired):
    # PowerShell not available (not on Windows) or timed out; fall back to scanning /mnt/c/Users
    windows_desktop = None

# Fallback: Scan /mnt/c/Users for valid Desktop directories if PowerShell query failed
if not windows_desktop or not windows_desktop.exists():
    users_dir = Path("/mnt/c/Users")
    if users_dir.exists():
        for user_folder in users_dir.iterdir():
            if user_folder.is_dir() and user_folder.name not in ("All Users", "Default", "Default User", "Public"):
                # Try OneDrive Desktop first
                onedrive_desktop = user_folder / "OneDrive" / "Desktop"
                if onedrive_desktop.exists():
                    windows_desktop = onedrive_desktop
                    break
                # Try standard Desktop
                std_desktop = user_folder / "Desktop"
                if std_desktop.exists():
                    windows_desktop = std_desktop
                    break

if windows_desktop and windows_desktop.exists():
    shortcut_path = windows_desktop / "CosmicDashboard.url"
    
    # Store the icon in a local Windows directory to avoid WSL UNC path loading issues
    windows_app_dir = windows_desktop / "CosmicDashboardAssets"
    try:
        windows_app_dir.mkdir(parents=True, exist_ok=True)
        local_win_ico = windows_app_dir / "galaxy_icon_v3.ico"
        shutil.copy(dest_ico, local_win_ico)
        print(f"Copied icon to Windows directory: {local_win_ico}")
        
        # Windows-style local path for the shortcut IconFile field
        windows_icon_path = to_windows_path(local_win_ico)
        
        url_content = f"""[InternetShortcut]
URL=http://localhost:8000/
IconIndex=0
IconFile={windows_icon_path}
"""
        with open(shortcut_path, 'w') as f:
            f.write(url_content)
        print(f"Windows Desktop shortcut created at: {shortcut_path}")
    except Exception as e:
        print(f"Failed to copy icon or create Windows shortcut: {e}")
else:
    print("Windows Desktop path not found. Skipping Windows shortcut creation.")

# 2. Create Linux Desktop Shortcut (.desktop file)
linux_desktop = Path.home() / "Desktop"
if linux_desktop.exists():
    desktop_file = linux_desktop / "cosmic-dashboard.desktop"
    desktop_content = f"""[Desktop Entry]
Version=1.0
Type=Application
Name=CosmicDashboard
Comment=Launch CosmicDashboard Web UI
Exec=xdg-open http://localhost:8000/
Icon={dest_png}
Terminal=false
Categories=Science;Astronomy;Education;
"""
    try:
        with open(desktop_file, 'w') as f:
            f.write(desktop_content)
        os.chmod(desktop_file, 0o755)
        print(f"Linux Desktop shortcut created at: {desktop_file}")
    except Exception as e:
        print(f"Failed to create Linux shortcut: {e}")

print("Desktop icon deployment complete!")
