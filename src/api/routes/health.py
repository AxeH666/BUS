"""GET /health route handler."""

import redis.asyncio as aioredis
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import settings
from src.database import get_db

router = APIRouter()


async def _check_database(session: AsyncSession) -> str:
    try:
        await session.execute(text("SELECT 1"))
        return "ok"
    except Exception:
        return "error"


async def _check_redis() -> str:
    client = aioredis.from_url(settings.REDIS_URL)
    try:
        await client.ping()
        return "ok"
    except Exception:
        return "error"
    finally:
        await client.aclose()


@router.get("/health")
async def health(db: AsyncSession = Depends(get_db)) -> dict[str, str]:
    """Return overall and per-service health for PostgreSQL and Redis."""
    database = await _check_database(db)
    redis_status = await _check_redis()
    overall = "ok" if database == "ok" and redis_status == "ok" else "error"
    return {
        "status": overall,
        "database": database,
        "redis": redis_status,
    }
