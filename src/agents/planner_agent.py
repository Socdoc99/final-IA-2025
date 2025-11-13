from typing import List, Dict

BASE_TOPICS = {
    "Frontend": [
        "Fundamentos de programación",
        "HTML y CSS",
        "JavaScript",
        "Git y control de versiones",
        "Consumo de APIs REST",
        "Framework frontend (React/Angular/Vue)",
        "Buenas prácticas y despliegue"
    ],
    "Backend": [
        "Fundamentos de programación",
        "Git y control de versiones",
        "HTTP y APIs REST",
        "Lenguaje backend (Node/Python/Java/etc.)",
        "Bases de datos SQL/NoSQL",
        "Autenticación y seguridad básica",
        "Despliegue y buenas prácticas"
    ],
    "DevOps": [
        "Linux y terminal",
        "Git",
        "Redes básicas",
        "Docker y contenedores",
        "CI/CD",
        "Cloud (AWS/Azure/GCP) fundamentos",
        "Monitoreo y observabilidad"
    ],
    "Mobile": [
        "Fundamentos de programación",
        "Git",
        "Fundamentos de diseño móvil",
        "Framework móvil (React Native/Flutter)",
        "Consumo de APIs",
        "Almacenamiento local/remoto",
        "Publicación básica de apps"
    ],
}

def run_planner(objective: str,
                retrieved_chunks: List[Dict],
                hours_per_week: int,
                months: int) -> List[Dict]:
    total_weeks = max(1, months * 4)
    topics = BASE_TOPICS.get(objective, BASE_TOPICS["Frontend"])
    weeks_per_topic = max(1, total_weeks // len(topics))

    plan: List[Dict] = []
    current_week = 1

    for topic in topics:
        if current_week > total_weeks:
            break

        end_week = min(total_weeks, current_week + weeks_per_topic - 1)

        related_docs = [
            r["metadata"]["doc_id"]
            for r in retrieved_chunks
            if topic.split()[0].lower() in r["text"].lower()
        ]
        related_docs = sorted(set(related_docs))[:3]

        plan.append({
            "start_week": current_week,
            "end_week": end_week,
            "topic": topic,
            "hours_per_week": hours_per_week,
            "docs": related_docs
        })

        current_week = end_week + 1

    return plan
