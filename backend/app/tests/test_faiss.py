# backend/app/tests/test_faiss.py

from app.services.vector_store import save_to_faiss, load_faiss_index

# Sample extracted text (simulate 2 paragraphs from 1 document)
sample_data = [
    {
        "doc_id": "Sample_Doc.pdf",
        "page": 1,
        "paragraph": 1,
        "text": "The tribunal observed that the company failed to disclose required financial statements on time."
    },
    {
        "doc_id": "Sample_Doc.pdf",
        "page": 1,
        "paragraph": 2,
        "text": "Regulatory action was initiated under Clause 49 of the SEBI Listing Agreement."
    }
]

# Step 1: Save to FAISS
print("Saving to FAISS...")
count = save_to_faiss(sample_data)
print(f"Stored {count} embeddings.")

# Step 2: Load from FAISS
print("Loading FAISS index...")
index, metadata = load_faiss_index()
print("Index loaded:", "Yes" if index else "No")
print("Sample metadata:", metadata[0] if metadata else "None")
