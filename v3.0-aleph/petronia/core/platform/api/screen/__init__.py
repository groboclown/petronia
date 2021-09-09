
"""
State definitions for the display areas for the computer.

The screen resolution has already been scaled based on the user's scaling
preference.  For large monitors, this can mean each screen pixel reported
implies several real pixels.
"""

from .screen_state import (
    STATE_ID_SCREENS,
    ScreenState,
    VirtualScreenArea,
    set_screen_state,
)
