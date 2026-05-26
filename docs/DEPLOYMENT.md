# Deployment

## Quick Start
```bash
cp .env.example .env
# Set required vars: DATABASE_URL, REDIS_URL, SECRET_KEY
# Add SMTP / MSG91 vars only if you use those channels

docker compose -f docker/docker-compose.yml up -d
source .venv/bin/activate && pip install -r requirements.txt
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

## Services
- bus-api: FastAPI application (`src/main.py`, port 8000)
- bus-worker: Dramatiq worker (planned)
- bus-db: PostgreSQL (`docker/docker-compose.yml`)
- bus-redis: Redis (`docker/docker-compose.yml`)

## Production Checklist
- [ ] Set strong SECRET_KEY
- [ ] Configure SMTP credentials (if using email)
- [ ] Configure MSG91 credentials (if using SMS)
- [ ] Set up reverse proxy (nginx/caddy)
- [ ] Enable HTTPS
- [ ] Set LOG_LEVEL=WARNING
