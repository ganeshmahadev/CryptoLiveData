import psycopg2
import logging
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()

# Get QuestDB configuration from environment variables
QUESTDB_HOST = os.getenv("QUESTDB_HOST", "localhost")
QUESTDB_PORT = os.getenv("QUESTDB_PORT", "8812")  # Default port for PostgreSQL protocol
QUESTDB_USER = os.getenv("QUESTDB_USER", "admin")  # Default user
QUESTDB_PASSWORD = os.getenv("QUESTDB_PASSWORD", "quest")  # Default password
QUESTDB_DB = os.getenv("QUESTDB_DB", "qdb")  # Default database

# Configure logger
logging.basicConfig(
    filename="data/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def insert_into_questdb(data):
    """
    Inserts cryptocurrency data into QuestDB using the PostgreSQL wire protocol.
    """
    try:
        # Establish a connection to QuestDB
        conn = psycopg2.connect(
            host=QUESTDB_HOST,
            port=QUESTDB_PORT,
            user=QUESTDB_USER,
            password=QUESTDB_PASSWORD,
            database=QUESTDB_DB,
        )
        cursor = conn.cursor()

        # Prepare SQL INSERT statements
        sql = """
        INSERT INTO crypto_data (name, symbol, price, market_cap, volume_24h, percent_change_24h, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Insert each coin's data
        for coin in data:
            cursor.execute(sql, (
                coin['name'],
                coin['symbol'],
                coin['price'],
                coin['market_cap'],
                coin['volume_24h'],
                coin['percent_change_24h'],
                time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(coin['timestamp']/ 1e9))
            ))

        # Commit the transaction
        conn.commit()
        print("Data inserted successfully into QuestDB via PostgreSQL wire protocol!")
        logging.info("Data inserted successfully into QuestDB.")

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error while inserting data into QuestDB: {e}")
        logging.error(f"Error while inserting data into QuestDB: {e}")
