import psycopg2
from config import host, port, db, user, password

def getpgsql_connect():
    conn = psycopg2.connect(
							host = host,
							port = port,
							db   = db,
							user = user,
							password = password)
    return conn