import re

class Template(object):
    
    def __init__(self, templateString):
        self.templateString = templateString

    @classmethod
    def PrepareData(cls, data):
        dataPrepared = data.copy()

        for key, value in data.items():
            if isinstance(value, list):
                dataPrepared[key] = "\n".join(value)

        return dataPrepared

    def Render(self, data=None):
        if data is None:
            data = {}

        formatPattern = re.compile(r"\{(\w+)\}", re.MULTILINE)

        lines = []

        for line in self.templateString.split("\n"):
            groups = re.findall(formatPattern, line)

            # remove format groups
            for group in groups:
                if not group in data.keys() or data[group] is None:
                    line = line.replace("{{{}}}".format(group), "")

            if line:
                # get indentation level
                indentation = len(line) - len(line.lstrip())

                # populate with data
                dataPrepared = Template.PrepareData(data)
                
                lineFormatted = line.format(**dataPrepared)

                # add indentation
                line = lineFormatted.replace("\n", "\n{}".format(" " * indentation))

            lines.append(line)

        return "\n".join(lines)