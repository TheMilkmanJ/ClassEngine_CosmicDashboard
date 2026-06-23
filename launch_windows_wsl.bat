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
echo Starting backend server using WSL Python...
echo (Press Ctrl+C to stop)
echo.

REM Change to the WSL path and run the backend
wsl bash -c "cd /home/themilkmanj/prtoe_class && python3 -m uvicorn scripts.cosmo_dashboard_backend:app --host 0.0.0.0 --port 8000 --reload"

pause

@REM Made with Bob
