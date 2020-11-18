from bootstrap.template import Template

STR_CONTAINER_TEMPLATE = Template(
"""STRINGTABLE {name}
{{
    {pluginName}

    {children}
}}
"""
)

STR_DEFINITION_TEMPLATE = Template("{key} \"{value}\";")