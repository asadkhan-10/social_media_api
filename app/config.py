# app/config.py
from typing import ClassVar
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str  # PGHOST
    database_port: int  # PGPORT
    database_username: str  # PGUSER
    database_password: str  # PGPASSWORD
    database_name: str  # PGDATABASE
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Pydantic v2: Class variables
    env_prefix: ClassVar[str] = "PG"  # maps PGHOST, PGPORT etc.
    env_file: ClassVar[str] = ".env"  # optional local testing
    env_file_encoding: ClassVar[str] = "utf-8"


settings = Settings()  # type: ignore
