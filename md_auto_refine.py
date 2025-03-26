import os
import openai
import git
import requests
from dotenv import load_dotenv

# Ensure Python can find the repo_utils module
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "repo_utils"))

from repo_utils.clone import clone_repo
from repo_utils.md_refine import refine_markdown
from repo_utils.puller import create_branch, update_markdown_file, commit_and_push, create_pull_request

def load_env():
    openai_env = ".env"
    github_env = "2.env"
    
    if not os.path.exists(github_env):
        raise FileNotFoundError("2.env file not found")
    if not os.path.exists(openai_env):
        raise FileNotFoundError(".env file not found")
    
    load_dotenv(github_env)
    load_dotenv(openai_env)
    
    openai_api_key = os.getenv("OPENAI_API_KEY")
    github_token = os.getenv("GITHUB_TOKEN")
    
    # Debugging
    print(f"Loaded OPENAI_API_KEY: {openai_api_key is not None}")
    print(f"Loaded GITHUB_TOKEN: {github_token is not None}")
    
    if not openai_api_key:
        raise ValueError("Missing OPENAI_API_KEY environment variable")
    if not github_token:
        raise ValueError("Missing GITHUB_TOKEN environment variable")
    
    return openai_api_key, github_token

def main():
    repo_url = "https://github.com/Darshan-222004/Repodarshan.git"
    md_file_path = "README.md"
    
    try:
        openai_api_key, github_token = load_env()
        
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        local_dir = os.path.join(os.getcwd(), repo_name)
        repo = clone_repo(repo_url, local_dir)
        
        if repo is None:
            print("Error: Could not clone the repository.")
            return
        
        full_md_path = os.path.join(local_dir, md_file_path)
        
        if not os.path.exists(full_md_path):
            print(f"Error: Markdown file '{md_file_path}' not found in the repository.")
            return
        
        with open(full_md_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        
        refined_content = refine_markdown(md_content, openai_api_key)
        
        branch_name = "markdown-refinement"
        create_branch(repo, branch_name)
        
        if update_markdown_file(repo, full_md_path, refined_content):
            commit_and_push(repo, branch_name, "Refined Markdown content")
            
            repo_owner = repo_url.split("/")[-2]
            create_pull_request(repo_owner, repo_name, branch_name, github_token)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
