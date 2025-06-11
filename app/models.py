from pydantic import BaseModel, Field


class LogAnalysisRequest(BaseModel):
    log_text: str = Field(..., example="ERROR 503: Service Unavailable at /api/user")

class LogAnalysisResponse(BaseModel):
    analysis: str

class JDMatchingRequest(BaseModel):
    log_text: str = Field(..., example="NullPointerException at line 32")
    jd_text: str = Field(..., example="The engineer should handle backend exceptions gracefully.")

class JDMatchingResponse(BaseModel):
    matched_insight: str