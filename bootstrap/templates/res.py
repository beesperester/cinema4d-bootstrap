from bootstrap.template import Template

CONTAINER_TEMPLATE = Template(
"""{resource} {name}
{{
    {flags}

    {children}
}}
"""
)

FLAG_TEMPLATE = Template("{key} {value};")