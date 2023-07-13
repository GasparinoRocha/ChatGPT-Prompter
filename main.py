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

def load_csv_file(filename):
    df = pandas.read_csv(filename)
    print(df)

    df['Response'] = df.apply(lambda row : get_completion(row["Prompt"]), axis = 1)
    print(df)

    df.to_csv(filename, index=False)

load_csv_file("prompts.csv")