# Automated-Resume-Relevance-Check-System

This project is a Streamlit-based web application that automatically checks the relevance of a resume against a given job description (JD). It uses both keyword matching and semantic similarity to provide a comprehensive relevance score and verdict.

## Features
- **Upload Resume**: Supports PDF and DOCX formats.
- **Paste Job Description**: Enter the JD directly into the app.
- **Text Extraction**: Extracts text from uploaded resumes.
- **Keyword Match Score**: Calculates the percentage of JD keywords present in the resume.
- **Semantic Similarity Score**: Uses sentence-transformers to compute semantic similarity between the JD and resume.
- **Final Relevance Score**: Weighted combination of keyword and semantic scores.
- **Verdict**: Classifies the match as High, Medium, or Low.

## How to Run
1. **Install dependencies**
	```bash
	pip install -r requirements.txt
	```
2. **Start the Streamlit app**
	```bash
	streamlit run resume.py
	```
3. **Access the app**
	- Open the provided local URL in your browser (e.g., http://localhost:8501)
	- If using a cloud IDE, make sure to forward port 8501 to public.

## File Structure
- `resume.py` : Main Streamlit app
- `requirements.txt` : Python dependencies

## Dependencies
- streamlit
- PyMuPDF (fitz)
- python-docx
- sentence-transformers
- scikit-learn
- langchain
- openai


