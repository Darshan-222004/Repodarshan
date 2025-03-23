# Introduction
Markdown format, a text file type leveraged in GitHub for documentation, has its unique syntax distinct from HTML. It supports a range of multimedia possibilities, including images, text paragraphs, links, videos, and other types of media. This document provides guidelines on refining prompts to drive better responses from AI. Harnessing AI for clarity and precision is the main objective of this tool.

# The Tool’s Capabilities
To optimize Markdown files, the AI tool should be capable of:

1. Transforming passive voice to active voice.  
   **Example**: "The decision was made by the team." becomes "The team made the decision."
2. Trimming superfluous and partial sentences.
3. Omitting first-person perspectives.  
   **Example**: "I believe this tool is helpful." becomes "This tool is beneficial to writing clarity."
4. Augmenting AI prompt clarity.
5. Identifying vague or open-ended prompts and providing more precise rekajiggers.  
   **Example**: "Tell me about this product." changes to "Define the key features and benefits of this product in two sentences." 

## Intended Users 

The AI tool is designed for:
1. **Students**: Facilitating clear project documentation and AI prompts.
2. **Content Creators & Editors**: Ensuring intelligible software instructions and AI-generated content.
3. **Project Managers**: Maintaining organized, professional project documentation.
4. **AI Engineers & Prompt Designers**: Constructing well-framed prompts for precise AI-generated responses.

## Usage Procedure

1. Users enter their text or prompt into the tool’s interface.
2. The tool reviews the text for issues such as passive voice, unclear statements, vague prompts, and weak words.
3. The tool presents an enhanced version of the text with suggested improvements.
4. An advanced AI option is available, which overlays the Markdown file, identifies errors and applies automatic corrections.

## Example Scenarios

### **Scenario 1**
Darshan types his AI prompt guide as:
> "Sometimes, users might want a summary, so you could try to generate one."

The tool marks *"sometimes"* and *"might"* as weak words and proposes:
> "Generate a concise summary when a user request is made."

### **Scenario 2**
Gagan prompts a vague AI command:
> "Explain this topic."

The tool refines the prompt:
> "Summarize this topic’s main points in under 100 words."

With adjusted prompts, Darshan and Gagan achieve superior AI outcomes.

## Key Benefits

1. **Improves Clarity**: For example, "Some users might find this feature useful." becomes "This feature is most useful to beginner users."
2. **Enhances Professionalism**: Documentation and AI prompts are easy to understand.
3. **Optimizes AI Prompts**: More precise AI responses.
4. **Time Efficient**: Expedited workflow for writers and editors.

This tool functions as a Markdown and AI prompt **writing coach**, assuring clarity before delivery to developers, AI models, or end users.

## Markdown Checking Tools Survey
Several tools are available to scrutinize and enhance Markdown files:

#### 1. Word Level (Spelling Checkers)
- *[Typos](https://github.com/crate-ci/typos)*: Identifies spelling errors in code and markdown.
- *[Hunspell](https://hunspell.github.io/)*: A mainstay in LibreOffice as a spell checker.

#### 2. Phrase Level (Grammar & Hyperlink Checkers)
- *[Vale](https://vale.sh/)*: Operates as a flexible style and grammar checker.
- *[markdown-link-check](https://github.com/tcort/markdown-link-check)*: Spot broken links in Markdown files.

#### 3. Reader Level (Clarity, Readability, Rephrasers)
- *[WriteGood](https://github.com/btford/write-good)*: Scrutinizes weak writing patterns like passive voice and weasel words.
- *[Hemingway Editor](http://www.hemingwayapp.com/)*: Assesses readability and suggests enhancements.

Survey Objective: 
- To prevent needlessly reinventing the wheel.
- Enable objective evaluation of our tool during operation.

## Definitive Acceptance Criteria
The tool should:

✔ Accept user prompt as input.  
✔ Spot weak indicators such as  "**sometimes**", "**might**", and hazy statements like "**Explain this topic**".  
✔ Propose a refined version of the prompt.  
✔ Cater to inputs even if they do not match preset patterns.  
✔ Reject empty input. 
