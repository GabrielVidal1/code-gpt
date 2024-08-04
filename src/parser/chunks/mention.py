from .base_chunk import Chunk

from src.constants import FILE_FORMAT


class MentionChunk(Chunk):
    """
    Mention a file and return its content.
    ```
    @file.txt
    ```
    """

    def __init__(self, data: str):
        super().__init__(data, "mention")
        self.path = data[1:].split(" ")[0]

    def format(self, **kwargs):
        if self.error:
            return f"Error: {self.error}"
        return FILE_FORMAT.format(file_path=self.path, content=self.content)

    def process(self, result: list[Chunk], **kwargs) -> list["Chunk"]:
        try:
            with open(self.path, "r") as file:
                self.content = file.read()
        except FileNotFoundError:
            print(f"Error: File not found : {self.path}")
            self.content = ""
            self.error = f"Error: File not found : {self.path}"

        return [*result, self]

    def to_json(self):
        return {**super().to_json(), "path": self.path}
