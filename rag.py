
from embeddings import embed_text
from vector_store import search_docs
from llm import generate

def answer_query(query):
    docs = search_docs(embed_text(query))
    context = "\n".join(docs)

    prompt = f"""You are a helpful student assistant.
Use the context below to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

    return generate(prompt)
