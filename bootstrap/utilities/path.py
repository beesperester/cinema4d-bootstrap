"""
This module provides methods for working with the filesystem
"""

__author__ = "Bernhard Esperester <bernhard@esperester.de>"

from os import makedirs
from os.path import isdir, dirname


def assert_directories(path, is_file_path=False):
    """
    This method asserts the existence of all directories in the path.
    :param path: string
    :param is_file_path: boolean
    :return:
    """
    directory_path = path

    if is_file_path:
        directory_path = dirname(path)

    if not isdir(directory_path):
        makedirs(directory_path)
