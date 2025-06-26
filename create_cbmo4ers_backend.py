#!/usr/bin/env python3
import os
import textwrap

# Define all files & their content
FILES = {
    "backend": {
        "app.py": textwrap.dedent("""
import os
import time
from flask import Flask, jsonify
from flask_cors import CORS
from cache_utils import ttl_cache

def create_app():
    """
    Application factory for Flask app.
    """
    app = Flask(__name__)
    CORS(app)  # Enable CORS
    app.start_time = time.time()

    @app.route('/api/health')
    def health_check():
        return jsonify({
            "status": "healthy",
            "port": app.config.get('PORT', 'unknown')
        }), 200

    @app.route('/api/data')
    @ttl_cache(ttl_seconds=30)
    def get_data():
        # TODO: Replace with live Coinbase/CoinGecko fetch logic
        return jsonify({
            "banner": [],
            "volume": [],
            "gainers": [],
            "losers": []
        }), 200

    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app = create_app()
    app.config['PORT'] = port
    app.run(host='0.0.0.0', port=port)
"""),

        "cache_utils.py": textwrap.dedent("""
import time
import functools

def ttl_cache(ttl_seconds):
    """
    Simple in-memory TTL cache decorator.
    """
    def decorator(fn):
        cache = {}
        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in cache:
                result, expires = cache[key]
                if now < expires:
                    return result
            result = fn(*args, **kwargs)
            cache[key] = (result, now + ttl_seconds)
            return result
        return wrapped
    return decorator
"""),

        "config.py": textwrap.dedent("""
# External API endpoints
COINBASE_API = "https://api.exchange.coinbase.com"
COINGECKO_API = "https://api.coingecko.com/api/v3"
"""),

        "requirements.txt": textwrap.dedent("""
flask==3.1.1
flask-cors==6.0.1
requests==2.31.0
python-dotenv==1.0.1
psutil==6.1.1
flask-limiter==3.8.0
flask-talisman==1.1.0
pytest==8.3.5
gunicorn==21.2.0
sentry-sdk[flask]==2.21.0
"""),

        "Dockerfile": textwrap.dedent("""
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5002
EXPOSE 5002

CMD ["gunicorn", "-b", "0.0.0.0:5002", "app:create_app()"]
"""),

        "start_backend.sh": textwrap.dedent("""
#!/usr/bin/env bash
# Smart backend launcher with port fallback

for p in 5002 5003 5004; do
  if ! lsof -i:$p > /dev/null; then
    export PORT=$p
    echo "🖥️ Starting backend on port $p"
    python app.py
    exit 0
  fi
done

echo "❌ All fallback ports in use. Pick a free port!"
exit 1
"""),

        "test_app.py": textwrap.dedent("""
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_health(client):
    rv = client.get('/api/health')
    data = rv.get_json()
    assert rv.status_code == 200
    assert data['status'] == 'healthy'

def test_data(client):
    rv = client.get('/api/data')
    data = rv.get_json()
    assert rv.status_code == 200
    assert all(key in data for key in ('banner','volume','gainers','losers'))
"""),

        "utils.py": textwrap.dedent("""
# Any shared helper functions can go here
def format_decimal(val, places=2):
    try:
        return f"{float(val):.{places}f}"
    except:
        return '0.00'
"""),
    }
}

def mkdir_p(path):
    os.makedirs(path, exist_ok=True)

def write_tree(base, tree):
    for name, content in tree.items():
        full = os.path.join(base, name)
        if isinstance(content, dict):
            mkdir_p(full)
            write_tree(full, content)
        else:
            with open(full, 'w') as f:
                f.write(content)
            # make scripts executable
            if full.endswith('.sh'):
                os.chmod(full, 0o755)

if __name__ == '__main__':
    write_tree(os.getcwd(), FILES)
    print("✅ backend/ scaffolded successfully.")