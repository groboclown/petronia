
"""
Area for displaying the notification icons.  Used primarily for the taskbar,
if you want one.  The contents are entirely up to the platform to show.
"""

from ...defs import Color

class NotificationIconArea:
    """
    An area which is left up to the platform to render.

    The end-user can request the maximum number of icons
    to display and the background color.
    """
    __slots__ = ('__max', '__bg',)

    def __init__(self, maximum_icon_display: int, background: Color) -> None:
        self.__max = maximum_icon_display
        self.__bg = background
