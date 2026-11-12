#!/usr/bin/env bash
set -e
echo "=========================================================="
echo "  ISPR News Monitoring System - Mac/Linux Launcher"
echo "=========================================================="
if command -v python3 >/dev/null 2>&1; then
    if [ ! -d ".venv" ]; then
        python3 -m venv .venv
    fi
    source .venv/bin/activate
    pip install -q -r requirements.txt
    (sleep 2 && (open "http://127.0.0.1:5000" 2>/dev/null || xdg-open "http://127.0.0.1:5000" 2>/dev/null || true)) &
    python3 app.py
else
    echo "Python3 not found. Opening index.html directly in browser..."
    open "index.html" 2>/dev/null || xdg-open "index.html" 2>/dev/null
fi