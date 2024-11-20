import requests
from config import OPENAI_API_KEY, OPENAI_API_URL
from utils.html_parser import preprocess_html_to_text

def generate_summary(prompt: str, text: str) -> str:
    """
    Sends a request to OpenAI API to summarize content.

    Args:
        prompt (str): The prompt for the summarizer.
        text (str): The content to be summarized.

    Returns:
        str: Summarized content.
    """
    cleaned_text = preprocess_html_to_text(text)
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": cleaned_text}
        ],
        "max_tokens": 150,
        "temperature": 0.7
    }
    response = requests.post(OPENAI_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    response_data = response.json()
    return response_data['choices'][0]['message']['content']
