"""Test str reducer module."""

import hashlib
import unittest

from bootstrap4c4d.classes.description import Description
from bootstrap4c4d.reducers.str import reduce_strings


class TestStringsReducer(unittest.TestCase):

    def test_reduce_strings(self):
        description = Description({
            "id": "MY_DESCRIPTION",
            "key": "CONTAINER",
            "value": None,
            "locales": {
                "strings_us": "My Description"
            }
        })

        result = reduce_strings(description)
        expected_result = {
            "strings_us": [{
                "key": "MY_DESCRIPTION",
                "value": "My Description"
            }]
        }

        self.assertDictEqual(result, expected_result)
