from bs4 import BeautifulSoup

def preprocess_html_to_text(html_content: str) -> str:
    """
    Preprocesses HTML content by extracting clean text for AI summarization.

    Args:
        html_content (str): Raw HTML content.

    Returns:
        str: Cleaned and readable plain text.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    clean_text = ' '.join(soup.stripped_strings)
    return clean_text
