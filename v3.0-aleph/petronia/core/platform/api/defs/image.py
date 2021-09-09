
"""
Definition of an image.
"""

from typing import Optional, Union
from .color import Color


class ImageTransform:
    """
    Basic transformation of an image.
    """
    __slots__ = (
        '__scale', '__rotation', '__crop_top', '__crop_left', '__width', '__height',
    )

    def __init__(
            self,
            scale: float,
            rotation: int,
            crop_top: int,
            crop_left: int,
            width: int,
            height: int
    ) -> None:
        assert scale > 0
        assert rotation in (0, 90, 180, 270)
        assert crop_top >= 0
        assert crop_left >= 0
        self.__scale = scale
        self.__rotation = rotation
        self.__crop_top = crop_top
        self.__crop_left = crop_left
        self.__width = width
        self.__height = height

    @property
    def scale(self) -> float:
        return self.__scale

    @property
    def rotation(self) -> int:
        return self.__rotation

    @property
    def crop_top(self) -> int:
        return self.__crop_top

    @property
    def crop_left(self) -> int:
        return self.__crop_left

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height


class ImageLocation:
    """
    A reference to an image stored elsewhere.  The platform will know how to
    transform the name into the location.  Some platforms may have different
    image support capabilities than others, or may search for images in
    different locations.

    Some image formats may allow for altering the displayed color of the
    image.  This is not guaranteed to be used by the platform.
    """
    __slots__ = ('__location', '__color',)

    def __init__(self, location: str, color: Optional[Color]) -> None:
        self.__location = location
        self.__color = color

    @property
    def location(self) -> str:
        """Location relative to search paths for the platform."""
        return self.__location

    @property
    def color(self) -> Optional[Color]:
        """
        Optional display color of the image.  The platform has disgression
        whether to use the color for the image or not.
        """
        return self.__color


class ImageRaw:
    """
    The raw image.  Primarily used for generated images, such as SVG.  The
    platform may refuse to show the image and instead show a placeholder,
    if the mime type is not supported.
    """
    __slots__ = ('__raw', '__mime', '__color',)

    def __init__(self, raw: Union[str, bytes], mime: str, color: Optional[Color]) -> None:
        self.__raw = raw
        assert mime.count('/') == 1
        self.__mime = mime
        self.__color = color

    @property
    def raw(self) -> Union[str, bytes]:
        return self.__raw

    @property
    def mime(self) -> str:
        """The MIME type of the image (e.g. image/svg)"""
        return self.__mime

    @property
    def color(self) -> Optional[Color]:
        """Optional color of the image, if the image format and platform
        supports it."""
        return self.__color


Image = Union[ImageLocation, ImageRaw]
