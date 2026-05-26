# Changelog

## [Unreleased]
- Initial project structure and documentation
- D-003: `src/config.py` with pydantic-settings; optional channel credentials at startup
- Docs: add `GET /stream/{client_id}` to API reference; align SSE naming in architecture
- Add `README.md`, `docker/`, and `scripts/` scaffolds; expand `.gitignore`
- Tests: real `test_config.py`; conftest sets default env for config import
