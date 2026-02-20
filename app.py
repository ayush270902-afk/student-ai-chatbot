
import streamlit as st
from rag import answer_query
from vector_store import init_store
from embeddings import embed_text

st.title("Student AI Chatbot")

# Move init_store inside safe block
if "initialized" not in st.session_state:
    try:
        init_store(embed_text)
        st.session_state.initialized = True
    except Exception as e:
        st.error(f"Initialization error: {e}")

query = st.text_input("Ask a question")

if query:
    try:
        with st.spinner("Thinking..."):
            st.write(answer_query(query))
    except Exception as e:
        st.error(f"Error: {e}")
