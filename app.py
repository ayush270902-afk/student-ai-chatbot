
import streamlit as st
from rag import answer_query

st.set_page_config(page_title="Student AI Chatbot")
st.title("🎓 Student AI Chatbot (Local LLaMA)")

query = st.text_input("Ask a student-related question")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        response = answer_query(query)
    st.write(response)
