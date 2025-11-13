# Curador Multiagente de Roadmaps Tech con RAG y Base Vectorial

Proyecto académico que implementa un asistente inteligente para generar roadmaps de estudio personalizados
(Frontend, Backend, DevOps, Mobile) usando:

- Extracción de PDFs/TXT desde `data/`
- Chunking (80-150 palabras)
- Embeddings con `sentence-transformers/all-MiniLM-L6-v2`
- Base vectorial en memoria con FAISS
- Búsqueda por similitud (coseno)
- Arquitectura multiagente (extractor, chunking, indexación, consulta, planificación, respuesta, guardrails)
- Interfaz en Streamlit

## Cómo usar

1. Crear entorno e instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Agregar documentos PDF/TXT con roadmaps a la carpeta `data/`.

3. Ejecutar la aplicación:

```bash
streamlit run app.py
```

Luego abre el enlace local que te da Streamlit y genera tu roadmap personalizado.
