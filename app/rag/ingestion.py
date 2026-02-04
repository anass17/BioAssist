from pathlib import Path
import pdfplumber
from typing import Dict, List, Any


def extract_pdf_content(pdf_path: str) -> List[Dict[str, Any]]:

    raw_blocks = []

    pdf_path = Path(pdf_path)

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):

            # -------- TEXT --------
            text = page.extract_text()
            if text:
                raw_blocks.append({
                    "type": "text",
                    "content": text,
                    "page": page_number,
                    "source": pdf_path.name
                })

            # -------- TABLES --------
            tables = page.extract_tables()
            for table_id, table in enumerate(tables):
                if not table or len(table) < 2:
                    continue

                raw_blocks.append({
                    "type": "table",
                    "content": table,
                    "page": page_number,
                    "table_id": table_id,
                    "source": pdf_path.name
                })

            # -------- IMAGES --------
            for image_id, _ in enumerate(page.images):
                raw_blocks.append({
                    "type": "image",
                    "content": None,
                    "page": page_number,
                    "image_id": image_id,
                    "source": pdf_path.name
                })

    return raw_blocks

data = extract_pdf_content('../../data/rag-data.pdf')

print(data[1]['content'])
