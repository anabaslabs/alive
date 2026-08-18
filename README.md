<h1 align="center">
  <b>🔰</b>
    <br>
  <b>ALIVE</b>
</h1>

<p align="center">
  A lightweight, concurrent asynchronous uptime monitoring service built with FastAPI and HTTPX.
</p>

<p align="center">
  <a href="https://github.com/anabaslabs/alive">
    <img alt="Version" src="https://img.shields.io/badge/version-v1.0.0-emerald">
  </a>
  <a href="https://github.com/anabaslabs/alive/blob/main/LICENSE">
    <img alt="GitHub License" src="https://img.shields.io/github/license/anabaslabs/alive?color=crimson">
  </a>
</p>

---

## ✳️ _API Endpoints_

| Method | Endpoint | Tag | Auth | Description |
| :---: | :---: | :---: | :---: | :---: |
| ![GET](https://img.shields.io/badge/GET-blue) | `/` | `Health` | No | Service status and version information. |
| ![POST](https://img.shields.io/badge/POST-green) | `/monitor` | `Snapshot` | No | Real-time status and response codes of all monitored targets. |
| ![GET](https://img.shields.io/badge/GET-blue) | `/download` | `Data` | No | Download monitor JSON template. |
| ![POST](https://img.shields.io/badge/POST-green) | `/upload` | `Data` | `Token` | Upload and replace monitor definitions. |
| ![PUT](https://img.shields.io/badge/PUT-orange) | `/update` | `Data` | `Token` | Update monitor configuration via JSON body. |
| ![DELETE](https://img.shields.io/badge/DELETE-red) | `/delete` | `Data` | `Token` | Delete active monitor definitions. |
| ![GET](https://img.shields.io/badge/GET-blue) | `/docs` | `Docs` | No | Interactive OpenAPI / Swagger UI. |

---

## ✳️ _Project Structure_

```text
alive/
├── app/                         # Core application package
│   ├── auth.py                  # Token authentication dependency
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

---

## ✳️ _Getting Started_

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

---

## ✳️ _API Documentation_

▶️ [**_`API`_**](http://localhost:8000) - API runs at [`localhost:8000`](http://localhost:8000)

▶️ [**_`Swagger UI Docs`_**](http://localhost:8000/docs) - Swagger UI docs at [`localhost:8000/docs`](http://localhost:8000/docs)
