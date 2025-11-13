import streamlit as st
from src.pipeline import build_pipeline

st.set_page_config(
    page_title="Curador Multiagente de Roadmaps Tech",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Curador Multiagente de Roadmaps Tech con RAG y Base Vectorial")
st.write(
    "Este asistente analiza documentos en la carpeta `data/` "
    "y genera un roadmap personalizado según tu objetivo y tiempo disponible."
)

objective = st.selectbox(
    "🎯 ¿Cuál es tu objetivo principal?",
    ["Frontend", "Backend", "DevOps", "Mobile"]
)

hours_per_week = st.slider(
    "⏱️ Horas de estudio por semana",
    min_value=5, max_value=30, value=10, step=1
)

months = st.slider(
    "📆 Duración del plan (meses)",
    min_value=1, max_value=12, value=6, step=1
)

if st.button("Generar roadmap"):
    with st.spinner("Generando tu roadmap con ayuda de los agentes..."):
        pipeline = build_pipeline()
        result = pipeline.invoke({
            "objective": objective,
            "hours_per_week": hours_per_week,
            "months": months
        })

        if isinstance(result, tuple):
            roadmap_text, used_docs = result
        else:
            roadmap_text, used_docs = str(result), []

        st.subheader("📚 Roadmap recomendado")
        st.text(roadmap_text)

        st.subheader("📂 Documentos utilizados")
        if used_docs:
            for d in used_docs:
                st.markdown(f"- `{d}`")
        else:
            st.write("No se identificaron documentos específicos o no hay data suficiente.")
