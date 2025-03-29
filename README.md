# Goal

Our goal is to enhance the use of Markdown files, commonly employed on GitHub for documentation needs. Markdown has a unique syntax compared to HTML, using characters such as `#`, `##`, `###` for headings rather than `<h1>`, `<h2>`, `<h3>`. Markdown files encompass a range of media types including images, videos, and text. To provide a superior user experience, we trust upon carefully crafted prompts to guide AI in generating suitable responses. Our proposed tool will guarantee these prompts are clear, concise, and meaningful.

## Specific Criteria for Perfecting Markdown Files

The tool we recommend should be capable of:

1. Converting passive voice to active voice. For example, it should change "The decision was made by the team" to "The team made the decision."
2. Recognizing and deleting unnecessary and incomplete sentences.
3. Avoiding first-person subjective views. For example, "I believe this tool is helpful" should be altered to "This tool aids in enhancing writing clarity".
4. Boosting the transparency of AI prompts.
5. Pinpointing ambiguous or broad prompts and recommend more specific alternatives. For instance, a vague query like "Tell me about this product" should be refined to "Summarize the key features and benefits of this product in two sentences."

## Anticipated Users of Our Tool

The tool will prove advantageous for:

1. **Students** – who require precise documentation and AI prompts for their projects.
2. **Content Creators & Editors** – who can utilize the tool to assure clarity in software guidelines and AI-generated content.
3. **Project Managers** – aiming for systematic, professional project documentation.
4. **AI Engineers & Prompt Designers** – working on developing clear and properly structured prompts that evoke precise AI responses.

## Usage Method

To use this tool:

1. Users input their text or prompt into the specified interface.
2. The tool reviews the text for potential weaknesses such as passive voice, imprecise statements, unclear prompts, and weasel word usage.
3. The tool then provides a polished version of the text with suggestions for improvements.
4. An advanced AI can further be utilized to comb through the Markdown file, spot errors, and automatically apply corrections.

## Real-world Applications

Take into account the below scenarios:

If Darshan submits an AI prompt guide that states "Sometimes, users might want a summary, so you could try to generate one", our tool will recognize "sometimes" and "might" as indicative of uncertainty. The tool would then recommend a stronger directive, such as "If the user requests a summary, produce a brief one."

Another example: if Gagan inputs a generic AI prompt like "Explain this topic", the tool would suggest a more exact prompt like "Summarize the main points of this topic in under 100 words." These tweaked prompts would enable more accurate AI outcomes.

## Primary Advantages

This tool extends:

1. Increased clarity, by rephrasing statements like "Some users might find this feature useful" to become "Beginner users will find this feature helpful".
2. Greater professionalism, guaranteeing all documentation and AI prompts maintain formality and are effortlessly understood.
3. More targeted AI prompts, resulting in more pertinent and accurate AI outputs.
4. Time-efficiency, thereby enhancing the productivity of writers and editors.

In short, our tool functions as a writing mentor, augmenting the clarity, correctness, and user-friendliness of markdown files and AI prompts.

## Markdown Checking Tools Currently Available

Several tools already exist to check and refine Markdown files including spellcheck tools like [Typos](https://github.com/crate-ci/typos) and [Hunspell](https://hunspell.github.io/), grammar verification like [Vale](https://vale.sh/) and [markdown-link-check](https://github.com/tcort/markdown-link-check), and clarity and readability assessment like [WriteGood](https://github.com/btford/write-good) and [Hemingway Editor](http://www.hemingwayapp.com/). We mention these to avoid replication of efforts and to evaluate the effectiveness of our tool.

## Required Functionalities

For our tool to be deemed effective, it should be able to:

✅ Receive a user's input (a prompt).  
✅ Identify and highlight weak words or ambiguous phrases.  
✅ Propose an improved version of the prompt.  
✅ Manage instances when the input does not follow typical patterns.  
✅ Prevent submission of empty input.