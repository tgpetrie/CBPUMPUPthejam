#!/usr/bin/env bash
PORT=${PORT:-5002}
if lsof -i:$PORT >/dev/null; then
  PORT=$((PORT+1))
fi
export PORT
echo "Starting on port $PORT"
python app.py
