import streamlit as st

st.title("🔒 Security Scanner")

code = st.text_area("Paste code here")

if st.button("Scan"):
    warnings = []

    if "eval(" in code:
        warnings.append("⚠️ Avoid using eval().")

    if "exec(" in code:
        warnings.append("⚠️ Avoid using exec().")

    if "pickle.load" in code:
        warnings.append("⚠️ pickle.load() can execute malicious code.")

    if warnings:
        for w in warnings:
            st.warning(w)
    else:
        st.success("No major security issues found.")