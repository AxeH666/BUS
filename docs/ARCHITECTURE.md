# Architecture
## Overview
BUS (Background Unified Sender) is a self-hosted notification dispatch service.
Single API call → multi-channel delivery (Email, SMS, Webhook, SSE).

## Stack
- API: FastAPI
- Queue: Dramatiq + Redis
- Database: PostgreSQL + SQLAlchemy async
- Migrations: Alembic
- Configuration: pydantic-settings (`src/config.py`)
- Deployment: Docker Compose

## Configuration
`src/config.py` exposes a module-level `settings` object (`Settings` via `pydantic-settings`). Core vars (`DATABASE_URL`, `REDIS_URL`, `SECRET_KEY`) are required at startup; channel credentials are optional until those channels are used. See `docs/CONFIGURATION.md`.

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
