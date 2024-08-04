import os
from typing import Optional
from clients import get_client
from parser.file_parser import OutputChunk, parse_file
from args_parser import get_parser
import traceback
from src.prompts import LAST

from process import process_chunks
import json


def main(
    source_filename,
    target_filename: Optional[str] = None,
    prompt_debug=True,
    client_name="openai",
    model="gpt-4o",
    log_folder="logs",
    script=False,
    only_print_chunks=False,
):
    client = get_client(client_name, prompt_debug, model)

    chunks = parse_file(source_filename)

    if only_print_chunks:
        print(json.dumps([chunk.to_json() for chunk in chunks], indent=2))
        return

    # If no output chunk is present, add one with the source filename
    if (
        not script
        and target_filename is None
        and not isinstance(chunks[-1], OutputChunk)
    ):
        chunks.append(OutputChunk(f">{source_filename}", custom=LAST))

    # Prepare the messages for the API
    try:
        result = process_chunks(source_filename, client, chunks, prompt_debug)

        if prompt_debug:
            os.makedirs(log_folder, exist_ok=True)
            with open(os.path.join(log_folder, "debug.txt"), "w") as file:
                file.write("\n\n---\n\n".join([str(r) for r in result]))

            with open(os.path.join(log_folder, "debug_processed.txt"), "w") as file:
                processed = [chunk.format() for chunk in result]
                file.write("\n\n---\n\n".join(processed))

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    main(
        args.source_filename,
        args.target_filename,
        args.prompt_debug,
        args.client,
        args.model,
        args.log_folder,
        args.script,
        args.only_print_chunks,
    )
