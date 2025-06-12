# backend/app/services/gemini_service.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Set your API key in .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def ask_gemini(question: str, context_chunks: list):
    try:
        context_text = "\n\n".join([
            f"[Doc: {c['doc_id']} | Page {c['page']}, Para {c['paragraph']}]: {c['text']}"
            for c in context_chunks
        ])

        prompt = f"""
You are a legal research assistant AI. Based on the question and document snippets, provide a clear, concise answer and cite source locations.

### Question:
{question}

### Document Context:
{context_text}

- Include citations (doc_id, page, para)
- At the end, summarize common themes if more than one document is involved.
"""

        print("🧠 Sending to Gemini...")
        response = model.generate_content(prompt)
        print("✅ Gemini responded.")
        return response.text

    except Exception as e:
        print("❌ Gemini Error:", str(e))
        return f"Gemini Error: {str(e)}"

print("🔐 GEMINI KEY:", os.getenv("GEMINI_API_KEY"))
