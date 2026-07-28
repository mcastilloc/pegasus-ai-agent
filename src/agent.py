import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest"
)

while True:

    question = input("\nPregunta: ")

    if question.lower() == "salir":
        break

    docs = retriever.invoke(question)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Responde únicamente usando la información del contexto.

Contexto:
{context}

Pregunta:
{question}
"""

    response = llm.invoke(prompt)

    print("\nRespuesta:")
    print(response.text)
