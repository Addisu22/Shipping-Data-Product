import psycopg2
import os
from dotenv import load_dotenv

from config import pgsql_host, pgsql_port, pgsql_db, pgsql_user, pgsql_password

def getpgsql_connect():
    conn = psycopg2.connect(
							host = pgsql_host,
							port = pgsql_port,
							db   = pgsql_db,
							user = pgsql_password,
							password = pgsql_password)
    return conn