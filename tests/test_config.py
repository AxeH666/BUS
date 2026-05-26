"""Tests for configuration module."""

from src.config import Settings


def test_settings_required_fields() -> None:
    s = Settings(
        DATABASE_URL="postgresql://localhost/db",
        REDIS_URL="redis://localhost:6379/0",
        SECRET_KEY="secret",
    )
    assert s.DATABASE_URL == "postgresql://localhost/db"
    assert s.REDIS_URL == "redis://localhost:6379/0"
    assert s.SECRET_KEY == "secret"


def test_settings_optional_channel_fields_default_none() -> None:
    s = Settings(
        DATABASE_URL="postgresql://localhost/db",
        REDIS_URL="redis://localhost:6379/0",
        SECRET_KEY="secret",
    )
    assert s.SMTP_HOST is None
    assert s.SMTP_PORT is None
    assert s.MSG91_API_KEY is None


def test_settings_optional_defaults() -> None:
    s = Settings(
        DATABASE_URL="postgresql://localhost/db",
        REDIS_URL="redis://localhost:6379/0",
        SECRET_KEY="secret",
    )
    assert s.LOG_LEVEL == "INFO"
    assert s.WORKER_CONCURRENCY == 4
    assert s.MAX_RETRIES == 3
    assert s.RETRY_BACKOFF_SECONDS == 60
