import os
from typing import Optional
from src.clients.client import Client
from src.helpers import extract_code
from src.constants import FILE_FORMAT, OUTPUT_FORMAT
from src.prompts import ONLY_CODE
from src.constants import CODE_EXTENSIONS
from .base_chunk import Chunk


def process_stream(stream, debug: bool = False) -> str:
    """
    Print the stream and return the response.
    """
    response = ""
    for chunk in stream:
        response += chunk
        if debug:
            print(chunk, end="")
    return response


class OutputChunk(Chunk):
    """
    Output the current chunk to a file.
    usually the output from the llm.
    ```
    >file.txt
    ```
    """

    def __init__(self, data: str, custom: Optional[str] = None):
        super().__init__(data, "output")
        self.path = data[1:].split(" ")[0]
        self.custom = custom
        self.only_code = self.path is not None and any(
            [self.path.endswith(ext) for ext in CODE_EXTENSIONS]
        )
        self.content = ""

    def format_prompt(self):
        if self.custom:
            return self.custom

        res = ""

        if self.only_code:
            res += ONLY_CODE

        return res + OUTPUT_FORMAT.format(file_path=self.path)

    def format(self, debug: bool = True):
        if self.error:
            return f"Error: {self.error}"
        if debug:
            return self.full_response

        return FILE_FORMAT.format(file_path=self.path, content=self.content)

    def process_output(self, response: str):
        """
        Write the response to an existing file or create a new one.
        """
        self.content = response

        if not os.path.exists(self.path):
            try:
                os.makedirs(os.path.dirname(self.path), exist_ok=True)
                open(self.path, "w").close()
            except Exception as e:
                self.error = str(e)
                return

        if self.only_code:
            with open(self.path, "w") as file:
                code = extract_code(response)
                self.content = code
                file.write(code)
        else:
            with open(self.path, "a") as file:
                file.write("\n\n" + response)

    def process(
        self, result: list[Chunk], client: Client, prompt_debug: bool, **kwargs
    ) -> list["Chunk"]:
        source_file = kwargs.get("source_file", "out.out")
        print(source_file, self.path, "path")
        if self.path.strip() == "":
            self.only_code = False
            self.path = source_file + ".out"

        processed = [chunk.format() for chunk in result]
        processed.append(self.format_prompt())

        stream = client.get_completion(
            processed,
            stream=True,
        )

        response = process_stream(stream, prompt_debug)
        self.full_response = response
        self.process_output(response)

        return [*result, self]

    def to_json(self):
        return {
            **super().to_json(),
            "path": self.path,
            "custom": self.custom,
            "only_code": self.only_code,
            "response": self.content,
        }
