from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_DRIVER: str
    DATABASE_SERVER: str
    DATABASE: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str