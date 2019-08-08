
"""
Low-level UI text description.
"""

from typing import Iterable, Tuple, Sequence
from .color import Color
from .units import FontQUnit

class TextDisplay:
    """
    The lowest level description about how to display text.
    """
    __slots__ = (
        '__size', '__font',
        '__weight', '__italic', '__underline',
        '__color', '__bidi', '__baseline',
    )

    def __init__(
            self,
            size: int,
            font: str,
            weight: int,
            italic: int,
            underline: int,
            color: Color,
            baseline: FontQUnit,
            bidi: bool
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
        assert color
        self.__color = color
        self.__baseline = baseline
        self.__bidi = bidi

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
    def bidi(self) -> bool:
        """Is the text bi-directional?  If true, then the text can be shown
        either left-to-right or right-to-left, depending on the user locale.
        Examples of non-bi-directional text are numbers."""
        return self.__bidi


# left-to-right
TEXT_ORIENTATION_LTR = 'l'

# right-to-left, bidi
TEXT_ORIENTATION_RTL = 'r'

# top-to-bottom, no rotation
TEXT_ORIENTATION_TTB = 't'

# left-to-right, with the text rotated and aligned at the top of the screen.
TEXT_ORIENTATION_LTR_ROTATE_TOP = 'lt'

# left-to-right, with the text rotated and aligned at the bottom of the screen.
TEXT_ORIENTATION_LTR_ROTATE_BOTTOM = 'lb'

# right-to-left, with the text rotated and aligned at the top of the screen.
TEXT_ORIENTATION_RTL_ROTATE_TOP = 'rt'

# right-to-left, with the text rotated and aligned at the bottom of the screen.
TEXT_ORIENTATION_RTL_ROTATE_BOTTOM = 'rb'

TEXT_ORIENTATIONS = (
    TEXT_ORIENTATION_LTR,
    TEXT_ORIENTATION_RTL,
    TEXT_ORIENTATION_TTB,
    TEXT_ORIENTATION_LTR_ROTATE_TOP,
    TEXT_ORIENTATION_LTR_ROTATE_BOTTOM,
    TEXT_ORIENTATION_RTL_ROTATE_TOP,
    TEXT_ORIENTATION_RTL_ROTATE_BOTTOM,
)

TextFragment = Tuple[str, TextDisplay]


class Text:
    """
    A full bit of text to display.
    """
    __slots__ = ('__orientation', '__fragments',)

    def __init__(self, orientation: str, fragments: Iterable[TextFragment]) -> None:
        assert orientation in TEXT_ORIENTATIONS
        self.__orientation = orientation
        self.__fragments = tuple(fragments)

    @property
    def orientation(self) -> str:
        """Direction to draw the text."""
        return self.__orientation

    @property
    def fragments(self) -> Sequence[TextFragment]:
        """Bits of text to show."""
        return self.__fragments
