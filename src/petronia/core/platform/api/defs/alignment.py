
"""
Constants and types for aligning things against other things.
"""

# Text Bi-directional display direction.
TextBiDi = bool
TEXT_BIDI_LTR = True
TEXT_BIDI_RTL = False

# Text display rotation
TextRotation = str

# Characters are aligned along the horizontal line.
TEXT_ROTATE_HORIZ = 'h'

# Characters are rotated 90 degrees clockwise,
# so for L-T-R BiDi text, the start of the text is at the top.
TEXT_ROTATE_90_CLOCKWISE = 'c'

# Characters are rotated 90 degrees counter-clockwise,
# so for L-T-R BiDi text, the start of the text is at the bottom.
TEXT_ROTATE_90_COUNTER_CLOCKWISE = 'n'

TEXT_ROTATE_ALL = (
    TEXT_ROTATE_HORIZ,
    TEXT_ROTATE_90_CLOCKWISE,
    TEXT_ROTATE_90_COUNTER_CLOCKWISE,
)

# How the text aligns with paired graphic items or the contained box.
TextAlignment = str

# Text is start-of-line aligned to the upper-left.
TEXT_ALIGN_UPPER_LEFT = 'ul'

# Text is end-of-line aligned to the upper-right.
TEXT_ALIGN_UPPER_RIGHT = 'ur'

# Text is start-of-line aligned to the bottom-left.
TEXT_ALIGN_BOTTOM_LEFT = 'bl'

# Text is end-of-line aligned to the bottom-right.
TEXT_ALIGN_BOTTOM_RIGHT = 'br'

# Text is vertically centered, start-of-line left.
TEXT_ALIGN_CENTER_LEFT = 'cl'

# Text is vertically centerd, end-of-line right.
TEXT_ALIGN_CENTER_RIGHT = 'cr'

# Text is top, centered horizontally.
TEXT_ALIGN_UPPER_CENTER = 'uc'

# Text is bottom, center horizontally.
TEXT_ALIGN_BOTTOM_CENTER = 'bc'

# Text is center aligned vertically and horizontally.
TEXT_ALIGN_CENTER_CENTER = 'cc'

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
