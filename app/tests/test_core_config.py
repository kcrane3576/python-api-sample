import os
from core import config

def test_env_config_loads():
    print(f"ENV_FILE: {os.getenv('ENV_FILE')}")
    print(f"Actual ENV loaded: {config.settings.ENV}")
    assert config.settings.ENV == "test"
