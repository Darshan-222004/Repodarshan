import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
HEADERS = {"Authorization": f"Bearer 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"}

def query_huggingface(prompt):
    data = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=data)
    return response.json()

if __name__ == "__main__":
    user_input = input("Enter a prompt: ")
    result = query_huggingface(user_input)
    
    if isinstance(result, list):
        print("\nGenerated Text:\n")
        print(result[0]['generated_text'])
    else:
        print("\nError:", result)
