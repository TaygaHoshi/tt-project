#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Converting Obsidian → Hugo ==="
python3 "$SCRIPT_DIR/convert.py"

echo ""
echo "=== Building Hugo site ==="
cd "$SCRIPT_DIR"
hugo --minify