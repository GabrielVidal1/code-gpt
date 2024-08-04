class Chunk:
    """
    Base class for all chunks.
    """

    def __init__(self, data: str, type: str = "text", processed=False, error=None):
        self.data = data.replace("\\@", "@")
        self.type = type
        self.processed = processed
        self.error = error

    def __str__(self) -> str:
        return self.data

    def __repr__(self) -> str:
        return f"<{self.type}: {self.data}>"

    def format(self, **kwargs):
        """
        format function is how the chunk will be displayed in the output file.
        """
        return self.data

    def process(self, result: list["Chunk"], **kwargs) -> list["Chunk"]:
        """
        the process function is where the chunk will be processed.
        The function returns a the result of processing the chunk after the list of previous chunks.
        """
        return [*result, self]

    def to_json(self):
        return {
            "type": self.type,
            "data": self.data,
            "processed": self.processed,
            "error": self.error,
        }
