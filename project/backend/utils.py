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
