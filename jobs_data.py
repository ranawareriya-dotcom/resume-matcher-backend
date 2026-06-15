# ─────────────────────────────────────────────────────────────────────────────
# Sample job database.
# In production: replace this with a PostgreSQL/SQLite query or a live scraper.
# ─────────────────────────────────────────────────────────────────────────────

JOBS = [
    {
        "id": 1,
        "title": "ML Engineer",
        "company": "Infosys AI Labs",
        "location": "Bengaluru",
        "description": (
            "We are looking for a Python developer with strong TensorFlow and PyTorch skills. "
            "Experience with Docker, Kubernetes, and MLflow for model deployment is required. "
            "Knowledge of REST APIs, FastAPI, and CI/CD pipelines is a plus. "
            "Must have hands-on experience with scikit-learn and data pipelines."
        ),
        "skills": ["python", "tensorflow", "pytorch", "docker", "kubernetes", "mlflow", "fastapi", "scikit-learn"],
        "salary": "12–20 LPA",
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "company": "Flipkart",
        "location": "Bengaluru",
        "description": (
            "Seeking a data scientist proficient in Python, SQL, and Apache Spark. "
            "Experience with PyTorch and pandas for building recommendation systems. "
            "Should know A/B testing, feature engineering, and data visualization using matplotlib or plotly. "
            "Knowledge of Airflow for scheduling pipelines is beneficial."
        ),
        "skills": ["python", "sql", "spark", "pytorch", "pandas", "matplotlib", "airflow", "feature engineering"],
        "salary": "10–18 LPA",
    },
    {
        "id": 3,
        "title": "AI / NLP Engineer",
        "company": "Sarvam AI",
        "location": "Remote",
        "description": (
            "Join our NLP team to build large-scale language models. "
            "Strong experience with HuggingFace transformers, PyTorch, and spacy required. "
            "Deep learning, NLTK, and text preprocessing skills needed. "
            "Python and Git are mandatory. Knowledge of REST API and FastAPI preferred."
        ),
        "skills": ["python", "pytorch", "huggingface", "transformers", "spacy", "nltk", "deep learning", "nlp", "fastapi", "git"],
        "salary": "15–25 LPA",
    },
    {
        "id": 4,
        "title": "Full-stack AI Developer",
        "company": "Zepto Tech",
        "location": "Mumbai",
        "description": (
            "Build AI-powered features using React frontend and Python backend. "
            "Experience with FastAPI, PostgreSQL, Docker, and Redis is required. "
            "Must know TypeScript and REST APIs. Machine learning integration with scikit-learn or tensorflow is a plus."
        ),
        "skills": ["react", "python", "fastapi", "postgresql", "docker", "redis", "typescript", "rest api", "scikit-learn"],
        "salary": "8–15 LPA",
    },
    {
        "id": 5,
        "title": "Data Engineer",
        "company": "Razorpay",
        "location": "Bengaluru",
        "description": (
            "Design and build scalable data pipelines using Apache Spark and Kafka. "
            "Strong SQL, Python, and DBT skills required. "
            "Experience with AWS (S3, Lambda, EC2) and Airflow scheduling. "
            "Knowledge of Terraform and Docker for infrastructure management."
        ),
        "skills": ["python", "sql", "spark", "kafka", "dbt", "aws", "airflow", "terraform", "docker"],
        "salary": "12–22 LPA",
    },
    {
        "id": 6,
        "title": "Computer Vision Engineer",
        "company": "Juspay",
        "location": "Bengaluru",
        "description": (
            "Work on real-time computer vision systems using OpenCV and TensorFlow. "
            "Deep learning experience with CNNs and PyTorch is required. "
            "Must know Python and Docker. Experience with REST APIs and FastAPI deployment preferred. "
            "MLflow for experiment tracking is a plus."
        ),
        "skills": ["python", "opencv", "tensorflow", "pytorch", "deep learning", "computer vision", "docker", "fastapi", "mlflow"],
        "salary": "10–20 LPA",
    },
]
