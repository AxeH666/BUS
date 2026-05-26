# Decisions Log
All architectural decisions are logged here before implementation.
Format: D-XXX | Date | Decision | Reason | Trade-offs

## D-001 | 2026-05-26 | Project documentation and structure initialized
Decision: Establish full documentation structure before any code is written.
Reason: Engineering hygiene. Every serious OSS project documents before building.
Trade-offs: Slower start, better long-term maintainability.

## D-002 | 2026-05-27 | Scaffold src/ and tests/ directory structure
Decision: Create full module scaffold with docstrings and placeholder tests before any logic is written.
Reason: Enforces structure discipline. Every module has a home before code is written.
Trade-offs: Extra setup time. Prevents structural drift later.

## D-003 | 2026-05-27 | Implement config.py — environment variable loading
Decision: Use pydantic-settings BaseSettings to load and validate env vars. DATABASE_URL, REDIS_URL, and SECRET_KEY are required at startup; SMTP and MSG91 credentials are optional until those channels are used.
Reason: Single source of truth. Fail fast on core deps at startup. No scattered os.environ calls.
Trade-offs: Adds pydantic-settings dependency. Channel creds not validated until channel use.

## D-004 | 2026-05-27 | Implement database.py — async SQLAlchemy engine and session
Decision: Use SQLAlchemy async engine with asyncpg driver. Session factory via async_sessionmaker. Engine reads DATABASE_URL from settings.
Reason: Async-first from the start. No sync/async mixing later.
Trade-offs: asyncpg adds a dependency. Required for FastAPI async routes.
