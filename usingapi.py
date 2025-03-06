import os  # Helps us work with environment variables
import cohere  # Cohere SDK for AI text generation
from dotenv import load_dotenv  # Helps us read the .env file

# Load the .env file
load_dotenv()

# Get API key from the hidden .env file
API_KEY = os.getenv("COHERE_API_KEY")

# Check if API key is loaded
if not API_KEY:
    raise ValueError("API key is missing. Please set it in the .env file.")

# Initialize the Cohere client
co = cohere.Client(API_KEY)

def query_cohere(prompt):
    try:
        response = co.generate(
            model="command",  # Use "command" for high-quality results or "command-light" for faster responses
            prompt=prompt,
            max_tokens=100,  # Adjust response length as needed
            temperature=0.7  # Controls randomness (0 = predictable, 1 = creative)
        )

        return response.generations[0].text

    except cohere.CohereError as e:
        return f"API Error: {e}"

if __name__ == "__main__":
    user_input = input("Enter a prompt: ")
    result = query_cohere(user_input)
    
    print("\nGenerated Text:\n")
    print(result)
