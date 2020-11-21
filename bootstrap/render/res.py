"""
This module provides methods for rendering resources
"""

__author__ = "Bernhard Esperester <bernhard@esperester.de>"

from bootstrap.classes.template import Template

resource_container = Template(
    """{key} {id}
{{
    {value}
}}"""
)
"""
Template for rendering generic container
"""

resource_assignment = Template("{key} {id} {value}")
"""
Template for rendering variable assignment
"""


def render_resource(resource_reduced):
    """
    This method applies template rendering to the provided input.
    :param resource_reduced: dict
    :return: string
    """
    data = {**resource_reduced}

    if isinstance(data["value"], list):
        data["value"] = [render_resource(x) for x in data["value"]]

        return resource_container.Render(data)

    return "{};".format(resource_assignment.Render(data).strip())
