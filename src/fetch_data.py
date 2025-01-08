import requests
import logging
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
API_KEY = os.getenv("COINMARKETCAP_API_KEY")

# Ensure the logs directory exists
log_dir = "data/logs"
os.makedirs(log_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Configure logger
logging.basicConfig(
    filename=os.path.join(log_dir, "app.log"),  # Use the correct log file path
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def fetch_crypto_data():
    """
    Fetches live cryptocurrency data for the top 50 cryptocurrencies from the CoinMarketCap API.
    """
    try:
        logging.info("Fetching live cryptocurrency data...")

        # API Endpoint and Headers
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        headers = {"X-CMC_PRO_API_KEY": API_KEY}
        params = {"start": "1", "limit": "50", "convert": "USD"}

        # Send Request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()["data"]

        # Extract Relevant Fields
        crypto_data = []
        for coin in data:
            crypto_data.append({
                "name": coin["name"],
                "symbol": coin["symbol"],
                "price": coin["quote"]["USD"]["price"],
                "market_cap": coin["quote"]["USD"]["market_cap"],
                "volume_24h": coin["quote"]["USD"]["volume_24h"],
                "percent_change_24h": coin["quote"]["USD"]["percent_change_24h"],
                "timestamp": int(datetime.utcnow().timestamp() * 1e9)  # Nanoseconds
            })

        logging.info("Successfully fetched cryptocurrency data.")
        return crypto_data

    except Exception as e:
        logging.error(f"Error while fetching cryptocurrency data: {e}")
        return []
