import os
from glob import glob
from typing import List, Optional
from pydantic import BaseModel


class File(BaseModel):
    path: str
    type: str
    children: Optional[List["File"]] = None


def read_gitignore(gitignore_path: str) -> List[str]:
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            return [
                line.strip() for line in f if line.strip() and not line.startswith("#")
            ]
    return []


def list_repository_files(base_path: str, ignored_patterns: List[str]) -> List[File]:
    file_structure = []
    for root, dirs, files in os.walk(base_path):
        # Filter out ignored directories
        dirs[:] = [
            d
            for d in dirs
            if not any(
                glob(os.path.join(root, d, pattern)) for pattern in ignored_patterns
            )
        ]
        file_structure.append(File(path=root, type="directory", children=[]))
        for file in files:
            if not any(
                glob(os.path.join(root, file, pattern)) for pattern in ignored_patterns
            ):
                file_structure[-1].children.append(
                    File(path=os.path.join(root, file), type="file")
                )
    return file_structure
