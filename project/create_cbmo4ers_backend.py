#!/usr/bin/env python3
import os
import textwrap

# Where to put the new backend folder
BASE_DIR = os.path.join(os.getcwd(), "backend")

# Files and their contents
STRUCTURE = {
    "backend": {
        "requirements.txt": textwrap.dedent("""\
            # Core Flask dependencies
            flask==3.1.1
            flask-cors==6.0.1
            flask-socketio==5.3.6

            # HTTP requests and data handling
            requests==2.31.0

            # Environment management
            python-dotenv==1.0.1

            # Caching & performance
            psutil==6.1.1

            # Rate limiting & security
            flask-limiter==3.8.0
            flask-talisman==1.1.0

            # Testing
            pytest==8.3.5

            # Production server
            gunicorn==21.2.0

            # Monitoring & logging
            sentry-sdk[flask]==2.21.0
            """),

        ".env.example": textwrap.dedent("""\
            # Port fallback (default 5002)
            PORT=5002

            # Public APIs
            COINBASE_API=https://api.exchange.coinbase.com
            COINGECKO_API=https://api.coingecko.com/api/v3
            """),

        "config.py": textwrap.dedent("""\
            import os
            from dotenv import load_dotenv

            load_dotenv()
            PORT = int(os.getenv("PORT", "5002"))
            COINBASE_API = os.getenv("COINBASE_API")
            COINGECKO_API = os.getenv("COINGECKO_API")
            """),

        "cache_utils.py": textwrap.dedent("""\
            import time
            import functools

            def ttl_cache(ttl_seconds):
                \"""
                Simple in-memory TTL cache decorator.
                \"""
                def decorator(fn):
                    cache = {}
                    @functools.wraps(fn)
                    def wrapped(*args, **kwargs):
                        key = (args, tuple(sorted(kwargs.items())))
                        now = time.time()
                        if key in cache:
                            result, expires_at = cache[key]
                            if now < expires_at:
                                return result
                        result = fn(*args, **kwargs)
                        cache[key] = (result, now + ttl_seconds)
                        return result
                    return wrapped
                return decorator
            """),

        "utils.py": textwrap.dedent("""\
            from cache_utils import ttl_cache
            from config import COINBASE_API, COINGECKO_API
            import requests

            @ttl_cache(30)
            def fetch_banner_data():
                # TODO: implement real fetch
                return []

            @ttl_cache(30)
            def fetch_volume_data():
                # TODO: implement real fetch
                return []

            @ttl_cache(30)
            def fetch_3min_data():
                # TODO: implement real fetch
                return [], []
            """),

        "app.py": textwrap.dedent("""\
            from flask import Flask, jsonify
            from flask_cors import CORS
            from config import PORT
            from utils import fetch_banner_data, fetch_volume_data, fetch_3min_data

            app = Flask(__name__)
            CORS(app)

            @app.route('/api/health')
            def health():
                return jsonify({'port': PORT, 'status': 'healthy'}), 200

            @app.route('/api/data')
            def data():
                banner = fetch_banner_data()
                volume = fetch_volume_data()
                gainers, losers = fetch_3min_data()
                return jsonify({
                    'banner': banner,
                    'volume': volume,
                    'gainers': gainers,
                    'losers': losers
                }), 200

            if __name__ == '__main__':
                app.run(host='0.0.0.0', port=PORT)
            """),

        "test_app.py": textwrap.dedent("""\
            import pytest
            from app import app

            @pytest.fixture
            def client():
                with app.test_client() as c:
                    yield c

            def test_health(client):
                resp = client.get('/api/health')
                assert resp.status_code == 200
                data = resp.get_json()
                assert data['status'] == 'healthy'

            def test_data(client):
                resp = client.get('/api/data')
                assert resp.status_code == 200
                json = resp.get_json()
                assert 'banner' in json and 'volume' in json
            """),

        "Dockerfile": textwrap.dedent("""\
            FROM python:3.11-slim
            WORKDIR /app
            COPY requirements.txt .
            RUN pip install --no-cache-dir -r requirements.txt
            COPY . .
            EXPOSE ${PORT}
            CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:${PORT}", "--workers", "2"]
            """),

        "start_backend.sh": textwrap.dedent("""\
            #!/usr/bin/env bash
            PORT=${PORT:-5002}
            if lsof -i:$PORT >/dev/null; then
              PORT=$((PORT+1))
            fi
            export PORT
            echo "Starting on port $PORT"
            python app.py
            """),
    }
}

def create_structure(base, struct):
    for name, content in struct.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)
            if path.endswith('.sh'):
                os.chmod(path, 0o755)

if __name__ == '__main__':
    if os.path.exists('backend'):
        print("Error: 'backend/' already exists. Remove or rename it first.")
        exit(1)
    create_structure(os.getcwd(), STRUCTURE)
    print("✅ `backend/` scaffolded successfully.")
