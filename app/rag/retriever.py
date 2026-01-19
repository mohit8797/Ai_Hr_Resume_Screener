# def get_relevant_docs(vector_store, query: str, k: int = 5):
#     retriever = vector_store.as_retriever(
#         search_kwargs={"k": k}
#     )

#     return retriever.invoke(query)

# app/rag/retriever.py

from langchain_core.documents import Document

def get_relevant_docs(resume_text: str):
    """
    Accepts a single resume string and returns a Document object
    compatible with agent workflow.
    """
    return [Document(page_content=resume_text)]