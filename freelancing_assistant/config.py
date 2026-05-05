import os
from dotenv import load_dotenv

load_dotenv()

# ── Ollama ──
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")
OLLAMA_HOST  = os.getenv("OLLAMA_HOST",  "http://localhost:11434")

# ── Freelancer.com API ──
FREELANCER_API_TOKEN = os.getenv("FREELANCER_API_TOKEN", "")

# ── Job Fetcher defaults ──
DEFAULT_KEYWORDS         = "python developer"
DEFAULT_LIMIT_PER_SOURCE = 5

# ── App settings ──
APP_TITLE = "FreelanceAI M28"
APP_PORT  = 7860
APP_HOST  = "0.0.0.0"