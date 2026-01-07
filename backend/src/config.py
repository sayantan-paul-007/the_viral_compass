import os
from dotenv import load_dotenv
import google.generativeai as genai
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing in .env file")

genai.configure(api_key=GOOGLE_API_KEY)
print("✅ Gemini API Key configured successfully.")

# backend/src/config.py → backend/
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"

# Default DB path (local/dev)
DEFAULT_CACHE_DB = DATA_DIR / "video_cache.db"

# Allow override (Kaggle / Docker / Prod)
CACHE_DB_PATH = Path(
    os.getenv("VIDEO_CACHE_DB", DEFAULT_CACHE_DB)
)
