from typing import List, Dict, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer
from ..config import EMBEDDING_MODEL_NAME
from ..vectorstore_faiss import FaissVectorStore

_model = None

def get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    return _model

def _normalize(vecs: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-10
    return vecs / norms

def run_indexing(chunks: List[Dict]) -> Tuple[FaissVectorStore, SentenceTransformer]:
    if not chunks:
        raise ValueError("No hay chunks para indexar. Verifica que existan documentos en data/.")

    model = get_model()
    texts = [c["text"] for c in chunks]
    metadatas = [c["metadata"] for c in chunks]

    embeddings = model.encode(texts, convert_to_numpy=True)
    embeddings = _normalize(embeddings)
    dim = embeddings.shape[1]

    vs = FaissVectorStore(dim)
    vs.add(embeddings, metadatas, texts)
    return vs, model
