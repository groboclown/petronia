
"""
Low-level UI text description.
"""

from typing import Iterable, Tuple
from .color import Color
from .units import FontQUnit
from .alignment import TextBiDi

class TextDisplay:
    """
    The lowest level description about how to display text.
    """
    __slots__ = (
        '__size', '__font',
        '__weight', '__italic', '__underline', '__strikethrough',
        '__color', '__baseline', '__base_dir',
    )

    def __init__(
            self,
            size: int,
            font: str,
            weight: int,
            italic: int,
            underline: int,
            strikethrough: int,
            color: Color,
            baseline: FontQUnit,
            base_direction: TextBiDi
    ) -> None:
        assert size > 0
        self.__size = size
        assert font
        self.__font = font
        assert weight >= 0
        self.__weight = weight
        assert italic >= 0
        self.__italic = italic
        assert underline >= 0
        self.__underline = underline
        assert strikethrough >= 0
        self.__strikethrough = strikethrough
        assert color
        self.__color = color
        self.__baseline = baseline
        self.__base_dir = base_direction

    @property
    def size(self) -> int:
        """."""
        return self.__size

    @property
    def font(self) -> str:
        """The name of the font to print.  It is left to the platform to
        interpret how to show this font face."""
        return self.__font

    @property
    def weight(self) -> int:
        """The weight of the drawing stroke (boldness).  This is limited
        by the font.  `0` means normal weight."""
        return self.__weight

    @property
    def italic(self) -> int:
        """The amount of italic to show.  This is limited by the font.
        `0` means no italics."""
        return self.__italic

    @property
    def underline(self) -> int:
        """The number of underlines to put on the text.  Some platforms will
        have a maximum number."""
        return self.__underline

    @property
    def strikethrough(self) -> int:
        """The number of lines to draw through the text.  Some platforms will
        have a maximum number."""
        return self.__strikethrough

    @property
    def color(self) -> Color:
        """Text color."""
        return self.__color

    @property
    def baseline(self) -> FontQUnit:
        """Distance from the baseline to draw the text.  This allows for
        superscript or subscript display.  This is measured as quarter
        font size increments, so -2 means a half font height lower, and 1
        means a quarter font height higher."""
        return self.__baseline

    @property
    def base_direction(self) -> TextBiDi:
        """Initial BiDi direction to start rendering this fragment.  Each
        fragment has its own BiDi initial direction for rendering.  The
        renderer does not keep track of cross-fragment direction switches."""
        return self.__base_dir


# The text to display, and how to display it.
TextFragment = Tuple[str, TextDisplay]

Text = Iterable[TextFragment]
