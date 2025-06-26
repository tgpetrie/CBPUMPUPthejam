import requests
import os
from cache_utils import ttl_cache

COINBASE = os.getenv("COINBASE_API", "https://api.exchange.coinbase.com")
COINGECKO = os.getenv("COINGECKO_API", "https://api.coingecko.com/api/v3")

@ttl_cache(30)
def fetch_top_movers_1h(limit=10):
    """
    Fetch top coins by market cap, then find top `limit` by 1h absolute % price change.
    """
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100, # Fetch a larger pool to sort from
        "page": 1,
        "price_change_percentage": "1h"
    }
    resp = requests.get(f"{COINGECKO}/coins/markets", params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    # Sort by absolute value of 1h price change
    sorted_data = sorted(data, key=lambda c: abs(c.get("price_change_percentage_1h_in_currency", 0) or 0), reverse=True)

    return [
        {
            "symbol": c["symbol"].upper() + "-USD",
            "current_price": c["current_price"],
            "price_change_1h": c.get("price_change_percentage_1h_in_currency", 0),
        }
        for c in sorted_data[:limit]
    ]

@ttl_cache(30)
def fetch_top_by_volume_24h(limit=10):
    """
    Fetch top `limit` coins by 24h trading volume from CoinGecko.
    """
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": limit,
        "page": 1
    }
    resp = requests.get(f"{COINGECKO}/coins/markets", params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return [
        {
            "symbol": c["symbol"].upper() + "-USD",
            "current_price": c["current_price"],
            "volume_24h": c["total_volume"],
        }
        for c in data
    ]

@ttl_cache(10)
def fetch_top_3min_gainers_and_losers(limit=10):
    """
    Placeholder: 3-minute gainers/losers logic.
    CoinGecko doesn't expose 3min; 
    you can plug in your own data source or compute via websocket.
    Returns { "gainers": [...], "losers": [...] }.
    """
    # TODO: implement real 3-minute fetch
    return {"gainers": [], "losers": []}
