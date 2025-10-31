# Amharic US Immigration Assistant

Small Gradio-based chat app using Google Gemini (via langchain_google_genai) to answer US immigration questions in Amharic.

## Features
- Conversational chat with memory (in-memory session history)
- Immigration law Q/A in Amharic
- Gradio UI
- Run locally and public server via HuggingFace
## Future plan 
- Add voice chat using Speach to Text (STT)
- add RAG piple line for the extrnal knowledge 
## Prerequisites
- Python 3.8+
- Langchain 
- A virtual environment (recommended)
- HuggingFace space to host the chatbot in public server 
- Install dependencies (example):
  pip install -r requirements.txt
  (If you don't have a requirements file, install: langchain-google-genai langchain-core gradio python-dotenv)

## Environment variables
Create a `.env` file in the project root (this file must NOT be committed). Example:
```
GOOGLE_API_KEY=your_google_api_key_here
# Optionally:
# OPENAI_API_KEY=your_openai_api_key_here
# GOOGLE_APPLICATION_CREDENTIALS=/full/path/to/service-account.json

## Run locally
1. Activate your virtualenv (example):
   source .venv/bin/activate
2. Start the app:
   python legalChatBot.py
3. Open the Gradio link printed in the terminal.

## Git / GitHub
- Add a `.gitignore` that includes `.env`, `*.json`, `__pycache__/`, `venv/`, etc.
- Basic push flow:
  git init
  git add .
  git commit -m "Initial commit"
  git remote add origin https://github.com/<OWNER>/<REPO>.git
  git branch -M main
  git push -u origin main

## Security notes
- Never commit `.env` or credentials. Rotate keys if they were pushed accidentally.
- Use secret managers or CI/CD secrets for deployment.

## Troubleshooting
- If dependencies fail, confirm package names and Python version.
- If the model or API access errors appear, verify API keys and quota.

