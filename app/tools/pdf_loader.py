from pypdf import PdfReader

def load_pdf_text(file_path: str) -> str:
    """
    Extract text from a PDF resume
    """
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    return text