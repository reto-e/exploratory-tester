from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import asyncio

load_dotenv()

task = """
Open the URL https://automationintesting.online/ and print out a list of all 
significant elements you find on the page (such as forms, buttons, inputs, 
scripts, iframes, navigation, etc.).

You are an experienced software tester. Take the elements you found and analyze them for potential risks.
These risks can be related to security, privacy, usability, accessibility, or other relevant aspects.

List the risks in a structured way, grouping them by the elements they relate to.
"""

async def main():
    llm = ChatOpenAI(model="gpt-4o")
    agent = Agent(
        task=task,
        llm=llm,
    )
    result = await agent.run()
    print(result)
    with open("output/01_page_analysis.md", "w") as f:
        f.write(result.final_result())

if __name__ == "__main__":
    asyncio.run(main())
