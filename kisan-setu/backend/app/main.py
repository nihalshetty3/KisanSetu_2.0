from fastapi import FastAPI 
from app.routes.voice import router as voice_router

app = FastAPI(
    title="KisanSetu API",
    description="Voice-first agricultural marketplace",
    version="1.0.0"
)

app.include_router(voice_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to KisanSetu"
    }