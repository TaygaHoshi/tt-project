#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Converting Obsidian → Hugo ==="
python3 "$SCRIPT_DIR/convert.py"

echo ""
echo "=== Configuring Hugo ==="

if [[ $# -gt 0 && "$1" != "--test" ]]; then
    echo "Error: unsupported argument: $1"
    exit 1
fi

if [[ "${1:-}" == "--test" ]]; then
    sed -i \
        "s|baseURL = 'https://sigil.tyghsh.cc/'|baseURL = 'https://sigil-test.tyghsh.cc/'|" \
        "$SCRIPT_DIR/hugo.toml"
fi

echo ""
echo "=== Building Hugo site ==="
cd "$SCRIPT_DIR"
hugo --minify
