from langchain_google_genai import ChatGoogleGenerativeAI
import os
import gradio as gr
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import AIMessage, HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
# Load environment variables from .env
load_dotenv()
# If GOOGLE_API_KEY is set in .env, propagate to os.environ (some libs read it from env)
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key:
    os.environ["GOOGLE_API_KEY"] = google_api_key

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, max_tokens=None,
    timeout=None,
    max_retries=2,)
# Step 1: define a memory store (dict keyed by session_id)
session_store = {}

def get_history_from_config(cfg):
    session_id = None
    if isinstance(cfg, dict):
        cfg_conf = cfg.get("configurable") if isinstance(cfg.get("configurable"), dict) else {}
        session_id = cfg_conf.get("session_id")
    if not session_id:
        session_id = "default"
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

def format_history(history_obj):
    # Convert messages to readable text
    text_history = ""
    for msg in history_obj.messages:
        if isinstance(msg, HumanMessage):
            text_history += f"User: {msg.content}\n"
        elif isinstance(msg, AIMessage):
            text_history += f"AI: {msg.content}\n"
    return text_history

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful and knowledgeable US immigration assistant. Your task is to understand the user's qestions with 
            the input language and provide a clear, natural, and detailed answer in Amharic that is easy for humans to read. 
            You only answer US related immigration questions. If you do not know the answer, simply reply with 'አላውቅም' 
            (I don’t know)."""
        ),
        ("human","Previous conversation: {history} \nCurrent question: {input}"),
    ]
)

chain = prompt | llm |StrOutputParser() 

# print(result.content)
chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_history_from_config,
    input_messages_key="input",
    history_messages_key="history",
)

# Use a fixed session_id so history persists
config = {"configurable": {"session_id": "user123"}}

def ChatPot(message):
     result = chain_with_memory.invoke(
    {
        "input": message,
    },
    config=config
) 
     return result
     
# Create ChatGPT-style chat interface
with gr.Blocks() as demo:
    chatbot = gr.Chatbot(label="Amharic US immigration Assistant")
    with gr.Row():
        txt = gr.Textbox(placeholder="Type your message (Amharic or English)...", show_label=False, lines=2)
        btn = gr.Button("Send")
    state = gr.State([])

    def submit(message, history):
        if not message or not str(message).strip():
            return history, "", history
        try:
            result = chain_with_memory.invoke({"input": str(message).strip()}, config=config)
        except Exception as e:
            result = f"Error getting response: {e}"
        history = history + [(message, result)]
        return history, "", history

    btn.click(submit, inputs=[txt, state], outputs=[chatbot, txt, state])
    txt.submit(submit, inputs=[txt, state], outputs=[chatbot, txt, state])

demo.launch(share=True)

# Git / GitHub quick push instructions:
# 1) From project root:
#    cd /Users/kenny/Desktop/legal
#    git init                      # if repo not initialized
#    echo ".venv\n__pycache__/\n*.pyc\n*.json\n.env\nvenv/" > .gitignore
#    git add . && git commit -m "Initial commit"
#
# 2) Create GitHub repo:
#    - Option A (gh CLI): gh repo create <OWNER>/<REPO> --public --source=. --remote=origin --push
#    - Option B (web): create a new repo on github.com, then:
#        git remote add origin https://github.com/<OWNER>/<REPO>.git
#        git branch -M main
#        git push -u origin main
#
# 3) If using HTTPS, create a Personal Access Token (PAT) and use it when prompted (instead of password).
#    Or set up SSH keys and use the SSH repo URL:
#        git remote set-url origin git@github.com:<OWNER>/<REPO>.git
#        git push -u origin main
#
# Security note: remove hard-coded API keys/credentials from source before pushing.
# - Put secrets in a .env file (add .env to .gitignore), or use a secrets manager.
# - Rotate any keys already committed to history (use git filter-repo / BFG if needed).