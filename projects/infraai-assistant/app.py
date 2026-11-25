"""
InfraAI Assistant – Scaffold
AI-assisted infrastructure runbook and incident summarizer.
"""

import streamlit as st

st.set_page_config(page_title="InfraAI Assistant", layout="wide")

st.title("InfraAI Assistant")
st.caption("AI-assisted infrastructure runbook and incident summarizer")

st.write("""
This is a scaffold. The full implementation will accept a log snippet or incident description
and return a structured runbook-style response.
""")

incident = st.text_area("Paste log snippet or incident description", height=200)

if st.button("Generate Runbook Guidance") and incident:
    st.info("LLM integration coming next. Scaffold is ready.")
    st.code(incident[:500] + ("..." if len(incident) > 500 else ""))
