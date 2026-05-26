# Changelog

## [Unreleased]
- Initial project structure and documentation
- D-003: `src/config.py` with pydantic-settings; optional channel credentials at startup
- D-004: `src/database.py` async SQLAlchemy engine, session factory, `get_db`
- D-005: `GET /health` with PostgreSQL and Redis checks
- `src/main.py` mounts `api_router`; uvicorn in `requirements.txt`
- Docs: `GET /stream/{client_id}` in API reference; SSE naming; architecture/database/health sections
- Add `README.md`, `docker/docker-compose.yml` (Postgres + Redis), `scripts/` scaffold; expand `.gitignore`
- Cursor: `bus-hygiene.mdc` post-change sweep rule
- Tests: `test_config`, `test_database`, `test_health`, `test_main`, `test_router`; conftest test env defaults
