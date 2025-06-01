from crewai.tools import BaseTool
from browser_use import Agent
from langchain_openai import ChatOpenAI
import os

class MyCustomTool(BaseTool):
    name: str = "Exploratory Browser Testing Tool"
    description: str = (
        "This tool uses the browser-use framework to perform exploratory testing on a given webpage. "
        "Provide the URL of the page you want to test as the argument."
    )

    def _run(self, url: str) -> str:
        """
        Performs exploratory testing on the given URL using the browser-use framework.

        Args:
            url: The URL of the webpage to test.

        Returns:
            A string containing the results of the exploratory testing.
        """
        # Define the exploratory testing task
        task = f"Perform exploratory testing on the page at {url}.  " \
               f"Identify potential issues, gather information about the page's functionality and content, " \
               f"and report your findings. Be creative and thorough."

        # Initialize the browser-use agent
        agent = Agent(
            task=task,
            llm=ChatOpenAI(model="gpt-4o", openai_api_key=os.environ.get("OPENAI_API_KEY")), # Ensure API key is set
        )

        # Run the browser-use agent
        result = agent.run()

        return result
