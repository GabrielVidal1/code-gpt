from fastapi import APIRouter
from .get_files import get_files
from .process_file import process_file
from .process_chunks import process_chunks_route

router = APIRouter()

# Register routes
router.add_api_route("/files", get_files, methods=["GET"])
router.add_api_route("/file/process", process_file, methods=["POST"])
router.add_api_route("/chunk/process", process_chunks_route, methods=["POST"])
