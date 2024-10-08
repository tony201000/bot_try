from typing import Dict, List

import g4f
from g4f.client import Client

g4f.debug.logging = True


def chat_completion(message: List[Dict]) -> str:
    """Use OpenAI API via gpt4free providers"""
    try:
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=message,
            ignored=["Cnote", "Aichatos"]
        )
        response = response.choices[0].message.content

    except Exception as e:
        response = (
        "There're something wrong in openai api, please try again.\n"
        "Or connect to developer: https://github.com/Lin-jun-xiang/chatgpt-line-bot/issues \n"
        f"{e}"
        )
        print(e)

    return response
