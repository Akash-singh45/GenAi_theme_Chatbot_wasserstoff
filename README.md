# 📄 GenAI Theme Chatbot

A full-stack AI-powered document Q\&A chatbot that allows users to upload PDF or image files and ask natural language questions. The chatbot retrieves relevant content using semantic search (FAISS) and answers using Gemini Pro (Google Generative AI).

---

## 🚀 Features

* 📁 **Document Upload**: Upload PDFs or scanned images
* 📄 **Text Extraction**: Extracts paragraphs from text or OCR
* 🧠 **Semantic Indexing**: Embeds document paragraphs using Sentence Transformers
* 🔍 **FAISS Vector Search**: Finds the most relevant chunks for each query
* 🤖 **Gemini Pro Answering**: Uses Google Generative AI (Gemini Pro) for accurate responses with citations
* 💻 **Streamlit Frontend**: Simple, interactive UI for document upload and Q\&A

---

## 🧱 Tech Stack

* **Frontend**: Streamlit (Python)
* **Backend**: FastAPI (Python)
* **Vector DB**: FAISS
* **LLM API**: Google Gemini Pro (`google-generativeai`)
* **OCR Engine**: pytesseract
* **Embeddings**: Sentence Transformers (`all-MiniLM-L6-v2`)
* **PDF Parsing**: PyMuPDF (`fitz`)

---

## 🗂️ Project Structure

```
genai_theme_chatbot/
├── backend/
│   ├── app/
│   │   ├── api/               # FastAPI routes (upload, query)
│   │   ├── core/              # (Reserved for settings/utilities)
│   │   ├── models/            # (Reserved for pydantic models or db schemas)
│   │   ├── services/          # Text extraction, FAISS logic, Gemini call
│   │   └── main.py            # FastAPI app entry point
│   ├── data/                  # Uploaded files + vector store
│   ├── .env                   # Gemini API key config
│   └── requirements.txt       # Backend dependencies
│
├── frontend/
│   └── app.py                 # Streamlit app
│
├── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/yourusername/genai_theme_chatbot.git
cd genai_theme_chatbot
```

### 🔹 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 🔹 3. Install Dependencies

```bash
pip install -r backend/requirements.txt
pip install streamlit
```

### 🔹 4. Add `.env` in `backend/`

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get the key from [Google MakerSuite](https://makersuite.google.com/app/apikey)

---

## 🚦 Running the Project

### 🔸 1. Start Backend (FastAPI)

```bash
cd backend
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Test it at: [http://localhost:8000/docs](http://localhost:8000/docs)

### 🔸 2. Start Frontend (Streamlit)

```bash
cd frontend
streamlit run app.py
```

Runs at: [http://localhost:8501](http://localhost:8501)

---

## 🧪 How It Works

1. Upload a document (PDF or image)
2. Text is extracted and embedded into vector space
3. FAISS stores vectors for fast semantic retrieval
4. Ask a question in plain English
5. Top-k relevant paragraphs are retrieved
6. Gemini Pro reads them and generates a natural answer with citations

---

## 🔍 Sample Questions for Testing

* "What are the powers of the President mentioned in this document?"
* "Who appoints the Prime Minister and what are the conditions?"
* "List the responsibilities of the Supreme Commander of the Armed Forces."

---

## 🛡️ Security & Limitations

* API key is stored via `.env` (never commit to GitHub)
* Gemini API usage may be rate-limited depending on plan
* FAISS index is local — no external storage or cloud vector DB used

---

## 📦 Future Improvements (optional)

* Add file list with history in sidebar
* Add chat-style history with session memory
* Deploy backend + frontend to Hugging Face or Streamlit Cloud
* Add support for multi-language documents

---

## 🧑‍💻 Developed By

**Akash Singh**
AI Engineer | Data Analyst | GenAI Enthusiast
Feel free to reach out or connect on LinkedIn https://www.linkedin.com/in/akash-singh234/

---

## 🏁 Final Note

This project showcases your ability to combine document processing, semantic search, and large language models into a full-stack real-world application. Perfect for internship, portfolio, or hiring demonstrations.

💡 Star this repo if you found it helpful!
