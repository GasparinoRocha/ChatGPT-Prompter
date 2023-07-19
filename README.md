# ChatGPT-Prompter

Python scprit that reads a prompt from a file, queries ChatGPT with it, and stores the answer in a timestamped file.

## How to run

- Create a `.env` file in the root of the repository with the following content:
```
OPENAI_KEY=<YOUR OPENAI API KEY>
MODEL=gpt-3.5-turbo
TEMPERATURE=0.6
```
- Add your prompts to the [prompts.csv](prompts.csv) file
- Run `pip install -r requirements.txt`
- Run `python .\main.py`
- The [responses.csv](responses.csv) file will have been filled in with the responses