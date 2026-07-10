# AI Scenario Writer

Generate immersive, skill-based training scenarios powered by Groq AI (Llama 3.3 70B). Supports English and Hindi with difficulty levels M01–M07.

## Features

| Feature | Description |
|---------|-------------|
| 🎯 Any Skill | Works for any skill target you enter |
| 🌐 Multi-Language | English & Hindi (Devanagari script) |
| 📊 Difficulty Levels | M01 (Beginner) to M07 (Expert) |
| ⚡ Real-time AI | Instant scenario generation using Groq |
| 🔐 JWT Auth | Secure user registration and login |
| 🗄 PostgreSQL | Persistent scenario history per user |

## Project Structure

```
AI-scenario-writer/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── main.py             # App entry point
│   │   ├── config.py           # Environment settings
│   │   ├── database.py         # SQLAlchemy setup
│   │   ├── models/             # PostgreSQL models
│   │   ├── schemas/            # Pydantic request/response schemas
│   │   ├── routers/            # API routes (auth, scenarios)
│   │   ├── services/           # Business logic + Groq integration
│   │   └── utils/              # JWT & password utilities
│   ├── requirements.txt
│   └── .env.example
├── frontend/                   # React 18 frontend
│   ├── src/
│   │   ├── components/         # Reusable UI components
│   │   ├── pages/              # Login, Register, Dashboard, History
│   │   ├── context/            # Auth context provider
│   │   ├── services/           # Axios API client
│   │   ├── styles/             # Global CSS
│   │   └── utils/              # Constants
│   ├── package.json
│   └── vite.config.js
├── .vscode/                    # VS Code launch, tasks, settings
├── docker-compose.yml          # PostgreSQL container
└── README.md
```

## Prerequisites

- Python 3.8+
- Node.js 14+
- Docker (for PostgreSQL)
- [Groq API Key](https://console.groq.com) (free tier)

## Quick Start (VS Code)

### 1. Clone and open in VS Code

```bash
cd AI-scenario-writer
code .
```

Install recommended extensions when prompted.

### 2. Start PostgreSQL

```bash
docker compose up -d
```

Or run the VS Code task: **Terminal → Run Task → Docker: Start PostgreSQL**

### 3. Backend setup

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

Edit `backend/.env` and set your `GROQ_API_KEY` and a strong `SECRET_KEY`.

```bash
uvicorn app.main:app --reload --port 8000
```

Or press **F5** and select **Backend: FastAPI** (or **Full Stack** to run both).

### 4. Frontend setup

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

Open [http://localhost:5173](http://localhost:5173)

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/register` | No | Register new user |
| POST | `/api/auth/login` | No | Login (returns JWT) |
| GET | `/api/auth/me` | Yes | Get current user |
| POST | `/api/scenarios/generate` | Yes | Generate AI scenario |
| GET | `/api/scenarios/` | Yes | List user's scenarios |
| GET | `/api/scenarios/{id}` | Yes | Get scenario by ID |
| GET | `/api/health` | No | Health check |

API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Tech Stack

**Frontend:** React 18, Vite, Axios, CSS3 (glassmorphism)

**Backend:** FastAPI, SQLAlchemy, PostgreSQL, JWT (python-jose), Groq AI (Llama 3.3 70B), Uvicorn

## Environment Variables

### Backend (`backend/.env`)

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | JWT signing secret |
| `GROQ_API_KEY` | Groq API key from console.groq.com |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT expiry (default: 60) |
| `CORS_ORIGINS` | Allowed frontend origins |

### Frontend (`frontend/.env`)

| Variable | Description |
|----------|-------------|
| `VITE_API_URL` | Backend URL (default: proxied via Vite) |

## License

MIT
