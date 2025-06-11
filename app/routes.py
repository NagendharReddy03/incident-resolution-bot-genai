# routes.py
from fastapi import APIRouter, HTTPException
from app.models import LogAnalysisRequest, LogAnalysisResponse, JDMatchingRequest, JDMatchingResponse
from app.ai_logic import analyze_logs, match_with_context

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to the GenAI Incident Resolution Bot API!"}

@router.post("/analyze", response_model=LogAnalysisResponse)
def analyze_log_route(request: LogAnalysisRequest):
    try:
        result = analyze_logs(request.log_text)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during analysis: {str(e)}")

@router.post("/match-context", response_model=JDMatchingResponse)
def match_context_route(request: JDMatchingRequest):
    try:
        result = match_with_context(request.log_text, request.context_text)
        return {"match_analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during context matching: {str(e)}")