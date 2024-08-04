import re
from typing import List

from .chunks import Chunk, MentionChunk, OutputChunk, CommandChunk
from src.commands import COMMANDS


all_commands = {command.name: command for command in COMMANDS}


def parse_command(line: str) -> list["Chunk"]:
    """ """
    assert line.startswith("/")
    command = line[1:].split(" ")[0]
    if command not in all_commands:
        return [CommandChunk(line, error=f"Error: Command not found : {command}")]
    return all_commands[command](line).preprocess()


def parse_file(path: str) -> List[Chunk]:
    """
    Parse file and return the list of chunks.
    Works recursively for .llm files.

    Args:
        path (str): The path to the file.

    Returns:
        List[Chunk]: The list of parsed chunks.
    """
    try:
        with open(path, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found : {path}")
        return []

    return parse_content(content, path)


def parse_content(content: str, path: str) -> List[Chunk]:
    """
    Parse content and return the list of chunks.

    Args:
        content (str): The content to parse.

    Returns:
        List[Chunk]: The list of parsed chunks.
    """
    special_mentions_re = r"[@>/][^\s]+"

    chunks = []
    current_chunk = ""
    lines = content.split("\n")
    for line in lines:
        if re.match(special_mentions_re, line):
            if current_chunk.strip():
                chunks.append(Chunk(current_chunk.strip()))

            if line.startswith("@"):
                chunk = MentionChunk(line)
                if chunk.path.endswith(".llm"):
                    chunks.extend(parse_file(chunk.path))
                else:
                    chunks.append(chunk)
            if line.startswith(">"):
                chunks.append(OutputChunk(line))
            if re.match(r"^/[a-zA-Z]+", line):
                chunks.extend(parse_command(line))

            current_chunk = ""
        else:
            current_chunk += line + "\n"
    if current_chunk.strip():
        chunks.append(Chunk(current_chunk.strip()))

    return chunks
