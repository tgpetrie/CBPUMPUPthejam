from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/api/health')
    def health_check():
        return jsonify({"status": "healthy"}), 200

    @app.route('/api/component/gainers-table')
    def gainers_table():
        return jsonify([
            {"symbol": "BTC", "change": 2.31},
            {"symbol": "ETH", "change": 1.85},
            {"symbol": "SOL", "change": 1.28},
        ])

    @app.route('/api/component/losers-table')
    def losers_table():
        return jsonify([
            {"symbol": "ETH", "change": -1.23},
            {"symbol": "ADA", "change": -2.54},
            {"symbol": "MATIC", "change": -3.75},
        ])

    @app.route('/api/component/top-banner-scroll')
    def top_banner():
        return jsonify([
            {"symbol": "BTC", "change": 1.24},
            {"symbol": "AVAX", "change": 0.94},
            {"symbol": "XRP", "change": 0.88},
        ])

    @app.route('/api/component/bottom-banner-scroll')
    def bottom_banner():
        return jsonify([
            {"symbol": "SOL", "volume_change": 12.4},
            {"symbol": "SHIB", "volume_change": 9.2},
            {"symbol": "UNI", "volume_change": 6.1},
        ])

    return app