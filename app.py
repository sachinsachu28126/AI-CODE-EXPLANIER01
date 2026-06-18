import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from utils import analyze_code
import os

load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

st.set_page_config(
    page_title="AI Code Explainer Ultra",
    layout="wide"
)

st.title("🤖 AI Code Explainer Ultra")

language = st.selectbox(
    "Choose Language",
    [
        "Python",
        "Java",
        "c++",
        "JavaScript"
    ]
)

code = st.text_area(
    "Paste your code here",
    height=400
)

if st.button("Analyze Code"):

    if code.strip():

        result = analyze_code(
            code,
            language
        )

        st.markdown(result)

    else:
        st.warning(
            "Please enter code."
        )