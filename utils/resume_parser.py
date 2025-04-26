
import docx2txt
import os

def extract_resume_text(file_path):
    if file_path.endswith('.docx'):
        return docx2txt.process(file_path)
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif file_path.endswith('.pdf'):
        import PyPDF2
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    else:
        raise ValueError("Unsupported file format. Use .pdf, .docx, or .txt")

if __name__ == '__main__':
    test_path = '../data/sample_resume.pdf'
    if os.path.exists(test_path):
        print(extract_resume_text(test_path))
    else:
        print("Sample resume not found.")
