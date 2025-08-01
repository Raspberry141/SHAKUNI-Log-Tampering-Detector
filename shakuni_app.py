import streamlit as st

st.title("🎲 SHAKUNI - Log Tampering Detector")

uploaded_file = st.file_uploader("Upload log file (.txt)", type="txt")
if uploaded_file:
    lines = uploaded_file.readlines()
    tampered = False
    for i in range(1, len(lines)):
        if lines[i] < lines[i-1]:
            st.error(f"Suspicious log disorder at line {i+1}")
            tampered = True
    if not tampered:
        st.success("Log appears consistent.")