from typing import Tuple, List
from langchain_core.runnables import RunnableLambda
from .agents.extractor_agent import run_extractor
from .agents.chunking_agent import run_chunking
from .agents.indexing_agent import run_indexing
from .agents.query_agent import run_query
from .agents.planner_agent import run_planner
from .agents.response_agent import build_final_response
from .agents.guardrails_agent import is_valid_query

def build_pipeline():
    def pipeline_fn(objective: str, hours_per_week: int, months: int) -> Tuple[str, List[str]]:
        if not is_valid_query(objective):
            return (
                "⚠️ Solo puedo ayudarte con roadmaps de aprendizaje en tecnología "
                "(Frontend, Backend, DevOps, Mobile, etc.). Ajusta tu objetivo.",
                []
            )

        docs = run_extractor()
        if not docs:
            return (
                "No se encontraron documentos en la carpeta 'data/'. "
                "Agrega PDFs o TXT con roadmaps para poder generar el plan.",
                []
            )

        chunks = run_chunking(docs)
        vs, model = run_indexing(chunks)
        retrieved = run_query(vs, model, objective, hours_per_week, months)
        plan = run_planner(objective, retrieved, hours_per_week, months)
        final_text = build_final_response(objective, hours_per_week, months, plan)

        used_docs = sorted(set(r["metadata"]["doc_id"] for r in retrieved)) if retrieved else []
        return final_text, used_docs

    return RunnableLambda(lambda inputs: pipeline_fn(
        inputs["objective"],
        inputs["hours_per_week"],
        inputs["months"]
    ))
