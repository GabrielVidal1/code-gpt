from src.parser.chunks import CommandChunk, Chunk
import subprocess

BASH_COMMAND_FORMAT = "Output of the following command: `{command}`\n```{output}```"


class BashCommand(CommandChunk):
    name = "bash"

    def __init__(self, data: str):
        super().__init__(data)
        assert self.command == "bash"
        assert len(self.args[0]) > 0

        self.bash_command = self.args[0]
        self.bash_args = self.args[1:]

    def format(self):
        return BASH_COMMAND_FORMAT.format(command=self.data, output=self.result)

    def process(self, result: list[Chunk], **kwargs) -> list["Chunk"]:
        try:
            res = subprocess.run(
                [self.bash_command] + self.bash_args,
                check=True,
                text=True,
            )
            self.result = res.stdout
        except subprocess.CalledProcessError as e:
            self.error = e.stderr
        except Exception as e:
            self.error = str(e)
        finally:
            self.processed = True
        return [*result, self]
