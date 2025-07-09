from app.core import config

def test_env_config_loads():
    assert config.settings.ENV == "test"
