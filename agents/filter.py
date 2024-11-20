from crewai import Agent
import logging
from typing import List, Dict


class FilterAgent(Agent):
    def __init__(self, name: str, role: str, goal: str, backstory: str, keywords: List[str]):
        """
        Initializes the Filter Agent with name, role, goal, backstory, and keywords.
        """
        super().__init__(name=name, role=role, goal=goal, backstory=backstory)
        # Armazena as palavras-chave no atributo 'tools_results'
        self.tools_results = keywords

    def run(self, collected_content: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Filters the fetched content based on keywords.
        """
        logging.info("FilterAgent: Filtering content.")
        filtered_results = []
        keywords = self.tools_results  # Recupera palavras-chave de 'tools_results'
        for item in collected_content:
            if any(keyword.lower() in item["content"].lower() for keyword in keywords):
                filtered_results.append(item)
        logging.info(f"Filtered {len(filtered_results)} items.")
        return filtered_results  # Deve retornar uma lista de dicionários
