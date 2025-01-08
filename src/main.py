import time
from fetch_data import fetch_crypto_data
from store_data import insert_into_questdb
import logging
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

# Configure logger
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    filename="data/logs/app.log",
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(levelname)s - %(message)s",
)

if __name__ == "__main__":
    while True:
        logging.info("Starting the data fetching and insertion process...")
        
        # Fetch data
        crypto_data = fetch_crypto_data()
        
        # Insert into QuestDB
        if crypto_data:
            insert_into_questdb(crypto_data)
        
        # Wait for 5 minutes before the next update
        logging.info("Waiting for 5 minutes before the next update...")
        time.sleep(300)  # 300 seconds = 5 minutes
