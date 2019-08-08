
"""
Units for display sizes.
"""

from typing import Tuple

# Pixels according to the screen size measurement.
ScreenUnit = int

# x, y
ScreenPosition = Tuple[ScreenUnit, ScreenUnit]
SCREEN_POSITION_X = 0
SCREEN_POSITION_Y = 1

# w, h
ScreenSize = Tuple[ScreenUnit, ScreenUnit]
SCREEN_SIZE_WIDTH = 0
SCREEN_SIZE_HEIGHT = 1
SCREEN_SIZE_W = SCREEN_SIZE_WIDTH
SCREEN_SIZE_H = SCREEN_SIZE_HEIGHT

# x, y, w, h
ScreenArea = Tuple[ScreenUnit, ScreenUnit, ScreenUnit, ScreenUnit]
SCREEN_AREA_X = 0
SCREEN_AREA_Y = 1
SCREEN_AREA_WIDTH = 2
SCREEN_AREA_HEIGHT = 3
SCREEN_AREA_W = SCREEN_AREA_WIDTH
SCREEN_AREA_H = SCREEN_AREA_HEIGHT

# Quarter font unit.
FontQUnit = int
