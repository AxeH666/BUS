"""Tests for GET /health route."""

from collections.abc import AsyncGenerator
from unittest.mock import AsyncMock, patch

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.router import api_router
from src.database import get_db

app = FastAPI()
app.include_router(api_router)


async def _mock_db_ok() -> AsyncGenerator[AsyncSession, None]:
    session = AsyncMock(spec=AsyncSession)
    session.execute = AsyncMock(return_value=None)
    yield session


@pytest.mark.asyncio
async def test_health_all_ok() -> None:
    app.dependency_overrides[get_db] = _mock_db_ok
    mock_client = AsyncMock()
    mock_client.ping = AsyncMock(return_value=True)
    mock_client.aclose = AsyncMock(return_value=None)

    try:
        with patch(
            "src.api.routes.health.aioredis.from_url",
            return_value=mock_client,
        ):
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                response = await client.get("/health")

        assert response.status_code == 200
        assert response.json() == {
            "status": "ok",
            "database": "ok",
            "redis": "ok",
        }
    finally:
        app.dependency_overrides.clear()


@pytest.mark.asyncio
async def test_health_database_error() -> None:
    async def _mock_db_fail() -> AsyncGenerator[AsyncSession, None]:
        session = AsyncMock(spec=AsyncSession)
        session.execute = AsyncMock(side_effect=RuntimeError("db down"))
        yield session

    app.dependency_overrides[get_db] = _mock_db_fail
    mock_client = AsyncMock()
    mock_client.ping = AsyncMock(return_value=True)
    mock_client.aclose = AsyncMock(return_value=None)

    try:
        with patch(
            "src.api.routes.health.aioredis.from_url",
            return_value=mock_client,
        ):
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                response = await client.get("/health")

        assert response.status_code == 200
        body = response.json()
        assert body["status"] == "error"
        assert body["database"] == "error"
        assert body["redis"] == "ok"
    finally:
        app.dependency_overrides.clear()


@pytest.mark.asyncio
async def test_health_redis_error() -> None:
    app.dependency_overrides[get_db] = _mock_db_ok
    mock_client = AsyncMock()
    mock_client.ping = AsyncMock(side_effect=ConnectionError("redis down"))
    mock_client.aclose = AsyncMock(return_value=None)

    try:
        with patch(
            "src.api.routes.health.aioredis.from_url",
            return_value=mock_client,
        ):
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                response = await client.get("/health")

        assert response.status_code == 200
        body = response.json()
        assert body["status"] == "error"
        assert body["database"] == "ok"
        assert body["redis"] == "error"
    finally:
        app.dependency_overrides.clear()
