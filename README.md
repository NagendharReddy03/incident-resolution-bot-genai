<p align="center">
  <img src="https://img.shields.io/github/languages/top/NagendharReddy03/incident-resolution-bot-genai?style=for-the-badge"/>
  <img src="https://img.shields.io/github/last-commit/NagendharReddy03/incident-resolution-bot-genai?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/OpenAI-Integrated-blueviolet?style=for-the-badge"/>
</p>

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
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── routes.py            # All API endpoints
│   ├── ai_logic.py          # OpenAI interaction & logic
│   └── models.py            # Pydantic schemas
│
├── config/
│   └── config.yaml          # API Keys and settings
│
├── logs/                    # Stores request logs
│
├── ci/
│   ├── Dockerfile           # Docker config
│   ├── requirements.txt     # Dependencies
│   └── docker-compose.yml   # Containerized setup
│
├── .env                     # Set your OpenAI key here
└── README.md                # You’re reading it!

---

## Setup Instructions

# Clone the repo
git clone https://github.com/NagendharReddy03/incident-resolution-bot-genai.git
cd incident-resolution-bot-genai

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r ci/requirements.txt

# Set your OpenAI key
cp .env.example .env
# Then edit .env and paste your OPENAI_API_KEY

## Run the Bot

Run locally:
uvicorn app.main:app --reload
Go to: http://localhost:8000/docs

Run with Docker:

cd ci
docker compose up --build

## Future Enhancements
	•	JD context matching
	•	Streamlit or React frontend
	•	Role-Based Access Control (Admin / Agent)
	•	Feedback voting on suggestions
	•	CI/CD GitHub Actions Pipeline

---

Connect
	•	GitHub: https://github.com/NagendharReddy03
	•	LinkedIn: https://www.linkedin.com/in/nagendharreddy/
	•	📧 nagendharreddy.work@gmail.com

