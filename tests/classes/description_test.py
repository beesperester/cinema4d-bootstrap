"""Test description module."""

import hashlib
import unittest

from bootstrap4c4d.classes.description import \
    Description, \
    Container, \
    Assignment, \
    Group


class TestDescriptionMethods(unittest.TestCase):

    def test_description_getid(self):
        result = Description({
            "id": "MY_DESCRIPTION",
            "key": "CONTAINER",
            "value": None,
            "locales": {
                "strings_us": "My Description"
            }
        }).GetId()

        expected_result = int(
            hashlib.sha1("MY_DESCRIPTION".encode('utf-8')).hexdigest(), 16
        ) % (10 ** 8)

        self.assertEqual(result, expected_result)

    def test_description_attribute_access(self):
        result = Description({
            "id": "MY_DESCRIPTION",
            "key": "CONTAINER",
            "value": None,
            "locales": {
                "strings_us": "My Description"
            }
        }).key

        expected_result = "CONTAINER"

        self.assertEqual(result, expected_result)

    def test_group(self):
        result = Group("MY_GROUP").id
        expected_result = "MY_GROUP"

        self.assertEqual(result, expected_result)

    def test_container(self):
        result = Container("MY_CONTAINER").id
        expected_result = "MY_CONTAINER"

        self.assertEqual(result, expected_result)

    def test_assignment(self):
        result = Assignment("ANIM", "OFF").key
        expected_result = "ANIM"

        self.assertEqual(result, expected_result)
