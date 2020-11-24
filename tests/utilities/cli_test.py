"""Test utilities cli module."""

import unittest

from bootstrap4c4d.utilities.cli import cli_format_error, cli_format_success


class TestCliMethods(unittest.TestCase):

    def test_cli_format_error(self):
        message = "Hello World"
        result = cli_format_error(message)
        excpected_result = "\x1b[31mError:\x1b[0m {}".format(message)

        self.assertEqual(result, excpected_result)

    def test_cli_format_success(self):
        message = "Hello World"
        result = cli_format_success(message)
        excpected_result = "\x1b[32mSuccess:\x1b[0m {}".format(message)

        self.assertEqual(result, excpected_result)
