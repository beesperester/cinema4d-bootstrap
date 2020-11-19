from bootstrap.template import Template

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

header_assignment = Template("{key} = {value},")

def render_header(header_reduced):
    data = {
        "value": [header_assignment.Render(x) for x in header_reduced]
    }

    return header_container.Render(data)