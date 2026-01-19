import os
from pdf_loader import load_pdf_text
from text_cleaner import clean_text
from skill_extractor import extract_skills

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
resume_path = os.path.join(BASE_DIR, "data/resumes/sample_resume.pdf")

if not os.path.exists(resume_path):
    raise FileNotFoundError(f"Resume not found at {resume_path}")

raw_text = load_pdf_text(resume_path)
cleaned_text = clean_text(raw_text)
skills = extract_skills(cleaned_text)

print("Extracted Skills:", skills)