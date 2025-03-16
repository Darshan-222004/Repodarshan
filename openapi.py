import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("Missing API key! Check your .env file.")

openai.api_key = API_KEY  # Set OpenAI API key

def refine_prompt(prompt):
    """Refines a vague input into a well-structured, specific, and natural-sounding prompt."""
    
    instruction = (
        "Transform the given statement into a well-structured, specific, and natural-sounding prompt. "
        "Ensure it is between 1 to 4 lines, framed as an effective question or instruction. "
        "Focus on clarity, key details, and natural language refinement. The response must be enclosed in double quotes (\"\").\n\n"
        f"Original: \"{prompt}\"\n"
        "Improved:"
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You refine user prompts for clarity, specificity, and completeness."},
            {"role": "user", "content": instruction}
        ],
        temperature=0.7
    )

    # Extract the refined prompt
    refined_text = response["choices"][0]["message"]["content"].strip()

    # Ensure it is properly formatted with double quotes
    for line in refined_text.split("\n"):
        if line.startswith('"') and line.endswith('"'):
            return line.strip()  # Return the first valid quoted line

    return '"No refined prompt generated."'  # Fallback case

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ").strip()
    improved_prompt = refine_prompt(user_prompt)
    
    print("\n🔹 Refined Prompt:\n")
    print(improved_prompt)
