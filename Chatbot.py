import streamlit as st
from utils import analyze_code

st.title("🤖 AI Chatbot")

question = st.text_area("Ask anything about programming:")

if st.button("Ask AI"):
    if question:
        answer = ask_ai(question)
        st.write(answer)