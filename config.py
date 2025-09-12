import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_KEY = os.getenv("MISTRAL_API_KEY")

# FastAPI Configuration
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
