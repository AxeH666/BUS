"""Tests for FastAPI application entry point."""

from collections.abc import AsyncGenerator
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.main import app


async def _mock_db_ok() -> AsyncGenerator[AsyncSession, None]:
    session = AsyncMock(spec=AsyncSession)
    session.execute = AsyncMock(return_value=None)
    yield session


def test_app_mounts_health_route() -> None:
    app.dependency_overrides[get_db] = _mock_db_ok
    mock_client = AsyncMock()
    mock_client.ping = AsyncMock(return_value=True)
    mock_client.aclose = AsyncMock(return_value=None)

    try:
        with patch(
            "src.api.routes.health.aioredis.from_url",
            return_value=mock_client,
        ):
            client = TestClient(app)
            response = client.get("/health")

        assert response.status_code == 200
        assert response.json()["status"] in ("ok", "error")
    finally:
        app.dependency_overrides.clear()
