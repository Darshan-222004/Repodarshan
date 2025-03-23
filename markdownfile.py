import os
import openai
import git
import shutil
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
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Adjust model as needed
        messages=[{"role": "system", "content": "You are a professional technical writer."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def clone_and_create_branch(repo_url, branch_name):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    clone_dir = f"./{repo_name}_clone"
    
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    
    repo = git.Repo.clone_from(repo_url, clone_dir)
    new_branch = repo.create_head(branch_name)
    new_branch.checkout()
    return repo, clone_dir

def commit_and_push_changes(repo, clone_dir, md_path, new_content, branch_name):
    md_full_path = os.path.join(clone_dir, md_path)
    with open(md_full_path, "w", encoding="utf-8") as file:
        file.write(new_content)
    
    repo.git.add(md_path)
    repo.git.commit(m=f"Improve {md_path} clarity and readability")
    
    print("Changes committed. Please push manually using:")
    print(f"cd {clone_dir} && git push origin {branch_name}")

def main(md_path, purpose, repo_url, branch_name="markdown-improvements"):
    md_content = fetch_markdown_content(md_path)
    prompt = generate_prompt(md_content, purpose)
    improved_md = call_openai_api(prompt)
    
    repo, clone_dir = clone_and_create_branch(repo_url, branch_name)
    commit_and_push_changes(repo, clone_dir, md_path, improved_md, branch_name)
    print("Now manually push the branch and create a pull request on GitHub.")

# Example Usage
if __name__ == "__main__":
    md_path = "README.md"  # Path to your markdown file in repo
    purpose = "Prompts should be in natural language, very specific, and purpose clear"
    repo_url = "git@github.com:yourusername/yourrepo.git"  # Use SSH instead of HTTPS
    
    main(md_path, purpose, repo_url)
