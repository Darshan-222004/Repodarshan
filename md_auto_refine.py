import os
import openai
import git
import requests
import logging
from dotenv import load_dotenv

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_env():
    load_dotenv(".env")
    load_dotenv("2.env")
    
    openai_api_key = os.getenv("OPENAI_API_KEY")
    github_token = os.getenv("GITHUB_TOKEN")
    
    if not openai_api_key:
        raise ValueError("Missing OPENAI_API_KEY environment variable")
    if not github_token:
        raise ValueError("Missing GITHUB_TOKEN environment variable")
    
    return openai_api_key, github_token

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
    
    try:
        client = openai.OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Error in OpenAI API call: {e}")
        return md_content  # Return original content on failure

def clone_repo(repo_url, local_dir):
    if os.path.exists(local_dir):
        logging.info("Repository already cloned.")
        return git.Repo(local_dir)
    try:
        logging.info(f"Cloning repository from {repo_url} to {local_dir}...")
        return git.Repo.clone_from(repo_url, local_dir)
    except Exception as e:
        logging.error(f"Error cloning repo: {e}")
        return None

def create_branch(repo, branch_name):
    try:
        if branch_name in [b.name for b in repo.branches]:
            logging.info(f"Branch '{branch_name}' already exists. Checking out...")
            repo.git.checkout(branch_name)
            return
        
        if branch_name in [ref.name.split('/')[-1] for ref in repo.remote().refs]:
            logging.info(f"Branch '{branch_name}' exists remotely. Creating a local tracking branch.")
            repo.git.checkout('-b', branch_name, f'origin/{branch_name}')
            repo.git.pull('origin', branch_name)
            return
        
        logging.info(f"Creating new branch '{branch_name}' and switching to it.")
        repo.git.checkout('-b', branch_name)
    except git.exc.GitCommandError as e:
        logging.error(f"Error handling branch: {e}")
        raise

def update_markdown_file(repo, file_path, refined_content):
    if not os.path.exists(file_path):
        logging.error(f"Error: Markdown file '{file_path}' does not exist.")
        return False
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(refined_content)
    repo.git.add(file_path)
    return True

def commit_and_push(repo, branch_name, commit_message):
    try:
        if not repo.is_dirty():
            logging.info("No changes to commit.")
            return
        repo.git.commit('-m', commit_message)
        origin = repo.remote(name='origin')
        origin.push(branch_name)
        logging.info(f"Changes pushed to branch '{branch_name}'")
    except Exception as e:
        logging.error(f"Error during commit/push: {e}")

def create_pull_request(repo_owner, repo_name, branch_name, github_token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    headers = {"Authorization": f"token {github_token}", "Accept": "application/vnd.github.v3+json"}
    data = {
        "title": "Refined Markdown Content",
        "head": branch_name,
        "base": "main",
        "body": "This PR improves the markdown file for clarity, specificity, and natural language."
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 201:
            logging.info("Pull Request Created: " + response.json().get("html_url"))
        else:
            logging.error("Failed to create Pull Request: " + str(response.json()))
    except Exception as e:
        logging.error(f"Error creating pull request: {e}")

def main():
    setup_logging()
    repo_url = "https://github.com/Darshan-222004/Repodarshan.git"
    md_file_path = "README.md"
    
    try:
        openai_api_key, github_token = load_env()
        
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        local_dir = os.path.join(os.getcwd(), repo_name)
        repo = clone_repo(repo_url, local_dir)
        
        if repo is None:
            logging.error("Error: Could not clone the repository.")
            return
        
        full_md_path = os.path.join(local_dir, md_file_path)
        
        if not os.path.exists(full_md_path):
            logging.error(f"Error: Markdown file '{md_file_path}' not found in the repository.")
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
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
