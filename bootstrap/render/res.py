from bootstrap.template import Template

resource_container = Template(
"""{key} {id}
{{
    {value}
}}"""
)

resource_assignment = Template("{key} {value};")

def render_resource(resource_reduced):
    data = {**resource_reduced}

    if isinstance(data["value"], list):
        data["value"] = [render_resource(x) for x in data["value"]]

        return resource_container.Render(data)
    
    return resource_assignment.Render(data)