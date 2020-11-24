"""Test str render module."""

import hashlib
import unittest

from bootstrap4c4d.classes.description import Description
from bootstrap4c4d.reducers.str import reduce_strings
from bootstrap4c4d.render.str import render_strings


class TestStringsRender(unittest.TestCase):

    def test_render_strings(self):
        description = Description({
            "id": "MY_DESCRIPTION",
            "key": "CONTAINER",
            "value": None,
            "locales": {
                "strings_us": "My Description"
            }
        })

        result = render_strings(reduce_strings(description))
        expected_result = {
            "strings_us": """STRINGTABLE MY_DESCRIPTION
{
    MY_DESCRIPTION "My Description";
}"""
        }

        self.assertDictEqual(result, expected_result)
