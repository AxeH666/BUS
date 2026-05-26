# Docker

Docker Compose and Dockerfiles for BUS live in this directory.

## `docker-compose.yml`

Infra services for local development:

- `bus-db` — PostgreSQL 16 (host port **5433** → container 5432; avoids conflict with a system Postgres on 5432)
- `bus-redis` — Redis 7 (host port **6379**)

Set `DATABASE_URL=postgresql+asyncpg://bus:bus@localhost:5433/bus` in `.env`.

Run the API on the host with uvicorn (see `docs/DEPLOYMENT.md`). `bus-api` and `bus-worker` images are planned.
