"""pytest fixtures for database and Redis."""

import os
from collections.abc import AsyncGenerator
from unittest.mock import AsyncMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

# Defaults so `import src.config` succeeds during test collection
os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://bus:bus@localhost:5433/bus_test")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379/15")
os.environ.setdefault("SECRET_KEY", "test-secret-key")

from src.database import get_db  # noqa: E402


@pytest.fixture
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Yield an async DB session via get_db (integration tests; requires PostgreSQL)."""
    async for session in get_db():
        yield session


@pytest.fixture
def redis_client() -> AsyncMock:
    """Redis client mock for unit tests."""
    client = AsyncMock()
    client.ping = AsyncMock(return_value=True)
    client.aclose = AsyncMock(return_value=None)
    return client
