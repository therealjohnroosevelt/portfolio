"""
InfraAI Assistant
AI-assisted infrastructure runbook and incident summarizer.
"""

import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="InfraAI Assistant", layout="wide")

st.title("InfraAI Assistant")
st.caption("Turn logs and incident notes into structured runbook guidance")

# Sidebar configuration
with st.sidebar:
    st.header("LLM Configuration")
    api_key = st.text_input("API Key", type="password", help="OpenAI, Groq, or compatible key")
    base_url = st.text_input(
        "Base URL (optional)",
        value="",
        help="Leave blank for OpenAI. Example for Groq: https://api.groq.com/openai/v1"
    )
    model = st.text_input("Model", value="gpt-4o-mini", help="e.g. gpt-4o-mini, llama-3.1-8b-instant")
    st.caption("Supports any OpenAI-compatible endpoint (OpenAI, Groq, Azure OpenAI, local, etc.)")

# Main input
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Incident / Log Input")
    incident = st.text_area(
        "Paste log snippet, error message, or short incident description",
        height=280,
        placeholder="Example: User cannot sign in. Azure AD logs show AADSTS50076..."
    )
    generate = st.button("Generate Runbook Guidance", type="primary", use_container_width=True)

with col2:
    st.subheader("Runbook Guidance")
    output_placeholder = st.empty()

if generate:
    if not incident.strip():
        st.warning("Please paste an incident or log snippet first.")
    elif not api_key:
        st.error("API key required. Add it in the sidebar.")
    else:
        with st.spinner("Analyzing and drafting guidance..."):
            try:
                client_kwargs = {"api_key": api_key}
                if base_url.strip():
                    client_kwargs["base_url"] = base_url.strip()

                client = OpenAI(**client_kwargs)

                system_prompt = """You are an experienced infrastructure and identity engineer.
Given a log snippet or incident description, produce clear, practical runbook-style guidance.

Respond in this exact structure:

**Summary**
[1-2 sentence plain-language summary]

**Likely Cause**
[Most probable root cause based on the input]

**Recommended Actions**
- [Actionable step 1]
- [Actionable step 2]
- [Actionable step 3]

**Suggested Commands / Checks** (if applicable)
```powershell
# or bash / az cli / etc.
```

Keep the tone professional, concise, and operational. Do not invent facts not supported by the input."""

                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": incident}
                    ],
                    temperature=0.3,
                    max_tokens=800
                )

                result = response.choices[0].message.content
                output_placeholder.markdown(result)

            except Exception as e:
                st.error(f"Error calling LLM: {str(e)}")

# Footer samples hint
st.divider()
st.caption("Tip: Sample incidents are available in the `samples/` folder of this project.")
