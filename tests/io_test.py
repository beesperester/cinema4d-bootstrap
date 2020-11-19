"""Test io module."""

import unittest
import os
import sys

project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
examples_path = os.path.join(project_path, "examples")

sys.path.append(examples_path)

try:
    import c4d
    from tmyplugin import root
except ImportError:
    pass

from bootstrap.io import build


class TestIoMethods(unittest.TestCase):

    def test_build(self):
        if "c4d" in sys.modules:
            plugin_file = os.path.join(examples_path, "tmyplugin.py")
            destination_directory = os.path.join(project_path, "tests", "dist")

            result = build(root, plugin_file, destination_directory, "tmyplugin")

            self.assertTrue(result)
        else:
            self.skipTest("missing module c4d")
