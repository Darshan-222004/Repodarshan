import os
import openai
import git
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",  # Adjust model as needed
        messages=[{"role": "system", "content": "You are a professional technical writer."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def create_branch_and_update_file(repo_path, branch_name, md_path, new_content):
    repo = git.Repo(repo_path)
    repo.git.checkout("-b", branch_name)
    md_full_path = os.path.join(repo_path, md_path)
    
    with open(md_full_path, "w", encoding="utf-8") as file:
        file.write(new_content)
    
    repo.git.add(md_path)
    repo.git.commit(m=f"Improve {md_path} clarity and readability")
    
    print("Changes committed. Please push manually using:")
    print(f"cd {repo_path} && git push origin {branch_name}")

def main(md_path, purpose, repo_path, branch_name="markdown-improvements"):
    md_content = fetch_markdown_content(md_path)
    prompt = generate_prompt(md_content, purpose)
    improved_md = call_openai_api(prompt)
    
    create_branch_and_update_file(repo_path, branch_name, md_path, improved_md)
    print("Now manually push the branch and create a pull request on GitHub.")

# Example Usage
if __name__ == "__main__":
    md_path = "README.md"  # Path to your markdown file in repo
    purpose = "Prompts should be in natural language, very specific, and purpose clear"
    repo_path = "."  # Local path to the repo
    
    main(md_path, purpose, repo_path)
