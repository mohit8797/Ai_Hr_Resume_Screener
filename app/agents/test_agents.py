from app.tools.pdf_loader import load_pdf_text
from app.tools.text_cleaner import clean_text
from app.rag.vector_store import create_vector_store
from app.agents.resume_scoring_agent import score_resume
from app.agents.skill_gap_agent import analyze_skill_gap
from app.agents.interview_agent import generate_interview_questions

resume_text = clean_text(load_pdf_text("data/resumes/sample_resume.pdf"))
vector_store = create_vector_store([resume_text])

job_description = """
Looking for a Machine Learning Engineer with experience in Python,
Deep Learning, TensorFlow, and deployment using Flask or FastAPI.
"""

print("Resume Score:\n", score_resume(vector_store, job_description))
print("\nSkill Gap:\n", analyze_skill_gap(vector_store, job_description))
print("\nInterview Questions:\n", generate_interview_questions(vector_store, job_description))