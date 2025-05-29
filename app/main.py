from fastapi import FastAPI, Request
from app.ai_logic import analyze_logs
from app.models import LogRequest, LogResponse

app = FastAPI(title="GenAI Incident Resolution Bot")

@app.post("/analyze", response_model=LogResponse)
async def analyze_log_endpoint(request: LogRequest):
    result = analyze_logs(request.log_text)
    return {"suggested_fix": result}