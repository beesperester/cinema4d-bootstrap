"""
This module provides methods for rendering headers
"""

__author__ = "Bernhard Esperester <bernhard@esperester.de>"

from bootstrap.classes.template import Template

header_container = Template(
    """#ifndef _Oatom_H_
#define _Oatom_H_

enum
{{
    {value}
}};

#endif
"""
)
"""
Template for rendering header container
"""

header_assignment = Template("{key} = {value},")
"""
Template for rendering variable assignment
"""


def render_header(header_reduced):
    """
    This method applies template rendering to the provided input.
    :param header_reduced: dict
    :return: string
    """
    data = {
        "value": [header_assignment.Render(x) for x in header_reduced]
    }

    return header_container.Render(data)
