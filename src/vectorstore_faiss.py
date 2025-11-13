import faiss
import numpy as np
from typing import List, Dict

class FaissVectorStore:
    """
    Base vectorial simple en memoria con FAISS,
    usando IndexFlatIP + embeddings normalizados (similitud de coseno).
    """
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatIP(dim)
        self.embeddings = None
        self.texts: List[str] = []
        self.metadatas: List[Dict] = []

    def add(self, vectors: np.ndarray, metadatas: List[Dict], texts: List[str]):
        vectors = vectors.astype("float32")
        if self.embeddings is None:
            self.embeddings = vectors
        else:
            self.embeddings = np.vstack([self.embeddings, vectors])

        self.index.add(vectors)
        self.metadatas.extend(metadatas)
        self.texts.extend(texts)

    def search(self, query_vector: np.ndarray, top_k: int = 10) -> List[Dict]:
        query_vector = query_vector.astype("float32")
        D, I = self.index.search(query_vector, top_k)
        results: List[Dict] = []
        for score, idx in zip(D[0], I[0]):
            if idx == -1:
                continue
            results.append({
                "score": float(score),
                "text": self.texts[idx],
                "metadata": self.metadatas[idx]
            })
        return results
