"""
This module provides methods for rendering locales
"""

from bootstrap4c4d.classes.template import Template

locales_container = Template(
    """STRINGTABLE {id}
{{
    {value}
}}"""
)
"""
Template for rendering locales container
"""

locales_assignment = Template("{key} \"{value}\";")
"""
Template for rendering variable assignment
"""


def render_strings(strings_reduced: dict) -> str:
    """
    This method applies template rendering to the provided input
    """
    locales = {}

    for key, value in strings_reduced.items():
        data = {
            "id": value[0]["key"],
            "value": "\n".join([locales_assignment.Render(x) for x in value])
        }

        locales[key] = locales_container.Render(data)

    return locales
