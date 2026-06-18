import streamlit as st
import json
import os

st.set_page_config(
    page_title="History",
    page_icon="📜"
)

st.title("📜 History")

# Create history folder if it doesn't exist
os.makedirs("history", exist_ok=True)

history_file = "history/history.json"

# Create history.json if it doesn't exist
if not os.path.exists(history_file):
    with open(history_file, "w") as f:
        json.dump([], f)

# Load history safely
try:
    with open(history_file, "r") as f:
        data = json.load(f)
except (json.JSONDecodeError, FileNotFoundError):
    data = []

# Display history
if not data:
    st.info("No analysis history available.")
else:
    for i, item in enumerate(reversed(data), start=1):
        with st.expander(f"📄 Analysis {i}", expanded=False):

            st.write(
                f"**Language:** {item.get('language', 'Unknown')}"
            )

            st.write("**Code:**")
            st.code(
                item.get("code", ""),
                language=item.get("language", "").lower()
            )

            st.write("**Analysis:**")
            st.write(
                item.get("analysis", "No analysis available.")
            )

# Clear history button
if st.button("🗑️ Clear History"):
    with open(history_file, "w") as f:
        json.dump([], f, indent=4)

    st.success("History cleared successfully!")
    st.rerun()