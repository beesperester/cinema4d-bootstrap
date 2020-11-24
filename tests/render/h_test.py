"""Test h render module."""

import hashlib
import unittest

from bootstrap4c4d.classes.description import Description
from bootstrap4c4d.reducers.h import reduce_header
from bootstrap4c4d.render.h import render_header


class TestHeaderRender(unittest.TestCase):

    def test_render_header(self):
        description = Description({
            "id": "MY_DESCRIPTION",
            "key": "CONTAINER",
            "value": None,
            "locales": {
                "strings_us": "My Description"
            }
        })

        result = render_header(reduce_header(description))
        expected_result = """#ifndef _Oatom_H_
#define _Oatom_H_

enum
{{
    MY_DESCRIPTION = {},
}};

#endif""".format(description.GetId())

        self.assertEqual(result, expected_result)
