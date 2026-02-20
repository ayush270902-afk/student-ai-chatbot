
# Student AI Chatbot (ChatGPT-like with Local LLaMA + RAG)

This project uses:
- Streamlit UI
- FAISS vector database
- Sentence-transformer embeddings
- Local LLaMA/Mistral model via llama-cpp-python

## Requirements
- Python 3.10 or 3.11 (MANDATORY)
- 8GB RAM minimum

## Setup
1. pip install -r requirements.txt
2. Download a GGUF model (see below)
3. streamlit run app.py

## Recommended Model
Mistral-7B-Instruct-GGUF (Q4):
https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF
