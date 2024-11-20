import logging
import requests
from typing import List, Dict
from config import WHATSAPP_API_URL

class NotifierAgent:
    def __init__(self, api_token: str, user_phone: str):
        self.api_url = WHATSAPP_API_URL
        self.api_token = api_token
        self.user_phone = user_phone

    def send_notifications(self, summaries: List[Dict[str, str]]):
        """
        Logs summaries and sends them via WhatsApp.
        """
        logging.info("Sending notifications.")
        for summary in summaries:
            message = f"Source: {summary['source']}\nSummary:\n{summary['summary']}"
            logging.info(message)
            self._send_whatsapp_message(message)

    def _send_whatsapp_message(self, message: str):
        payload = {"to": self.user_phone, "type": "text", "text": {"body": message}}
        headers = {"Authorization": f"Bearer {self.api_token}", "Content-Type": "application/json"}
        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            logging.info("Message sent successfully.")
        except Exception as e:
            logging.error(f"Error sending message: {e}")
