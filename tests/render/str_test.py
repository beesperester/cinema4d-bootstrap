"""Test str render module."""

import hashlib
import unittest

from bootstrap.classes.description import Description
from bootstrap.reducers.str import reduce_strings
from bootstrap.render.str import render_strings


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
