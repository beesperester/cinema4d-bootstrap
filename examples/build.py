import os

from bootstrap.io import build
from tmyplugin import root

root_path = os.path.dirname(os.path.realpath(__file__))

plugin_file = os.path.join(root_path, "tmyplugin.py")
destination_directory = os.path.join(root_path, "dist")

result = build(root, plugin_file, destination_directory, "tmyplugin")