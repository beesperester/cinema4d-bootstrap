from bootstrap.template import Template

HEADER_CONTAINER_TEMPLATE = Template(
"""#ifndef _Oatom_H_
#define _Oatom_H_

enum
{{
    {children}
}};

#endif
"""
)

HEADER_DEFINITION_TEMPLATE = Template("{key} = {value},")