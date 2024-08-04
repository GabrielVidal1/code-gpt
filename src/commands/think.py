from src.clients.client import Client
from src.parser.chunks import Chunk, CommandChunk, OutputChunk

PROMPT = """Here are files that you will be modifying:
{file_paths}

For each given file, write a summary of the changes you need to make
"""


class ThinkCommand(OutputChunk, CommandChunk):
    name = "think"
    """
    Think about the changes you need to make to the files.
    """

    def __init__(self, data: str):
        super().__init__(data)
        self.type = "think"
        self.prompt = ""

    def process_output(self, response: str):
        self.content = response

    def format(self, debug: bool = False):
        if debug:
            return self.custom + "\n" + self.full_response
        return self.content

    def process(
        self,
        input: list[Chunk],
        result: list[Chunk],
        client: Client,
        prompt_debug: bool,
        **kwargs,
    ) -> list[Chunk]:
        fileoutputs = [i if isinstance(i, OutputChunk) else None for i in input]
        paths = "\n".join([f"* {i.path}" for i in fileoutputs if i])
        self.custom = PROMPT.format(file_paths=paths)
        return super().process(result, client, prompt_debug)
