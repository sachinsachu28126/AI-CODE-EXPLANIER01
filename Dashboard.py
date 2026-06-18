import streamlit as st
import os

st.title("📊 Dashboard")

upload_count = len(os.listdir("uploads"))
report_count = len(os.listdir("reports"))
history_count = len(os.listdir("history"))

st.metric("Uploaded Files", upload_count)
st.metric("Reports Generated", report_count)
st.metric("History Records", history_count)