import os
import re
from typing import List, Dict
from pypdf import PdfReader
from ..config import DATA_DIR

def _clean_text(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def _extract_pdf(path: str) -> str:
    reader = PdfReader(path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return _clean_text(" ".join(pages))

def _extract_txt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return _clean_text(f.read())

def _infer_topic(filename: str) -> str:
    name = filename.lower()
    if "front" in name:
        return "Frontend"
    if "back" in name:
        return "Backend"
    if "devops" in name:
        return "DevOps"
    if "mobile" in name or "android" in name:
        return "Mobile"
    return "General"

def run_extractor() -> List[Dict]:
    """
    Lee PDF/TXT en data/ y devuelve lista de documentos:
    {id, filename, topic, content}
    """
    docs: List[Dict] = []

    if not os.path.exists(DATA_DIR):
        return docs

    for filename in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, filename)
        if not os.path.isfile(path):
            continue

        content = ""
        if filename.lower().endswith(".pdf"):
            content = _extract_pdf(path)
        elif filename.lower().endswith(".txt"):
            content = _extract_txt(path)

        content = content.strip()
        if not content:
            continue

        docs.append({
            "id": filename,
            "filename": filename,
            "topic": _infer_topic(filename),
            "content": content
        })

    return docs
