# frontend/app.py

import streamlit as st
import requests

st.set_page_config(page_title="GenAI Theme Chatbot", layout="wide")

st.title("📄 GenAI Theme Chatbot")
st.write("Upload documents and ask intelligent questions — powered by Gemini + FAISS")

# BACKEND API URL
API_URL = "http://localhost:8000"

# File Upload
st.subheader("📤 Upload a PDF or image document")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    with st.spinner("Uploading and processing..."):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post(f"{API_URL}/api/upload", files=files)
        if response.status_code == 200:
            st.success("✅ File uploaded and indexed in FAISS!")
        else:
            st.error(f"❌ Upload failed: {response.json()['detail']}")

# Ask Question
st.subheader("💬 Ask a Question About the Documents")

query = st.text_input("Enter your question here")

if st.button("Get Answer"):
    if not query:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(f"{API_URL}/api/query", json={"question": query, "top_k": 3})
            if response.status_code == 200:
                result = response.json()
                st.markdown("### 🤖 Gemini’s Answer")
                st.success(result["response"])

                st.markdown("### 📚 Cited Paragraphs")
                for chunk in result["matched_chunks"]:
                    st.markdown(f"**📄 {chunk['doc_id']}** — Page {chunk['page']}, Para {chunk['paragraph']}")
                    st.write(chunk['text'])
                    st.markdown("---")
            else:
                st.error(f"❌ Query failed: {response.json()['detail']}")
