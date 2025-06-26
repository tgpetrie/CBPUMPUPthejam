import os
import time
import logging
from flask import Flask, jsonify
from flask_cors import CORS
from cache_utils import ttl_cache
from crypto_api import fetch_top_movers_1h, fetch_top_by_volume_24h
from data_fetcher import get_mock_gainers_losers

def safe_format_float(value, precision):
    """Safely formats a value to a float with given precision, defaulting to 0.0 on error."""
    try:
        return f"{float(value):.{precision}f}"
    except (ValueError, TypeError):
        return f"{0.0:.{precision}f}"

def create_app():
    """
    Application factory for Flask app.
    """
    app = Flask(__name__)
    CORS(app)  # Enable CORS
    app.start_time = time.time()
    logging.basicConfig(level=logging.INFO)

    @app.route('/api/health')
    def health_check():
        """
        Health check endpoint to confirm the server is running.
        """
        return jsonify({"status": "ok"}), 200

    @app.route('/api/data')
    @ttl_cache(ttl_seconds=30) # Cache the result for 30 seconds
    def get_data():
        """
        Aggregated market data endpoint.
        Serves real data for banners and mock data for gainers/losers.
        """
        try:
            # Fetch real data for banners
            banner_data_raw = fetch_top_movers_1h(limit=10)
            volume_data_raw = fetch_top_by_volume_24h(limit=10)

            # Fetch mock data for tables where live data is unavailable
            gainer_loser_data = get_mock_gainers_losers()

            def format_url(symbol):
                base = symbol.split('-')[0].lower()
                return f"https://www.coinbase.com/price/{base}"

            banner_data = [
                {
                    "id": c["symbol"],
                    "price": safe_format_float(c.get("current_price"), 4),
                    "change_1h": safe_format_float(c.get("price_change_1h"), 2),
                    "url": format_url(c["symbol"]),
                }
                for c in banner_data_raw
            ]

            volume_data = [
                {
                    "id": c["symbol"],
                    "price": safe_format_float(c.get("current_price"), 4),
                    "volume_24h": c.get("volume_24h", 0),
                    "url": format_url(c["symbol"]),
                }
                for c in volume_data_raw
            ]

            market_data = {
                "banner": banner_data,
                "volume": volume_data,
                **gainer_loser_data,
            }
            return jsonify(market_data)
        except Exception as e:
            app.logger.error(f"Error fetching market data: {e}", exc_info=True)
            # Return a generic error to the client
            return jsonify({"error": "Failed to fetch market data from external APIs."}), 500

    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app = create_app()
    app.run(host='0.0.0.0', port=port)
