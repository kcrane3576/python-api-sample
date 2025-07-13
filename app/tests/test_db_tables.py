from sqlalchemy import inspect
from core.database import engine

def test_document_table_exists():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert "documents" in tables