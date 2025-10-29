# Amharic US Immigration Assistant

Small Gradio-based chat app using Google Gemini (via langchain_google_genai) to answer US immigration questions in Amharic.

## Features
- Conversational chat with memory (in-memory session history)
- Gradio UI for local testing
- Loads API keys from a `.env` file

## Prerequisites
- Python 3.8+
- A virtual environment (recommended)
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
```

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

### Git push error: "src refspec master does not match any"
This means Git couldn't find a local branch named `master` with commits to push.

Quick fixes (pick one):

A) You have no commits yet — create an initial commit and push:
```bash
# from project root
git add .
git commit -m "Initial commit"
# push default branch (use 'main' if your local branch is main)
git push -u origin main
# OR, if you prefer 'master':
git branch -M master
git push -u origin master
```

B) Your local branch is named `main` (common modern default) — push `main` instead of `master`:
```bash
git branch           # shows current branch (e.g. * main)
git push -u origin main
```

C) Confirm remotes and branches:
```bash
git remote -v        # verify origin URL
git branch -a        # list local and remote branches
```

D) Create and push a branch named `master` if needed:
```bash
git checkout -b master
git add .
git commit -m "Initial commit on master"
git push -u origin master
```

E) Use GitHub CLI to create repo and push (handles branches automatically):
```bash
gh auth login
gh repo create <OWNER>/<REPO> --public --source=. --remote=origin --push
```

### Git error: "remote origin already exists"

If you see "error: remote origin already exists" it means a remote named `origin` is already configured locally.

Options to fix:

1) Inspect current remotes
```bash
git remote -v
```

2) Update the existing origin URL (no removal)
```bash
git remote set-url origin https://github.com/<OWNER>/<REPO>.git
git push -u origin main
```

3) Remove and recreate origin
```bash
git remote remove origin
git remote add origin https://github.com/<OWNER>/<REPO>.git
git push -u origin main
```

4) Add remote under a different name
```bash
git remote add upstream https://github.com/<OWNER>/<REPO>.git
git push -u upstream main
```

Notes:
- Replace <OWNER> and <REPO> with your GitHub username/org and repository name.
- Use a PAT for HTTPS authentication or configure SSH and use the SSH URL.