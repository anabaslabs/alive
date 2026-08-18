# Alive

A lightweight, concurrent asynchronous uptime monitoring service built with FastAPI and HTTPX.

## Project Structure

```
alive/
├── app/                         # Core application package
│   ├── config.py                # App settings, env variables
│   ├── main.py                  # Application entry point & FastAPI instance
│   │
│   ├── routes/                  # HTTP Layer (Routing, Request/Response handling)
│   │   ├── delete.py
│   │   ├── download.py
│   │   ├── monitor.py
│   │   ├── update.py
│   │   └── upload.py
│   │
│   └── services/                # Business Logic Layer (Domain logic)
│       ├── delete.py
│       ├── download.py
│       ├── monitor.py
│       ├── update.py
│       └── upload.py
│
├── data/                        # Monitor definitions & template data
│   ├── monitors.json
│   └── template.json
│
├── .env                         # Local environment variables
├── .env.example                 # Example environment variables template
├── .gitignore                   # Python & environment gitignore rules
├── .python-version              # Local Python version pin (3.13)
├── Dockerfile                   # Docker build instructions
├── package.json                 # Node package scripts
├── pyproject.toml               # Project dependencies & tool configurations
└── README.md                    # Project documentation & setup guide
```

## Running the Application

### 1. Install Dependencies

```bash
uv sync
```

### 2. Start the Server

```bash
uv run python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Or using pnpm:

```bash
pnpm dev
```

Or using npm:

```bash
npm run dev
```

## Endpoints

- `GET /` — Service status.
- `GET /monitors` — Returns current status and last response code of all monitored endpoints.
- `GET /download` — Download monitor template.
- `POST /upload` — Upload monitor definitions.
- `PUT /update` — Update monitor definitions.
- `DELETE /delete` — Delete monitor definitions.
- `GET /docs` — Interactive OpenAPI / Swagger UI.
