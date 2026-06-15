import io
import spacy
from pdfminer.high_level import extract_text

# Load spaCy model - run: python -m spacy download en_core_web_md
nlp = spacy.load("en_core_web_md")

# ──────────────────────────────────────────────
# Master skill keyword list - add more freely!
# ──────────────────────────────────────────────
SKILL_KEYWORDS = {
    # Programming languages
    "python", "java", "javascript", "typescript", "c++", "c#", "r", "scala", "go", "rust",
    # ML / DL frameworks
    "tensorflow", "pytorch", "keras", "scikit-learn", "xgboost", "lightgbm", "catboost",
    "huggingface", "transformers", "opencv", "nltk", "spacy",
    # Data & databases
    "sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch",
    "pandas", "numpy", "matplotlib", "seaborn", "plotly",
    # MLOps / DevOps
    "docker", "kubernetes", "mlflow", "airflow", "prefect", "dvc",
    "terraform", "ansible", "jenkins", "github actions",
    # Cloud
    "aws", "gcp", "azure", "ec2", "s3", "lambda", "bigquery",
    # Web / API
    "fastapi", "flask", "django", "react", "nextjs", "nodejs",
    # Big data
    "spark", "hadoop", "kafka", "hive", "dbt",
    # Other
    "git", "linux", "rest api", "graphql", "microservices",
    "machine learning", "deep learning", "nlp", "computer vision",
    "data analysis", "data visualization", "feature engineering",
}


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract raw text from uploaded PDF bytes."""
    return extract_text(io.BytesIO(file_bytes))


def extract_skills(text: str) -> list[str]:
    """
    Use spaCy to tokenize the resume and match against SKILL_KEYWORDS.
    Also checks noun chunks for multi-word skills like 'machine learning'.
    """
    doc = nlp(text.lower())
    found = set()

    # Single-token skill matching
    for token in doc:
        clean = token.text.strip()
        if clean in SKILL_KEYWORDS:
            found.add(clean)

    # Multi-word noun chunk matching (e.g. "machine learning", "rest api")
    for chunk in doc.noun_chunks:
        clean = chunk.text.strip()
        if clean in SKILL_KEYWORDS:
            found.add(clean)

    return sorted(list(found))
