![Python Package](https://github.com/beesperester/cinema4d-bootstrap/workflows/Python%20Package/badge.svg?branch=main)

# cinema4d-bootstrap

Simplify your Cinema 4D plugin development process by generating all the necessary c-headers, strings and resources automatically.

## Table of contents
1. [Description](#Description)
1. [Examples](#Examples)
1. [Plugins](#Plugins)

## Description

With **bootstrap** you can automate a lot of the back and force gerally associated with writing Cinema 4D plugins. No need to write all those pesky header, string and resource files by hand. Just define them in your plugin.py file and automagically build your plugin.h, plugin.res, plugin.str and plugin.pyp file.

> You need to use **c4dpy** to build your plugin

In the following excerpt you can see a very basic setup for a **REAL** value called **STRENGTH** which willbe displayed as **PERCENT**. This is wrappend in a **GROUP** with the name **SETTINGS** which is itself wrapped in a **CONTAINER** that represents the plugin. 

```python
#----begin_resource_section----
from bootstrap import Container, Assignment, Group, Description

strength = Description({
    "id": "STRENGTH",
    "key": "REAL",
    "value": [
        Assignment("UNIT", "PERCENT")
    ],
    "locales": {
        "strings_us": "Strength"
    }
})

settings_group = Group("SETTINGS", {
    "value": [
        strength
    ],
    "locales": {
        "strings_us": "Settings"
    }
})

root = Container("Tmyplugin", {
    "value": [
        Assignment("NAME", "Tmyplugin"),
        Assignment("INCLUDE", "Tbase"),
        Assignment("INCLUDE", "Texpression"),
        settings_group
    ],
    "locales": {
        "strings_us": "My awesome plugin"
    }
})
#----end_resource_section----

#----begin_id_section----
# IDs will be automatically injected
STRENGTH = strength.GetId()
#----end_id_section----

[...]
```

Building this will result in the following generated files:

**tmyplugin.res**
```C++
CONTAINER Tmyplugin
{
    NAME Tmyplugin;
    INCLUDE Tbase;
    INCLUDE Texpression;
    GROUP SETTINGS
    {
        REAL STRENGTH
        {
            UNIT PERCENT;
        }
    }
}
```

**tmyplugin.h**
```C++
#ifndef _Oatom_H_
#define _Oatom_H_

enum
{
    Tmyplugin = 72636982,
    SETTINGS = 59543963,
    STRENGTH = 34087515,
};

#endif
```

**tmyplugin.str**
```C++
STRINGTABLE Tmyplugin
{
    Tmyplugin "My awesome plugin";
    SETTINGS "Base Settings";
    STRENGTH "Strength";
}
```

**tmyplugin.pyp**
```python
STRENGTH = 34087515

[...]
```

## Examples

Check out `tmyplugin.py` for a simple working example.

You will notice two types of comments which describe specific parts of your plugin setup.

This will be where you setup the layout of your plugin, this will be omitted in the final output.

```python
#----begin_resource_section----
...
#----end_resource_section----
```

This will be where you define your plugin IDs, the static IDs will be injected as integers during the build process
```python
#----begin_id_section----
...
#----end_id_section----
```

Executing the `build.py` file with c4dpy will generate the following files:

```python
tmyplugin.pyp # the actual plugin file
res/description/tmyplugin.h # the header file with the IDs
res/description/tmyplugin.res # the layout
res/strings_us/description/tmyplugin.str # the localized strings
```

## Plugins

Plugins that are using bootstrap:

1. [cinema4d-jiggle](https://github.com/beesperester/cinema4d-jiggle)