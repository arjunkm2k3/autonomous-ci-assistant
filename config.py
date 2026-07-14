import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Config:
    # GitHub
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    REPO_NAME = os.getenv("REPO_NAME")
    GITHUB_BASE_BRANCH = os.getenv("GITHUB_BASE_BRANCH", "main")
    
    # LLM
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.1"))
    MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "3"))
    
    # RAG
    CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./data/chroma_db")
    
    # Paths
    BASE_DIR = Path(__file__).parent
    KNOWLEDGE_BASE_DIR = BASE_DIR / "knowledge_base"
    LOGS_DIR = BASE_DIR / "logs"
    
    # Ensure directories exist
    for d in [BASE_DIR / "data", LOGS_DIR, KNOWLEDGE_BASE_DIR]:
        d.mkdir(parents=True, exist_ok=True)

    @classmethod
    def validate(cls):
        if not cls.GITHUB_TOKEN or not cls.REPO_NAME:
            raise ValueError("Missing GITHUB_TOKEN or REPO_NAME in .env")
        return True

Config.validate()