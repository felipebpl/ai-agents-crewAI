import logging
from agents.content_fetcher import ContentFetcher
from agents.content_filter import ContentFilter
from agents.summarizer import Summarizer
from agents.notifier import Notifier
from utils.config import Config


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True 
    )



def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    if not Config.SOURCE_URLS:
        logger.error("No source URLs provided in the configuration.")
        return

    logger.info("Initializing agents...")
    content_fetcher = ContentFetcher(
        source_urls=Config.SOURCE_URLS,
        firecrawl_api_key=Config.FIRECRAWL_API_KEY
    )
    content_filter = ContentFilter(
        user_interests=Config.USER_INTERESTS
    )
    summarizer = Summarizer()
    notifier = Notifier(
        session_name='news_notifier',
        user_phone_number=Config.USER_PHONE_NUMBER
    )

    print("Initializing agents...")
    logger.info("Fetching articles using Firecrawl...")
    contents = content_fetcher.start_extraction()
    logger.info(f"Fetched {len(contents)} articles.")

    logger.info("Filtering articles for relevance...")
    relevant_articles = content_filter.filter_articles(contents)
    logger.info(f"Found {len(relevant_articles)} relevant articles.")

    if not relevant_articles:
        logger.info("No relevant articles found.")
        return

    logger.info("Summarizing articles...")
    summaries = summarizer.summarize_articles(relevant_articles)
    logger.info("Summaries generated.")

    logger.info("Sending notifications via WhatsApp...")
    notifier.send_notifications(summaries)
    logger.info("Notifications sent successfully.")

if __name__ == "__main__":
    main()
