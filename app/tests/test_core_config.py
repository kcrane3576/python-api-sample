from core import config

def test_env_config_loads():
    print(f"config.settings.ENV: ${config.settings.ENV}")
    assert config.settings.ENV == "test"
