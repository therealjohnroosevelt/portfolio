# InfraAI Assistant

AI-assisted infrastructure runbook and incident assistant.

Takes raw operational input (log snippets, error messages, or short incident descriptions) and returns a concise summary, probable cause, and suggested remediation steps written in runbook style.

## Purpose

Demonstrates practical application of AI to everyday infrastructure and operations work — without requiring access to a production environment.

## Features

- Structured runbook-style output (Summary, Likely Cause, Recommended Actions, Suggested Commands)
- Works with any OpenAI-compatible API (OpenAI, Groq, Azure OpenAI, local endpoints, etc.)
- Simple Streamlit UI
- Configurable model and endpoint via sidebar

## Quick Start

```bash
cd projects/infraai-assistant
python -m venv .venv
source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows
pip install -r requirements.txt
streamlit run app.py
```

Then:
1. Open the sidebar
2. Enter an API key (and optional base URL / model)
3. Paste a log snippet or incident description
4. Click **Generate Runbook Guidance**

### Free / Low-cost LLM options

| Provider | Base URL | Notes |
|----------|----------|-------|
| Groq | `https://api.groq.com/openai/v1` | Fast free tier, good for demos |
| OpenAI | (leave blank) | Standard |
| Azure OpenAI | Your Azure endpoint | Use your deployment name as the model |

## Sample Inputs

See `samples/sample_incidents.md` for realistic examples covering Entra ID, AWS, and Windows scenarios.

## Status

Functional. Ready for demos and further extension.
