"""Test h reducer module."""

import hashlib
import unittest

from bootstrap.classes.description import Description
from bootstrap.reducers.h import reduce_header


class TestHeaderReducer(unittest.TestCase):

    def test_reduce_header(self):
        description = Description({
            "id": "MY_DESCRIPTION",
            "key": "CONTAINER",
            "value": None,
            "locales": {
                "strings_us": "My Description"
            }
        })

        result = reduce_header(description)
        expected_result = [{
            "key": "MY_DESCRIPTION",
            "value": description.GetId()
        }]

        self.assertListEqual(result, expected_result)
