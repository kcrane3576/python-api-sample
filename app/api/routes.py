from fastapi import FastAPI
from api.endpoints import root

def register_routes(app: FastAPI) -> None:
    app.include_router(root.router)