import logging
from fastapi import FastAPI
from api.routes import register_routes
from core.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def create_app():
    app = FastAPI()
    register_routes(app)
    logger.info("App created successfully")

    return app

app = create_app()
