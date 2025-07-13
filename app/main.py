import logging
from fastapi import FastAPI
from sqlalchemy import text
from core. database import engine
from core.logging_config import setup_logging
from core.startup import init_db
from route_registry import register_routes
from services.elasticsearch import get_elasticsearch_client

setup_logging()
logger = logging.getLogger(__name__)

def create_app():
    app = FastAPI()
    init_db()
    register_routes(app)
    logger.info("App created successfully")

    try:
        with engine.connect() as conn:
            if conn.execute(text("SELECT 1")).scalar() == 1:
                logger.info("Connected to Postgres.")
    except Exception as ex:
        logger.error("Postgres connection failed: %s", ex)


    elasticsearch = get_elasticsearch_client()
    if not elasticsearch.ping():
        logger.error("Elasticsearch is not reachable at startup.")

    return app

app = create_app()
