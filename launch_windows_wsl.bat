@echo off
echo ===================================================
echo        CosmicDashboard - WSL Launcher
echo ===================================================
echo.

echo Checking WSL installation...
wsl --list --quiet >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: WSL is not installed or not configured.
    echo Please install WSL from Microsoft Store or run: wsl --install
    pause
    exit /b
)

echo.
echo Starting CosmicDashboard with launch_cosmic.sh ...
echo.
echo (Press Ctrl+C to stop)
echo.

cd /d "%~dp0"

REM Dynamically resolve WSL path of the current directory to make it portable
for /f "delims=" %%i in ('wsl wslpath -u "%cd%"') do set "WSL_DIR=%%i"

REM Prompt for credentials
set "LT_SUBDOMAIN="
set /p LT_SUBDOMAIN="Enter LT_SUBDOMAIN (optional, press Enter for random): "

set "DASHBOARD_USER=admin"
set /p DASHBOARD_USER="Enter DASHBOARD_USER [admin]: "

set "DASHBOARD_PASS="
set /p DASHBOARD_PASS="Enter DASHBOARD_PASS (optional, press Enter for random): "

REM Run the launcher with environment variables inside WSL
wsl bash -c "export LT_SUBDOMAIN='%LT_SUBDOMAIN%' && export DASHBOARD_USER='%DASHBOARD_USER%' && export DASHBOARD_PASS='%DASHBOARD_PASS%' && cd '%WSL_DIR%' && chmod +x launch_cosmic.sh && ./launch_cosmic.sh"

echo.
echo CosmicDashboard has stopped.
pause
