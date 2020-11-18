from os import makedirs
from os.path import isdir, dirname

def assert_directories(path):
    directoy_path = dirname(path)

    if not isdir(directoy_path):
        makedirs(directoy_path)