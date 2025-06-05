from fastapi import APIRouter, HTTPException
from app.ai_logic import analyze_logs
from app.models import LogRequest, LogResponse

router = APIRouter()

@router.post("/analyze", response_model=LogResponse)
def analyze_log_route(request: LogRequest):
    result = analyze_logs(request.log_text)
    if result.startswith("Error"):
        raise HTTPException(status_code=500, detail=result)
    return LogResponse(analysis=result)

