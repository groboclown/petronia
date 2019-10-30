
"""
Constants for the layout.
"""

from ....aid.std import (
    create_singleton_identity,
)

MODULE_ID = create_singleton_identity('default.layout.tile')

MOVE_WINDOW_DIRECTION_NORTH = 1
MOVE_WINDOW_DIRECTION_SOUTH = 2
MOVE_WINDOW_DIRECTION_EAST = 3
MOVE_WINDOW_DIRECTION_WEST = 4
MOVE_WINDOW_DIRECTION_ALL = (
    MOVE_WINDOW_DIRECTION_NORTH,
    MOVE_WINDOW_DIRECTION_SOUTH,
    MOVE_WINDOW_DIRECTION_EAST,
    MOVE_WINDOW_DIRECTION_WEST,
)

PORTAL_COMPONENT_CATEGORY = 'default.layout.tile/tile-portal'
