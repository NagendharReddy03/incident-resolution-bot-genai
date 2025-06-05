from fastapi import FastAPI
from app.routes import router as log_router

app = FastAPI(title="GenAI Incident Resolution Bot")

# Include the routes
app.include_router(log_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the GenAI Incident Resolution Bot API!"}

