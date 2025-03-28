import os
import git
import requests
from dotenv import load_dotenv

def load_env():
    if not os.path.exists(".env"):
        raise FileNotFoundError(".env file not found")
    if not os.path.exists("2.env"):
        raise FileNotFoundError("2.env file not found")
    
    load_dotenv(".env")  # Load OpenAI key
    load_dotenv("2.env")  # Load GitHub token

    github_token = os.getenv("GITHUB_TOKEN")

    if not github_token:
        raise ValueError("Missing GITHUB_TOKEN environment variable")
    
    return github_token

def commit_and_push(repo, branch_name, commit_message):
    try:
        if not repo.is_dirty(untracked_files=True):
            print("No changes detected in the repository. Skipping commit.")
            return
        
        repo.git.add(A=True)
        repo.git.commit('-m', commit_message)
        origin = repo.remote(name='origin')
        origin.push(branch_name)
        print(f"Changes successfully pushed to '{branch_name}'")
    except Exception as e:
        print(f"Error during commit/push: {e}")

def create_pull_request(repo_owner, repo_name, branch_name, github_token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    headers = {"Authorization": f"Bearer {github_token}", "Accept": "application/vnd.github.v3+json"}
    data = {
        "title": "Refined README.md Content",
        "head": branch_name,
        "base": "main",
        "body": "This PR improves the README.md file for clarity and professionalism."
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print("Pull Request Created:", response.json().get("html_url"))
    else:
        print("Failed to create Pull Request:", response.json())

if __name__ == "__main__":
    repo_url = "https://github.com/Darshan-222004/Repodarshan.git"
    branch_name = "md_refine_2"
    commit_message = "Refined README.md content"

    try:
        github_token = load_env()
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        local_dir = os.path.join(os.getcwd(), repo_name)
        repo = git.Repo(local_dir)
        
        commit_and_push(repo, branch_name, commit_message)
        repo_owner = repo_url.split("/")[-2]
        create_pull_request(repo_owner, repo_name, branch_name, github_token)
    except Exception as e:
        print(f"An error occurred: {e}")
