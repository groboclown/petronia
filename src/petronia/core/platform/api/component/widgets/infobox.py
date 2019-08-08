
"""
Widgets are added into custom components that support them.
"""

from typing import Optional
from ...defs import (
    RespondsToAction,
    Text,
    TextAlignment,
    TextRotation,
    Image,
    Color,
)
from ......base import create_singleton_identity


COMPONENT_ID_CREATE_INFOBOX = create_singleton_identity('core.platform.api/infobox')


class InfoBoxWidget:
    """
    Information for creating an information display widget inside another
    component.  It can display text and an image, and the data can be updated
    by sending it configuration update events.  This can double as a button
    by adding in "RespondsToAction" for mouse clicks.

    Pass to RequestNewComponentEvent or as part of a widget list.  Also
    pass to the Configuration state event.
    """

    __slots__ = (
        '__text', '__image',
        '__bg', '__fg', '__border_style', '__responds_to',
    )

    def __init__(
            self,
            text: Optional[Text],
            image: Optional[Image],
            text_alignment: Optional[TextAlignment] = None,
            text_rotation: Optional[TextRotation] = None,
            background_color: Optional[Color] = None,
            foreground_color: Optional[Color] = None,
            border_style: Optional[str] = None,
            responds_to: Optional[RespondsToAction] = None
    ) -> None:
        self.__text = text
        self.__image = image
        self.__bg = background_color
        self.__fg = foreground_color
        self.__border_style = border_style
        self.__responds_to = responds_to

    @property
    def text(self) -> Optional[Text]:
        """Localized message."""
        return self.__text

    @property
    def image(self) -> Optional[Image]:
        """Image to show."""
        return self.__image

    @property
    def foreground_color(self) -> Optional[Color]:
        """A theme name for the foreground text color.  For some images, will
        also be used for that.  If not specified, the theme appropriate color
        is used."""
        return self.__fg

    @property
    def background_color(self) -> Optional[Color]:
        """A theme name for the background color."""
        return self.__bg

    @property
    def border_style(self) -> Optional[str]:
        """Style definition for the border around the widget."""
        return self.__border_style

    @property
    def responds_to(self) -> Optional[RespondsToAction]:
        """All the actions that this widget should send out events when they
        occur."""
        return self.__responds_to
