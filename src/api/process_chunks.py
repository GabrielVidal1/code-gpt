import os
import traceback
from fastapi import Body, HTTPException
from src.parser.chunks import parse_chunk
from src.process import process_chunks
from src.clients import get_client


async def process_chunks_route(data: dict = Body(...)):
    chunks = data["chunks"]
    work_dir = data.get("work_dir", os.getcwd())
    source_file = data.get("source_file", None)
    try:
        client = get_client(client_name="openai", debug=True, model="gpt-4o")
        chunks = [parse_chunk(chunk) for chunk in chunks]
        processed_chunks = process_chunks(
            work_dir, source_file, client, chunks, prompt_debug=True
        )
        return [
            {
                "data": str(chunk),
                "type": chunk.type,
                "processed": chunk.processed,
                "error": chunk.error,
            }
            for chunk in processed_chunks
        ]
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
