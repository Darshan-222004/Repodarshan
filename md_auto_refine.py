import os
import openai
import git
import requests
from dotenv import load_dotenv

# Load environment variables from .env or GitHub Secrets
load_dotenv()

# Set these explicitly or via GitHub Secrets
GITHUB_REPO = "Darshan-222004/Repodarshan"  # Format: username/repo
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")    # Add this in GitHub Secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Add this in GitHub Secrets

# Replace these based on your repo
repo_url = "https://github.com/Darshan-222004/Repodarshan"
repo_path = "."  # This assumes GitHub Actions checks out the repo root
md_path = "README.md"  # Relative to root
purpose = "Prompts should be in natural language, very specific, and purpose clear"
branch_name = "file_modification"

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY

def generate_prompt(md_content, purpose):
    return f"""
    The following Markdown document was written for this purpose: {purpose}
    Improve its clarity, conciseness, and readability while preserving the original intent.
    Ensure the prompts are in natural language, highly specific, and clearly state their purpose.
    Maintain proper formatting, grammar, and logical flow.
    Here is the content:
    {md_content}
    """

def fetch_markdown_content(md_path):
    with open(md_path, "r", encoding="utf-8") as file:
        return file.read()

def call_openai_api(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional technical writer."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

def create_branch_and_update_file(repo_path, branch_name, md_path, new_content):
    repo = git.Repo(repo_path)
    if branch_name in repo.heads:
        repo.git.checkout(branch_name)
    else:
        repo.git.checkout("-b", branch_name)

    md_full_path = os.path.join(repo_path, md_path)
    with open(md_full_path, "w", encoding="utf-8") as file:
        file.write(new_content)

    repo.git.add(md_path)
    repo.git.commit(m=f"Improve {md_path} clarity and readability")
    repo.git.push("origin", branch_name)

def create_pull_request(branch_name):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/pulls"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": "Improve README.md clarity",
        "head": branch_name,
        "base": "main",
        "body": "This PR improves the clarity and readability of the README file."
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"✅ Pull request created successfully: {response.json()['html_url']}")
    else:
        print(f"❌ Failed to create pull request: {response.json()}")

def main():
    print("Fetching and refining markdown...")
    md_content = fetch_markdown_content(md_path)
    prompt = generate_prompt(md_content, purpose)
    improved_md = call_openai_api(prompt)

    print("Creating branch and updating file...")
    create_branch_and_update_file(repo_path, branch_name, md_path, improved_md)
    
    print("Creating pull request...")
    create_pull_request(branch_name)

# Run the script automatically (no input)
if __name__ == "__main__":
    main()
