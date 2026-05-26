# Docker

Docker Compose and Dockerfiles for BUS live in this directory.

## `docker-compose.yml`

Infra services for local development:

- `bus-db` — PostgreSQL 16
- `bus-redis` — Redis 7

Run the API on the host with uvicorn (see `docs/DEPLOYMENT.md`). `bus-api` and `bus-worker` images are planned.
