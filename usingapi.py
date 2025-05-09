import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("Missing API key! Check your .env file.")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Choose the correct model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Function to refine the prompt
def refine_prompt(prompt):
    refined_prompt = (
        f"Enhance the following statement into a well-structured, specific, and purpose-driven question.\n"
        f"Ensure the improved prompt clarifies the intent and includes relevant details like comparison factors or key aspects:\n\n"
        f"Original: \"{prompt}\"\n"
        f"Improved (specific and well-defined):"
    )
    
    response = model.generate_content(refined_prompt)
    return response.text.strip() if response else "No refined prompt generated."

# Take user input for the prompt
user_prompt = input("Enter your prompt: ")

# Generate refined prompt
improved_prompt = refine_prompt(user_prompt)

# Print the improved prompt
print("\nRefined Prompt:\n")
print(improved_prompt)
