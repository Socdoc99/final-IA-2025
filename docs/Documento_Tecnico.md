# Documento Técnico -- Proyecto Final Introducción a IA

### Curador Multiagente de Roadmaps Tech con RAG y Base Vectorial

## 1. Introducción

Este proyecto desarrolla un asistente inteligente multiagente capaz de
analizar documentos técnicos almacenados en la carpeta `data/`,
procesarlos mediante extracción, chunking, embeddings y recuperación
semántica (RAG), y generar un roadmap personalizado según los objetivos
del usuario. La solución integra LangChain, LangGraph, bases vectoriales
y Streamlit.

## 2. Problema a Resolver

Las rutas de aprendizaje suelen ser genéricas y no se adaptan al perfil,
objetivos ni disponibilidad del estudiante. Este proyecto busca
automatizar la curaduría de contenido técnico para producir roadmaps
personalizados basados en información real y organizada.

## 3. Metodología

### 3.1 Extracción

Lectura y normalización de documentos ubicados en `data/`.

### 3.2 Chunking

División del contenido usando `RecursiveCharacterTextSplitter`.

### 3.3 Embeddings

Conversión de los chunks en vectores utilizando modelos compatibles con
LangChain.

### 3.4 Base Vectorial

Indexación y almacenamiento mediante FAISS.

### 3.5 Recuperación Semántica (RAG)

Búsqueda contextualizada según el objetivo del usuario.

### 3.6 Pipeline Multiagente

Agentes:\
- Analizador\
- Recuperación\
- Curador\
- Redactor

### 3.7 Interfaz

Desarrollada en Streamlit. Permite seleccionar objetivo, horas semanales
y duración del plan.

## 4. Arquitectura de Agentes

### Agente Analizador

Interpreta inputs y define necesidades.

### Agente Recuperación

Consulta la base vectorial y obtiene contenido relevante.

### Agente Curador

Ordena y estructura los temas según tiempo disponible.

### Agente Redactor

Genera el roadmap final a partir de la información procesada.

### Flujo Completo

Usuario → Streamlit → Analizador → Recuperación → Curador → Redactor →
Roadmap Final

## 5. Resultados y Conclusiones

El sistema procesa documentos reales, genera roadmaps personalizados y
demuestra la eficacia de integrar agentes, RAG, embeddings y Streamlit.

## 6. Trabajo Futuro

-   Modelos de embeddings más robustos\
-   Nuevos agentes (evaluador, sintetizador, planificador semanal)\
-   Integración con API\
-   Fuentes de conocimiento externas\
-   Persistencia en base de datos
