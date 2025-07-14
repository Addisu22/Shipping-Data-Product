from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")  # Automatically reads from .env

api_id     = os.getenv("tg_api_id")
api_hash   = os.getenv("tg_api_hash")
session_name = os.getenv("session_name")
pgsql_host       = os.getenv("pgsql_host"),
pgsql_port       = int(os.getenv("pgsql_port").strip()),
pgsql_db         = os.getenv("pgsql_db"),
pgsql_user       = os.getenv("pgsql_user"),
pgsql_password   = os.getenv("pgsql_pass")