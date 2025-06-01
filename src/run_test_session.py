from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import os
import glob
import asyncio

def run(url_param: str = "https://automationintesting.online/"):
    # read the latest testing charta file from output/
    url = url_param.strip()
    charta_file = "output/02_testing_charta.md"
    if not charta_file:
        raise FileNotFoundError("No testing charta found in output/02_testing_charta_*.md")
    with open(charta_file, "r") as f:
        charta_md = f.read()

    task = f"""
    Follow this exploratory testing charta and perform a browser-based test session on the page {url}. 
    Document your findings in detail.\n\nTesting Charta:\n{charta_md}
    Include in the documentation:
    - The steps you took during the test session
    - Any issues or bugs you encountered
    - Observations about the page's functionality and usability
    """
    # use the browser_use module to run the test session
    load_dotenv()
    llm = ChatOpenAI(model="gpt-4o")
    agent = Agent(
        task=task,
        llm=llm,
        save_conversation_path="output/04_detailed_testrun.md",
    )
    async def run_agent():
        return await agent.run(max_steps=20)

    # compile a report of findings and save it to output/03_test_session_report.md
    os.makedirs("output", exist_ok=True)
    report_path = "output/03_test_session_summary.md"
    with open(report_path, "w") as f:
        f.write(findings.final_result())
    print(f"Test session report saved to {report_path}")

if __name__ == "__main__":
    run("https://automationintesting.online/")