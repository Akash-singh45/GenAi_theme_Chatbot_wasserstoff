# backend/app/api/upload.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.file_utils import save_uploaded_file
from app.services.doc_processor import extract_text_from_pdf, extract_text_from_scanned_pdf
import os

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Uploads a file, saves it, processes it for text extraction using PDF or OCR,
    and returns structured text with doc_id, page, and paragraph.
    """
    # Save file to disk
    file_path = save_uploaded_file(file)

    # Check file type
    ext = os.path.splitext(file.filename)[-1].lower()

    try:
        if ext == ".pdf":
            try:
                extracted = extract_text_from_pdf(file_path)
                # If no text found, fallback to OCR
                if not extracted:
                    extracted = extract_text_from_scanned_pdf(file_path)
            except Exception:
                extracted = extract_text_from_scanned_pdf(file_path)
        elif ext in [".png", ".jpg", ".jpeg"]:
            extracted = extract_text_from_scanned_pdf(file_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        return {"status": "success", "extracted_data": extracted}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during processing: {str(e)}")
