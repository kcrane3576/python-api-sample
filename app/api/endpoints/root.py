import logging
from fastapi import APIRouter
from core.config import settings

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/")
def read_root():
    message = {"message": f"Hello, {settings.ENV} World!"}
    logger.info(message)

    return message