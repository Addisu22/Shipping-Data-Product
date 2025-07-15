import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")  # Automatically reads from .env

def getpgsql_connect():
    conn = psycopg2.connect(
        host=os.getenv("pgsql_host"),
        port=int(os.getenv("pgsql_port")),
        dbname=os.getenv("pgsql_db"),
        user=os.getenv("pgsql_user"),
        password=os.getenv("pgsql_pass")
    )
    return conn