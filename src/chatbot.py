import os
from dotenv import load_dotenv
from openai import OpenAI

class OpenAIChat:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPEN_AI_API')
        self.client = OpenAI(api_key=self.api_key)

    def generate_response(self, user_message: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a coding expert. Write answer to coding questions."},
                {"role": "user", "content": user_message}
            ]
        )

        response = completion.choices[0].message.content
        return response