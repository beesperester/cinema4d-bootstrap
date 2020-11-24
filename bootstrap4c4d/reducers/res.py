"""
This module provides methods for reducing Description to resource
"""

import bootstrap4c4d


def reduce_resource(description: bootstrap4c4d.Description) -> dict:
    """
    This method reduces Description instance to nested resource dictionary
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
