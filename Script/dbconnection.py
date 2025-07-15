from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('../.env')
pgsql_pass= os.getenv("pgsql_pass")

# Our actual PostgreSQL database connection string
db_url = os.getenv("db_url", "postgresql://postgres:yourpassword@localhost:5432/telegram_db")

engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()