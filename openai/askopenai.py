import json
import os
import pathlib

import openai

dir = pathlib.Path(__file__).parent.parent
filename = "api_key.json"

with open(os.path.join(dir, filename), "r") as fp:
    jsonfile = json.load(fp)

openai.api_key = jsonfile["API_KEY"]


def ask_question(prompt):
    model_engine = "davinci"  # Replace with the model you want to use
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )
    answer = response.choices[0].text.strip()
    return answer


prompt = input("Ask your question to the ChatGPT? \n")
answer = ask_question(prompt)
print(answer)
