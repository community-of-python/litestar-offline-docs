import os
import pathlib

from litestar.static_files.config import StaticFilesConfig


def generate_static_files_config(
    static_files_handler_path: str = "/static",
    static_dir_path: os.PathLike[str] = pathlib.Path(__file__).parent / "static",
) -> StaticFilesConfig:
    return StaticFilesConfig(directories=[static_dir_path], path=static_files_handler_path, name="static")
