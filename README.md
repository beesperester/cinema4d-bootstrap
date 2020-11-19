# cinema4d-bootstrap

Simplify your Cinema 4D plugin development process by generating all the necessary c-headers, strings and resources automatically.

## Table of contents
1. [Description](#Description)
1. [Examples](#Examples)

## Description

With **bootstrap** you can automate a lot of the back and force gerally associated with writing Cinema 4D plugins. No need to write all those pesky header, string and resource files by hand. Just define them in your plugin.py file and automagically build your plugin.h, plugin.res, plugin.str and plugin.pyp file.

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
