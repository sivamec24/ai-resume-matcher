import streamlit as st
import pandas as pd
from analyzer import pdf_to_jpg, process_image

st.set_page_config(page_title="AI Resume Matcher", layout="wide")

# --- Hide Streamlit header/footer/deploy + Add Background + Custom Font ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;600;800&display=swap');
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
                          url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=2000&q=80');
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        color: white;
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 12px;
    }
    .stTextArea, .stFileUploader, .stDataFrame, .stAlert {
        background-color: rgba(255, 255, 255, 0.95) !important;
        color: black !important;
        border-radius: 10px;
        padding: 1rem;
    }
    .stButton > button {
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1.5rem;
        border-radius: 6px;
        border: none;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #1b5e20;
    }
    h1, h2, h3, .stSubheader {
        color: white !important;
    }
    
    /* Custom colors for main titles */
    .main-title {
        color: #FF6B35 !important; /* Orange color */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        font-weight: 800;
    }
    
    .results-title {
        color: #2196F3 !important; /* Blue color */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        font-weight: 800;
    }
    #MainMenu, header, footer, [data-testid="stDeployButton"], [data-testid="collapsedControl"] {
        visibility: hidden;
        height: 0;
    }
    
    /* Custom white box styling for suggestions */
    .suggestions-container {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .suggestions-container h3 {
        color: #2e7d32 !important;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    .suggestion-item {
        background-color: rgba(46, 125, 50, 0.1);
        color: #1b5e20;
        padding: 0.8rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 4px solid #2e7d32;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# --- Session state setup ---
if "page" not in st.session_state:
    st.session_state.page = 1
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# --- Page 1: Home (upload + description) ---
def show_home():
    st.markdown('<h1 class="main-title">🧳 AI-Powered Resume Matcher</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📝 Job Description")
        job_desc = st.text_area("Paste job description", height=220)

    with col2:
        st.subheader("📄 Upload Resume (PDF)")
        uploaded_pdf = st.file_uploader("Upload PDF resume", type="pdf")

    st.markdown("---")

    if uploaded_pdf and job_desc:
        if st.button("🚀 Analyze Resume"):
            with st.spinner("Analyzing your resume..."):
                pdf_path = pdf_to_jpg(uploaded_pdf)
                results = process_image(pdf_path, job_desc)

                st.session_state.analysis_results = results
                st.session_state.analyzed = True
                st.session_state.page = 2
                st.rerun()
    else:
        st.info("📥 Please upload a PDF and enter the job description.")

# --- Page 2: Results ---
def show_results():
    results = st.session_state.analysis_results

    st.markdown('<h1 class="results-title">📊 Resume Match Results</h1>', unsafe_allow_html=True)

    st.subheader(f"🎯 Matching Score: {results['score']}%")
    st.progress(results["score"] / 100)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("✅ Matched Skills")
        st.success(", ".join(results["matched_skills"]))

    with col2:
        st.subheader("⚠️ Missing Skills")
        st.error(", ".join(results["missing_skills"]))

    # Updated suggestions section with custom styling
    st.markdown("""
        <div class="suggestions-container">
            <h3>💡 Suggestions to Improve Resume</h3>
            <div class="suggestion-item">🔹 Highlight experience with scalable web application development.</div>
            <div class="suggestion-item">🔹 Explicitly mention experience with responsive design principles.</div>
            <div class="suggestion-item">🔹 Add projects demonstrating experience with Django framework.</div>
            <div class="suggestion-item">🔹 Showcase familiarity with Google Gemini APIs (if any).</div>
            <div class="suggestion-item">🔹 Quantify accomplishments in projects (e.g., performance improvements, user growth).</div>
            <div class="suggestion-item">🔹 Describe the deployment process used in past projects.</div>
            <div class="suggestion-item">🔹 Emphasize commitment to clean code practices.</div>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("📌 High Priority Improvements")
    df = pd.DataFrame(results["priority_table"])
    st.dataframe(df, use_container_width=True)

    st.markdown("---")
    if st.button("🔙 Back to Home"):
        st.session_state.page = 1
        st.session_state.analyzed = False
        st.rerun()

# --- Routing ---
if st.session_state.page == 1:
    show_home()
elif st.session_state.page == 2:
    show_results()