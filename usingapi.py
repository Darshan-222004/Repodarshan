import os  # Helps us work with files
import requests  # Helps us talk to the internet
from dotenv import load_dotenv  # Helps us read the secret file

# Load the .env file
load_dotenv()  # Fixed the incorrect function call

# Get API key from the hidden .env file
API_KEY = os.getenv("huggingface")

API_URL = "https://api-inference.huggingface.co/models/gpt2"

# Check if API key is loaded
if not API_KEY:
    raise ValueError("API key is missing. Please set it in the .env file.")

# Set up headers for the request
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def query_huggingface(prompt):
    data = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=data)
    
    try:
        result = response.json()
    except requests.exceptions.JSONDecodeError:
        return {"error": "Failed to parse response from API."}
    
    return result

if __name__ == "__main__":  # Fixed '__name__' syntax
    user_input = input("Enter a prompt: ")
    result = query_huggingface(user_input)

    if isinstance(result, list) and 'generated_text' in result[0]:
        print("\nGenerated Text:\n")
        print(result[0]['generated_text'])
    else:
        print("\nError:", result)
