#!/usr/bin/env bash
# Smart startup: picks first free port ≥ 5002 and configures frontend

# --- Clean Up ---
echo "🧹 Clearing cache..."
rm -rf .pytest_cache/
# ---

DEFAULT_PORT=5002
FRONTEND_ENV_FILE="../frontend/.env"

function find_free_port() {
  port=$1
  while lsof -i :"$port" &>/dev/null; do
    port=$((port+1))
  done
  echo $port
}

PORT=$(find_free_port $DEFAULT_PORT)
export PORT

# Write the port to the frontend .env file to sync proxy target
echo "VITE_API_PORT=$PORT" > "$FRONTEND_ENV_FILE"
echo "✅ Wrote backend port $PORT to $FRONTEND_ENV_FILE"

echo "🔌 Starting Flask backend on port $PORT"
exec python3 app.py
