import os
import git
from dotenv import load_dotenv

def load_env():
    if not os.path.exists("2.env"):
        raise FileNotFoundError("2.env file not found")
    
    load_dotenv("2.env")  # Load GitHub token
    github_token = os.getenv("GITHUB_TOKEN")
    
    if not github_token:
        raise ValueError("Missing GITHUB_TOKEN environment variable")
    
    return github_token

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

if __name__ == "__main__":
    repo_url = "https://github.com/Darshan-222004/Repodarshan.git"
    
    try:
        github_token = load_env()
        
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        local_dir = os.path.join(os.getcwd(), repo_name)
        repo = clone_repo(repo_url, local_dir)
        
        if repo is None:
            print("Error: Could not clone the repository.")
            exit(1)
        
        print("Repository cloned successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
