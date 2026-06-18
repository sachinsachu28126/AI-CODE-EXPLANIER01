import streamlit as st

st.title("⚙️ Settings")

theme = st.selectbox(
    "Choose Theme",
    ["Light", "Dark"]
)

ai_model = st.selectbox(
    "Choose AI Model",
    ["Gemini 2.5 Flash", "Gemini 2.5 Pro"]
)

show_history = st.checkbox("Enable History", value=True)
save_reports = st.checkbox("Auto Save Reports", value=True)

st.write("### Current Settings")
st.write(f"Theme: {theme}")
st.write(f"AI Model: {ai_model}")
st.write(f"History Enabled: {show_history}")
st.write(f"Auto Save Reports: {save_reports}")