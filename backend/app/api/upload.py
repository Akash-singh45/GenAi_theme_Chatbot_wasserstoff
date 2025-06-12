# backend/app/api/upload.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.file_utils import save_uploaded_file
from app.services.doc_processor import extract_text_from_pdf, extract_text_from_scanned_pdf
from app.services.vector_store import save_to_faiss  # ✅ NEW

import os

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        print("📁 File received:", file.filename)

        file_path = save_uploaded_file(file)
        print("💾 File saved to:", file_path)

        ext = os.path.splitext(file.filename)[-1].lower()

        # Extract text
        if ext == ".pdf":
            print("📄 Attempting PDF text extraction...")
            extracted = extract_text_from_pdf(file_path)
            if not extracted:
                print("🧠 Falling back to OCR for scanned PDF...")
                extracted = extract_text_from_scanned_pdf(file_path)
        elif ext in [".jpg", ".jpeg", ".png"]:
            print("🧠 Processing image file via OCR...")
            extracted = extract_text_from_scanned_pdf(file_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        if not extracted:
            raise HTTPException(status_code=422, detail="No text extracted from file")

        print(f"📝 Extracted {len(extracted)} paragraphs")

        # Save to FAISS
        from app.services.vector_store import save_to_faiss
        saved_count = save_to_faiss(extracted)
        print(f"✅ Embedded and saved {saved_count} paragraphs to FAISS.")

        return {
            "status": "success",
            "file": file.filename,
            "paragraphs_indexed": saved_count
        }

    except Exception as e:
        print("❌ Upload Error:", str(e))
        raise HTTPException(status_code=500, detail=str(e))


        # ✅ Embed & store in FAISS
        saved_count = save_to_faiss(extracted)

        return {
            "status": "success",
            "file": file.filename,
            "paragraphs_indexed": saved_count
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during processing: {str(e)}")
