"""
This module provides methods for reducing Description to headers
"""

__author__ = "Bernhard Esperester <bernhard@esperester.de>"

from bootstrap.classes.description import IdError


def reduce_header(description):
    """
    This method reduces Description instance to nested header dictionary.
    :param description: bootstrap.Description
    :return: dict
    """
    data = []

    try:
        data.append({
            "key": description.id,
            "value": description.GetId()
        })
    except IdError:
        pass

    if isinstance(description.value, list):
        for item in description.value:
            data = data + list(filter(None, reduce_header(item)))

    return data
