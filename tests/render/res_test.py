"""Test res render module."""

import hashlib
import unittest

from bootstrap.classes.description import Description, Assignment
from bootstrap.reducers.res import reduce_resource
from bootstrap.render.res import render_resource


class TestResourceRender(unittest.TestCase):

    def test_render_resource(self):
        description = Description({
            "id": "MY_DESCRIPTION",
            "key": "CONTAINER",
            "value": [Assignment("INCLUDE", "Tbase")],
            "locales": {
                "strings_us": "My Description"
            }
        })

        result = render_resource(reduce_resource(description))
        expected_result = """CONTAINER MY_DESCRIPTION
{
    INCLUDE Tbase;
}"""

        self.assertEqual(result, expected_result)
