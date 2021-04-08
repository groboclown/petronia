
"""
Constants and types for aligning things against other things.
"""

from typing import Tuple
from .units import FontQUnit

# Text display rotation
TextRotation = int

# Characters are aligned along the horizontal line.
TEXT_ROTATE_HORIZ = 0

# Characters are rotated 90 degrees clockwise,
# so for L-T-R BiDi text, the start of the text is at the top.
TEXT_ROTATE_90_CLOCKWISE = 270

# Characters are rotated 90 degrees counter-clockwise,
# so for L-T-R BiDi text, the start of the text is at the bottom.
TEXT_ROTATE_90_COUNTER_CLOCKWISE = 90

TEXT_ROTATE_ALL = (
    TEXT_ROTATE_HORIZ,
    TEXT_ROTATE_90_CLOCKWISE,
    TEXT_ROTATE_90_COUNTER_CLOCKWISE,
)

# How the text aligns with paired graphic items or the contained box.
TextAlignment = str

# Text is start-of-line aligned to the upper-left.
TEXT_ALIGN_UPPER_LEFT = 'ul'

# Text is top, centered horizontally.
TEXT_ALIGN_UPPER_CENTER = 'uc'

# Text is end-of-line aligned to the upper-right.
TEXT_ALIGN_UPPER_RIGHT = 'ur'

# Text is vertically centered, start-of-line left.
TEXT_ALIGN_CENTER_LEFT = 'cl'

# Text is center aligned vertically and horizontally.
TEXT_ALIGN_CENTER_CENTER = 'cc'

# Text is vertically centered, end-of-line right.
TEXT_ALIGN_CENTER_RIGHT = 'cr'

# Text is start-of-line aligned to the bottom-left.
TEXT_ALIGN_BOTTOM_LEFT = 'bl'

# Text is bottom, center horizontally.
TEXT_ALIGN_BOTTOM_CENTER = 'bc'

# Text is end-of-line aligned to the bottom-right.
TEXT_ALIGN_BOTTOM_RIGHT = 'br'

TEXT_ALIGN_ALL = (
    TEXT_ALIGN_UPPER_LEFT,
    TEXT_ALIGN_UPPER_RIGHT,
    TEXT_ALIGN_BOTTOM_LEFT,
    TEXT_ALIGN_BOTTOM_RIGHT,
    TEXT_ALIGN_CENTER_LEFT,
    TEXT_ALIGN_CENTER_RIGHT,
    TEXT_ALIGN_UPPER_CENTER,
    TEXT_ALIGN_BOTTOM_CENTER,
    TEXT_ALIGN_CENTER_CENTER,
)

# How much extra space to put around the item (text or image)
Padding = Tuple[FontQUnit, FontQUnit, FontQUnit, FontQUnit]

# Where to put the image, relative to the text.
ImageRelativeVerticalAlign = int
IMAGE_RELATIVE_VERTICAL_TOP = 0
IMAGE_RELATIVE_VERTICAL_CENTER = 1
IMAGE_RELATIVE_VERTICAL_BASELINE = 2
IMAGE_RELATIVE_VERTICAL_BOTTOM = 3
IMAGE_RELATIVE_VERTICAL_ALL = (
    IMAGE_RELATIVE_VERTICAL_TOP,
    IMAGE_RELATIVE_VERTICAL_CENTER,
    IMAGE_RELATIVE_VERTICAL_BASELINE,
    IMAGE_RELATIVE_VERTICAL_BOTTOM,
)

ImageRelativePosition = int
IMAGE_RELATIVE_POSITION_N = 0
IMAGE_RELATIVE_POSITION_E = 1
IMAGE_RELATIVE_POSITION_S = 2
IMAGE_RELATIVE_POSITION_W = 3
IMAGE_RELATIVE_POSITION_CENTER = 4
IMAGE_RELATIVE_POSITION_ALL = (
    IMAGE_RELATIVE_POSITION_N,
    IMAGE_RELATIVE_POSITION_E,
    IMAGE_RELATIVE_POSITION_S,
    IMAGE_RELATIVE_POSITION_W,
    IMAGE_RELATIVE_POSITION_CENTER,
)

ImageRelativeZOrder = int
# The image does not overlap the text at all.
IMAGE_RELATIVE_Z_ORDER_HARD = 0

# The image is in front of the text
IMAGE_RELATIVE_Z_ORDER_FRONT = 1

# The image is behind the text
IMAGE_RELATIVE_Z_ORDER_BACK = 2
IMAGE_RELATIVE_Z_ORDER_ALL = (
    IMAGE_RELATIVE_Z_ORDER_HARD,
    IMAGE_RELATIVE_Z_ORDER_FRONT,
    IMAGE_RELATIVE_Z_ORDER_BACK,
)

ImageRelativeTextPosition = Tuple[ImageRelativeVerticalAlign, ImageRelativePosition, ImageRelativeZOrder]
