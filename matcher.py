from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_match_score(resume_text: str, job_description: str) -> float:
    """
    Compute TF-IDF cosine similarity between resume and job description.
    Returns a score from 0 to 100.
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(float(score) * 100, 1)


def find_skill_gaps(resume_skills: list[str], job_skills: list[str]) -> dict:
    """
    Compare resume skills vs job required skills.
    Returns matched skills and missing (gap) skills.
    """
    resume_set = set(s.lower().strip() for s in resume_skills)
    job_set    = set(s.lower().strip() for s in job_skills)

    return {
        "matched": sorted(list(resume_set & job_set)),
        "missing": sorted(list(job_set - resume_set)),
    }
