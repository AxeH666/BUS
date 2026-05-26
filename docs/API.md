# API Reference

## Endpoints

### POST /notify
Send a notification via one or more channels.

### GET /logs
Query delivery logs with filters.

### GET /health
Service health check. Returns status of API, Redis, and PostgreSQL.

### GET /stream/{client_id}
Server-sent events stream for a client. BUS pushes notification events as they arrive. See `docs/CHANNELS.md` (SSE).

## Authentication
Planned: Bearer API key in the `Authorization` header on all endpoints. **Not implemented yet.**

## Error Codes
To be filled as implementation progresses.
