class Description(object):

    def __init__(self, label, strings, description, flags):
        self.label = label
        self.strings = strings
        self.description = description
        self.flags = flags

    def __repr__(self):
        return str(abs(hash(self.label)) % (10 ** 8))

class DescriptionFlag(object):

    def __init__(self, label, value):
        self.label = label
        self.value = value

class Group(Description):

    def __init__(self, label, strings, flags, children):
        self.children = children

        super(Group, self).__init__(label, strings, "GROUP", flags)

    def GenerateStrings(self, locale):
        lines = []
        for child in self.children:
            lines.append("\t{}".format(Layout.FormatEntry(child.label, child.strings[locale])))

            if isinstance(child, Group):
                lines = lines + child.GenerateStrings(locale)

        return lines

class Layout(object):

    def __init__(self, label, strings, flags, group):
        self.label = label
        self.strings = strings
        self.flags = flags
        self.group = group

    @classmethod
    def FormatEntry(cls, key, value):
        return "{} \"{}\";".format(key, value)

    def GenerateStrings(self, locale):
        lines = []

        lines.append("STRINGTABLE {}".format(self.label))
        lines.append("{")

        lines.append("\t{}".format(Layout.FormatEntry(self.label, self.strings[locale])))

        lines = lines + self.group.GenerateStrings(locale)

        lines.append("}")

        return "\n".join(lines)

    def GenerateHeaders(self):
        lines = []

        lines.append("#ifndef _Oatom_H_")
        lines.append("#define _Oatom_H_")

        lines.append("")

        lines.append("enum")

        return "\n".join(lines)

class TemplateNode(object):
    """TemplateNode"""

    def __init__(self, nodename, begin, end, children = None):
        if children is None:
            children = []

        self.nodename = nodename
        self.begin = begin
        self.end = end
        self.children = children

    @classmethod
    def RenderLine(cls, line, level, indendation=2):
        return "{}{}".format(" " * level * indendation, line)

    def Render(self, level=0, indendation=4):
        lines = []

        if self.nodename:
            lines.append(TemplateNode.RenderLine(self.nodename, level, indendation))

        if self.begin and self.end:
            lines.append(TemplateNode.RenderLine(self.begin, level, indendation))

        for child in self.children:
            lines.append(TemplateNode.RenderLine(child, level + 1, indendation))

        if self.begin and self.end:
            lines.append(TemplateNode.RenderLine(self.end, level, indendation))
        
        return "\n".join(lines)


headersTemplate = TemplateNode(
    "enum",
    "{", "};",
    [
        "foobar"
    ]
)

print(headersTemplate.Render())