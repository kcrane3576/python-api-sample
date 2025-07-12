from api.routes import register_routes
from fastapi import FastAPI

def create_app():
    app = FastAPI()

    register_routes(app)

    return app

app = create_app()
