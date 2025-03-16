import openai
import os
from dotenv import load_dotenv

def load_api_key():
    load_dotenv(".env")  # Load API key from .env file
    return os.getenv("OPENAI_API_KEY")

def optimize_prompt(prompt):
    api_key = load_api_key()
    if not api_key:
        raise ValueError("OpenAI API key not found. Please check your .env file.")
    
    client = openai.OpenAI(api_key=api_key)  # Initialize OpenAI client

    system_instruction = (
        "You refine user prompts by making them more precise, naturally worded, and aligned with a clear purpose. "
        "Ensure that the optimized prompt conveys the same idea effectively with better structure and clarity."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Improve this prompt while keeping it concise and effective:\n\n{prompt}"}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content  # Extract improved prompt

if __name__ == "__main__":
    user_prompt = input("Enter a short prompt (1-4 lines) to optimize: ")
    optimized_prompt = optimize_prompt(user_prompt)
    print("\nOptimized Prompt:\n", optimized_prompt)
