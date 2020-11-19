import os

from bootstrap.io import build

from ttest import root

root_path = os.path.dirname(os.path.realpath(__file__))

plugin_file = os.path.join(root_path, "ttest.py")
destination_directory = os.path.join(root_path, "dist")

build(root, plugin_file, destination_directory, "ttest")