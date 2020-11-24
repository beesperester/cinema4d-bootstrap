"""Test template module."""

import unittest

from bootstrap4c4d import Template


class TestTemplateMethods(unittest.TestCase):

    def test_render(self):
        template = Template(
            """{key} {id}
{{
    {value}
}}"""
        )

        data = {
            "key": "NAME",
            "id": "test",
            "value": "FOOBAR;"
        }

        result = template.Render(data)
        result_excpected = """NAME test
{
    FOOBAR;
}"""

        self.assertEqual(result, result_excpected)
