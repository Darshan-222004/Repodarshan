# Take user input
user_input = input("Enter your AI prompt: ")

# Provide a fixed improved output based on use cases
if "sometimes" in user_input.lower() and "might" in user_input.lower():
    improved_prompt = "If the user asks for a summary, generate a concise one."
elif "explain this topic" in user_input.lower():
    improved_prompt = "Summarize the main points of this topic in under 100 words."
else:
    improved_prompt = "Your prompt looks fine, but consider making it clearer."

# Print the improved prompt
print("Optimized Prompt:", improved_prompt)
