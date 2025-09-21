import streamlit as st
import fitz  # PyMuPDF
from docx import Document
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ------------------ Text Extraction Functions ------------------

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    return " ".join([para.text for para in doc.paragraphs])

# ------------------ Streamlit UI ------------------

st.title("📄 Automated Resume Relevance Checker")

# Text input for Job Description
jd_text = st.text_area("📌 Paste Job Description (JD) here", key="jd_input")

# File uploader for resume with a unique key
resume_file = st.file_uploader("📤 Upload Resume (PDF or DOCX)", type=["pdf", "docx"], key="resume_uploader")

resume_text = ""
if resume_file:
    if resume_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(resume_file)
    elif resume_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_text_from_docx(resume_file)
    
    # Display extracted resume preview
    st.subheader("📄 Extracted Resume Text (Preview)")
    st.write(resume_text[:500] + "..." if len(resume_text) > 500 else resume_text)

# ------------------ Matching Functions ------------------

def keyword_score(jd, resume):
    jd_words = set(jd.lower().split())
    resume_words = set(resume.lower().split())
    match = jd_words.intersection(resume_words)
    score = len(match) / len(jd_words) * 100 if jd_words else 0
    return round(score, 2), match

def semantic_score(jd, resume):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    jd_emb = model.encode([jd])
    resume_emb = model.encode([resume])
    sim = cosine_similarity(jd_emb, resume_emb)[0][0]
    return round(sim * 100, 2)

# ------------------ Score Calculation ------------------

if jd_text and resume_text:
    st.subheader("📊 Matching Scores")

    # Keyword Score
    score, matched = keyword_score(jd_text, resume_text)
    st.write(f"🔑 **Keyword Match Score:** {score}%")
    st.write(f"✅ **Matched Keywords:** {', '.join(matched)}")

    # Semantic Score
    sem_score = semantic_score(jd_text, resume_text)
    st.write(f"🧠 **Semantic Similarity Score:** {sem_score}%")

    # Final Weighted Score
    final_score = (0.6 * sem_score + 0.4 * score)
    st.subheader("🎯 Final Relevance Score")
    st.write(f"✅ **{final_score:.2f}%**")

    # Verdict
    if final_score > 75:
        verdict = "High Match"
        st.success(f"Verdict: {verdict}")
    elif final_score > 50:
        verdict = "Medium Match"
        st.warning(f"Verdict: {verdict}")
    else:
        verdict = "Low Match"
        st.error(f"Verdict: {verdict}")
