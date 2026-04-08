from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.deps.types.celery import CeleryDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_VHOST: str

    @computed_field
    @property
    def DB_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+psycopg",
            host=self.DB_HOST,
            port=self.DB_PORT,
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            path=self.DB_NAME,
        )

    @computed_field
    @property
    def CELERY_URI(self) -> CeleryDsn:
        return CeleryDsn.build(
            host=self.RABBITMQ_HOST,
            port=self.RABBITMQ_PORT,
            username=self.RABBITMQ_USER,
            password=self.RABBITMQ_PASSWORD,
            vhost=self.RABBITMQ_VHOST,
        )


def get_settings() -> Settings:
    return Settings()
