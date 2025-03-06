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

# Function to generate text from user input
def generate_text(prompt, num_sentences=50):
    response = model.generate_content(f"{prompt}\nWrite {num_sentences} sentences.")
    return response.text if response else "No response received."

# Take user input for the prompt
user_prompt = input("Enter your prompt: ")

# Generate text based on user input
output_text = generate_text(user_prompt)

# Print the output
print("\nGenerated Text:\n")
print(output_text)
