#!/bin/bash
echo "==================================================="
echo "       CosmicDashboard - One-Click Launcher"
echo "==================================================="
echo ""

# Check for Docker
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker is not installed or not running."
    echo "Please install Docker from https://docs.docker.com/get-docker/"
    exit 1
fi

echo "Building Docker container (this may take a few minutes the first time)..."
docker build -t cosmic-dashboard .

echo "Opening Dashboard in your browser..."
if command -v open &> /dev/null; then
    open dashboard/index.html
elif command -v xdg-open &> /dev/null; then
    xdg-open dashboard/index.html
else
    echo "Please open dashboard/index.html manually in your web browser."
fi

echo "Starting backend server (Press Ctrl+C to stop)..."
docker stop cosmic-backend >/dev/null 2>&1 || true
docker rm cosmic-backend >/dev/null 2>&1 || true
docker run --rm --name cosmic-backend -p 8000:8000 -v "$(pwd)/chains:/app/chains" cosmic-dashboard