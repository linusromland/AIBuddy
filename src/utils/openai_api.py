""" OpenAI API. """
from typing import Dict, List
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_response(prompt: List[Dict[str, str]]) -> str:
    """ Generate text using the OpenAI API. """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=prompt,
    )

    return response.choices[0].message.content
