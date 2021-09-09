
"""
Text input widget.  Has its own response events.
"""

from typing import Sequence
from ......base import create_singleton_identity
from ...defs import (
    TextAlignment, TextRotation, TextDisplay,
)


COMPONENT_ID_CREATE_TEXTFIELD = create_singleton_identity('core.platform.api/textfield')


class TextFieldWidget:
    """
    Displays a text field - an area where the user can enter text, and the entered text is
    displayed.  If the mask is a non-empty string, then each character typed will be replaced with
    that mask value instead (allows for password entry).  If there are drop-down values, then they
    are shown below the text field like a combo-box, and the user can select one of the values.

    The standard keyboard entry usage will be allowed.  On each update to the text value, an action is
    sent to the component.  The drop-down values are replaceable through events.

    If the user hasn't entered any text, then the default text, shown in the default_text_display,
    is shown to the user in the text field.

    If you want a label or icon or activation button, that will need to be added in the owning
    container.
    """
    __slots__ = (
        '__default_text', '__char_width', '__text_alignment', '__text_rotation',
        '__display', '__default_text_display', '__text_mask', '__drop_down_values'
    )

    def __init__(
            self,
            default_text: str,
            char_width: int,
            text_alignment: TextAlignment,
            text_rotation: TextRotation,
            display: TextDisplay,
            default_text_display: TextDisplay,
            text_mask: str,
            drop_down_values: Sequence[str]
    ) -> None:
        self.__default_text = default_text
        self.__char_width = char_width
        self.__text_alignment = text_alignment
        self.__text_rotation = text_rotation
        self.__display = display
        self.__default_text_display = default_text_display
        self.__text_mask = text_mask
        self.__drop_down_values = drop_down_values
