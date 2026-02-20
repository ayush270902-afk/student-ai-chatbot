
from embeddings import embed_text
from vector_store import search_docs
from llm import generate


def answer_query(query: str) -> str:
    # Get embedding
    query_embedding = embed_text(query)

    # Search documents
    docs = search_docs(query_embedding)

    # Safety check
    if not docs:
        context = "No relevant context found."
    else:
        context = "\n".join([str(doc) for doc in docs])

    prompt = f"""
You are a helpful student assistant.
Use the context below to answer the question clearly and concisely.

Context:
{context}

Question:
{query}

Answer:
"""

    return generate(prompt)
