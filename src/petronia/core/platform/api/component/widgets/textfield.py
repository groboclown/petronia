
"""
Text input widget.  Has its own response events.
"""

from ......base import create_singleton_identity


COMPONENT_ID_CREATE_TEXTFIELD = create_singleton_identity('core.platform.api/textfield')


class TextFieldWidget:
    """
    Displays a text field with an optional label and picture and activation button.
    """
    __slots__ = (
        '__label', '__icon', '__char_width', '__button_label',
        '__default_text',
    )

    def __init__(self) -> None:
        pass
