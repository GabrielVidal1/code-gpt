from fastapi import HTTPException
import os
from ..services.list_files import list_repository_files, read_gitignore


async def get_files():
    base_path = os.getcwd()
    gitignore_path = os.path.join(base_path, ".gitignore")
    ignored_patterns = read_gitignore(gitignore_path)
    files = list_repository_files(base_path, ignored_patterns)
    if not files:
        raise HTTPException(status_code=404, detail="No files found")
    return files
