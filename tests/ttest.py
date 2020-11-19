import c4d
import os

#----begin_resource_section----
from bootstrap import Description

strength = Description({
    "id": "STRENGTH",
    "key": "REAL",
    "value": [
        Description({
            "key": "MIN",
            "value": 0.0
        }),
        Description({
            "key": "MAX",
            "value": 100.0
        }),
        Description({
            "key": "MINSLIDER",
            "value": 0.0
        }),
        Description({
            "key": "MAXSLIDER",
            "value": 100.0
        }),
        Description({
            "key": "STEP",
            "value": 1.0
        }),
        Description({
            "key": "UNIT",
            "value": "PERCENT"
        }),
        Description({
            "key": "CUSTOMGUI",
            "value": "REALSLIDER"
        })
    ],
    "locales": {
        "strings_us": "Strength"
    }
})

up_vector_xplus = Description({
    "id": "UP_VECTOR_XPLUS",
    "key": "UP_VECTOR_XPLUS",
    "locales": {
        "strings_us": "X+"
    }
})

up_vector_xminus = Description({
    "id": "UP_VECTOR_XMINUS",
    "key": "UP_VECTOR_XMINUS",
    "locales": {
        "strings_us": "X-"
    }
})

up_vector = Description({
    "id": "UP_VECTOR",
    "key": "LONG",
    "value": [
        Description({
            "key": "ANIM",
            "value": "OFF"
        }),
        Description({
            "key": "CYCLE",
            "value": [
                up_vector_xplus,
                up_vector_xminus
            ]
        })
    ],
    "locales": {
        "strings_us": "Up Vector"
    }
})

base_settings = Description({
    "id": "GROUP_BASE_SETTINGS",
    "key": "GROUP",
    "value": [
        Description({
            "key": "DEFAULT",
            "value": 1
        }),
        strength,
        up_vector
    ],
    "locales": {
        "strings_us": "Base Settings"
    }
})

root = Description({
    "id": "Tmyawesomeplugin",
    "key": "CONTAINER",
    "value": [
        Description({
            "key": "NAME",
            "value": "Tmyawesomeplugin"
        }),
        Description({
            "key": "INCLUDE",
            "value": "Tbase"
        }),
        Description({
            "key": "INCLUDE",
            "value": "Texpression"
        }),
        base_settings
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

# Be sure to use a unique ID obtained from www.plugincafe.com
PLUGIN_ID = 223456790

class Test(c4d.plugins.TagData):
    """MyAwesomePlugin Class"""

    def Init(self, node):
        """
        Called when Cinema 4D Initialize the TagData (used to define, default values)
        :param node: The instance of the TagData.
        :type node: c4d.GeListNode
        :return: True on success, otherwise False.
        """

        data = node.GetDataInstance()

        data[STRENGTH] = 0.5

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
    fn = os.path.join(directory, "res", "ttest.png")

    # Creates a BaseBitmap
    bmp = c4d.bitmaps.BaseBitmap()
    if bmp is None:
        raise MemoryError("Failed to create a BaseBitmap.")

    # Init the BaseBitmap with the icon
    if bmp.InitWith(fn)[0] != c4d.IMAGERESULT_OK:
        raise MemoryError("Failed to initialize the BaseBitmap.")

    c4d.plugins.RegisterTagPlugin(id=PLUGIN_ID,
        str="Test plugin",
        info=c4d.TAG_EXPRESSION | c4d.TAG_VISIBLE | c4d.TAG_IMPLEMENTS_DRAW_FUNCTION,
        g=Test,
        description="Ttest",
        icon=bmp
    )