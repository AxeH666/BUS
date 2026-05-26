# Deployment

## Quick Start
```bash
cp .env.example .env
# Fill in your credentials
docker compose up -d
```

## Services
- bus-api: FastAPI application
- bus-worker: Dramatiq worker
- bus-db: PostgreSQL
- bus-redis: Redis

## Production Checklist
- [ ] Set strong SECRET_KEY
- [ ] Configure SMTP credentials
- [ ] Configure MSG91 credentials
- [ ] Set up reverse proxy (nginx/caddy)
- [ ] Enable HTTPS
- [ ] Set LOG_LEVEL=WARNING
