import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

st.title("Pegasus AI Agent")
st.caption("Asistente corporativo para documentación interna")

@st.cache_resource
def load_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

    return FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

db = load_vectorstore()

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest"
)

question = st.text_input(
    "Haz una pregunta sobre la documentación"
)

if question:

    docs = retriever.invoke(question)

    context = "\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
Responde únicamente utilizando la información del contexto.

Si la respuesta no está en el contexto responde:
'No encontré información sobre eso en la documentación disponible.'

Contexto:
{context}

Pregunta:
{question}
"""

    with st.spinner("Consultando documentación..."):
        response = llm.invoke(prompt)

    st.subheader("Respuesta")
    st.write(response.text)