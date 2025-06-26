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
