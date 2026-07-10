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
AI-scenario-writer/
├── backend/ # FastAPI backend
│ ├── app/
│ │ ├── main.py # App entry point
│ │ ├── config.py # Environment settings
│ │ ├── database.py # SQLAlchemy setup
│ │ ├── models/ # PostgreSQL models
│ │ ├── schemas/ # Pydantic request/response schemas
│ │ ├── routers/ # API routes (auth, scenarios)
│ │ ├── services/ # Business logic + Groq integration
│ │ └── utils/ # JWT & password utilities
│ ├── requirements.txt
│ └── .env.example
├── frontend/ # React 18 frontend
│ ├── src/
│ │ ├── components/ # Reusable UI components
│ │ ├── pages/ # Login, Register, Dashboard, History
│ │ ├── context/ # Auth context provider
│ │ ├── services/ # Axios API client
│ │ ├── styles/ # Global CSS
│ │ └── utils/ # Constants
│ ├── package.json
│ └── vite.config.js
├── .vscode/ # VS Code launch, tasks, settings
├── docker-compose.yml # PostgreSQL container
├── recordings/ # Demo recordings
└── README.md

text

## Prerequisites

- Python 3.8+
- Node.js 14+
- Docker (for PostgreSQL)
- [Groq API Key](https://console.groq.com) (free tier)

## Quick Start (VS Code)

### 1. Clone and open in VS Code

```bash
git clone https://github.com/rajdeep547/scenario_writer.git
cd scenario_writer
code .
