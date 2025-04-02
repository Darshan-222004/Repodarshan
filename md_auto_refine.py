
import os
import git
import openai
import chardet
import fitz  # PyMuPDF for PDF handling
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
        if branch_name in repo.branches:
            print(f"Branch '{branch_name}' already exists. Checking out...")
            repo.git.checkout(branch_name)
            return
        print(f"Creating new branch '{branch_name}' and switching to it.")
        repo.git.checkout('-b', branch_name)
    except git.exc.GitCommandError as e:
        print(f"Error handling branch: {e}")
        raise

def detect_encoding(file_path):
    with open(file_path, "rb") as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result["encoding"]

def read_file(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    encoding = detect_encoding(file_path)
    with open(file_path, "r", encoding=encoding, errors="ignore") as f:
        return f.read()

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text("text") for page in doc)
    return text.strip()

def refine_content(file_content, user_instruction, openai_api_key):
    prompt = f"""
    Based on the following user instructions: {user_instruction}, modify the given content accordingly.
    
    Original Content:
    {file_content}
    
    Modified Content:
    """
    
    client = openai.OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def update_file(repo, file_path, refined_content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(refined_content)
    repo.git.add(file_path)
    return True

def commit_and_push(repo, branch_name, commit_message):
    try:
        if not repo.is_dirty(untracked_files=True):
            print("No changes detected in the repository.")
            return
        repo.git.commit('-m', commit_message)
        repo.remote(name='origin').push(branch_name)
        print(f"Changes pushed to '{branch_name}'")
    except Exception as e:
        print(f"Error during commit/push: {e}")

if __name__ == "__main__":
    repo_url = input("Enter the GitHub repository URL: ")
    file_path = input("Enter the path of the file you want to modify (relative to repo root): ")
    user_instruction = input("Describe how you want the file to be modified: ")
    
    try:
        openai_api_key, github_token = load_env()
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        local_dir = os.path.join(os.getcwd(), repo_name)
        repo = clone_repo(repo_url, local_dir)
        
        if repo is None:
            print("Error: Could not clone the repository.")
            exit(1)
        
        full_file_path = os.path.join(local_dir, file_path)
        if not os.path.exists(full_file_path):
            print(f"Error: File '{file_path}' not found.")
            exit(1)
        
        file_content = read_file(full_file_path)
        refined_content = refine_content(file_content, user_instruction, openai_api_key)
        
        branch_name = "file_modification"
        create_branch(repo, branch_name)
        
        if update_file(repo, full_file_path, refined_content):
            commit_and_push(repo, branch_name, f"Updated {file_path} based on user instructions")
    except Exception as e:
        print(f"An error occurred: {e}")
