import c4d
import os

#----begin_resource_section----
from bootstrap.bootstrap import Description, DescriptionFlag, Layout, Group

# this creates a new description object with the ID "MY_PERCENTAGE_INPUT"
# the strings_us locale "My Percentage Input"
# the datatype "REAL"
# and the flags "MIN" and "MAX"
my_percentage_data = Description(
    "MY_PERCENTAGE_INPUT",
    {
        "strings_us": "My Percentage Input"
    },
    "REAL",
    [
        DescriptionFlag("MIN", 0.0),
        DescriptionFlag("MAX", 100.0)
    ]
)

# this creates a new layout as a representation 
# of the plugin structure in Cinema 4D 
# it will include Tbase and Texpression
# it will create a group called "Settings" with a sub group called "Base Data"
# which will contain the Description of "my_percentage_data"
layout = Layout(
    "Tmyawesomeplugin",
    {
        "strings_us": "My Awesome Plugin"
    },
    [
        DescriptionFlag("NAME", "Tmyawesomeplugin"),
        DescriptionFlag("INCLUDE", "Tbase"),
        DescriptionFlag("INCLUDE", "Texpression")
    ],
    Group(
        "GROUP_SETTINGS",
        {
            "strings_us": "Settings"
        },
        [
            DescriptionFlag("DEFAULT", 1)
        ],
        [
            Group(
                "GROUP_BASE_DATA",
                {
                    "strings_us": "Base Data"
                },
                [
                    DescriptionFlag("DEFAULT", 1)
                ],
                [
                    my_percentage_data
                ]
            )
        ]
    )
)
#----end_resource_section----

#----begin_id_section----
# IDs will be automatically injected
MY_PERCENTAGE_DATA = my_percentage_data.GetId()
#----end_id_section----

# Be sure to use a unique ID obtained from www.plugincafe.com
PLUGIN_ID = 223456790

class MyAwesomePlugin(c4d.plugins.TagData):
    """MyAwesomePlugin Class"""

    def Init(self, node):
        """
        Called when Cinema 4D Initialize the TagData (used to define, default values)
        :param node: The instance of the TagData.
        :type node: c4d.GeListNode
        :return: True on success, otherwise False.
        """

        data = node.GetDataInstance()

        data[MY_PERCENTAGE_DATA] = 0.5

        c4d.EventAdd()

        return True

    def Execute(self, tag, doc, op, bt, priority, flags):
        """
        Called by Cinema 4D at each Scene Execution, this is the place where calculation should take place.
        :param tag: The instance of the TagData.
        :type tag: c4d.BaseTag
        :param doc: The host document of the tag's object.
        :type doc: c4d.documents.BaseDocument
        :param op: The host object of the tag.
        :type op: c4d.BaseObject
        :param bt: The Thread that execute the this TagData.
        :type bt: c4d.threading.BaseThread
        :param priority: Information about the execution priority of this TagData.
        :type priority: EXECUTIONPRIORITY
        :param flags: Information about when this TagData is executed.
        :type flags: EXECUTIONFLAGS
        :return:
        """

        return c4d.EXECUTIONRESULT_OK 

if __name__ == "__main__":
    # Retrieves the icon path
    directory, _ = os.path.split(__file__)
    fn = os.path.join(directory, "res", "tmyawesomeplugin.png")

    # Creates a BaseBitmap
    bmp = c4d.bitmaps.BaseBitmap()
    if bmp is None:
        raise MemoryError("Failed to create a BaseBitmap.")

    # Init the BaseBitmap with the icon
    if bmp.InitWith(fn)[0] != c4d.IMAGERESULT_OK:
        raise MemoryError("Failed to initialize the BaseBitmap.")

    c4d.plugins.RegisterTagPlugin(id=PLUGIN_ID,
        str="My Awesome Plugin",
        info=c4d.TAG_EXPRESSION | c4d.TAG_VISIBLE | c4d.TAG_IMPLEMENTS_DRAW_FUNCTION,
        g=MyAwesomePlugin,
        description="Tmyawesomeplugin",
        icon=bmp
    )