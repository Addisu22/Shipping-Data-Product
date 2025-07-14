import psycopg2
from config import host, port, db, user, password

def getpgsql_connect(host, port, db, user, password):
    conn = psycopg2.connect(
							host = host,
							port = port,
							db   = db,
							user = user,
							password = password
    )