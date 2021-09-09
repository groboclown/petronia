
"""
State of the monitors.  There is no configuration here, just a published
state.
"""

from typing import Sequence
from .....aid.std import (
    EventBus,
    set_state,
)
from .....aid.bootstrap import (
    create_singleton_identity,
)
from ..defs.screen import (
    VirtualScreenInfo,
    VirtualScreenArea,
)

# ---------------------------------------------------------------------------
STATE_ID_SCREENS = create_singleton_identity('core.platform.api/screen-state')


class ScreenState:
    """
    Information about the current virtual screen setup.  If the monitors change,
    say by connecting an HDMI monitor on the fly, or connecting remotely, or
    docking a laptop, the state will update to the new state.
    """

    __slots__ = (
        '__screens',
    )

    def __init__(self, screens: VirtualScreenInfo) -> None:
        self.__screens = screens

    @property
    def screens(self) -> VirtualScreenInfo:
        return self.__screens

    def __repr__(self) -> str:
        return repr(self.__screens.blocks)


def set_screen_state(bus: EventBus, blocks: Sequence[VirtualScreenArea]) -> None:
    set_state(bus, STATE_ID_SCREENS, ScreenState, ScreenState(VirtualScreenInfo(blocks)))
