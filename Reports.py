import streamlit as st
import os

st.title("📄 Reports")

files = os.listdir("reports")

if files:
    for file in files:
        path = f"reports/{file}"

        with open(path, "rb") as f:
            st.download_button(
                label=f"Download {file}",
                data=f,
                file_name=file
            )
else:
    st.info("No reports generated.")