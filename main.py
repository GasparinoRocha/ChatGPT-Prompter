import openai
from os import getenv
from dotenv.main import load_dotenv
import pandas

load_dotenv()

openai.api_key = getenv('OPENAI_KEY')

def get_completion(prompt):

    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=getenv('MODEL'),
        messages=messages,
        temperature=float(getenv('TEMPERATURE')),
    )

    return response.choices[0].message["content"]

def query_prompts(filename):
    df = pandas.read_csv(filename)

    df['Response'] = df.apply(lambda row : get_completion(row["Prompt"]), axis = 1)

    df.to_csv(filename, index=False)

query_prompts("prompts.csv")