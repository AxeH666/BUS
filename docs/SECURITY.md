# Security Policy

## Reporting Vulnerabilities
Do not open a public GitHub issue for security vulnerabilities.
Email: security@blacklynx.dev

## Supported Versions
Only the latest release receives security patches.

## Known Considerations
- API keys are stored hashed in PostgreSQL
- All secrets must be passed via environment variables
- Never commit .env files
- Webhook URLs are validated before dispatch
