"""
This module provides methods for rendering resources
"""

from bootstrap4c4d.classes.template import Template

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


def render_resource(resource_reduced: dict) -> str:
    """
    This method applies template rendering to the provided input
    """
    data = {**resource_reduced}

    if isinstance(data["value"], list):
        data["value"] = [render_resource(x) for x in data["value"]]

        return resource_container.Render(data)

    return "{};".format(resource_assignment.Render(data).strip())
