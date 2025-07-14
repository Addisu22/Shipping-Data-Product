from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")  # Automatically reads from .env

api_id     = os.getenv("tg_api_id")
api_hash   = os.getenv("tg_api_hash")
session_name = os.getenv("session_name")
host       = os.getenv("pgsql_host"),
port       = os.getenv("pgsql_port"),
db         = os.getenv("pgsql_db"),
user       = os.getenv("pgsql_user"),
password   = os.getenv("pgsql_pass")