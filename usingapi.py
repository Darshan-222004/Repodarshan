import os  # Helps us work with files
import requests  # Helps us talk to the internet
from dotenv import load_dotenv  # Helps us read the secret file
import google.generativeai as genai  # Import Gemini SDK

# Load the .env file
load_dotenv()

# Get API key from the hidden .env file
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API key is loaded
if not API_KEY:
    raise ValueError("API key is missing. Please set it in the .env file.")

# Configure Google Gemini API
genai.configure(api_key=API_KEY)

# Function to query Gemini API
def query_gemini(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text if response else "Error: No response from Gemini API."

if __name__ == "__main__":
    user_input = input("Enter a prompt: ")
    result = query_gemini(user_input)
    
    print("\nGenerated Text:\n")
    print(result)
