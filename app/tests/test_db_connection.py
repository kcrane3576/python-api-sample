from sqlalchemy import text
from core.database import engine

def test_database_connection():
    with engine.connect() as conn:
        assert conn.execute(text("SELECT 1")).scalar() == 1