""" OpenAI API. """
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_text(prompt: str):
    """ Generate text using the OpenAI API. """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
