from .base_chunk import Chunk


class CommandChunk(Chunk):
    """
    Run a command and return the output.
    ```
    /bash tree -L 3
    /ls
    /git commit -m "qsdqsdqsd"
    /clear
    ```
    """

    def __init__(self, data: str, result=None, error=None):
        super().__init__(data, "command")
        self.command = data[1:].split(" ")[0]
        self.args = data[1:].split(" ")[1:]
        self.result = result
        self.error = error

    def format(self, **kwargs):
        if not self.processed:
            return self.data
        return self.result

    def preprocess(self) -> list["Chunk"]:
        return [self]

    def process(self, result: list["Chunk"], **kwargs) -> list["Chunk"]:
        return [*result, self]

    def to_json(self):
        return {**super().to_json(), "command": self.command, "args": self.args}
