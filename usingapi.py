import requests

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/gpt2"
HEADERS = {"Authorization": "Bearer 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"}  #api ket

def query_huggingface(prompt):
    """Sends prompt to Hugging Face API and returns the response."""
    data = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=data)
    return response.json()

# Keep asking until user enters something
while True:
    user_input = input("Enter your AI prompt: ").strip()
    if user_input:
        break
    print("Input cannot be empty. Please enter a prompt.")

# Convert input to lowercase
lower_input = user_input.lower()

# Dictionary of patterns and responses for prompt optimization
prompt_fixes = {
    ("sometimes", "might"): "If asking for a summary, generate a concise one.",
    ("explain this topic",): "Summarize the main points of this topic in under 100 words."
}

# Default response
new_prompt = user_input

# Check for matching patterns
for keywords, response in prompt_fixes.items():
    if all(word in lower_input for word in keywords):
        new_prompt = response
        break  # Stop once a match is found

print("\nOptimized Prompt:", new_prompt)

# Query the Hugging Face model with the optimized prompt
result = query_huggingface(new_prompt)

# Print the AI-generated response
if isinstance(result, list):
    print("\nAI Response:\n")
    print(result[0]['generated_text'])
else:
    print("\nError:", result)
