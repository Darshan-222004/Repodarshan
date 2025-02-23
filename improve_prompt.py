
# Keep asking until user enters something
while True:
    user_input = input("Enter your AI prompt: ").strip()
    if user_input:
        break
    print("Input cannot be empty. Please enter a prompt.")

# Provide an improved version of the input
if "sometimes" in user_input.lower() and "might" in user_input.lower():
    improved_prompt = "If the user asks for a summary, generate a concise one."
elif "explain this topic" in user_input.lower():
    improved_prompt = "Summarize the main points of this topic in under 100 words."
else:
    improved_prompt = "Your prompt looks fine, but consider making it clearer."

# Print the improved prompt
print("Optimized Prompt:", improved_prompt)
