import os
from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv("PORT", "5002"))
COINBASE_API = os.getenv("COINBASE_API")
COINGECKO_API = os.getenv("COINGECKO_API")
