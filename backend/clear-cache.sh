#!/usr/bin/env bash
# Removes temporary Python cache files.

echo "🧹 Clearing Python and Pytest cache..."
find . -type d -name "__pycache__" -exec rm -r {} +
rm -rf .pytest_cache/
echo "✅ Cache cleared."
