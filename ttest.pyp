import os
import c4d


SETTINGS_STRENGTH = 27890828
SETTINGS_OFFSET = 15150201

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