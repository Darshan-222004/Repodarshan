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
        "Improve the given prompt by making it clearer, more specific, and well-structured. "
        "Ensure it is framed as an effective and natural-sounding question, considering key aspects relevant to the topic."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Rewrite this prompt to be clearer, more specific, and well-structured:\n\n{prompt}"}
        ],
        temperature=0.5  # Lower temperature for more controlled outputs
    )

    return response.choices[0].message.content.strip()  # Extract and clean output

if __name__ == "__main__":
    user_prompt = input("Enter a short prompt (1-4 lines) to optimize: ")
    optimized_prompt = optimize_prompt(user_prompt)
    print("\nOptimized Prompt:\n", optimized_prompt)
