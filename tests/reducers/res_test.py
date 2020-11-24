"""Test res reducer module."""

import hashlib
import unittest

from bootstrap4c4d.classes.description import Description
from bootstrap4c4d.reducers.res import reduce_resource


class TestResourceReducer(unittest.TestCase):

    def test_reduce_resource(self):
        description = Description({
            "id": "MY_DESCRIPTION",
            "key": "CONTAINER",
            "value": None,
            "locales": {
                "strings_us": "My Description"
            }
        })

        result = reduce_resource(description)
        expected_result = {
            "id": "MY_DESCRIPTION",
            "key": "CONTAINER",
            "value": None
        }

        self.assertDictEqual(result, expected_result)
