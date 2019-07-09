
"""
Basic parts that must be implemented by each OS implementation.

Everything else is interacted on at the event bus level.
"""


class PlatformDescription(object):
    """
    Allows the Petronia system to discover information about the platform.
    """

    def get_screen_sizes(self):
        raise NotImplementedError()


class PlatformGuiToolkit(object):
    """
    Allows the Petronia system to construct user interface elements on the
    platform.  The platform must handle the proper underlying registration.
    """

    def text_box(self, title, text):
        raise NotImplementedError()
