from typing import List

from src.clients.client import Client
from src.parser.chunks import Chunk


def process_chunks(
    source_file: str, client: Client, chunks: List[Chunk], prompt_debug: bool
) -> List[Chunk]:
    """
    Process the chunks in order and return the result.
    """
    result = []

    for chunk in chunks:
        if chunk.type == "text":
            result.append(chunk)
        else:
            result = chunk.process(
                **{
                    "source_file": source_file,
                    "input": chunks,
                    "result": result,
                    "client": client,
                    "prompt_debug": prompt_debug,
                }
            )

    return result
