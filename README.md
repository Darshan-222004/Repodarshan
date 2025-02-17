# Problem Statement
A Markdown file is a text file used in GitHub for documentation. It is similar to HTML but does not use HTML syntax. Instead, it has its own formatting rules—for example, HTML uses `<h1>`, `<h2>`, and `<h3>` for headers, while Markdown uses `#`, `##`, and `###`.

Markdown files can display images, write text, create paragraphs, and include links, videos, and other media. Good prompts help AI give better answers. If a prompt is unclear, the AI might give a bad response. This tool fixes prompts by making them clear and direct.

## To Optimize Markdown Files Using AI Tools, the Tool Should Be Able to Do the Following:
1. **Convert passive voice to active voice**  
   **Example:** "The decision was made by the team." → "The team made the decision."
2. **Remove unnecessary and incomplete sentences**
3. **Eliminate first-person opinions**  
   **Example:** "I believe this tool is helpful." → "This tool helps improve writing clarity."
4. **Enhance AI Prompting Clarity**
5. **Detect vague or open-ended prompts and suggest more precise versions**  
   **Example:** "Tell me about this product." → "Summarize the key features and benefits of this product in two sentences."

## Who Will Use This Tool?
1. **Students** – Working on projects that require clear documentation and AI prompts.
2. **Content Creators & Editors** – Ensuring that software instructions and AI-generated content are clear.
3. **Project Managers** – Keeping project documentation structured and professional.
4. **AI Engineers & Prompt Designers** – Crafting well-structured prompts to get accurate AI-generated responses.

## How Will They Use It?
1. Users paste or type their text or prompt into the tool’s interface.
2. The tool scans the text for issues such as passive voice, vague statements, unclear prompts, and weasel words.
3. The tool provides optimized text with suggested improvements.
4. Alternatively, an advanced AI can layer over the Markdown file, detect errors, and apply corrections automatically.

## Example Use Cases
### **Use Case 1**
Darshan writes this in his AI prompt guide:
> "Sometimes, users might want a summary, so you could try to generate one."

The tool flags *"sometimes"* and *"might"* as weasel words and suggests:
> "If the user asks for a summary, generate a concise one."

### **Use Case 2**
Gagan writes a vague AI prompt:
> "Explain this topic."

The tool suggests a more precise prompt:
> "Summarize the main points of this topic in under 100 words."

Darshan and Gagan update their prompts and get better AI results.

## Benefits
1. **Provides Clarity** –  
   **Example:** "Some users might find this feature useful." → "Beginner users will find this feature helpful."
2. **Improves Professionalism** – Ensures documentation and AI prompts are formal and easy to understand.
3. **Optimizes AI Prompts** – Helps generate more relevant and precise AI responses.
4. **Saves Time** – Helps both writers and editors speed up their workflow.

This tool acts like a **writing coach** for Markdown files and AI prompts, ensuring clarity before content reaches developers, AI models, or end users.

### Survey of Markdown Checking Tools  

There are several tools available to check and improve Markdown files. Below is a classification:  

#### 1. Word Level (Spelling Checkers)  
- *[Typos](https://github.com/crate-ci/typos)* – Detects spelling mistakes in code and markdown.  
- *[Hunspell](https://hunspell.github.io/)* – A popular spell checker used in LibreOffice.  

#### 2. Phrase Level (Grammar & Hyperlink Checkers)  
- *[Vale](https://vale.sh/)* – A customizable style and grammar checker.  
- *[markdown-link-check](https://github.com/tcort/markdown-link-check)* – Detects broken links in Markdown files.  

#### 3. Reader Level (Clarity, Readability, Rephrasers)  
- *[WriteGood](https://github.com/btford/write-good)* – Detects weak writing (e.g., passive voice, weasel words).  
- *[Hemingway Editor](http://www.hemingwayapp.com/)* – Measures readability and suggests improvements.  

*Motivation for this Survey:*  
- Avoid reinventing the wheel.  
- Objectively evaluate our tool when it runs.









