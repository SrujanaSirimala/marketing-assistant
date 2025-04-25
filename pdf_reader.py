from pypdf import PdfReader

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    all_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            all_text += text + "\n"
    return all_text
