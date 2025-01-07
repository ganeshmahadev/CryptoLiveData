import requests
import logging
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from environment variables
API_KEY = os.getenv("COINMARKETCAP_API_KEY")

# Configure logger
logging.basicConfig(
    filename="data/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def fetch_crypto_data():
    """
    Fetches live cryptocurrency data for the top 50 cryptocurrencies from the CoinMarketCap API.
    """
    try:
        logging.info("Fetching live cryptocurrency data...")
        url = "https://api.coingecko.com/api/v3/coins/markets"
        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": API_KEY
        }
        params = {
            "start": "1",                # Starting rank
            "limit": "50",               # Top 50 cryptocurrencies
            "convert": "USD",            # Convert market data to USD
            "sort": "market_cap"         # Sort by market cap
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()["data"]

        # Extract relevant fields
        crypto_data = []
        for coin in data:
            crypto_data.append((
                coin["name"],                         # Cryptocurrency name
                coin["symbol"],                       # Symbol
                coin["quote"]["USD"]["price"],        # Current price
                coin["quote"]["USD"]["market_cap"],   # Market capitalization
                coin["quote"]["USD"]["volume_24h"],   # 24-hour trading volume
                coin["quote"]["USD"]["percent_change_24h"]  # 24-hour % change
            ))
        logging.info("Successfully fetched cryptocurrency data.")
        return crypto_data
    except Exception as e:
        logging.error(f"Error while fetching cryptocurrency data: {e}")
        return []
