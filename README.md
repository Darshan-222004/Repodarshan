# Objective

We aim to optimize the use of markdown files as commonly used in GitHub for documentation purposes. Unlike HTML syntax, markdown utilizes its unique syntax, such as `#`, `##`, `###` for headings instead of `<h1>`, `<h2>`, `<h3>`. Markdown files can incorporate various forms of media including images, video links, and other text entries. For a satisfactory user experience, it is crucial to have clearly framed prompts to guide AI towards generating appropriate responses. The tool we're proposing will ensure these prompts are clear, concise and directly to the point.

## Detailed Requirements for Optimizing Markdown Files

The proposed tool should be able to:

1. Transform passive voice to active voice. For example, it should convert "The decision was made by the team" to "The team made the decision."
2. Identify and remove redundant and incomplete sentences.
3. Eliminate the usage of first-person opinions. For instance, "I believe this tool is helpful" should be modified to "This tool aids in enhancing writing clarity".
4. Improve the clarity of AI prompting.
5. Detect ambiguous or open-ended prompts and suggest more specific variants. For example, a vague request like "Tell me about this product" should be narrowed down to "Summarize the key features and benefits of this product in two sentences."

## Potential Users of This Tool

This tool will be beneficial for:

1. **Students** – needing clear documentation and AI prompts for their projects.
2. **Content Creators & Editors** – employing the tool to ensure the clarity of software instructions and AI-generated content.
3. **Project Managers** – to maintain organized, professional project documentation.
4. **AI Engineers & Prompt Designers** – developing lucid, well-structured prompts that garner precise AI-generated responses.

## Method of Usage

To apply this tool:

1. Users enter their text or prompt into the designated interface.
2. The tool scrutinizes the text for weak areas such as passive voice, vague statements, unclear prompts, and usage of weasel words.
3. The tool then produces an optimized version of the text with suggested improvements.
4. An advanced AI can also be employed to trawl through the Markdown file, identify errors, and automatically implement corrections.

## Practical Applications

Consider the following scenarios:

If Darshan types in his AI prompt guide that "Sometimes, users might want a summary, so you could try to generate one", our tool will detect "sometimes" and "might" as uncertain words. The tool would then suggest a more robust command, such as "If the user requests a summary, produce a succinct one."

Another example: if Gagan creates a vague AI prompt like "Explain this topic", the tool would recommend a more descriptive prompt such as "Summarize the main aspects of this topic in less than 100 words." These refined prompts would facilitate more accurate AI responses.

## Key Benefits

The tool offers:

1. Enhanced clarity, by transforming statements like "Some users might find this feature useful" to become "Beginner users will find this feature helpful".
2. Improved professionalism, ensuring all documentation and AI prompts maintain formality and are easily understood.
3. More effective AI prompts, leading to more relevant and accurate AI responses.
4. Time-saving capabilities, boosting the productivity of writers and editors alike.

In essence, our tool operates as a writing coach, streamlining the clarity, accuracy, and user-friendliness of markdown files and AI prompts.

## Existing Markdown Checking Tools  

Several tools are currently available for checking and improving Markdown files, including spelling checkers like [Typos](https://github.com/crate-ci/typos) and [Hunspell](https://hunspell.github.io/), grammar checkers like [Vale](https://vale.sh/) and [markdown-link-check](https://github.com/tcort/markdown-link-check), and clarity and readability analyzers like [WriteGood](https://github.com/btford/write-good) and [Hemingway Editor](http://www.hemingwayapp.com/). These exist to avoid duplicating efforts and to gauge our tool's effectiveness.

## Expected Capabilities 

To be considered effective, the tool should be able to:

✅ Accept a user's input (a prompt).  
✅ Spot and highlight weak words or vague phrases.  
✅ Provide an improved version of the prompt.  
✅ Handle instances when the input does not align with typical patterns.  
✅ Disallow submission of empty input.