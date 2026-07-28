from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

def load_documents():
    documents = []

    pdf_dir = Path("data")

    for pdf in pdf_dir.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())

    return documents