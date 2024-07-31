
<!-- Edit README.md, not index.md -->

# RobotChat is AI pair programming in your terminal for robots

RobotChat (based on Aider) lets you pair program with LLMs,
to edit code in your local git repository.
Start a new project or work with an existing git repo.
RobotChat works best with GPT-4o & Claude 3.5 Sonnet and can
[connect to almost any LLM](https://aider.chat/docs/llms.html).

## Getting started
<!--[[[cog
# We can't "include" here.
# Because this page is rendered by GitHub as the repo README
cog.out(open("aider/website/_includes/get-started.md").read())
]]]-->

You can get started quickly like this:

```
$ pip install robot-chat

# Change directory into a git repo
$ cd /to/your/git/repo

# Work with Claude 3.5 Sonnet on your repo
$ export ANTHROPIC_API_KEY=your-key-goes-here
$ aider

# Work with GPT-4o on your repo
$ export OPENAI_API_KEY=your-key-goes-here
$ aider
```
<!--[[[end]]]-->

See the
[installation instructions](https://aider.chat/docs/install.html)
and other
[documentation](https://aider.chat/docs/usage.html)
for more details.

## Features

- Run robotchat with the files you want to edit: `robotchat <file1> <file2> ...`
- Ask for changes:
  - Add new features or test cases.
  - Describe a bug.
  - Paste in an error message or or GitHub issue URL.
  - Refactor code.
  - Update docs.
- RobotChat will edit your files to complete your request.
- RobotChat [automatically git commits](https://aider.chat/docs/git.html) changes with a sensible commit message.
- RobotChat works with [most popular languages](https://aider.chat/docs/languages.html): python, javascript, typescript, php, html, css, and more...
- RobotChat works best with GPT-4o & Claude 3.5 Sonnet and can [connect to almost any LLM](https://aider.chat/docs/llms.html).
- RobotChat can edit multiple files at once for complex requests.
- RobotChat uses a [map of your entire git repo](https://aider.chat/docs/repomap.html), which helps it work well in larger codebases.
- Edit files in your editor while chatting with aider,
and it will always use the latest version.
Pair program with AI.
- [Add images to the chat](https://aider.chat/docs/usage/images-urls.html) (GPT-4o, Claude 3.5 Sonnet, etc).
- [Add URLs to the chat](https://aider.chat/docs/usage/images-urls.html) and aider will read their content.
- [Code with your voice](https://aider.chat/docs/usage/voice.html).
