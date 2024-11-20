import logging
from agents.fetcher import FetcherAgent
from agents.filter import FilterAgent
from agents.summarizer import SummarizerAgent
from crewai import Task, Crew

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Define sources and preferences
    sources = ["https://news.ycombinator.com/", "https://www.paulgraham.com/articles.html"]
    keywords = ["AI", "machine learning", "venture capital"]
    prompt = """
    You are a specialized assistant for a busy founder. Extract and summarize the most relevant points.
    """

    # Goal and backstory for agents
    fetcher_goal = "Collect newsletter content for summarization."
    fetcher_backstory = "This agent is designed to efficiently scrape newsletters and deliver raw content for analysis."
    
    logging.info("Starting run method.")

    # Initialize CrewAI agents
    fetcher_agent = FetcherAgent(
        name="Newsletter Fetcher",
        role="Fetcher",
        goal="Collect newsletter content for summarization.",
        backstory="This agent is designed to efficiently scrape newsletters and deliver raw content for analysis.",
        sources=["https://news.ycombinator.com/", "https://www.paulgraham.com/articles.html"]
    )


    filter_agent = FilterAgent(
        name="Content Filter",
        role="Filter",
        goal="Filter relevant content from collected articles.",
        backstory="You are a highly skilled filter designed to sift through content and find the most relevant pieces.",
        keywords=["AI", "machine learning", "venture capital"]
    )


    summarizer_agent = SummarizerAgent(
        name="Content Summarizer",
        role="Summarizer",
        goal="Summarize filtered content.",
        backstory="You are an expert in extracting and summarizing key insights from given content."
    )


    # Define tasks
    fetch_task = Task(
        agent=fetcher_agent,
        description="Fetch content from newsletters.",
        expected_output="A list of articles fetched from the sources with raw content."
    )

    logging.info("Fetch Task Result:")
    logging.info(fetch_task.output)

    filter_task = Task(
        agent=filter_agent,
        description="Filter relevant content.",
        expected_output="A list of articles containing keywords relevant to the user's preferences.",
        dependencies=[fetch_task]
    )

    logging.info("Filter Task output:")
    logging.info(filter_task.output)
    
    # Define summarize_task
    summarize_task = Task(
        agent=summarizer_agent,
        description="Summarize filtered content.",
        expected_output="Summarized content from the filtered articles.",
        dependencies=[filter_task]
    )

    logging.info("Summarize Task output:")
    logging.info(summarize_task.output)

    # Execute Crew
    crew = Crew(tasks=[fetch_task, filter_task, summarize_task])
    outputs = crew.kickoff()

    logging.info("Finished run method. Returning result.")

    # Log dos resultados finais
    logging.info("Final Results of Crew Execution:")
    logging.info(outputs)

