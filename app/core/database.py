import os
from sqlalchemy import create_engine

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST", "db")
name = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:5432/{name}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)