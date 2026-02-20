
import numpy as np
import hashlib

def embed_text(text: str) -> np.ndarray:
    """
    Lightweight deterministic embedding (cloud-safe)
    """
    h = hashlib.sha256(text.encode()).digest()
    return np.frombuffer(h, dtype=np.uint8).astype("float32")
