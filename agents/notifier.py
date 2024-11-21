import logging
from typing import List, Dict
from WPP_Whatsapp import Create
import time

logger = logging.getLogger(__name__)


class Notifier:
    """Sends summaries to the user via WhatsApp using WPP_Whatsapp."""

    def __init__(self, session_name: str, user_phone_number: str):
        self.session_name = session_name
        self.user_phone_number = user_phone_number
        self.client = None
        self.creator = None
        self._initialize_client()

    def _initialize_client(self):
        """Initializes the WhatsApp client."""
        try:
            logger.info("Initializing WhatsApp client...")
            self.creator = Create(session=self.session_name)
            self.client = self.creator.start()
            logger.info("Please scan the QR code in the opened browser to connect WhatsApp.")
            while self.creator.state != 'CONNECTED':
                logger.info(f"Current state: {self.creator.state}. Waiting for connection...")
                time.sleep(5)
            logger.info("WhatsApp client connected successfully.")
        except Exception as e:
            logger.error(f"Error initializing WhatsApp client: {e}")
            raise

    def send_notifications(self, summaries: List[Dict[str, str]]):
        """Sends summaries to the user via WhatsApp."""
        for message in summaries:
            self._send_whatsapp_message(message)

    def _send_whatsapp_message(self, message: str):
        """Sends a message via WhatsApp client."""
        try:
            result = self.client.sendText(self.user_phone_number, message)
            if result:
                logger.info(f"Message sent to {self.user_phone_number}")
            else:
                logger.error(f"Failed to send message to {self.user_phone_number}")
        except Exception as e:
            logger.error(f"Error sending message: {e}")
