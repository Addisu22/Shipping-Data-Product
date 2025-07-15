import psycopg2
import os
from dotenv import load_dotenv

from config import pgsql_host, pgsql_port, pgsql_db, pgsql_user, pgsql_password

def getpgsql_connect():
    conn = psycopg2.connect(
							pgsql_host       = os.getenv("pgsql_host"),
							pgsql_port       = int(os.getenv("pgsql_port")),
							pgsql_db         = os.getenv("pgsql_db"),
							pgsql_user       = os.getenv("pgsql_user"),
							pgsql_password   = os.getenv("pgsql_pass")
	)
    return conn