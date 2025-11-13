from typing import List, Dict
from ..config import MIN_CHUNK_WORDS, MAX_CHUNK_WORDS

def chunk_text(text: str, doc_id: str, topic: str) -> List[Dict]:
    words = text.split()
    chunks: List[Dict] = []
    i = 0
    chunk_id = 0

    while i < len(words):
        end = min(i + MAX_CHUNK_WORDS, len(words))
        fragment = " ".join(words[i:end])

        if len(fragment.split()) >= MIN_CHUNK_WORDS:
            chunks.append({
                "text": fragment,
                "metadata": {
                    "doc_id": doc_id,
                    "topic": topic,
                    "chunk_id": chunk_id
                }
            })
            chunk_id += 1

        i = end

    return chunks

def run_chunking(docs: List[Dict]) -> List[Dict]:
    all_chunks: List[Dict] = []
    for doc in docs:
        all_chunks.extend(chunk_text(doc["content"], doc["id"], doc["topic"]))
    return all_chunks
