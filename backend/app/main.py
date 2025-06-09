# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import upload

app = FastAPI(title="GenAI Theme Chatbot Backend")

# Allow CORS for frontend (Streamlit or React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include upload route
app.include_router(upload.router, prefix="/api")
