"""Environment variable loading and application settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str

    SMTP_HOST: str | None = None
    SMTP_PORT: int | None = None
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None

    MSG91_API_KEY: str | None = None
    MSG91_SENDER_ID: str | None = None
    MSG91_TEMPLATE_ID: str | None = None

    LOG_LEVEL: str = "INFO"
    WORKER_CONCURRENCY: int = 4
    MAX_RETRIES: int = 3
    RETRY_BACKOFF_SECONDS: int = 60


settings = Settings()
