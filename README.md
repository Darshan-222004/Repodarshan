# Objective

This document describes the reason behind, and function of, a resource designed to optimize Markdown files for increased clarity and accuracy. Markdown files, which follow a particular syntax different from HTML, are primarily used on Github for documentation purposes. For example, while HTML uses `<h1>`, `<h2>`, and `<h3>` for headers, Markdown employs `#`, `##`, and `###`.

Markdown files are capable of holding different types of content - images, text, links, videos, and more. However, for AI outputs to be clear, the immense importance of properly constructed prompts cannot be overstated. Our tool is designed to improve the clarity and precision of these prompts.

## What the Tool Does:

Here are the specific functions of our optimizing tool:

1. **Active Voice Over Passive**
   It switches instances of passive voice into active voice sentences. 
   For example: "The decision was made by the team." transforms to "The team made the decision."
2. **Sentence Refinement**
   The tool identifies and gets rid of unnecessary or incomplete sentences.
3. **Objective Phrasing**
   To maintain objectivity, the tool takes out first-person statements. 
   Example: "I believe this tool is helpful." changes to "This tool helps improve writing clarity."
4. **Clarity of AI prompting**
   It fine-tunes AI prompts for increased clarity.
5. **Refining Open-Ended Queries**
   The tool transforms vague or open-ended prompts into more precise instructions to garner accurate responses. 
   Example: "Tell me about this product." revises to "Summarize the key features and benefits of this product in two sentences."

## Who will use this tool?

1. **Students**: For creating clear documentation and AI-prompting in project execution.
2. **Content Creators & Editors**: To guarantee clarity in AI-based content and software instructions.
3. **Project Managers**: To promote a professional and organized format in project documentation.
4. **AI Engineers & Prompt Designers**: To craft accurate and well-structured prompts for AI outputs.

## How to use the tool?

1. Users write their text or prompt into the user interface of the tool.
2. The tool then inspects the text for potential issues- passive voice, unclear prompts, ambiguity, and weasel words.
3. After this, the tool produces optimized text incorporating the recommended enhancements.
4. In an upgraded version, AI might automatically correct the Markdown file by recognising and amending mistakes.

## Tool Usage Examples:

**Example 1**:  
Darshan's AI prompt guide says, "Sometimes, users might want a summary, so you could try to generate one."
The tool identifies "sometimes" and "might" as weasel words and offers an alternative: "If the user asks for a summary, generate a concise one."

**Example 2**:  
Gagan writes an unclear AI prompt: "Explain this topic."
The tool recommends a more specific prompt: "Summarize the main points of this topic in under 100 words."

## Benefits of using this tool:
1. **Enhances Clarity**: A sentence like "Some users might find this feature useful." adjusts to "Beginner users will find this feature helpful."
2. **Promotes Professionalism**: Assists in crafting professional and comprehensible AI prompts and documentation.
3. **Better AI prompts**: The tool helps AI provide more accurate answers.
4. **Saves Time**: Speeds up the writing and editing process.

Think of our tool as a checklist for Markdown files and AI prompts, ensuring content is clear and precise for developers, AI models, and end users.

### Review of current Markdown enhancement tools

There are several existing tools aimed at improving Markdown files. They include:

1. **Word Level (Spelling Checkers)**  
   - *[Typos](https://github.com/crate-ci/typos)*: Detects spelling errors in code and markdown.  
   - *[Hunspell](https://hunspell.github.io/)*: A widely-used spell-checking tool in LibreOffice.
2. **Phrase Level (Grammar & Hyperlink Checkers)**  
   - *[Vale](https://vale.sh/)*: A customizable grammar and style checking tool.   
   - *[markdown-link-check](https://github.com/tcort/markdown-link-check)*: Locates broken links in Markdown files.
3. **Reader Level (Clarity, Readability, Rephrasers)**   
   - *[WriteGood](https://github.com/btford/write-good)*: Pinpoints weak language usage (e.g., passive voice, weasel words).   
   - *[Hemingway Editor](http://www.hemingwayapp.com/)*: Assesses readability and suggests improvements.   

**The need for this survey:**  
- To avoid re-inventing the wheel with our tool.  
- To have a standard measurement for our tool's performance once launched.

## Performance Criteria

Our tool needs to be capable of the following:
✅ Taking user input (a prompt).
✅ Identifying imprecise words like "sometimes", "might", or vague phrases like "Explain this topic".  
✅ Suggesting a more refined version of the prompt. 
✅ Effectively handling unusual input that does not adhere to standard patterns.
✅ Being robust enough to reject input if empty.