
"""
Widgets are added into custom components that support them.
"""

from typing import Iterable, Union, Optional
from ..defs import RespondsToAction
from ......errors import PetroniaInternalError
from ......base import create_singleton_identity


COMPONENT_ID_CREATE_INFOBOX = create_singleton_identity('core.platform.api/infobox')


class InfoBoxWidget:
    """
    Information for creating an information display widget inside another
    component.  It can display text and an image, and the data can be updated
    by sending it configuration update events.  This can double as a button
    by adding in "RespondsToAction" for mouse clicks.

    The position of the image and text is up to the theme and locale.

    Pass to RequestNewComponentEvent or as part of a widget list.  Also
    pass to the Configuration state event.
    """

    __slots__ = (
        '__text', '__text_args', '__image_name', '__image_data', '__image_mime',
        '__bg', '__fg', '__border_style', '__responds_to',
    )

    def __init__(
            self,
            text: Optional[str] = None,
            text_args: Optional[Iterable[Union[str, int, float, bool, None]]] = None,
            image_name: Optional[str] = None,
            image_data: Optional[str] = None,
            image_mime: Optional[str] = None,
            background_color: Optional[str] = None,
            foreground_color: Optional[str] = None,
            border_style: Optional[str] = None,
            responds_to: Optional[RespondsToAction] = None
    ) -> None:
        if image_name is not None and image_data is not None:
            raise PetroniaInternalError(
                'cannot define both image name and image data at the same time.'
            )
        if image_data is not None and image_mime is None:
            raise PetroniaInternalError(
                'must provide both image_data and image_mime.'
            )
        self.__text = text
        self.__text_args = text_args
        self.__image_name = image_name
        self.__image_data = image_data
        self.__image_mime = image_mime
        self.__bg = background_color
        self.__fg = foreground_color
        self.__border_style = border_style
        self.__responds_to = responds_to

    @property
    def text_message(self) -> Optional[str]:
        """Display text message name.  This will be localized before display,
        using the text arguments as input."""
        return self.__text

    @property
    def text_args(self) -> Optional[Iterable[Union[str, int, float, bool, None]]]:
        """Localized message arguments."""
        return self.__text_args

    @property
    def image_name(self) -> Optional[str]:
        """Name of the image to show.  Should be a relative path to the
        user's Petronia directory or system Petronia directory or the active
        theme.  If this is provided, the image mime may be ignored, and the
        image data will not be used."""
        return self.__image_name

    @property
    def image_data(self) -> Optional[str]:
        """A text-encoded version of the image to show, for the cases where a
        generated image is needed.  The mime type is required, but should be
        a text format, like SVG."""
        return self.__image_data

    @property
    def image_mime(self) -> Optional[str]:
        """Mime-type (like `image/svg`) of the image."""
        return self.__image_mime

    @property
    def foreground_color(self) -> Optional[str]:
        """A theme name for the foreground text color.  For some images, will
        also be used for that.  If not specified, the theme appropriate color
        is used."""
        return self.__fg

    @property
    def background_color(self) -> Optional[str]:
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
