# ChatGPT-Prompter

Python scprit that reads a prompt from a file, queries ChatGPT with it, and stores the answer in a timestamped file.

## How to run

- Create a `.env` file in the root of the repository with the following content:
```
OPENAI_KEY=<YOUR OPENAI API KEY>
MODEL=gpt-3.5-turbo
TEMPERATURE=0.6
```
- Write your prompt to the [promt.txt](prompt.txt) file
- Run `pip install -r`
- Run `python .\main.py`
- Check the [responses](responses) folder for the most recent response