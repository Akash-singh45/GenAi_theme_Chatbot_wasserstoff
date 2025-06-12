# backend/app/services/vector_store.py

import faiss
import os
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model (we'll use this across steps)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Vector store path
INDEX_FILE = "backend/data/faiss_index.index"
METADATA_FILE = "backend/data/faiss_metadata.pkl"

def embed_text(texts):
    """
    Generate dense embeddings for a list of text paragraphs using SBERT.
    """
    return embedding_model.encode(texts, show_progress_bar=False)

def save_to_faiss(text_data):
    """
    Embeds and stores extracted text into FAISS vector index with metadata.
    """
    texts = [item["text"] for item in text_data]
    embeddings = embed_text(texts)

    print("💾 Embedding and saving to FAISS...")
    print("🧾 Sample text:", texts[:1])
    print("📦 Embeddings shape:", embeddings.shape)


    index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 distance index
    index.add(np.array(embeddings))

    # Save metadata (doc_id, page, paragraph)
    metadata = [{"doc_id": t["doc_id"], "page": t["page"], "paragraph": t["paragraph"], "text": t["text"]} for t in text_data]

    # Save index and metadata
    faiss.write_index(index, INDEX_FILE)
    with open(METADATA_FILE, "wb") as f:
        pickle.dump(metadata, f)

    return len(embeddings)

def load_faiss_index():
    """
    Loads FAISS index and metadata from disk.
    """
    if not os.path.exists(INDEX_FILE) or not os.path.exists(METADATA_FILE):
        return None, []

    index = faiss.read_index(INDEX_FILE)
    with open(METADATA_FILE, "rb") as f:
        metadata = pickle.load(f)

    return index, metadata


