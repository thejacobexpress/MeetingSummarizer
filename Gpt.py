import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def summarizeText(text):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        store=False,
        messages=[
            {"role": "system", "content": "Write a bullet point summary based on the prompt the user inputs."},
            {"role": "user", "content": text}
        ]
    )
    return completion.choices[0].message.content