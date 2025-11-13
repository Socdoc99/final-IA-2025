from typing import List, Dict

def format_plan(plan: List[Dict], objective: str,
                hours_per_week: int, months: int) -> str:
    if not plan:
        return (
            "No se pudo generar un roadmap porque no hay contenido suficiente. "
            "Verifica que la carpeta 'data/' tenga PDFs o TXT con roadmaps."
        )

    lines: List[str] = []
    header = (
        f"🚀 Roadmap personalizado para {objective} en {months} meses, "
        f"estudiando ~{hours_per_week} horas por semana.\n\n"
        "Avanzarás de fundamentos a temas más avanzados de forma progresiva.\n\n"
    )
    lines.append(header)

    for block in plan:
        if block["start_week"] == block["end_week"]:
            week_label = f"Semana {block['start_week']}"
        else:
            week_label = f"Semanas {block['start_week']}–{block['end_week']}"

        docs_info = ", ".join(block["docs"]) if block["docs"] else "roadmaps base"
        lines.append(
            f"{week_label}: {block['topic']} "
            f"({block['hours_per_week']}h/semana). "
            f"Basado en: {docs_info}."
        )

    lines.append(
        "\n✅ Adapta este plan a tu ritmo.\n"
        "✅ Refuerza con proyectos pequeños y práctica constante.\n"
    )

    return "\n".join(lines)

def build_final_response(objective: str,
                         hours_per_week: int,
                         months: int,
                         plan: List[Dict]) -> str:
    return format_plan(plan, objective, hours_per_week, months)
