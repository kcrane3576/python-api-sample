import os
from dotenv import load_dotenv
from pathlib import Path

# Read which file to load
env_file = os.getenv("ENV_FILE", ".env")

print(env_file)

# Resolve path relative to project root
env_path = Path(__file__).resolve().parent.parent / env_file
print(env_path)
load_dotenv(dotenv_path=env_path)

class Settings:
    ENV: str = os.getenv("ENV", "development")

settings = Settings()