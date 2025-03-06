import os
import google.generativeai as genai
from dotenv import load_dotenv  # Securely load API key

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Ensure API key is available
if not API_KEY:
    raise ValueError("API key is missing. Please set it in the .env file.")

# Configure Gemini AI
genai.configure(api_key=API_KEY)

# Choose a valid Gemini model
model = genai.GenerativeModel("gemini-1.0-pro")

def generate_text(prompt, num_sentences=50):
    """Generates text with the specified number of sentences."""
    full_prompt = f"{prompt}\n\nPlease generate {num_sentences} sentences."
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Get user input and generate text
user_prompt = input("Enter a prompt: ")
generated_text = generate_text(user_prompt)

# Display result
print("\nGenerated Text:\n")
print(generated_text)
