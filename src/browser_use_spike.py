from dotenv import load_dotenv
load_dotenv()
from crewai.tools import tool
from crewai.tools import BaseTool
from browser_use import Agent
from langchain_openai import ChatOpenAI

class BrowserUseSpike(BaseTool):
    """A tool that uses the browser-use framework to perform web browsing tasks."""
    async def run(self, task):
        """
        Run the browser-use task with the given task configuration."""
        agent = Agent(
            task=task,
            llm=ChatOpenAI(model="gpt-4o"),
        )
        result = await agent.run()
        print("Achtung....")
        print(result)
        return result