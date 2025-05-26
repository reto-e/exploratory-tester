import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from langchain_openai import ChatOpenAI

async def main():
    agent = Agent(
        task="""Mission: Explore input fields to discover how the form handles unexpected, 
        invalid, or malicious input in each field of the send us a message form at https://automationintesting.online/. 
        Print out your entry and the resulting error message on the form.
        evaluate if the reaction is as expected or not.""",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print("Achtung....")
    print(result)

asyncio.run(main())