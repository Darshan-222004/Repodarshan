# Keep asking until user enters something
while True:
    user_input = input("Enter your AI prompt: ").strip()
    if user_input:
        break
    print("Input cannot be empty. Please enter a prompt.")

# Convert input to lowercase once
lower_input = user_input.lower()

# Dictionary of patterns and responses
prompt_fixes = {
    ("sometimes", "might"): "If the user asks for a summary, generate a concise one.",
    ("explain this topic",): "Summarize the main points of this topic in under 100 words."
}

# Default response
new_prompt = "Your prompt looks fine, but consider making it clearer."

# Check for matching patterns
for keywords, response in prompt_fixes.items():
    if all(word in lower_input for word in keywords):
        new_prompt = response
        break  # Stop once we find a match

# Print the optimized prompt
print("Optimized Prompt:", new_prompt)

