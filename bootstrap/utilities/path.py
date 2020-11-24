"""
This module provides methods for working with the filesystem
"""

from os import makedirs
from os.path import isdir, dirname


def assert_directories(
    path: str,
    is_file_path: bool = False
) -> None:
    """
    This method asserts the existence of all directories in the path
    """
    directory_path = path

    if is_file_path:
        directory_path = dirname(path)

    if not isdir(directory_path):
        makedirs(directory_path)
