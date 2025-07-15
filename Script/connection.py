import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")  # Automatically reads from .env

def getpgsql_connect():
    conn = psycopg2.connect(
							pgsql_host       = os.getenv("pgsql_host"),
							pgsql_port       = int(os.getenv("pgsql_port")),
							pgsql_db         = os.getenv("pgsql_db"),
							pgsql_user       = os.getenv("pgsql_user"),
							pgsql_password   = os.getenv("pgsql_pass")
	)
    return conn