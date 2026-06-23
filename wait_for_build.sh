#!/bin/bash
echo "Waiting for CLASS build to complete..."
while pgrep -f "make|gcc|g\+\+" > /dev/null 2>&1; do
    sleep 2
done
echo "Build complete!"
if [ -f "python/classy.cpython"*.so ] || [ -f "python/classy.so" ]; then
    echo "✓ Python wrapper built successfully"
    ls -lh python/classy*.so
else
    echo "✗ Python wrapper not found"
fi

