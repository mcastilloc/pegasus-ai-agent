# Pegasus AI Agent

Asistente conversacional RAG desplegado en Oracle Cloud Infrastructure.

## Arquitectura

PDFs
→ LangChain
→ Sentence Transformers
→ FAISS
→ Gemini
→ Streamlit

## Tecnologías

- Python 3.12
- LangChain
- Google Gemini
- FAISS
- Sentence Transformers
- Hugging Face
- Streamlit
- Oracle Cloud Infrastructure

## Instalación

git clone ...

cd pegasus-ai-agent

./setup.sh

## Variables de entorno .env

GOOGLE_API_KEY=...

## Generación del índice

python index_documents.py

## Ejecución

streamlit run app.py \
  --server.address 0.0.0.0 \
  --server.port 8501

## Despliegue OCI

- OCI Compute
- Ubuntu 24.04
- VM.Standard.E2.1.Micro
- Puerto TCP 8501

## Consideraciones

El índice FAISS debe generarse localmente y copiarse a OCI debido a las limitaciones de memoria de la instancia Always Free.