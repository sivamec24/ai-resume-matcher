import os
import streamlit as st

def pdf_to_jpg(uploaded_pdf):
    """
    Simulates saving a PDF and returning the saved path.
    """
    temp_dir = "/tmp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
        
    path = os.path.join(temp_dir, uploaded_pdf.name)
    with open(path, "wb") as f:
        f.write(uploaded_pdf.getvalue())
    return path

def process_image(image_path, job_desc):
    """
    Returns mocked resume analysis results.
    """
    return {
        "score": 75,
        "matched_skills": [
            "React.js", "Python", "Flask", "OpenAI", "API", "Git", "GitHub"
        ],
        "missing_skills": [
            "Django", "scalable web applications", "responsive design",
            "Google Gemini APIs", "deployment", "clean code"
        ],
        "suggestions": [
            "Highlight experience with scalable web application development.",
            "Explicitly mention experience with responsive design principles.",
            "Add projects demonstrating experience with Django framework.",
            "Showcase familiarity with Google Gemini APIs (if any).",
            "Quantify accomplishments in projects (e.g., performance improvements, user growth).",
            "Describe the deployment process used in past projects.",
            "Emphasize commitment to clean code practices.",
        ],
        "priority_table": [
            {"Improvement Suggestion": "Highlight experience with scalable web application development.", "Priority": "🔴 High"},
            {"Improvement Suggestion": "Explicitly mention experience with responsive design principles.", "Priority": "🔴 High"},
            {"Improvement Suggestion": "Add projects demonstrating experience with Django framework.", "Priority": "🔴 High"},
            {"Improvement Suggestion": "Quantify accomplishments in projects.", "Priority": "🔴 High"},
            {"Improvement Suggestion": "Showcase familiarity with Google Gemini APIs.", "Priority": "🟢 Low"},
            {"Improvement Suggestion": "Describe the deployment process used in past projects.", "Priority": "🟢 Low"},
        ]
    }
