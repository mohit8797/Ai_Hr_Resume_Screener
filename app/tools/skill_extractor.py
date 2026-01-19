COMMON_SKILLS = [
    "python", "java", "c++", "sql", "machine learning", "deep learning",
    "nlp", "langchain", "fastapi", "flask", "docker", "aws",
    "data analysis", "pandas", "numpy", "tensorflow", "pytorch",
    "git", "github", "linux"
]

def extract_skills(text: str) -> list:
    """
    Extract skills from resume text
    """
    extracted = []

    for skill in COMMON_SKILLS:
        if skill.lower() in text:
            extracted.append(skill)

    return list(set(extracted))