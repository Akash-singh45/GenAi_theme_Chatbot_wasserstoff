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
            f"[Doc: {c['doc_id']} | Page {c['page']} | Para {c['paragraph']}]: {c['text']}"
            for c in context_chunks
        ])

        prompt = f"""
You are a legal assistant AI designed to answer questions using the context provided from legal or academic documents. Use only the information in the context below.

### User Question:
{question}

### Document Context:
{context_text}

### Your Task:
1. Answer the question clearly and concisely.
2. Back every claim with citations using (Doc ID, Page, Para).
3. If multiple documents or paragraphs are relevant, synthesize them.
4. At the end, summarize any key themes or common points across documents.

### Output Format:
Answer: <your main answer>

Citations:
- Doc ID: ..., Page: ..., Para: ...
- Doc ID: ..., Page: ..., Para: ...

Theme Summary:
<optional — a short 1-2 line summary if relevant>
"""

        print("🧠 Sending to Gemini...")
        response = model.generate_content(prompt)
        print("✅ Gemini responded.")
        return response.text

    except Exception as e:
        print("❌ Gemini Error:", str(e))
        return f"Gemini Error: {str(e)}"

