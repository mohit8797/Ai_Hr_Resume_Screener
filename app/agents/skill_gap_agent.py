# from app.agents.llm import get_llm
# from app.rag.retriever import get_relevant_docs
# from app.agents.response_parser import extract_text


# def analyze_skill_gap(vector_store, job_description: str):
#     llm = get_llm()

#     context_docs = get_relevant_docs(
#         vector_store,
#         query=job_description,
#         k=5
#     )

#     context = "\n".join([doc.page_content for doc in context_docs])

#     prompt = f"""
# You are an AI HR analyst.

# Job Description:
# {job_description}

# Candidate Resume Context:
# {context}

# Task:
# Identify missing or weak skills.

# Return ONLY JSON:
# {{
#   "missing_skills": [],
#   "suggestions": []
# }}
# """

#     response = llm.invoke(prompt)
#     return extract_text(response)


from app.rag.retriever import get_relevant_docs
from app.agents.llm import get_llm
from app.agents.response_parser import extract_text


def analyze_skill_gap(resume_text: str, job_description: str):
    llm = get_llm()

    context_docs = get_relevant_docs(resume_text)
    context = "\n".join([doc.page_content for doc in context_docs])

    prompt = f"""
You are an AI HR analyst.

Job Description:
{job_description}

Candidate Resume Context:
{context}

Task:
Identify missing or weak skills.

Return ONLY JSON:
{{
  "missing_skills": [],
  "suggestions": []
}}
"""

    response = llm.invoke(prompt)
    return extract_text(response)