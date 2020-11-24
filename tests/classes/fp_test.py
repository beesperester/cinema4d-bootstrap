"""Test fp module."""

import unittest

from bootstrap4c4d.classes import fp


class TestFpMethods(unittest.TestCase):

    def test_right(self):
        result = fp.Right(1).map(lambda x: fp.Right(x + 1))
        expected_result = 2

        self.assertEqual(result.value, expected_result)

    def test_left(self):
        result = fp.Left(1).map(lambda x: x + 1)
        expected_result = 1

        self.assertEqual(result.value, expected_result)

    def test_pipe(self):
        result = fp.pipe([
            lambda x: x + 1
        ])(fp.Right(1))
        expected_result = 2

        self.assertEqual(result, expected_result)

    def test_encase(self):
        result = fp.encase(lambda x: x + 1)(1)
        expected_result = 2

        self.assertEqual(result.value, expected_result)

    def test_chain(self):
        result = fp.chain(lambda x: x)(1)
        expected_result = 1

        self.assertEqual(result.value, expected_result)

    def test_pipe_encase_chain(self):
        pipe1 = fp.pipe([
            fp.encase(lambda x: x),
            fp.encase(lambda x: x + 1)
        ])

        pipe2 = fp.pipe([
            fp.encase(lambda x: x + 1),
            fp.encase(lambda x: x + 1)
        ])

        result = fp.pipe([
            fp.chain(pipe1),
            fp.chain(pipe2)
        ])(fp.Right(1))

        expected_result = fp.Right(4)

        self.assertEqual(result.value, expected_result.value)
