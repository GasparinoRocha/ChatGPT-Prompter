import openai
from os import getenv
from dotenv.main import load_dotenv
import datetime

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

f = open("prompt.txt", "r")
prompt = f.read()
f.close()

response = get_completion(prompt)

date = datetime.datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p')

f = open(f"responses/{date}.txt", "w")
f.write(response)
f.close()