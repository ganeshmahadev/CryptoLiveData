import psycopg2
from psycopg2.extras import execute_values
import logging
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# Configure logger
logging.basicConfig(
    filename="data/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Load database configuration
with open("config/db_config.json", "r") as f:
    db_config = json.load(f)

# Get PostgreSQL credentials from environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def store_to_postgresql(data):
    """
    Stores cryptocurrency data into the PostgreSQL database.
    """
    try:
        logging.info("Connecting to PostgreSQL database...")
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # Insert data into the table
        insert_query = """
        INSERT INTO crypto_data (name, symbol, price, market_cap, volume_24h, percent_change_24h)
        VALUES %s
        """
        execute_values(cursor, insert_query, data)
        conn.commit()

        logging.info("Successfully inserted data into the PostgreSQL database.")
        cursor.close()
        conn.close()
    except Exception as e:
        logging.error(f"Error while storing data into PostgreSQL: {e}")
