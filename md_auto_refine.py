import os
import git
import openai
import requests
from dotenv import load_dotenv

def load_env():
    if not os.path.exists(".env"):
        raise FileNotFoundError(".env file not found")
    if not os.path.exists("2.env"):
        raise FileNotFoundError("2.env file not found")
    
    load_dotenv(".env")  # Load OpenAI key
    load_dotenv("2.env")  # Load GitHub token

    openai_api_key = os.getenv("OPENAI_API_KEY")
    github_token = os.getenv("GITHUB_TOKEN")

    if not openai_api_key:
        raise ValueError("Missing OPENAI_API_KEY environment variable")
    if not github_token:
        raise ValueError("Missing GITHUB_TOKEN environment variable")

    return openai_api_key, github_token

def clone_repo(repo_url, local_dir):
    if os.path.exists(local_dir):
        print("Repository already cloned.")
        return git.Repo(local_dir)
    try:
        print(f"Cloning repository from {repo_url} to {local_dir}...")
        return git.Repo.clone_from(repo_url, local_dir)
    except Exception as e:
        print(f"Error cloning repo: {e}")
        return None

def create_branch(repo, branch_name):
    try:
        local_branches = [b.name for b in repo.branches]

        if branch_name in local_branches:
            print(f"Branch '{branch_name}' already exists. Checking out...")
            repo.git.checkout(branch_name)
            return
        
        print(f"Creating new branch '{branch_name}' and switching to it.")
        repo.git.checkout('-b', branch_name)
    
    except git.exc.GitCommandError as e:
        print(f"Error handling branch: {e}")
        raise

def refine_markdown(md_content, openai_api_key):
    prompt = f"""
    Convert the following Markdown content to be:
    1. Clear in purpose
    2. Very specific
    3. Written in natural language
    
    Content:
    {md_content}
    
    Refined version:
    """
    
    client = openai.OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def update_markdown_file(repo, file_path, refined_content):
    if not file_path.endswith("README.md"):
        print("Error: Attempted to modify a file other than README.md")
        return False
    if not os.path.exists(file_path):
        print(f"Error: Markdown file '{file_path}' does not exist.")
        return False
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(refined_content)
    repo.git.add(file_path)
    return True

def commit_and_push(repo, branch_name, commit_message):
    try:
        repo.git.commit('-m', commit_message)
        origin = repo.remote(name='origin')
        origin.push(branch_name)
        print(f"Changes pushed to branch '{branch_name}'")
    except Exception as e:
        print(f"Error during commit/push: {e}")

def create_pull_request(repo_owner, repo_name, branch_name, github_token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    headers = {"Authorization": f"Bearer {github_token}", "Accept": "application/vnd.github.v3+json"}
    data = {
        "title": "Refined README.md Content",
        "head": branch_name,
        "base": "main",
        "body": "This PR improves the README.md file for clarity, specificity, and natural language."
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print("Pull Request Created:", response.json().get("html_url"))
    else:
        print("Failed to create Pull Request:", response.json())

if __name__ == "__main__":
    repo_url = "https://github.com/Darshan-222004/Repodarshan.git"
    md_file_path = "README.md"
    
    try:
        openai_api_key, github_token = load_env()
        
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        local_dir = os.path.join(os.getcwd(), repo_name)
        repo = clone_repo(repo_url, local_dir)
        
        if repo is None:
            print("Error: Could not clone the repository.")
            exit(1)
        
        full_md_path = os.path.join(local_dir, md_file_path)
        
        if not os.path.exists(full_md_path):
            print(f"Error: Markdown file '{md_file_path}' not found in the repository.")
            exit(1)
        
        with open(full_md_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        
        refined_content = refine_markdown(md_content, openai_api_key)
        
        branch_name = "markdown-refinement"
        create_branch(repo, branch_name)
        
        if update_markdown_file(repo, full_md_path, refined_content):
            commit_and_push(repo, branch_name, "Refined README.md content")
            
            repo_owner = repo_url.split("/")[-2]
            create_pull_request(repo_owner, repo_name, branch_name, github_token)
    except Exception as e:
        print(f"An error occurred: {e}")
