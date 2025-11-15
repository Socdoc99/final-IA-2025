# Curador Multiagente de Roadmaps Tech con RAG y Base Vectorial

*Sistema Inteligente para Generación de Rutas de Aprendizaje
Personalizadas*

Este proyecto académico implementa un **asistente inteligente
multiagente** capaz de generar **roadmaps de estudio personalizados**
(Frontend, Backend, DevOps, Mobile o cualquier área técnica) utilizando
**procesamiento de documentos, embeddings, recuperación semántica
(RAG)** y una interfaz ligera en **Streamlit**.

El sistema integra componentes modernos de IA:

-   Extracción y procesamiento de PDFs/TXT desde `data/`
-   Chunking optimizado (80--150 palabras)
-   Embeddings con `sentence-transformers/all-MiniLM-L6-v2`
-   Base vectorial en memoria con **FAISS**
-   Recuperación semántica vía similitud coseno
-   Arquitectura **multiagente**:
    -   Extractor
    -   Chunker
    -   Indexador vectorial
    -   Recuperador RAG
    -   Planificador de roadmap
    -   Redactor final
    -   Guardrails para control de calidad
-   Interfaz de usuario construida en **Streamlit**

## 🧠 ¿Qué hace este sistema?

1.  Lee documentos técnicos almacenados en `data/`.
2.  Fragmenta el contenido en chunks semánticamente coherentes.
3.  Genera embeddings vectoriales con modelos eficientes.
4.  Indexa todo en una base vectorial FAISS.
5.  Utiliza recuperación semántica (RAG) para extraer información
    relevante según el objetivo del usuario.
6.  Los agentes colaboran para:
    -   analizar inputs del usuario,
    -   buscar contenido relevante,
    -   organizar temas según su tiempo disponible,
    -   redactar un roadmap claro, secuencial y comprensible.
7.  Streamlit muestra el roadmap final listo para usar.

## 📦 Requisitos Previos

-   Python 3.10 o superior\
-   pip actualizado\
-   Modelos de `sentence-transformers` descargables desde HuggingFace

## ⚙️ Instalación y Uso

### 1. Instalar dependencias

``` bash
pip install -r requirements.txt
```

### 2. Añadir documentos técnicos

Agrega archivos **PDF o TXT** dentro de la carpeta:

    data/

### 3. Ejecutar la aplicación

``` bash
streamlit run app.py
```

Accede desde:

    http://localhost:8501

## 🧩 Arquitectura Técnica

    data/ → Agente Extractor → Chunking → Embeddings → FAISS → Agente RAG
           → Agente Planificador → Agente Redactor → Roadmap Final

### Componentes Clave

-   **Extractor:** lee y normaliza documentos.
-   **Chunker:** fragmenta en 80-150 palabras.
-   **Indexador (FAISS):** almacena embeddings.
-   **Agente RAG:** recupera información relevante.
-   **Planificador:** estructura el roadmap según tiempo y objetivos.
-   **Redactor:** genera el documento final coherente.
-   **Guardrails:** validan calidad y formato.

## 📚 Tecnologías Utilizadas

-   Python 3.10+\
-   Streamlit\
-   LangChain / LangGraph\
-   Sentence-Transformers\
-   FAISS\
-   PyPDF2 / Unstructured

## 📈 Resultados Obtenidos

-   Roadmaps personalizados según objetivos reales.\
-   Uso eficiente de RAG + Multiagentes.\
-   Integración fluida entre embeddings, chunking y búsqueda vectorial.\
-   Interfaz simple para demostrar un flujo complejo de IA.



## 👤 Autor
Claudia Castaño Mendoza,

Juan José Restrepo Londoño,

Santiago Ospina

Universidad Tecnológica de Pereira\
Curso: Introducción a la Inteligencia Artificial

## 📄 Licencia

Proyecto disponible para uso académico y educativo.
