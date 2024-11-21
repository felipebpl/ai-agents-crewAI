import requests
from utils.config import Config

class OpenAIClient:
    def __init__(self) -> None:
        self.api_config = {
            'model': 'gpt-4o-mini',
            'temperature': 0.0,
        }
        self.reset_tokens_time_min = 1
        self.reset_tokens_time_max = 60

    def is_relevant(self, text, prompt):
        return self._call_openai_api(text, prompt)
    
    def summarize_article(self, text, prompt):
        return self._call_openai_api(text, prompt)

    @staticmethod
    def _get_headers():
        return {
            'Authorization': f'Bearer {Config.OPENAI_API_KEY}',
            'Content-Type': 'application/json',
        }

    @staticmethod
    def _convert_to_seconds(time_str: str):
        try:
            if time_str.endswith('ms'):
                return int(time_str[:-2]) / 1000.0
            elif time_str.endswith('s'):
                return float(time_str[:-1])
            else:
                return 60
        except ValueError:
            return 60

    def _call_openai_api(self, text: str, prompt: str):
        """
        Calls the OpenAI API with the given text and prompt.

        This method constructs the payload with the provided text and prompt,
        selects an API key using the key rotator, and sends a POST request to
        the OpenAI API. It also updates and prints the rate limit information
        based on the response headers.

        Args:
            text (str): The user input text to be sent to the OpenAI API.
            prompt (str): The system prompt to be included in the API request.

        Returns:
            str: The content of the response message from the OpenAI API.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """
        url = 'https://api.openai.com/v1/chat/completions'
        payload = {
            **self.api_config,
            'messages': [
                {'role': 'system', 'content': prompt},
                {'role': 'user', 'content': text},
            ],
        }
        response = requests.post(
            url, headers=self._get_headers(), json=payload
        )
        
        response.raise_for_status()
        response_data = response.json()
        return response_data['choices'][0]['message']['content']