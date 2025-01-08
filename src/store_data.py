import requests
import logging
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()

# Get QuestDB configuration from environment variables
QUESTDB_HOST = os.getenv("QUESTDB_HOST", "localhost")
QUESTDB_PORT = os.getenv("QUESTDB_PORT", "9000")

# Configure logger
logging.basicConfig(
    filename="data/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def insert_into_questdb(data):
    """
    Inserts cryptocurrency data into QuestDB using the REST API.
    """
    try:
        url = f"http://{QUESTDB_HOST}:{QUESTDB_PORT}/exec"

        # Prepare SQL INSERT statement
        sql_statements = []
        for coin in data:
            sql = f"""
            INSERT INTO crypto_data (name, symbol, price, market_cap, volume_24h, percent_change_24h, timestamp)
            VALUES (
                '{coin['name'].replace("'", "''")}',  -- Escape single quotes
                '{coin['symbol'].replace("'", "''")}',
                {coin['price']},
                {coin['market_cap']},
                {coin['volume_24h']},
                {coin['percent_change_24h']},
                CAST({coin['timestamp']} AS TIMESTAMP)
            )
            """
            sql_statements.append(sql)

        # Combine all SQL statements into one payload
        payload = "; ".join(sql_statements)

        # Send SQL query to QuestDB
        response = requests.post(url, data={"query": payload})
        if response.status_code == 200:
            print("Data inserted successfully into QuestDB via REST API!")
        else:
            print(f"Failed to insert data: {response.text}")
    except Exception as e:
        print(f"Error while inserting data into QuestDB: {e}")