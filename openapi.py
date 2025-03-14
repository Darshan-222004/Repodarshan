import openai
import os
from dotenv import load_dotenv

def load_api_key():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")

def optimize_prompt(prompt):
    api_key = load_api_key()
    if not api_key:
        raise ValueError("OpenAI API key not found. Please check your .env file.")
    
    openai.api_key = api_key
    
    system_instruction = (
        "You are a helpful assistant that refines and optimizes user prompts. "
        "Ensure the output is clear, specific, and written in natural language. "
        "Focus on improving purpose, specification, and fluency."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Optimize this prompt: {prompt}"}
        ],
        temperature=0.7
    )
    
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_prompt = input("Enter a short prompt (1-4 lines) to optimize: ")
    optimized_prompt = optimize_prompt(user_prompt)
    print("\nOptimized Prompt:\n", optimized_prompt)

