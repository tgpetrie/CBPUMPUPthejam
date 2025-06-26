import random
import time

# --- Configuration ---
# In a real app, you'd get this list from an API or a database.
TOKEN_LIST = [
    "BTC-USD", "ETH-USD", "SOL-USD", "XRP-USD", "DOGE-USD", "ADA-USD",
    "AVAX-USD", "SHIB-USD", "DOT-USD", "LINK-USD", "TRX-USD", "MATIC-USD",
    "LTC-USD", "BCH-USD", "NEAR-USD", "LEO-USD", "UNI-USD", "INJ-USD",
    "PYTH-USD", "SEI-USD", "GHST-USD", "LPT-USD", "MSOL-USD", "PYR-USD",
    "HOPR-USD", "MNDE-USD", "TURBO-USD", "AST-USD"
]

# --- Data Simulation ---
# In a real application, these functions would make API calls to services
# like CoinGecko or Coinbase. To demonstrate frontend functionality without
# requiring API keys, we are simulating the data structure here.

def _create_mock_token_data(token_id):
    """Generates a single, realistic-looking token data object."""
    base_price = random.uniform(0.01, 65000)
    return {
        "id": token_id,
        "price": f"{base_price:.4f}",
        "change_1h": f"{random.uniform(-5, 5):.2f}",
        "change_3m": f"{random.uniform(-2, 2):.2f}",
        "volume_24h": f"{random.uniform(1_000_000, 500_000_000):.2f}",
        "last_updated": time.time(),
        "url": f"https://www.coinbase.com/price/{token_id.split('-')[0].lower()}"
    }

def get_mock_gainers_losers():
    """
    Simulates fetching only gainers and losers data, as real 3-min data is not available.
    """
    all_tokens = [_create_mock_token_data(token) for token in TOKEN_LIST]

    # Sort by 3m change for gainers and losers tables
    sorted_by_3m = sorted(all_tokens, key=lambda x: float(x['change_3m']), reverse=True)
    gainers_data = sorted_by_3m[:8]
    losers_data = sorted_by_3m[-8:][::-1] # Reverse to show biggest loser first

    return {
        "gainers": gainers_data,
        "losers": losers_data,
    }

# Example of how to use this module:
if __name__ == '__main__':
    market_data = get_mock_gainers_losers()
    print("--- Gainers ---")
    print(market_data['gainers'])
    print("\n--- Losers ---")
    print(market_data['losers'])