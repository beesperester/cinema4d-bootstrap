![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg) ![Python Package](https://github.com/beesperester/cinema4d-bootstrap/workflows/Python%20Package/badge.svg?branch=main) ![Upload Python Package](https://github.com/beesperester/cinema4d-bootstrap/workflows/Upload%20Python%20Package/badge.svg)

# bootstrap4c4d

Simplify your Cinema 4D plugin development process by generating all the necessary c-headers, strings and resources automatically.

## Table of contents
1. [Description](#Description)
1. [Installation](#Installation)
1. [Usage](#Usage)
    - [Build](#Build)
    - [Create](#Create)
1. [Examples](#Examples)
1. [Plugins](#Plugins)
1. [To do](#To-do)

## Description

With **bootstrap4c4d** you can automate a lot of the back and fore generally associated with writing Cinema 4D plugins. No need to write all those pesky header, string and resource files by hand. Just define them in your plugin.py file and automagically build your plugin.h, plugin.res, plugin.str and plugin.pyp file.

In the following excerpt you can see a very basic setup for a **REAL** value called **STRENGTH** which willbe displayed as **PERCENT**. This is wrappend in a **GROUP** with the name **SETTINGS** which is itself wrapped in a **CONTAINER** that represents the plugin:

```python
#----begin_resource_section----
from bootstrap4c4d import Container, Assignment, Group, Description

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

## Installation

First you need to get the path to **c4dpy**. On macOS this will be something like this:
```
/Applications/Maxon Cinema 4D R23/c4dpy.app/Contents/MacOS/c4dpy
```

For further information about **c4dpy** please refer to the official [documentation](https://developers.maxon.net/docs/Cinema4DPythonSDK/html/manuals/introduction/python_c4dpy.html).

Next you need to download [pip](https://pip.pypa.io/en/stable/installing/)
```
$ curl https://bootstrap4c4d.pypa.io/get-pip.py -o /path/to/some/directory/get-pip.py
```

For installing pip you need to make sure to use the path to **c4dpy** instead of your system's python  installation
```
$ "/Applications/Maxon Cinema 4D R23/c4dpy.app/Contents/MacOS/c4dpy" /path/to/some/directory/get-pip.py
```

Now you are ready to install **bootstrap4c4d** via pip

```
$ "/Applications/Maxon Cinema 4D R23/c4dpy.app/Contents/MacOS/c4dpy" -m pip install bootstrap4c4d-beesperester
```

## Usage

Display available cli arguments:

```
$ "/Applications/Maxon Cinema 4D R23/c4dpy.app/Contents/MacOS/c4dpy" -m bootstrap4c4d -h
```

### Build

Build an existing python plugin which has already been set up with **bootstrap4c4d**:

```
$ "/Applications/Maxon Cinema 4D R23/c4dpy.app/Contents/MacOS/c4dpy" -m bootstrap4c4d build /path/to/your/plugin.py
```

### Create

Create a new tag / object plugin with **bootstrap4c4d**:

```
$ "/Applications/Maxon Cinema 4D R23/c4dpy.app/Contents/MacOS/c4dpy" -m bootstrap4c4d create YOUR_PLUGIN_NAME tag /path/to/your/plugin_directory
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

This will be where you define your plugin IDs, the static IDs will be injected as integers during the build process:

```python
#----begin_id_section----
...
#----end_id_section----
```

Using **bootstrap4c4d** like so will build the plugin:

```
$ "/Applications/Maxon Cinema 4D R23/c4dpy.app/Contents/MacOS/c4dpy" -m bootstrap4c4d build tmyplugin.py
```

This will result in the following files beeing created:

```python
tmyplugin.pyp # the actual plugin file
res/description/tmyplugin.h # the header file with the IDs
res/description/tmyplugin.res # the layout
res/strings_us/description/tmyplugin.str # the localized strings
```

## Plugins

Plugins build with **bootstrap4c4d**:

1. [cinema4d-jiggle](https://github.com/beesperester/cinema4d-jiggle)

## To do

- [ ] Rewrite build process in a functional way
- [x] Add create functionality to cli / io
- [x] Publish package to pypi