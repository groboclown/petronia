
"""
Area for displaying the notification icons.  Used primarily for the taskbar,
if you want one.  The contents are entirely up to the platform to show.
"""

from ......base import create_singleton_identity
from ...defs import Color

COMPONENT_ID_CREATE_NOTIFICATION_ICON_AREA = create_singleton_identity('core.platform.api/notification-icon-area')


class NotificationIconArea:
    """
    An area which is left up to the platform to render.

    The end-user can request the maximum number of icons
    to display and the background color.

    The behavior of icon clicking is up to the platform.
    """
    __slots__ = ('__max', '__bg',)

    def __init__(self, maximum_icon_display: int, background: Color) -> None:
        self.__max = maximum_icon_display
        self.__bg = background
