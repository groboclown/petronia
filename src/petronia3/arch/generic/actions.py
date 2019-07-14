
"""
Actions that the platform must implement.

These are made globally available (how?).
"""

class PlatformGuiToolkit(object):
    """
    Allows the Petronia system to construct user interface elements on the
    platform.  The platform must handle the proper underlying registration.
    """

    # TODO set the return type correctly; it should be a handle to the created
    # component.
    def text_box(self, title: str, text: str) -> None:
        """
        Create a text box on the screen as a visible component.
        """
        raise NotImplementedError()
