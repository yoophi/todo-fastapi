import os
from functools import lru_cache

from pydantic import BaseSettings


class SettingsInterface(BaseSettings):
    debug: bool = True
    db_user: str = "user"
    db_password: str = "secret"
    db_host: str = "localhost"
    db_port: int = 3306
    db_database: str = "todos"


class DevelopmentSettings(SettingsInterface):
    pass


class ProductionSettings(SettingsInterface):
    debug = False


@lru_cache()
def get_settings():
    config = os.environ.get("FAST_API_CONFIG", "default")
    configs = {
        "development": DevelopmentSettings,
        "production": ProductionSettings,
        "default": DevelopmentSettings,
    }

    return configs.get(config, DevelopmentSettings)()
