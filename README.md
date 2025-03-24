# Purpose

This document outlines the need and function of a tool that optimizes Markdown files. Markdown files are used on Github for documentation, similar in nature to HTML, but using a different syntax. For instance, HTML employs `<h1>`, `<h2>`, and `<h3>` for headers, whereas Markdown uses `#`, `##`, and `###`.

Markdown files encapsulate and present various forms of content like images, text, paragraphs, links, videos, and other media. However, achieving clarity in AI-generated responses often depends on well-formed prompts. Our tool directly addresses this issue by refining prompts to make them clear and concise.

## Core Functions of the Tool:

Our optimizing tool works in the following ways:

1. **Active Voice Over Passive**  
   Changes instances of passive voice to active. 
   Example: "The decision was made by the team." transforms to "The team made the decision."
2. **Sentence Refinement**  
   Extracts and deletes unnecessary or incomplete sentences.
3. **Objective Phrasing**  
   Excluding first-person statements to maintain objectivity. 
   Example: "I believe this tool is helpful." changes to "This tool helps improve writing clarity."
4. **Clarity of AI prompting**  
   Finesse AI prompts for better clarity.
5. **Refining Open-Ended Queries**  
   Amends vague or open-ended prompts to prompt more accurate responses. 
   Example: "Tell me about this product." revises to "Summarize the key features and benefits of this product in two sentences."

## Potential Users
1. **Students**: For clear documentation and AI promptings in projects.
2. **Content Creators & Editors**: To ensure clarity in software instructions and AI-content.
3. **Project Managers**: To enhance structure and professionalism in project documentation.
4. **AI Engineers & Prompt Designers**: To design accurate, structured prompts for AI responses.

## Usage Procedure

1. Users enter their text or prompt into the tool’s user interface.
2. The tool investigates the text for potential issues- passive voice, ambiguity, unclear prompts, and weasel words.
3. The tool generates optimized text with recommended improvements.
4. In an advanced version, AI could automatically rectify the Markdown file by identifying mistakes and making suitable corrections.

## Application Instances

**Use Case 1**  
Darshan's AI prompt guide has this: "Sometimes, users might want a summary, so you could try to generate one."
The tool identifies "sometimes" and "might" as weasel words and suggests an alternative: "If the user asks for a summary, generate a concise one."

**Use Case 2**  
Gagan writes a vague AI prompt: "Explain this topic."
The tool suggests a more detailed prompt: "Summarize the main points of this topic in under 100 words."

## Benefits
1. **Enhances Clarity**: 
   For instance, "Some users might find this feature useful." adjusts to "Beginner users will find this feature helpful."
2. **Promotes Professionalism**: Helps maintain formal, understandable AI prompts and documentation.
3. **Better AI prompts**: Aid the AI to give more precise responses.
4. **Saves Time**: Speed up processes for writers and editors.

Our tool works like a checklist for Markdown files and AI prompts, ensuring clear, precise content for developers, AI models, and users.

### Review of Existing Markdown Checking Tools  

Numerous tools are available to rectify and improve Markdown files. We categorized them as follows:

1. **Word Level (Spelling Checkers)**  
   - *[Typos](https://github.com/crate-ci/typos)*: It detects spelling errors in code and markdown.  
   - *[Hunspell](https://hunspell.github.io/)*: A widely-used spell checker in LibreOffice.
2. **Phrase Level (Grammar & Hyperlink Checkers)**  
   - *[Vale](https://vale.sh/)*: A customizable style and grammar checking tool.  
   - *[markdown-link-check](https://github.com/tcort/markdown-link-check)*: It identifies broken links in Markdown files.
3. **Reader Level (Clarity, Readability, Rephrasers)**  
   - *[WriteGood](https://github.com/btford/write-good)*: It identifies weak language usage (e.g., passive voice, weasel words).  
   - *[Hemingway Editor](http://www.hemingwayapp.com/)*: Evaluates readability and suggests improvements.  

**Reason for this Survey:**  
- To innovate prudently without repetition  
- To gauge our tool performance objectively upon launching.

## Performance Checklist

Our tool should be able to:
✅ Accept user input (a prompt).  
✅ Pinpoint weak words like "sometimes", "might", or vague phrases like "Explain this topic".  
✅ Suggest a more refined version of the prompt.  
✅ Appropriate handling of anomalous input not fitting standard patterns.  
✅ Robust enough to refuse empty input.