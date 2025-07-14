import psycopg2
from config import pgsql_host, pgsql_port, pgsql_db, pgsql_user, pgsql_pass

def getpgsql_connect():
    conn = psycopg2.connect(
							host = pgsql_host,
							port = pgsql_port,
							db   = pgsql_db,
							user = pgsql_user,
							password = pgsql_pass
    )