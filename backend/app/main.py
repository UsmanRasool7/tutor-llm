from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers import example 

load_dotenv()
app = FastAPI(title="LLM Tutor", description="Swagger interface to test endpoints for LLM Tutor", version="1.0.0")

app.include_router(example.router)

@app.get("/health")
def health():
    return {"status": "ok"}
