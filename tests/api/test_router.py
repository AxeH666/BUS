"""Tests for FastAPI router registration."""

from src.api.router import api_router


def test_api_router_includes_health_route() -> None:
    paths = [route.path for route in api_router.routes]
    assert "/health" in paths
