# Uptime Monitor

A lightweight, concurrent asynchronous uptime monitoring service built with FastAPI and HTTPX.

## Project Structure

```
backend/
├── app/                         # Core application package
│   ├── config.py                # App settings, env variables (pydantic-settings)
│   ├── main.py                  # Application entry point & FastAPI instance
│   │
│   ├── routes/                  # HTTP Layer (Routing, Request/Response handling)
│   │   └── monitors.py          # Monitor status endpoint handlers
│   │
│   ├── services/                # Business Logic Layer (Pure domain logic, NO HTTP imports)
│   │   └── monitors.py          # Business logic for background monitoring operations
│   │
│   └── static/                  # Static assets (HTML, CSS, JS, images)
│       └── index.html
│
├── .env                         # Local environment variables
├── .env.example                 # Example environment variables template
├── .gitignore                   # Python & environment gitignore rules
├── .python-version              # Local Python version pin (3.13)
├── pyproject.toml               # Project dependencies & tool configurations
└── README.md                    # Project documentation & setup guide
```

## Running the Application

### 1. Install Dependencies
```bash
pip install -r requirements.txt  # or install via uv / pip install -e .
```

### 2. Start the Server
```bash
cd backend
python -m app.main
```
Or using uvicorn directly:
```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Endpoints
- `GET /` — Returns current status and last response code of all monitored endpoints.
- `GET /docs` — Interactive OpenAPI / Swagger UI.
