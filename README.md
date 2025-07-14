# 🚀 AI Resume Analyzer – Built by Siva | Smart Job Application Assistant

> 🎯 Boost your resume using AI! Built with Streamlit, Google Gemini, and custom analytics.

---

## 📌 Overview

This is a **Smart AI Resume Matcher** developed by **Siva**, designed to help job seekers evaluate and improve their resumes using **Google Gemini AI**. It compares your resume against any job description and gives you:

✅ An **AI Resume Score**  
✅ Skill match and gap insights  
✅ Tailored improvement suggestions  
✅ A beautiful, responsive, and animated web UI using **Streamlit**

---

## 🎯 Key Features

- 📄 Upload your **PDF resume**
- 🧠 Get analysis powered by **Google Gemini API**
- 📝 Paste any **job description** and match it with your resume
- 📊 See score, missing keywords, and smart suggestions
- 💡 Insightful dashboards with **Plotly and Streamlit**
- 🎨 **Modern Glassmorphism UI**, animated backgrounds, and hidden deploy UI

---

## ⚙️ Installation & Setup

### 🔁 1. Clone the Repository
```bash
git clone https://github.com/siva-ai-dev/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
2️⃣ Install Requirements
Install from requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
OR manually install:

bash
Copy
Edit
pip install streamlit pandas plotly pymupdf Pillow google-generativeai python-dotenv
🔐 3️⃣ Configure Gemini API Key
Go to Google AI Studio

Generate your Gemini API Key

Create a .env file in your project root:

ini
Copy
Edit
GEMINI_API_KEY=your_api_key_here
▶️ 4️⃣ Run the App
bash
Copy
Edit
streamlit run app.py
🧠 How It Works
📄 Upload your Resume (PDF format)

📝 Paste any Job Description

🔍 Click "Analyze Resume"

✅ Get instant results:

Resume Score

Matching & Missing Keywords

Improvement Suggestions

Visual Analytics (Charts & Tables)

📁 Project Structure
bash
Copy
Edit
📂 AI-Resume-Analyzer  
 ┣ 📂 pdf_images/           # Temporary images from resume PDF  
 ┣ 📜 app.py                # Streamlit UI  
 ┣ 📜 analyzer.py           # Core processing logic (PDF + Gemini)  
 ┣ 📜 requirements.txt      # Python dependencies  
 ┣ 📜 .env.example          # Gemini API key format  
 ┗ 📜 README.md             # Documentation (this file)
☁️ Deploying on Streamlit Cloud
Note: This is a Python (Streamlit) app. Do not use Netlify. Instead:

✅ Recommended Platforms
Streamlit Cloud (Best)

Render

PythonAnywhere

Railway

🚀 Streamlit Deployment Steps
Push your full project to GitHub

Go to 👉 https://streamlit.io/cloud

Click “New App”

Choose your GitHub repo

Set up the secret key:

ini
Copy
Edit
GEMINI_API_KEY=your_api_key_here
Click Deploy

👨‍💻 About the Developer – Siva
💼 Aspiring Full Stack Developer & AI/IoT Enthusiast

📍 Mailam Engineering College, Tamil Nadu

🎓 B.Tech in Information Technology – Graduation: 2026

🧠 Skills: Python, React, Flask, Firebase, TensorFlow, MongoDB

🏆 Smart India Hackathon 2025 Finalist

🔗 GitHub: github.com/siva-ai-dev

📧 Email: sivamec24@gmail.com

