# Configuration

All configuration is via environment variables.

## Required
- DATABASE_URL
- REDIS_URL
- SECRET_KEY

## Email
- SMTP_HOST
- SMTP_PORT
- SMTP_USER
- SMTP_PASSWORD

## SMS (MSG91)
- MSG91_API_KEY
- MSG91_SENDER_ID
- MSG91_TEMPLATE_ID

## Optional
- LOG_LEVEL (default: INFO)
- WORKER_CONCURRENCY (default: 4)
- MAX_RETRIES (default: 3)
- RETRY_BACKOFF_SECONDS (default: 60)
