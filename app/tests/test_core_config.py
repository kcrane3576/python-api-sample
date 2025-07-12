import os
from core import config

def test_env_vars():
    print("DB_NAME:", os.getenv("DB_NAME"))
    print("ENV:", os.getenv("ENV"))
    assert os.getenv("ENV") == "test"

def test_env_config_loads():
    print(f"Actual ENV loaded: {config.settings.ENV}")
    assert config.settings.ENV == "test"
