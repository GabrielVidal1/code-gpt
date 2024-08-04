import os
from openai import OpenAI
from .client import Client


class OpenAIClient(Client):
    def __init__(self, debug=False, model="gpt-4o"):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("Please set the OPENAI_API_KEY environment variable.")
            return
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.debug = debug

    def process_messages(self, messages):
        return [
            {"role": "user", "content": chunk.strip()}
            for chunk in messages
            if chunk.strip()
        ]

    def get_completion(self, messages, stream=False):
        processed_messages = []

        processed_messages += self.process_messages(messages)

        if self.debug:
            self.log(processed_messages)

        response_stream = self.client.chat.completions.create(
            model=self.model, messages=processed_messages, stream=stream
        )
        if not stream:
            yield response_stream.choices[0].content or ""
        else:
            for chunk in response_stream:
                content = chunk.choices[0].delta.content or ""
                yield content
