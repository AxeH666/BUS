# BUS — Background Unified Sender

Self-hosted notification dispatch: one API call, multi-channel delivery (Email, SMS, Webhook, SSE).

## Cursor rules

Agent conventions live in `.cursor/rules/` (stack, structure, decisions, testing, docs, git, hygiene). After changes, agents run a hygiene sweep and **flag** gaps rather than fixing them without your say-so.

## Documentation

| Doc | Purpose |
|-----|---------|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Stack, data flow, ports |
| [docs/API.md](docs/API.md) | HTTP endpoints |
| [docs/CONFIGURATION.md](docs/CONFIGURATION.md) | Environment variables |
| [docs/CHANNELS.md](docs/CHANNELS.md) | Channel setup |
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Docker deployment |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Architecture decision log |
| [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) | Branch, commit, PR rules |

## Quick start (development)

```bash
cp .env.example .env
# Edit .env — set DATABASE_URL, REDIS_URL, SECRET_KEY
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## License

MIT — see [LICENSE](LICENSE).
