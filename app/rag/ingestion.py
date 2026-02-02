import pdfplumber
from pathlib import Path



def extract_text_from_pdf(pdf_path: str):
    text_pages = {}
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"{pdf_path} n'existe pas.")

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            text_pages[i] = text if text else ""
    
    return text_pages
