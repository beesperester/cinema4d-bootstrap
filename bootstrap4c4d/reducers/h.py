"""
This module provides methods for reducing Description to headers
"""

import bootstrap4c4d
from bootstrap4c4d.classes.description import IdError


def reduce_header(description: bootstrap4c4d.Description) -> dict:
    """
    This method reduces Description instance to nested header dictionary
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
