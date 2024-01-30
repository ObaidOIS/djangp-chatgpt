from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class ChatGPTService:
    def send_request(message):
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=message,
        )
        completion = response  # Parse the response as a Completion object
        return completion.choices[0].text  # Access content correctly
