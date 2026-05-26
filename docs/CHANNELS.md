# Channels

## Email (SMTP)
Credentials: SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD
Test: Send to a real inbox and verify delivery.

## SMS (MSG91)
Credentials: MSG91_API_KEY, MSG91_SENDER_ID, MSG91_TEMPLATE_ID
Note: MSG91 is the primary SMS provider. No Twilio support.

## Webhook
No credentials needed. User provides target URL at send time.
BUS sends HTTP POST with JSON payload to the provided URL.

## SSE (Server-Sent Events)
Client subscribes to GET /stream/{client_id}.
BUS pushes events as they arrive.
No credentials needed.
