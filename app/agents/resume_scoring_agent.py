# from app.agents.llm import get_llm
# from app.rag.retriever import get_relevant_docs
# from app.agents.response_parser import extract_text


# def score_resume(vector_store, job_description: str):
#     llm = get_llm()

#     context_docs = get_relevant_docs(
#         vector_store,
#         query=job_description,
#         k=5
#     )

#     context = "\n".join([doc.page_content for doc in context_docs])

#     prompt = f"""
# You are an AI HR assistant.

# Job Description:
# {job_description}

# Resume Context:
# {context}

# Task:
# Score the candidate from 0 to 100 based on:
# - Skill match
# - Experience relevance
# - Project alignment

# Return ONLY JSON:
# {{
#   "score": number,
#   "reason": "short explanation"
# }}
# """

#     response = llm.invoke(prompt)
#     return extract_text(response)

from app.rag.retriever import get_relevant_docs
from app.agents.llm import get_llm
from app.agents.response_parser import extract_text


def score_resume(resume_text: str, job_description: str):
    llm = get_llm()

    # wrap single resume text into Document
    context_docs = get_relevant_docs(resume_text)
    context = "\n".join([doc.page_content for doc in context_docs])

    prompt = f"""
You are an AI HR assistant.

Job Description:
{job_description}

Resume Context:
{context}

Task:
Score the candidate from 0 to 100 based on:
- Skill match
- Experience relevance
- Project alignment

Return ONLY JSON:
{{
  "score": number,
  "reason": "short explanation"
}}
"""

    response = llm.invoke(prompt)
    return extract_text(response)