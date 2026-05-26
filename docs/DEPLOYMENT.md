# Deployment

## Quick Start
```bash
cp .env.example .env
# Set required vars: DATABASE_URL, REDIS_URL, SECRET_KEY
# Add SMTP / MSG91 vars only if you use those channels
docker compose up -d
```

## Services
- bus-api: FastAPI application
- bus-worker: Dramatiq worker
- bus-db: PostgreSQL
- bus-redis: Redis

## Production Checklist
- [ ] Set strong SECRET_KEY
- [ ] Configure SMTP credentials (if using email)
- [ ] Configure MSG91 credentials (if using SMS)
- [ ] Set up reverse proxy (nginx/caddy)
- [ ] Enable HTTPS
- [ ] Set LOG_LEVEL=WARNING
