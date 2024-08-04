from fastapi import HTTPException, Body
from ..parser.file_parser import parse_content
import traceback


async def process_file(data: dict = Body(...)):
    print(data)
    try:
        path = data["path"]
        content = data["content"]
        chunks = parse_content(content, path)
        return [
            {
                "data": str(chunk),
                "type": chunk.type,
                "processed": chunk.processed,
                "error": chunk.error,
            }
            for chunk in chunks
        ]
    except Exception as e:
        print(e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
