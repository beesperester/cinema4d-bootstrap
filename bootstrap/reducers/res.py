"""
This module provides methods for reducing Description to resource
"""

__author__ = "Bernhard Esperester <bernhard@esperester.de>"

import bootstrap


def reduce_resource(description: bootstrap.Description) -> dict:
    """
    This method reduces Description instance to nested resource dictionary.
    :param description: bootstrap.Description
    :return: dict
    """
    data = {
        "id": description.id,
        "key": description.key
    }

    if isinstance(description.value, list):
        data["value"] = [reduce_resource(x) for x in description.value]
    else:
        data["value"] = description.value

    return data
