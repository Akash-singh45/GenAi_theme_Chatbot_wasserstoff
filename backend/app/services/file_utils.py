# backend/app/services/file_utils.py

import os
import shutil
import uuid

# Set your upload directory
UPLOAD_DIR = "backend/data"

# Create directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_uploaded_file(file):
    """
    Saves uploaded file with a unique name in the data directory.

    Args:
        file: File object from FastAPI UploadFile

    Returns:
        str: Path to saved file
    """
    ext = os.path.splitext(file.filename)[-1]
    unique_name = f"{uuid.uuid4()}{ext}"
    save_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return save_path
