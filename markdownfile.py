import asyncio
import openai
import os
import re
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("❌ Missing API key! Check your .env file.")

# Initialize OpenAI client
client = openai.AsyncOpenAI(api_key=API_KEY)

def read_markdown_file(file_path: str) -> str:
    """Reads the entire content of a Markdown file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()

def split_into_sections(markdown_text: str):
    """Splits the markdown file into sections based on headings."""
    sections = re.split(r"(#+ .*)", markdown_text)  # Split on markdown headings
    structured_sections = []

    for i in range(1, len(sections), 2):  # Process heading-content pairs
        heading = sections[i].strip()
        content = sections[i + 1].strip() if i + 1 < len(sections) else ""
        structured_sections.append((heading, content))

    return structured_sections

async def analyze_and_fix_section(heading: str, content: str) -> str:
    """Analyzes and improves a README section only if needed."""
    system_msg = "You are an expert in reviewing README files, improving clarity, and making them more purposeful."

    user_instruction = (
        "Analyze the following README section:\n\n"
        f"### {heading}\n{content}\n\n"
        "- If the section is **clear, structured, and serves its purpose**, reply with: `NO_CHANGE`.\n"
        "- If the section is **unclear, too vague, or lacks purpose**, improve it naturally without changing its intent.\n\n"
        "**Improved Section:**"
    )

    try:
        response = await client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_instruction}
            ],
            temperature=0.5
        )

        improved_content = response.choices[0].message.content.strip()

        return improved_content if improved_content != "NO_CHANGE" else content

    except openai.OpenAIError as e:
        return f"❌ API Error: {str(e)}"

async def main():
    markdown_file = "README.md"  # Change this to your actual README file
    
    try:
        markdown_text = read_markdown_file(markdown_file)
        sections = split_into_sections(markdown_text)

        if not sections:
            print("🚨 No sections found in the README.md file.")
            return

        print("\n📌 **Improved README:**\n")

        improved_sections = []
        for heading, content in sections:
            improved_content = await analyze_and_fix_section(heading, content)

            improved_sections.append(f"{heading}\n\n{improved_content}")

        improved_markdown = "\n\n".join(improved_sections)

        with open("README_improved.md", "w", encoding="utf-8") as file:
            file.write(improved_markdown)

        print("✅ README improvements saved to README_improved.md")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
