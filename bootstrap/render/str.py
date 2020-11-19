from bootstrap.template import Template

locales_container = Template(
"""STRINGTABLE {id}
{{
    {value}
}}
"""
)

locales_assignment = Template("{key} \"{value}\";")

def render_strings(strings_reduced):
    locales = {}

    for key, value in strings_reduced.items():
        data = {
            "id": value[0]["key"],
            "value": "\n".join([locales_assignment.Render(x) for x in value])
        }

        locales[key] = locales_container.Render(data)

    return locales