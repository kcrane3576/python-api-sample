from fastapi import APIRouter
from core.config import settings

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": f"Hello, {settings.ENV} World!"}