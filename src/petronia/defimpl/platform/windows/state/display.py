
"""
Sets up the state for the monitors, and listens for changes to the display
settings, to update the state on the fly.
"""

from typing import Sequence, List, Tuple
from .....aid.std import (
    EventBus,
    ListenerId,
)
from .....core.platform.api.screen import (
    set_screen_state,
    VirtualScreenArea,
)
from .....core.platform.api.defs import (
    NativeScreenInfo,
    NATIVE_SCREEN_AREA_X, NATIVE_SCREEN_AREA_Y,
    NATIVE_SCREEN_AREA_W, NATIVE_SCREEN_AREA_H,
)
from ..connect import (
    WindowsHookEvent,
    bootstrap_screens,
    get_monitors,
    WindowsErrorMessage,
)
from ..connect.messages import (
    display_changed_message,
)
from ..arch.native_funcs.monitor import WindowsMonitor


def bootstrap_display_detection(bus: EventBus, connect: WindowsHookEvent) -> Sequence[ListenerId]:
    errors = bootstrap_screens()
    for error in errors:
        print("DEBUG setup screens: {0}".format(error))

    active_monitors: List[Tuple[NativeScreenInfo, VirtualScreenArea]] = []

    def on_display_changed() -> None:
        _map_monitors(active_monitors)
        print("DEBUG announcing monitors: {0}".format(repr(active_monitors)))
        set_screen_state(bus, [mon[1] for mon in active_monitors])

    # Initial state setup.
    on_display_changed()

    connect.add_message_handler(display_changed_message(on_display_changed))

    return ()


def _map_monitors(store: List[Tuple[NativeScreenInfo, VirtualScreenArea]]) -> None:
    store.clear()
    active_displays = get_monitors()
    if isinstance(active_displays, WindowsErrorMessage):
        # Logging?
        return
    for display in active_displays:
        store.append((display.info, _as_virtual_screen(display),))


def _as_virtual_screen(native: WindowsMonitor) -> VirtualScreenArea:
    # If we need to scale the screen size, this is where we'd do it.
    work_area = native.info.work_area
    area = (
        work_area[NATIVE_SCREEN_AREA_X],
        work_area[NATIVE_SCREEN_AREA_Y],
        native.scale_x(work_area[NATIVE_SCREEN_AREA_W]),
        native.scale_y(work_area[NATIVE_SCREEN_AREA_H]),
    )
    return VirtualScreenArea(
        name=native.info.name,
        area=area,
        is_primary=native.info.is_primary
    )
