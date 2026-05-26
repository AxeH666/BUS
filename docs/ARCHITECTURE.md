# Architecture
## Overview
BUS (Background Unified Sender) is a self-hosted notification dispatch service.
Single API call → multi-channel delivery (Email, SMS, Webhook, SSE).

## Stack
- API: FastAPI
- Queue: Dramatiq + Redis
- Database: PostgreSQL + SQLAlchemy async
- Migrations: Alembic
- Deployment: Docker Compose

## Data Flow
Client → POST /notify → FastAPI → Dramatiq Queue (Redis) → Worker → Channel Handler → Delivery Log (PostgreSQL)

## Channels
- Email: SMTP
- SMS: MSG91
- Webhook: HTTP POST to user-defined URL
- Push: SSE stream

## Ports
- API: 8000
- Redis: 6379
- PostgreSQL: 5432
