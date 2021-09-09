
"""
Generic layout events.

Each layout can have its own interpretation of these events.
For example, a tiling layout manager can interpret "move window"
to mean swap the window with another adjacent window.
"""

from petronia.aid.std import (
    EventId,
    EventCallback,
    EventBus,
    create_singleton_identity,
)
from petronia.aid.bootstrap import (
    ListenerSetup,
)


TARGET_ID_LAYOUT_NAVIGATION = create_singleton_identity('core.layout.navigation.api/nav')

# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_CHANGE_ACTIVE_TILE = EventId('core.layout.window.api/request-change-active-tile')


class RequestChangeActiveTileEvent:
    """
    Change currently active tile to be one of the directions different than the currently active tile.
    """
    __slots__ = ('__direction', '__count')

    def __init__(self, direction: str, count: int) -> None:
        self.__direction = direction
        self.__count = count

    @property
    def direction(self) -> str:
        return self.__direction

    @property
    def count(self) -> int:
        return self.__count


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_MOVE_ACTIVE_WINDOW = EventId('core.layout.window.api/request-move-active-window')
# Move the currently active window to another tile in one of the directions.


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_MARK_ACTIVE_WINDOW = EventId('core.layout.window.api/request-mark-active-window')
# Mark the active window with a label, for quick actions.


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_MARK_ACTIVE_TILE = EventId('core.layout.window.api/request-mark-active-tile')
# Mark the active tile with a label, for quick actions.


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_ACTIVATE_MARKED_WINDOW = EventId('core.layout.window.api/request-activate-marked-window')

# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_ACTIVATE_MARKED_TILE = EventId('core.layout.window.api/request-activate-marked-tile')

# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_MOVE_ACTIVE_WINDOW_TO_MARKED_TILE = EventId('core.layout.window.api/request-move-to-marked-tile')

# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_MOVE_MARKED_WINDOW_TO_ACTIVE_TILE = EventId('core.layout.window.api/request-move-to-active-tile')
