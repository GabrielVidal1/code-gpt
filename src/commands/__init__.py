import os
import inspect
import importlib
from src.parser.chunks.command import CommandChunk

# Directory containing command modules
commands_dir = os.path.dirname(__file__)

# List to hold command classes
COMMANDS = []

# Iterate over all files in the commands directory
for filename in os.listdir(commands_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        module = importlib.import_module(f".{module_name}", package=__name__)

        # Inspect the module to find classes that inherit from Command
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, CommandChunk) and obj is not CommandChunk:
                COMMANDS.append(obj)

# Example usage
if __name__ == "__main__":
    for command in COMMANDS:
        print(f"Loaded command: {command.__name__}")
