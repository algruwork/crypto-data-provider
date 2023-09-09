"""
    Settings
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """ Settings class """
    main_url: str  # export MAIN_URL=/


settings = Settings()