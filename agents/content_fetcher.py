import logging
from typing import List, Dict, Optional
from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field
import re
import requests
from datetime import datetime

logger = logging.getLogger(__name__)

class ExtractionSchema(BaseModel):
    title: str
    url: str
    articles_titles_and_urls: List[Dict[str, str]]


class ContentFetcher:
    """Fetches articles from specified URLs using Firecrawl's LLM Extract."""

    def __init__(self, source_urls: List[str], firecrawl_api_key: str):
        self.source_urls = source_urls
        self.firecrawl_app = FirecrawlApp(api_key=firecrawl_api_key)
        self.articles: List[Dict[str, str]] = []

    def start_extraction(self):
        """Starts the extraction process."""
        self.fetch_articles()
        contents = self.fetch_content()
        return contents
        

    def fetch_articles(self) -> List[Dict[str, str]]:
        """Fetches articles from all specified URLs."""
        for url in self.source_urls:
            article = self._scrape_and_extract_original_url(url)
            if article:
                relevant_content = self._get_relevant_content(article["articles"])
                self.articles.append(relevant_content)
    
    def fetch_content(self) -> Dict[str, str]:
        """Fetches content from a specified URL."""
        contents = []
        for article in self.articles:
            for content in article:
                if content["url"]:
                    content = self._scrape_and_extract_article(content)
                    if content:
                        contents.append(content)
        return contents


    def _scrape_and_extract_original_url(self, url: str) -> Dict[str, str]:
        """Scrapes and extracts structured data from a URL using Firecrawl."""
        logger.info(f"Scraping and extracting data from: {url}")

        try:
            headers = {
                'Authorization': 'Bearer fc-f56d1ee6e4334f19b0e7f0d2aecffce6',
                'Content-Type': 'application/json'
            }

            payload = {
                "url": f"{url}",
                "pageOptions": {"onlyMainContent": False},
                "extractorOptions": {
                    "mode": "llm-extraction",
                    "extractionPrompt": f"""
                        Based on the information on the page at the {url}, extract the information from the schema.
                        The schema should include a list of articles with their titles, URLs, and published dates.

                        Today's date is: {datetime.today().strftime("%Y-%m-%d")}. 
                        Always extract the published_at field in the format: "%Y-%m-%d" (e.g. "2024-11-21"). 
                        
                        Always extract only the top newest articles and there entire urls.
                    """,
                    "extractionSchema": {
                        "type": "object",
                        "properties": {
                            "articles": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "title": {"type": "string"},
                                        "url": {"type": "string"}, 
                                        "published_at": {"type": "string"}
                                    }
                                }
                            }
                        }
                    }
                },
                "origin": "website"
            }

            response = requests.post('https://api.firecrawl.dev/v0/scrape', headers=headers, json=payload).json()
            if response.get("success"):
                extract = response["data"]
                metadata = extract.get("metadata", {})
                llm_extract = extract.get("llm_extraction", {})
                article = {
                    "title": metadata.get("title", ""),
                    "url": metadata.get("url", ""),
                    "markdown": extract.get("markdown", ""),
                    "articles": llm_extract.get("articles", [])
                }
                logger.info(f"{url} extracted")
                return article
            else:
                logger.error(f"Failed to extract data from {url}: {response}")
        except Exception as e:
            logger.error(f"Error extracting data from {url}: {e}")
        return {}
    
    def _scrape_and_extract_article(self, content: dict) -> Dict[str, str]:
        """Scrapes and extracts structured data from a URL using Firecrawl."""
        logger.info(f"Scraping and extracting data from: {content['url']}")
        try:
            response = self.firecrawl_app.scrape_url(content['url'], params={'formats': ['markdown']})
            if response.get("metadata", {}).get("statusCode") == 200:
                metadata = response["metadata"]
                content = {
                    "title": content.get("title", ""),
                    "url": content.get("url", ""),
                    "published_at": content.get("published_at", ""),
                    "description": metadata.get("description", ""),
                    "markdown": response.get("markdown", ""),
                }
                logger.info(f"Article extracted from {content['url']}")
                return content
            else:
                logger.error(f"Failed to extract data from {content['url']}: {response}")
        except Exception as e:
            logger.error(f"Error extracting data from {content['url']}: {e}")
        return {}
    
    def _get_relevant_content(self, articles) -> List[str]:
        """Select only the top newest articles from the page."""
        today = datetime.today()
        relevant_content = []
        for article in articles:
            if article["published_at"]:
                published_at = datetime.strptime(article["published_at"], "%Y-%m-%d")
                if (today - published_at).days <= 5:
                    relevant_content.append(article)
        return relevant_content

if __name__ == "__main__":
    source_urls = [
        "https://www.lennysnewsletter.com/archive?sort=new",
        ]
    fetcher = ContentFetcher(
        source_urls=source_urls, firecrawl_api_key="fc-f56d1ee6e4334f19b0e7f0d2aecffce6"
    )
    contents = fetcher.start_extraction()
    print(contents)
