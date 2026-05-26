"""pytest fixtures for database and Redis."""

import os

# Defaults so `import src.config` succeeds during test collection
os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://bus:bus@localhost:5432/bus_test")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379/15")
os.environ.setdefault("SECRET_KEY", "test-secret-key")

import pytest


@pytest.fixture
def db_session() -> None:
    """Database session fixture stub."""
    pass


@pytest.fixture
def redis_client() -> None:
    """Redis client fixture stub."""
    pass
