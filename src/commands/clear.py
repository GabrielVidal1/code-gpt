from src.parser.chunks import Chunk, CommandChunk


class ClearCommand(CommandChunk):
    name = "clear"

    def __init__(self, data: str):
        super().__init__(data)
        assert self.command == "clear"

    def process(self, result: list[Chunk], **kwargs) -> list[Chunk]:
        return []

    def format(self):
        return ""
