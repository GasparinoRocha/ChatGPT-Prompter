import openai
from os import getenv
from dotenv.main import load_dotenv
import pandas
import time

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

def query_prompts(prompts_filename, responses_filename):
    df = pandas.read_csv(prompts_filename)
    df = df.fillna("")

    # df['Response'] = df.apply(lambda row : get_completion(row["Prompt"]), axis = 1)

    i = 0
    for index, row in df.iterrows():
        df.at[i, "Response"] = get_completion(row["Prompt"])

        df.to_csv(responses_filename, index=False)

        i += 1
        if (i % 3 == 0):
            time.sleep(60)
        

    df.to_csv(responses_filename, index=False)

query_prompts("prompts.csv", "responses.csv")