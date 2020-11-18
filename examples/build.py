import os
from tmyawesomeplugin import layout
from bootstrap.utilities.path import assert_directories

rootDirectoryPath = os.path.dirname(os.path.realpath(__file__))
srcFilePath = os.path.join(rootDirectoryPath, "tmyawesomeplugin.py")
destDirectoryPath = os.path.join(rootDirectoryPath, "dist")

assert_directories(destDirectoryPath)

layout.Build(srcFilePath, destDirectoryPath)