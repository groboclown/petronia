
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


EVENT_ID_REQUEST_CHANGE_ACTIVE_TILE = EventId('core.layout.window.api/request-change-active-tile')
# Change currently active tile to be one of the directions different than the currently active tile.

EVENT_ID_REQUEST_MOVE_ACTIVE_WINDOW = EventId('core.layout.window.api/request-move-active-window')
# Move the currently active window to another tile in one of the directions.
