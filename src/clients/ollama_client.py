import ollama
from .client import Client


class OllamaClient(Client):
    def __init__(self, debug=False, model="mistral"):
        self.client = ollama
        self.debug = debug
        self.model = model

    def process_messages(self, messages):
        return [
            {"role": "user", "content": chunk.strip()}
            for chunk in messages
            if chunk.strip()
        ]

    def get_completion(self, messages, stream=False, system_prompt=None):
        processed_messages = []

        if system_prompt:
            processed_messages.append({"role": "system", "content": system_prompt})

        processed_messages += self.process_messages(messages)

        if self.debug:
            self.log(processed_messages)

        response_stream = ollama.chat(
            model=self.model, messages=processed_messages, stream=stream
        )
        if not stream:
            yield response_stream["message"]["content"] or ""
        else:
            for chunk in response_stream:
                content = chunk["message"]["content"] or ""
                yield content
