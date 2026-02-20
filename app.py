
import streamlit as st
from rag import answer_query
from vector_store import init_store
from embeddings import embed_text

init_store(embed_text)

st.title("Student AI Chatbot")

query = st.text_input("Ask a question")

if query:
    with st.spinner("Thinking..."):
        st.write(answer_query(query))
