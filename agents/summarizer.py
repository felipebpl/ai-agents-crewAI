from typing import List, Dict
import logging
from utils.openai_client import OpenAIClient

logger = logging.getLogger(__name__)


class Summarizer:
    """Summarizes articles."""

    def __init__(self):
        self.client = OpenAIClient()

    def summarize_articles(self, articles: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Generates summaries for the given articles."""
        summaries = []
        for content in articles:
            if content:
                summary = self._generate_summary(content)
                summaries.append(summary)
            else:
                logger.warning(f"No content to summarize for article '{content['title']}'")
        return summaries

    def _generate_summary(self, content: Dict[str, str]) -> str:
        """Generates a summary of the content using OpenAI API."""
        prompt = (
            "You are an assistant tasked with summarizing an article for an entrepreneur focused on lifelong learning. "
            "Your goal is to extract only the most valuable insights from the article content provided and present them in a super direct and clear manner, similar to how Paul Graham writes.\n\n"
            "Instructions:\n"
            "- Read the article content below.\n"
            "- Extract and summarize the key insights, main points, and actionable advice.\n"
            "- Write in a concise, clear, and direct style, like Paul Graham.\n"
            "- The summary should be suitable for a WhatsApp message, keeping it brief and to the point.\n"
            "- Start with the article's title, include a brief description, and mention the published date.\n"
            "- Do not include any irrelevant information or filler content in the end as you were talking to the user.\n\n"
            "Article Information:\n\n"
            f"Title: {content.get('title', 'No Title')}\n"
            f"Published Date: {content.get('published_at', '')}\n"
            f"URL: {content.get('url', '')}\n\n"
            f"Description: {content.get('description', '')}\n"
            "Article Content: \n"
        )
        text = content.get('markdown', '')
        try:
            response = self.client.summarize_article(text, prompt)
            summary = response.strip().replace("**", "*")
            return summary
        except Exception as e:
            logger.error(f"Error generating summary: {e}")
            return "Summary not available."
