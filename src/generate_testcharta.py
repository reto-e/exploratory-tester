import os
from openai import OpenAI
from dotenv import load_dotenv


def run():
    # read the file knowledge/tours.md
    with open("knowledge/tours.md", "r") as f:
        tours_md = f.read()

    # read the file output/01_page_analysis.md
    with open("output/01_page_analysis.md", "r") as f:
        page_analysis_md = f.read()

    # Use the content of those two files to call chatgpt and generate a testing charta for this specific page
    load_dotenv()
    client = OpenAI()
    prompt = (
        "You are a skilled exploratory tester. "
        "Given the following tour description and page analysis, generate a detailed, actionable testing charta in Markdown format for this specific page. "
        "Use the tour description as a collection of ideas. You can reuse those tours if they are relevant to the page.\n\n"
        "Focus on one, maximum two main focus areas for the testing charta. "
        "The charta should include goals, test ideas, exploration areas, risks, and any relevant notes.\n\n"
        "Tour description:\n" + tours_md + "\n\n"
        "Page analysis:\n" + page_analysis_md + "\n\n"
        "Please structure the charta clearly with headings and lists."
    )
    chat_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1200
    )
    charta_md = chat_response.choices[0].message.content

    # 2. Store this testing charta as md file in the output folder
    os.makedirs("output", exist_ok=True)
    charta_path = f"output/02_testing_charta.md"
    with open(charta_path, "w") as f:
        f.write(charta_md)

if __name__ == "__main__":
    run()