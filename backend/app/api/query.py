# backend/app/api/query.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.vector_store import load_faiss_index, embedding_model
from app.services.gemini_service import ask_gemini
import numpy as np

router = APIRouter()

class QueryRequest(BaseModel):
    question: str
    top_k: int = 3

@router.post("/query")
async def query_docs(req: QueryRequest):
    """
    Accepts a user question, retrieves top matching document chunks from FAISS,
    and returns Gemini's response + source metadata.
    """
    try:
        index, metadata = load_faiss_index()
        if index is None or not metadata:
            raise HTTPException(status_code=404, detail="FAISS index not found or empty.")

        # Embed user question
        question_vec = embedding_model.encode([req.question])
        D, I = index.search(np.array(question_vec), req.top_k)

        # Collect matching chunks
        matched_chunks = [metadata[i] for i in I[0]]

        # Send to Gemini
        response = ask_gemini(req.question, matched_chunks)

        return {
            "status": "success",
            "matched_chunks": matched_chunks,
            "response": response
        }

    except Exception as e:
        print("❌ Error in /api/query:", str(e))  # Add this for debugging
        raise HTTPException(status_code=500, detail=str(e))
   

