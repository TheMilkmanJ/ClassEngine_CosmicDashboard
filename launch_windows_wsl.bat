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
echo   LT_SUBDOMAIN   = TheMilkmanJ
echo   DASHBOARD_USER = TheMilkmanJ
echo   DASHBOARD_PASS = (set)
echo.
echo (Press Ctrl+C to stop)
echo.

cd /d "%~dp0"

REM Run the launcher with environment variables inside WSL
wsl bash -c "export LT_SUBDOMAIN=TheMilkmanJ && export DASHBOARD_USER=TheMilkmanJ && export DASHBOARD_PASS=Freemilk420! && cd /home/themilkmanj/prtoe_class && ./launch_cosmic.sh"

echo.
echo CosmicDashboard has stopped.
pause
