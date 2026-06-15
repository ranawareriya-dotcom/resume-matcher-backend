from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from parser import extract_text_from_pdf, extract_skills
from matcher import compute_match_score, find_skill_gaps
from jobs_data import JOBS

# ─────────────────────────────────────────────
# App setup
# ─────────────────────────────────────────────
app = FastAPI(
    title="Resume Analyser API",
    description="Upload a resume PDF, get matched jobs and skill gap analysis",
    version="1.0.0",
)

# Allow React dev server to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─────────────────────────────────────────────
# Route: Health check
# ─────────────────────────────────────────────
@app.get("/")
def root():
    return {"status": "Resume Analyser API is running ✅"}


# ─────────────────────────────────────────────
# Route: Analyse resume PDF
# ─────────────────────────────────────────────
@app.post("/analyse")
async def analyse_resume(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")

    # Read PDF bytes
    content = await file.read()

    # Step 1: Extract raw text from PDF
    resume_text = extract_text_from_pdf(content)

    if not resume_text.strip():
        raise HTTPException(status_code=400, detail="Could not extract text from PDF. Try a text-based PDF.")

    # Step 2: Extract skills using spaCy NLP
    resume_skills = extract_skills(resume_text)

    # Step 3: Score against each job
    results = []
    for job in JOBS:
        score = compute_match_score(resume_text, job["description"])
        gaps  = find_skill_gaps(resume_skills, job["skills"])

        results.append({
            "job_id":   job["id"],
            "title":    job["title"],
            "company":  job["company"],
            "location": job["location"],
            "salary":   job["salary"],
            "score":    score,
            "matched":  gaps["matched"],
            "missing":  gaps["missing"],
        })

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)

    # Step 4: Collect all unique missing skills across top 3 matches
    all_gaps = {}
    for job in results[:3]:
        for skill in job["missing"]:
            if skill not in all_gaps:
                all_gaps[skill] = 0
            all_gaps[skill] += 1

    # Sort gaps by frequency (most in-demand gaps first)
    priority_gaps = sorted(all_gaps.items(), key=lambda x: x[1], reverse=True)

    return {
        "resume_skills": resume_skills,
        "total_skills":  len(resume_skills),
        "matches":       results,
        "priority_gaps": [{"skill": g[0], "frequency": g[1]} for g in priority_gaps],
    }


# ─────────────────────────────────────────────
# Route: List all available jobs
# ─────────────────────────────────────────────
@app.get("/jobs")
def list_jobs():
    return {"jobs": JOBS}
