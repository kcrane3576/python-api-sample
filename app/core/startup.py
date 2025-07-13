from core.database import Base, engine
from models.document import Document

def init_db():
    Base.metadata.create_all(bind=engine)
