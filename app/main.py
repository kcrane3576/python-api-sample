import logging
from fastapi import FastAPI
from api.routes import register_routes
from core.logging_config import setup_logging
from services.elasticsearch import get_elasticsearch_client

setup_logging()
logger = logging.getLogger(__name__)

def create_app():
    app = FastAPI()
    register_routes(app)
    logger.info("App created successfully")

    elasticsearch = get_elasticsearch_client()
    if not elasticsearch.ping():
        logger.error("Elasticsearch is not reachable at startup.")

    return app

app = create_app()
