# Contributing

## Branch Naming
feature/D-XXX-short-description

## Commit Format
D-XXX: short description of change

## PR Rules
- Every PR references a D-number
- CI must pass before merge
- Never merge your own PR without review

## Running Tests
```bash
source .venv/bin/activate
pytest tests/ -v
```

## Adding a Channel
1. Log decision in DECISIONS.md
2. Create src/channels/your_channel.py
3. Create tests/channels/test_your_channel.py
4. Register in src/channels/__init__.py
5. Update docs/CHANNELS.md
