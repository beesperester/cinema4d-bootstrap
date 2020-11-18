from os import makedirs
from os.path import isdir, dirname

def assert_directories(path, is_file_path=False):
    directory_path = path

    if is_file_path:
        directory_path = dirname(path)

    if not isdir(directory_path):
        makedirs(directory_path)