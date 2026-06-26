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

# Ensure chains directory exists before running container
mkdir -p "$(pwd)/chains"

echo "Opening Dashboard in your browser..."
if command -v open &> /dev/null; then
    open dashboard/index.html
elif command -v xdg-open &> /dev/null; then
    xdg-open dashboard/index.html
else
    echo "Please open dashboard/index.html manually in your web browser."
fi

echo "Starting backend server (Press Ctrl+C to stop)..."
# Use exact name filter to avoid matching partial container names
CONTAINER_ID=$(docker ps -aq --filter "name=^cosmic-backend$")
if [ -n "$CONTAINER_ID" ]; then
    docker stop "$CONTAINER_ID" >/dev/null 2>&1 || true
    docker rm "$CONTAINER_ID" >/dev/null 2>&1 || true
fi
docker run --rm --name cosmic-backend -p 8000:8000 -v "$(pwd)/chains:/app/chains" cosmic-dashboard