import os
import pdfplumber
import docx
from fastapi import UploadFile
from typing import Optional

def extract_text_from_file(file: UploadFile) -> Optional[str]:
    filename = file.filename.lower()
    
    if filename.endswith(".txt"):
        return file.file.read().decode("utf-8")
    
    elif filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    
    elif filename.endswith(".docx"):
        doc = docx.Document(file.file)
        return "\n".join([para.text for para in doc.paragraphs])
    
    else:
        raise ValueError("Unsupported file format. Please upload a .txt, .pdf, or .docx file.")