import sys
import os
import requests
import openai
from dotenv import load_dotenv
import re

# Load API Key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("❌ Missing OPENAI_API_KEY in .env file")

# Initialize OpenAI client (new SDK style)
client = openai.OpenAI(api_key=API_KEY)

if len(sys.argv) != 4:
    print("Usage: python md_auto_refine.py <repo_url> <mdfile> <purpose>")
    sys.exit(1)

repo_url = sys.argv[1]
md_file = sys.argv[2]
purpose = sys.argv[3]

print(f"🔗 Cloning repo: {repo_url}")
print(f"📄 Target file: {md_file}")
print(f"🎯 Purpose: {purpose}")

def fetch_markdown_file(repo_url, file_path):
    """Fetch raw markdown content from GitHub"""
    print("🔄 Fetching markdown file...")

    if not repo_url.endswith(".git"):
        repo_url += ".git"

    parts = repo_url.replace("https://github.com/", "").replace(".git", "").split("/")
    if len(parts) < 2:
        raise ValueError("❌ Invalid GitHub repo URL.")

    user, repo = parts[0], parts[1]
    raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/main/{file_path}"

    response = requests.get(raw_url)
    if response.status_code != 200:
        raise Exception(f"❌ Could not fetch file. Status code: {response.status_code}")

    return response.text

def call_openai_api(prompt):
    """Call OpenAI to improve markdown"""
    print("✨ Refining markdown using OpenAI...")

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a markdown documentation expert. Improve the formatting, clarity, and structure."},
                {"role": "user", "content": f"Improve the following README.md content:\n\n{prompt}"}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ API Error: {str(e)}"

def save_file(content, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Saved improved markdown to {path}")

def main():
    print("Fetching and refining markdown...")

    try:
        original_md = fetch_markdown_file(repo_url, md_file)
        improved_md = call_openai_api(original_md)
        save_file(improved_md, f"refined_{md_file}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
