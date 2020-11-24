"""
This module provides generic Template class
"""

import re


class Template(object):
    """
    This class models a generic Template
    """

    def __init__(
        self,
        template_string: str
    ) -> None:
        """
        This method initializes a new instance of the Template class
        """
        self.template_string = template_string

    @classmethod
    def PrepareData(
        cls,
        data: dict
    ) -> None:
        """
        This method prepares data for rendering
        """
        dataPrepared = data.copy()

        for key, value in data.items():
            if isinstance(value, list):
                dataPrepared[key] = "\n".join(value)

        return dataPrepared

    def Render(
        self,
        data: dict
    ) -> str:
        """
        Render the template with the provided data
        """
        if data is None:
            data = {}

        formatPattern = re.compile(r"\{(\w+)\}", re.MULTILINE)

        lines = []

        for line in self.template_string.split("\n"):
            groups = re.findall(formatPattern, line)

            # remove format groups where no data is provided
            for group in groups:
                if group not in data.keys() or data[group] is None:
                    line = line.replace("{{{}}}".format(group), "")
                    # greedy replace whitespace
                    line = re.sub(r"\s+", " ", line)

                    line = line.strip()

            if line:
                # get indentation level
                indentation = len(line) - len(line.lstrip())

                # populate with data
                dataPrepared = Template.PrepareData(data)

                lineFormatted = line.format(**dataPrepared)

                # add indentation
                line = lineFormatted.replace(
                    "\n", "\n{}".format(" " * indentation)
                )

            lines.append(line)

        return "\n".join(lines)
