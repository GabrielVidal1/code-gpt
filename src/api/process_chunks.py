from fastapi import HTTPException
from src.process import process_chunks
from src.clients import get_client


async def process_chunks_route(chunks: list):
    try:
        client = get_client(client_name="openai", debug=True, model="gpt-4o")
        processed_chunks = process_chunks(client, chunks, prompt_debug=True)
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
        raise HTTPException(status_code=500, detail=str(e))
