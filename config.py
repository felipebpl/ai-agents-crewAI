import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Validate environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing 'OPENAI_API_KEY' in environment variables.")

OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
WHATSAPP_API_URL = "https://your-whatsapp-api-endpoint"
