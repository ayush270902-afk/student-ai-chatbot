
import faiss
import numpy as np

documents = [
    "Newton's laws describe motion in physics",
    "Photosynthesis occurs in chloroplasts",
    "Machine learning learns patterns from data",
    "Data structures organize data efficiently"
]

vectors = np.random.rand(len(documents), 384).astype("float32")
index = faiss.IndexFlatL2(384)
index.add(vectors)

def search_docs(query_vec):
    D, I = index.search(np.array([query_vec]).astype("float32"), 2)
    return [documents[i] for i in I[0]]
