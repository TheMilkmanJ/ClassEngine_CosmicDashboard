@echo off
echo ===================================================
echo        CosmicDashboard - One-Click Launcher
echo ===================================================
echo.

echo Checking for Docker...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Docker is not installed or not running.
    echo Please install Docker Desktop from https://www.docker.com/products/docker-desktop/
    pause
    exit /b
)

echo Building Docker container (this may take a few minutes the first time)...
docker build -t cosmic-dashboard .

echo Opening Dashboard in your browser...
start dashboard\index.html

echo Starting backend server (Press Ctrl+C or close this window to stop)...
docker stop cosmic-backend >nul 2>&1
docker rm cosmic-backend >nul 2>&1
docker run --rm --name cosmic-backend -p 8000:8000 -v "%cd%\chains:/app/chains" cosmic-dashboard