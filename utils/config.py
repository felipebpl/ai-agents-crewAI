import os
import json
from dotenv import load_dotenv
from typing import List

load_dotenv()

def parse_source_urls(env_var: str) -> List[str]:
    if not env_var:
        return []
    # Try to parse as JSON
    try:
        urls = json.loads(env_var)
        if isinstance(urls, list):
            return [url.strip() for url in urls if url.strip()]
        elif isinstance(urls, str):
            return [urls.strip()]
    except json.JSONDecodeError:
        pass
    # If JSON parsing fails, split on commas
    return [url.strip().strip('"').strip("'") for url in env_var.split(",") if url.strip()]


class Config:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    USER_INTERESTS: str = os.getenv(
        "USER_INTERESTS", "Artificial Intelligence, Machine Learning"
    )
    FIRECRAWL_API_KEY: str = os.getenv("FIRECRAWL_API_KEY")
    SOURCE_URLS: List[str] = parse_source_urls(os.getenv("SOURCE_URLS", ""))
    USER_PHONE_NUMBER: str = os.getenv("USER_PHONE_NUMBER", "+5519982789161")
