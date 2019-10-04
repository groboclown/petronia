
"""
Widgets are added into custom components that support them.
"""

from typing import Mapping, Optional, Union
from ...defs import (
    RespondsToAction,
    Text,
    TextAlignment,
    TextRotation,
    Image,
    ImageTransform,
    ImageRelativeTextPosition,
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

    TODO add events to allow changing the contents.
    """

    __slots__ = (
        '__text_format', '__image', '__text_data',
        '__text_alignment', '__text_rotation', '__image_transform',
        '__image_text_position',
        '__bg', '__fg', '__border_style', '__responds_to',
    )

    def __init__(
            self,
            text_format: Optional[Text],
            text_data: Optional[Mapping[str, Union[str, float, int, bool]]],
            image: Optional[Image],
            text_alignment: Optional[TextAlignment] = None,
            text_rotation: Optional[TextRotation] = None,
            image_transform: Optional[ImageTransform] = None,
            image_text_position: Optional[ImageRelativeTextPosition] = None,
            background_color: Optional[Color] = None,
            foreground_color: Optional[Color] = None,
            border_style: Optional[str] = None,
            responds_to: Optional[RespondsToAction] = None
    ) -> None:
        self.__text_format = text_format
        self.__text_data = text_data
        self.__image = image
        self.__text_alignment = text_alignment
        self.__text_rotation = text_rotation
        self.__image_transform = image_transform
        self.__image_text_position = image_text_position
        self.__bg = background_color
        self.__fg = foreground_color
        self.__border_style = border_style
        self.__responds_to = responds_to

    @property
    def text_format(self) -> Optional[Text]:
        """Localized message."""
        return self.__text_format

    @property
    def text_data(self) -> Optional[Mapping[str, Union[str, float, int, bool]]]:
        return self.__text_data

    @property
    def image(self) -> Optional[Image]:
        """Image to show."""
        return self.__image

    @property
    def text_alignment(self) -> Optional[TextAlignment]:
        return self.__text_alignment

    @property
    def text_rotation(self) -> Optional[TextRotation]:
        return self.__text_rotation

    @property
    def image_transform(self) -> Optional[ImageTransform]:
        return self.__image_transform

    @property
    def image_text_position(self) -> Optional[ImageRelativeTextPosition]:
        return self.__image_text_position

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
