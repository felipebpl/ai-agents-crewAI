from crewai import Agent
import logging
from typing import List, Dict


class SummarizerAgent(Agent):
    def __init__(self, name: str, role: str, goal: str, backstory: str):
        """
        Initializes the Summarizer Agent with name, role, goal, and backstory.
        """
        super().__init__(name=name, role=role, goal=goal, backstory=backstory)

    def run(self, filtered_content: List[Dict[str, str]]) -> str:
        """
        Summarizes the filtered content.
        """
        logging.info("SummarizerAgent: Summarizing content.")
        summaries = []
        for item in filtered_content:
            summaries.append(f"Summary of content from {item['source']}: {item['content'][:100]}...")
        return "\n".join(summaries)  # Retorna um resumo como string
