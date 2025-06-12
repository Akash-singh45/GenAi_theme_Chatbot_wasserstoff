# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import upload, query

app = FastAPI(title="GenAI Theme Chatbot Backend")

# CORS (for Streamlit or browser later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test root endpoint
@app.get("/")
def root():
    return {"message": "Backend is working fine ✅"}

# Upload route
app.include_router(upload.router, prefix="/api")

app.include_router(upload.router, prefix="/api")
app.include_router(query.router, prefix="/api")