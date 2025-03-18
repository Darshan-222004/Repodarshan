import asyncio
import openai
import ast
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ Missing OpenAI API key! Check your .env file.")

# Initialize OpenAI client
client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)

def extract_function_names(filename):
    """Extracts function names from a Python file."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"❌ File not found: {filename}")

    with open(filename, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

async def optimize_prompt_openai(prompt):
    """Enhances a function name using OpenAI's GPT-4-turbo."""
    try:
        response = await client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in improving function names for better AI understanding."},
                {"role": "user", "content": f"Optimize this function name to be clearer: \"{prompt}\""}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except openai.OpenAIError as e:
        return f"❌ OpenAI API Error: {str(e)}"

async def main():
    python_file = "markdownfile.py"  # Change this to your Python file
    
    try:
        function_names = extract_function_names(python_file)

        if not function_names:
            print("🚨 No functions found in the file.")
            return

        print("\n📌 Optimizing function names using OpenAI:\n")

        for func in function_names:
            openai_result = await optimize_prompt_openai(func)

            print(f"🔹 **Original Function Name:** {func}")
            print(f"  🔹 OpenAI Suggestion: {openai_result}")
            print("-" * 50)

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
