# Configuration

All configuration is via environment variables, loaded by `src/config.py` using `pydantic-settings` (`Settings` / `settings`).

## Required
- DATABASE_URL
- REDIS_URL
- SECRET_KEY

## Channel credentials (optional at startup)
Required only when using the corresponding channel. Omit for webhook- or SSE-only deployments.

### Email (SMTP)
- SMTP_HOST
- SMTP_PORT
- SMTP_USER
- SMTP_PASSWORD

### SMS (MSG91)
- MSG91_API_KEY
- MSG91_SENDER_ID
- MSG91_TEMPLATE_ID

## Optional (defaults applied if unset)
- LOG_LEVEL (default: INFO)
- WORKER_CONCURRENCY (default: 4)
- MAX_RETRIES (default: 3)
- RETRY_BACKOFF_SECONDS (default: 60)
