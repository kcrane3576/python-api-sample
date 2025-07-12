import os
from dotenv import load_dotenv
from pathlib import Path

# Resolve path relative to project root
ENV = os.getenv("ENV", "local")
env_path = Path(__file__).resolve().parent.parent / f".env.{ENV}"
print(f"config | env_path: {env_path}")
load_dotenv(dotenv_path=env_path)

class Settings:
    ENV: str = ENV
    ELASTICSEARCH_URL: str = os.getenv('ELASTICSEARCH_URL')

settings = Settings()
print(f"config | ENV: {settings.ENV}")