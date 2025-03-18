import asyncio
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("❌ Missing API key! Check your .env file.")

# Initialize OpenAI client
client = openai.AsyncOpenAI(api_key=API_KEY)

async def optimize_prompt(prompt: str) -> str:
    """
    Enhances a given prompt to be:
    - Clear and structured
    - More specific with relevant details
    - Focused on achieving better AI responses

    The improved version is returned in double quotes.
    """

    system_msg = "You are an expert in refining prompts to improve clarity, specificity, and effectiveness."
    
    user_instruction = (
        "Improve the following prompt for better AI responses. "
        "Make it more detailed, structured, and precise while maintaining natural language. "
        "Do NOT shorten or summarize it—only refine it for better clarity and intent. "
        "The response must be enclosed in double quotes (\"\").\n\n"
        f"Original Prompt: \"{prompt}\"\n"
        "Optimized Prompt:"
    )

    try:
        response = await client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_instruction}
            ],
            temperature=0.5  # Keeps responses structured and logical
        )

        refined_text = response.choices[0].message.content.strip()

        # Ensure response is properly quoted
        return refined_text if refined_text.startswith('"') and refined_text.endswith('"') else f'"{refined_text}"'

    except openai.OpenAIError as e:
        return f"❌ API Error: {str(e)}"

async def main():
    user_prompt = input("🔹 Enter your prompt: ").strip()
    optimized_prompt = await optimize_prompt(user_prompt)

    print("\n✅ Optimized Prompt:\n")
    print(optimized_prompt)

if __name__ == "__main__":
    asyncio.run(main())
