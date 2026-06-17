# README.md for Resume-Matcher-Backend

# Resume Matcher & Skill Gap Analyzer - Backend

A FastAPI-powered backend that processes resumes, extracts skills, performs job matching, and identifies skill gaps.

The system helps candidates evaluate their resumes against predefined job requirements and receive personalized recommendations.

## Features

- Resume Upload API
- PDF Parsing
- Skill Extraction
- Job Matching Algorithm
- Skill Gap Detection
- Compatibility Score Calculation
- REST API Architecture
- Cloud Deployment Ready

## Tech Stack

- Python
- FastAPI
- Uvicorn
- PyPDF2
- Joblib
- Pandas
- NumPy
- Scikit-Learn
<br>
## Project Structure
<br>
backend/
<br>
│
<br>
├── main.py
<br>
├── parser.py
<br>
├── matcher.py
<br>
├── jobs_data.py
<br>
├── requirements.txt
<br>
└── Procfile
<br>

<br><br>
## API Endpoints
<br><br>
### Health Check
<br><br>
http
<br><br>
GET /

{
  "status": "Resume Analyser API is running ✅"
}

**Analyze Resume
<br><br>
POST /analyse

**Input:
<br><br>
file: resume.pdf
<br><br>
**Response Example:

{
<br>
  "resume_skills": [
  <br>
    "Python",
    <br>
    "SQL",
    <br>
    "Machine Learning"
    <br>
  ],
  <br>
  "matches": [
  <br>
    {
    <br>
      "job": "Data Analyst",
      <br>
      "score": 85
      <br>
    }
    <br>
  ],
  <br>
  "priority_gaps": [
  <br>
    "Power BI",
    <br>
    "Tableau"
    <br>
  ]
  <br>
}
<br>
<br><br>
**Get Available Jobs**
<br>
GET /jobs

Returns all predefined job profiles.

**Working Flow**
<br>
-User uploads PDF resume.
<br>
-Backend receives file.
<br>
-Resume text is extracted.
<br>
-Skills are identified.
<br>
-Skills are compared with job profiles.
<br>
-Compatibility scores are calculated.
<br>
-Missing skills are identified.
<br>
-Results are returned as JSON.
<br>
<br>
**Deployment
<br>
Backend is deployed on Render.

<br><br>
**Build Command**
<br>
pip install -r requirements.txt
<br>
<br>
**Start Command**
<br>
uvicorn main:app --host 0.0.0.0 --port $PORT
<br>
<br>
**Future Scope**
<br><br>
-AI-Based Job Recommendations
<br>
-ATS Resume Scoring
<br>
-Resume Improvement Suggestions
<br>
-Real-Time Job Portal Integration
<br>
-DOCX Resume Support
<br>
-Recruiter Dashboard
<br>
<br>
**Author**
<br>
Riya Ranaware
<br>
M.Sc. Data Science
<br>
<br>
**License
<br>
This project is developed for educational and learning purposes.


### Repository Descriptions (GitHub)

**Frontend Description**

React-based Resume Matcher and Skill Gap Analyzer frontend with interactive dashboard and job recommendation visualization.

**Backend Description**

FastAPI backend for resume parsing, skill extraction, job matching, and skill gap analysis.

