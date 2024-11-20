from crewai import Agent
from crewai_tools import ScrapeWebsiteTool
import logging
from typing import List, Dict


class FetcherAgent(Agent):
    def __init__(self, name: str, role: str, goal: str, backstory: str, sources: List[str]):
        """
        Initializes the Fetcher Agent with name, role, goal, backstory, and sources.
        """
        super().__init__(name=name, role=role, goal=goal, backstory=backstory)
        # Armazena as fontes no campo 'tools_results'
        self.tools_results = sources
        # Registra o ScrapeWebsiteTool na lista de ferramentas
        self.tools = [ScrapeWebsiteTool()]

    def run(self) -> List[Dict[str, str]]:
        """
        Fetches content from the given sources.
        """
        logging.info(f"{self.name}: Fetching content from sources.")
        results = []
        sources = self.tools_results  # Recupera fontes de 'tools_results'
        scraper = self.tools[0]  # Obtém a ferramenta de scraping registrada
        for source in sources:
            try:
                content = scraper.scrape(source)
                results.append({"source": source, "content": content})
            except Exception as e:
                logging.error(f"Error fetching from {source}: {e}")
        return results  # Deve retornar uma lista de dicionários
