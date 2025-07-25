
<h1 align="center">GenAI Incident Resolution Bot</h1>

<p align="center">
  An AI-powered bot to automate L1/L2 IT incident resolution by parsing logs, matching job ticket context, and generating actionable solutions using OpenAI.
</p>

---

## Key Features

- Intelligent Log Analysis using GPT
- JD/Support Ticket Context Matching
- Upload `.txt`, `.pdf`, `.docx` for smarter resolution
- Suggests actionable fixes using historical data
- Dockerized App for Local/Cloud use
- Logging and Monitoring enabled
- Configurable via `.env` and `config.yaml`

---

## Project Structure

```bash
incident-resolution-bot-genai/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── routes.py            # API endpoints
│   ├── ai_logic.py          # OpenAI logic and context matching
│   └── models.py            # Pydantic schemas
├── config/
│   └── config.yaml          # API Keys and settings
├── logs/                    # Stores runtime logs
├── ci/
│   ├── Dockerfile           # Docker build
│   ├── requirements.txt     # Python dependencies
│   └── docker-compose.yml   # Docker orchestration
├── .github/workflows/
│   └── ci.yml               # GitHub Actions for CI/CD
├── .env.example             # Template for env variables
└── README.md
```
---

## Setup Instructions

## Clone the repo
git clone https://github.com/NagendharReddy03/incident-resolution-bot-genai.git
cd incident-resolution-bot-genai

## Set up virtual environment
python3 -m venv venv
source venv/bin/activate

## Install dependencies
pip install -r ci/requirements.txt

## Set your OpenAI key
cp .env.example .env
Then edit .env and paste your OPENAI_API_KEY

## Run the Bot

Run locally:
uvicorn app.main:app --reload
Go to: http://localhost:8000/docs

Run with Docker:

cd ci
docker compose up --build

## Future Enhancements
- JD context matching
- Streamlit or React frontend
- Role-Based Access Control (Admin / Agent)
- Feedback voting on suggestions
- CI/CD GitHub Actions Pipeline

---

## Connect
- GitHub: https://github.com/NagendharReddy03
- LinkedIn: https://www.linkedin.com/in/nagendharreddy/
- Mail: nagendharreddy.work@gmail.com

