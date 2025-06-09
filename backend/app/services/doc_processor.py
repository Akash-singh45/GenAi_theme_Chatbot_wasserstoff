# backend/app/services/doc_processor.py

import os
import pdfplumber
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import uuid

def extract_text_from_pdf(file_path):
    text_data = []
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                paragraphs = text.split('\n\n')
                for j, para in enumerate(paragraphs):
                    text_data.append({
                        "doc_id": os.path.basename(file_path),
                        "page": i + 1,
                        "paragraph": j + 1,
                        "text": para.strip()
                    })
    return text_data


def extract_text_from_scanned_pdf(file_path):
    text_data = []
    doc = fitz.open(file_path)
    for i, page in enumerate(doc):
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        ocr_text = pytesseract.image_to_string(img)
        if ocr_text:
            paragraphs = ocr_text.split('\n\n')
            for j, para in enumerate(paragraphs):
                text_data.append({
                    "doc_id": os.path.basename(file_path),
                    "page": i + 1,
                    "paragraph": j + 1,
                    "text": para.strip()
                })
    return text_data
