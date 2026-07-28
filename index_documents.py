from src.loader import load_documents
from src.chunker import split_documents
from src.vectorstore import build_vectorstore

docs = load_documents()

chunks = split_documents(docs)

build_vectorstore(chunks)

print("Índice FAISS creado correctamente.")