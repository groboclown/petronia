
"""
Text input widget.  Has its own response events.
"""

from ......system.participant import create_singleton_identity


COMPONENT_ID_CREATE_TEXTFIELD = create_singleton_identity('core.platform.api/textfield')


class TextFieldWidget:
    """
    Displays a text field with an optional label and picture and activation button.
    """
    __slots__ = ('placeholder',)

    def __init__(self) -> None:
        pass
