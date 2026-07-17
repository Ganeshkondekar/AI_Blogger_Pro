import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

MODEL = "openai/gpt-4.1-mini"

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"