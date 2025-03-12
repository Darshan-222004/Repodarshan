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

# Function to generate text from user input with improved prompt
def generate_text(prompt):
    refined_prompt = (
        f"Based on the following input, generate a well-structured, detailed, and engaging response:\n\n"
        f"---\n"
        f"User Input: {prompt}\n\n"
        f"### Requirements:\n"
        f"- Provide a clear and coherent response.\n"
        f"- Maintain an engaging and informative tone.\n"
        f"- Structure the content logically with well-defined sections.\n"
        f"- If answering a question, give thorough explanations with examples.\n"
        f"- If responding to an instruction, ensure precision and depth.\n"
        f"---"
    )
    
    response = model.generate_content(refined_prompt)
    return response.text if response else "No response received."

# Take user input for the prompt
user_prompt = input("Enter your prompt: ")

# Generate text based on user input
output_text = generate_text(user_prompt)

# Print the output
print("\nGenerated Text:\n")
print(output_text)

