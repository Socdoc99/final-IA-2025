from typing import List, Dict
from ..config import TOP_K
from .indexing_agent import _normalize

def build_query(objective: str, hours_per_week: int, months: int) -> str:
    return (
        f"Objetivo: {objective}. "
        f"Disponibilidad: {hours_per_week} horas por semana durante {months} meses. "
        "Generar roadmap de estudio técnico paso a paso."
    )

def run_query(vectorstore, model, objective: str,
              hours_per_week: int, months: int,
              top_k: int = TOP_K) -> List[Dict]:
    query_text = build_query(objective, hours_per_week, months)
    q_emb = model.encode([query_text], convert_to_numpy=True)
    q_emb = _normalize(q_emb)
    results = vectorstore.search(q_emb, top_k=top_k)
    return results
