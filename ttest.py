import os
import c4d

#----begin_resource_section----
from bootstrap.bootstrap import Description, DescriptionFlag, Layout, Group

settings_strength = Description(
    "SETTINGS_STRENGTH",
    {
        "strings_us": "Strength"
    },
    "REAL",
    [
        DescriptionFlag("MIN", 0.0),
        DescriptionFlag("MAX", 100.0)
    ]
)

settings_offset = Description(
    "SETTINGS_OFFSET",
    {
        "strings_us": "Offset"
    },
    "VECTOR",
    []
)

layout = Layout(
    "Ttest",
    {
        "strings_us": "Test"
    },
    [
        DescriptionFlag("NAME", "Ttest"),
        DescriptionFlag("INCLUDE", "Tbase"),
        DescriptionFlag("INCLUDE", "Texpression")
    ],
    Group(
        "SETTINGS_GROUP",
        {
            "strings_us": "Settings"
        },
        [
            DescriptionFlag("DEFAULT", 1)
        ],
        [
            settings_strength,
            Group(
                "GROUP_LABEL_OFFSET",
                {
                    "strings_us": "Offset Settings"
                },
                [
                    DescriptionFlag("INCLUDE", "Tbase"),
                    DescriptionFlag("INCLUDE", "Texpression")
                ],
                [
                    settings_offset
                ]
            )
        ]
    )
)
#----end_resource_section----

#----begin_id_section----
SETTINGS_STRENGTH = settings_strength.GetId()
SETTINGS_OFFSET = settings_offset.GetId()
#----end_id_section----

# Be sure to use a unique ID obtained from www.plugincafe.com
PLUGIN_ID = 223456790

class Test(c4d.plugins.TagData):
    """Test Class"""

if __name__ == "__main__":
    # Retrieves the icon path
    directory, _ = os.path.split(__file__)
    fn = os.path.join(directory, "res", "ttest.png")

    # Creates a BaseBitmap
    bmp = c4d.bitmaps.BaseBitmap()
    if bmp is None:
        raise MemoryError("Failed to create a BaseBitmap.")

    # Init the BaseBitmap with the icon
    if bmp.InitWith(fn)[0] != c4d.IMAGERESULT_OK:
        raise MemoryError("Failed to initialize the BaseBitmap.")

    c4d.plugins.RegisterTagPlugin(id=PLUGIN_ID,
        str="Test",
        info=c4d.TAG_EXPRESSION | c4d.TAG_VISIBLE | c4d.TAG_IMPLEMENTS_DRAW_FUNCTION,
        g=Test,
        description="Ttest",
        icon=bmp
    )