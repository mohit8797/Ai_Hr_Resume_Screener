from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.embeddings import get_embeddings

def create_vector_store(texts: list):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.create_documents(texts)

    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)

    return vector_store