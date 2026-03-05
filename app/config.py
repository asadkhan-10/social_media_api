# app/config.py
from typing import ClassVar
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database settings
    database_hostname: str
    database_port: int
    database_username: str
    database_password: str
    database_name: str

    # App settings
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Pydantic config
    env_prefix: ClassVar[str] = ""  # No prefix; match env var names exactly
    env_file: ClassVar[str] = ".env"  # Optional, local fallback


# Load settings
settings = Settings()
