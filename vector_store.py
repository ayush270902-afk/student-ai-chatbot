
import numpy as np

DOCUMENTS = [
    "Python is a programming language",
    "Machine learning is a subset of AI",
    "Streamlit is used to build web apps",
    "RAG stands for Retrieval Augmented Generation"
]

DOC_EMBEDDINGS = []

def init_store(embed_fn):
    global DOC_EMBEDDINGS
    DOC_EMBEDDINGS = [embed_fn(doc) for doc in DOCUMENTS]

def search_docs(query_embedding, top_k=2):
    sims = []
    for emb in DOC_EMBEDDINGS:
        sim = np.dot(query_embedding, emb)
        sims.append(sim)

    top_indices = np.argsort(sims)[-top_k:]
    return [DOCUMENTS[i] for i in top_indices]
