from fastapi import FastAPI
from app.core import config


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": f"Hello, {config.settings.ENV} World!"}