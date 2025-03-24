import os
import openai
import git
import requests
from dotenv import load_dotenv

def load_env():
    load_dotenv(".env")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    load_dotenv("2.env")
    github_token = os.getenv("GITHUB_TOKEN")
    return openai_api_key, github_token

def refine_markdown(md_content):
    prompt = f"""
    Convert the following Markdown content to be:
    1. Clear in purpose
    2. Very specific
    3. Written in natural language
    
    Content:
    {md_content}
    
    Refined version:
    """
    
    client = openai.OpenAI(api_key=openai.api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def clone_repo(repo_url, local_dir):
    if os.path.exists(local_dir):
        print("Repository already cloned.")
        return git.Repo(local_dir)
    return git.Repo.clone_from(repo_url, local_dir)

def create_branch(repo, branch_name):
    repo.git.checkout('-b', branch_name)

def update_markdown_file(repo, file_path, refined_content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(refined_content)
    repo.git.add(file_path)

def commit_and_push(repo, branch_name, commit_message):
    repo.git.commit('-m', commit_message)
    origin = repo.remote(name='origin')
    origin.push(branch_name)

def create_pull_request(repo_owner, repo_name, branch_name, github_token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    headers = {"Authorization": f"token {github_token}", "Accept": "application/vnd.github.v3+json"}
    data = {
        "title": "Refined Markdown Content",
        "head": branch_name,
        "base": "main",
        "body": "This PR improves the markdown file for clarity, specificity, and natural language."
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def main():
    repo_url = "https://github.com/Darshan-222004/Repodarshan.git"
    md_file_path = "README.md"
    
    openai_api_key, github_token = load_env()
    openai.api_key = openai_api_key
    
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    local_dir = f"./{repo_name}"
    repo = clone_repo(repo_url, local_dir)
    
    full_md_path = os.path.join(local_dir, md_file_path)
    with open(full_md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    refined_content = refine_markdown(md_content)
    
    branch_name = "markdown-refinement"
    create_branch(repo, branch_name)
    update_markdown_file(repo, full_md_path, refined_content)
    commit_and_push(repo, branch_name, "Refined Markdown content")
    
    repo_owner = repo_url.split("/")[-2]
    pr_response = create_pull_request(repo_owner, repo_name, branch_name, github_token)
    print("Pull Request Created:", pr_response.get("html_url"))

if __name__ == "__main__":
    main()
