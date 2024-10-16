from .base_chunk import Chunk
from .command import CommandChunk
from .mention import MentionChunk
from .output import OutputChunk


def parse_chunk(obj: dict):
    if "type" not in obj:
        return Chunk(**obj)
    type = obj.pop("type", "chunk")
    if type == "command":
        return CommandChunk(**obj)
    if type == "mention":
        obj.pop("processed", None)
        return MentionChunk(**obj)
    if type == "output":
        obj.pop("processed", None)
        obj.pop("error", None)
        return OutputChunk(**obj)
    return Chunk(**obj)
