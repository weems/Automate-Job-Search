
import spacy
from collections import Counter
import re

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, top_n=20):
    doc = nlp(text.lower())
    keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    most_common = Counter(keywords).most_common(top_n)
    return [word for word, freq in most_common]

def match_resume_to_job(resume_text, job_description):
    resume_keywords = set(extract_keywords(resume_text))
    job_keywords = set(extract_keywords(job_description))
    common = resume_keywords & job_keywords
    score = len(common) / len(job_keywords) if job_keywords else 0
    return {
        "match_score": round(score * 100, 2),
        "common_keywords": list(common)
    }

if __name__ == "__main__":
    sample_resume = "Experienced QA Engineer with Python, CI/CD, Jenkins, and manual testing skills."
    sample_job = "Looking for a QA Lead experienced with test automation, CI/CD, and scripting in Python."
    match = match_resume_to_job(sample_resume, sample_job)
    print(match)
