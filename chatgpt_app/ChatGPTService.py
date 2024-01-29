from openai import OpenAI

client = OpenAI(api_key="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")


class ChatGPTService:
    def send_request(message):
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt="Write a tagline for an ice cream shop.",
        )
        print("response: ", response)
        # response.raise_for_status()  # Raise an exception for error handling
        completion = response  # Parse the response as a Completion object
        print("completion: ", completion)
        print("completion.choices: ", completion.choices)
        print("completion.choices[0]: ", completion.choices[0])
        print("completion.choices[0].text: ", completion.choices[0].text)
        return completion.choices[0].text  # Access content correctly
