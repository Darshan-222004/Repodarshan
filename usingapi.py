import os
import google.generativeai as genai
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load the .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv("GOOGLE_API_KEY")

# Check if API key is loaded correctly
if not API_KEY:
    raise ValueError("API key is missing. Please set it in the .env file.")

# Configure Gemini API with the loaded key
genai.configure(api_key=API_KEY)

# List available models
models = genai.list_models()

# Print the available models (to debug and check what you can use)
for model in models:
    print(model.name)

# Use a supported model (change based on available models)
model = genai.GenerativeModel("gemini-1.0-pro")

response = model.generate_content("Hello, how are you?")
print(response.text)
