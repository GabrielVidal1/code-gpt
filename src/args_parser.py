import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description="Process a file and interact with OpenAI API."
    )
    parser.add_argument("source_filename", type=str, help="Source file to read from")
    parser.add_argument(
        "target_filename",
        type=str,
        nargs="?",
        default=None,
        help="Target file to write to (optional)",
    )
    parser.add_argument(
        "--no-debug",
        dest="prompt_debug",
        action="store_false",
        help="Disable writing debug information to a file",
    )
    parser.add_argument(
        "--client",
        type=str,
        choices=["openai", "ollama"],
        default="openai",
        help="Client to use for processing (default: openai)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o",
        help="Model to use for processing (optional)",
    )
    parser.add_argument(
        "--log-folder",
        type=str,
        default="logs",
        help="Folder to write log files to (default: logs)",
    )
    parser.add_argument(
        "--script", action="store_true", help="Prevent adding OutputChunk"
    )

    parser.add_argument(
        "--only_print_chunks",
        action="store_true",
        help="Only return the chunks in JSON format for a given file",
    )

    parser.add_argument(
        "--print_processed",
        action="store_true",
        help="Print the processed chunks in a file",
    )

    return parser
