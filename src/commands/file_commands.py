from src.parser.chunks import CommandChunk, Chunk, OutputChunk
import os
from src.parser.chunks.mention import MentionChunk


class ListFilesCommand(CommandChunk):
    name = "ls"
    """
    List the content of files in a directory
    """

    def parse_files(self, path: str) -> list[str]:
        """
        Parse recursively the files in a directory
        """
        files = []
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                files.append(os.path.join(path, file))

            if os.path.isdir(os.path.join(path, file)):
                files += self.parse_files(os.path.join(path, file))

        return files

    def __init__(self, data: str):
        super().__init__(data)
        self.path = self.args[0] if len(self.args) > 0 else "."
        if not os.path.isdir(self.path):
            self.files = [self.path]
        else:
            self.files = self.parse_files(self.path)

        if len(self.files) == 0:
            print(f"Error: No files found in directory : {self.path}")

    def preprocess(self) -> list["Chunk"]:
        return [
            MentionChunk(f"@{os.path.join(self.path, file)}") for file in self.files
        ]


class WriteFilesCommand(ListFilesCommand):
    name = "write"
    """
    Write the content of all files in a directory
    """

    def __init__(self, data: str):
        super().__init__(data)

    def preprocess(self) -> list["Chunk"]:
        return [OutputChunk(f">{os.path.join(self.path, file)}") for file in self.files]
