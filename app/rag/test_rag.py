from app.tools.pdf_loader import load_pdf_text
from app.tools.text_cleaner import clean_text
from app.rag.vector_store import create_vector_store
from app.rag.retriever import get_relevant_docs

# Load Resume
resume_text = load_pdf_text("data/resumes/sample_resume.pdf")
resume_text = clean_text(resume_text)

# Create Vector Store
vector_store = create_vector_store([resume_text])

# Query like HR
query = "experience with machine learning and deep learning"

docs = get_relevant_docs(vector_store, query)

print("\nRetrieved Chunks:\n")
for doc in docs:
    print(doc.page_content)
    print("-" * 80)