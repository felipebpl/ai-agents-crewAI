from typing import List, Dict
import logging
from utils.openai_client import OpenAIClient
import json

logger = logging.getLogger(__name__)


class ContentFilter:
    """Filters content based on user-defined interests."""

    def __init__(self, user_interests: str):
        self.user_interests = user_interests
        self.client = OpenAIClient()

    def filter_articles(self, articles: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Filters articles to keep only those relevant to user interests."""
        relevant_articles = []
        for article in articles:
            if self._is_relevant(article):
                relevant_articles.append(article)
        return relevant_articles

    def _is_relevant(self, article: Dict[str, str]) -> bool:
        """Determines if an article is relevant using OpenAI API."""
        prompt = f"""You are an expert content curator specializing in selecting high-quality articles for entrepreneurs committed to lifelong learning. 
        
        Your goal is to determine if the following article (markdown format) is truly relevant and valuable to the user's interests.

        User Interests:
        {self.user_interests}

        Article Title:
        {article['title']}

        Article Description:
        {article['description']}

        Based on the content of the article with the user's interests and its potential to provide valuable insights, answer with "Yes" if the article is relevant or "No" if it is not. 
        
        Do not provide any additional information or explanation, just a simple "Yes" or "No" response.
        """

        text = article["markdown"]

        try:
            response = self.client.is_relevant(text, prompt)
            answer = response.strip().lower()
            is_relevant = answer == "yes"
            logger.debug(f"Article '{article['title']}' relevance: {is_relevant}")
            return is_relevant
        except Exception as e:
            logger.error(f"Error filtering article '{article['title']}': {e}")
            return False
        
    