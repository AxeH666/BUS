"""Tests for database module."""

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import async_session_factory, engine, get_db


def test_engine_uses_database_url_from_settings() -> None:
    assert "postgresql" in str(engine.url)


@pytest.mark.asyncio
async def test_get_db_yields_async_session() -> None:
    gen = get_db()
    session = await anext(gen)
    assert isinstance(session, AsyncSession)
    await gen.aclose()


@pytest.mark.asyncio
async def test_async_session_factory_creates_session() -> None:
    async with async_session_factory() as session:
        assert isinstance(session, AsyncSession)
