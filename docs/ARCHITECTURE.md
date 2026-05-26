# Architecture
## Overview
BUS (Background Unified Sender) is a self-hosted notification dispatch service.
Single API call → multi-channel delivery (Email, SMS, Webhook, SSE).

## Stack
- API: FastAPI (`src/main.py` → `src/api/router.py`)
- Queue: Dramatiq + Redis (planned)
- Database: PostgreSQL + SQLAlchemy async (`src/database.py`)
- Migrations: Alembic (planned)
- Configuration: pydantic-settings (`src/config.py`)
- Deployment: Docker Compose (`docker/docker-compose.yml` for infra)

## Configuration
`src/config.py` exposes a module-level `settings` object (`Settings` via `pydantic-settings`). Core vars (`DATABASE_URL`, `REDIS_URL`, `SECRET_KEY`) are required at startup; channel credentials are optional until those channels are used. See `docs/CONFIGURATION.md`.

## Database
`src/database.py` provides an async SQLAlchemy engine (`create_async_engine`), `async_sessionmaker`, and `get_db()` for FastAPI dependency injection. Uses the `asyncpg` driver via `DATABASE_URL`.

## API (implemented)
- `GET /health` — pings PostgreSQL (`SELECT 1`) and Redis (`PING`); returns `status`, `database`, `redis` (`src/api/routes/health.py`)

## Data Flow
Client → POST /notify → FastAPI → Dramatiq Queue (Redis) → Worker → Channel Handler → Delivery Log (PostgreSQL)

## Channels
- Email: SMTP
- SMS: MSG91
- Webhook: HTTP POST to user-defined URL
- SSE: Server-sent events stream (`GET /stream/{client_id}`)

## Ports
- API: 8000
- Redis: 6379
- PostgreSQL: 5432
