"""Screen and monitor connections between the message loop and the Petronia events."""

from typing import Sequence, Optional
import threading
from concurrent.futures.thread import ThreadPoolExecutor
from petronia_common.util import EMPTY_TUPLE
from petronia_ext_lib.runner import EventRegistryContext
from petronia_native.common import virtual_screen, user_messages, defs
from petronia_native.common.handlers import monitor_screen
from . import configuration, message_loop, hook_messages, windows_vs
from .arch import native_funcs
from .arch.native_funcs.monitor import WindowsMonitor, are_monitors_different


class WindowsScreen(monitor_screen.AbstractMonitorHandler[WindowsMonitor]):
    """Windows state for the monitors and screens, tying the message loop and events together.

    For Windows, the OS handles the screen layout (relative position between each other).

    """

    __slots__ = ('__context', '__config', '__old_monitors', '__executor', '__lock')

    def __init__(
            self, context: EventRegistryContext, config: configuration.ConfigurationStore,
            executor: Optional[ThreadPoolExecutor] = None,
    ) -> None:
        windows_monitors = windows_vs.get_windows_monitors()
        monitor_screen.AbstractMonitorHandler.__init__(
            self, context, WindowsWindowScreenMapper(
                windows_monitors, windows_vs.to_petronia_screen(windows_monitors),
            ),
        )
        self.__config = config
        self.__lock = threading.Lock()
        self.__executor = executor or ThreadPoolExecutor(1)
        self.__old_monitors: Sequence[WindowsMonitor] = EMPTY_TUPLE
        if native_funcs.WINDOWS_FUNCTIONS.monitor.find_monitors:
            self.__old_monitors = native_funcs.WINDOWS_FUNCTIONS.monitor.find_monitors()  # pylint:disable=not-callable

    def register_with_loop(self, loop: message_loop.WindowsMessageLoop) -> None:
        """Register this handler with the loop."""
        loop.add_message_handler(hook_messages.display_changed_message(
            self.on_display_changed_message,
        ))
        loop.add_message_handler(hook_messages.system_settings_changed_message(
            self.on_system_settings_changed_message,
        ))
        loop.add_message_handler(hook_messages.device_changed_message(
            self.on_device_changed_message,
        ))

    def on_display_changed_message(self) -> None:
        """Callback for display_changed_message hook"""
        self.__executor.submit(self._maybe_monitors_changed)

    def on_system_settings_changed_message(self, _what_changed: native_funcs.WPARAM) -> None:
        """Callback for system_settings_changed_message hook"""
        self.__executor.submit(self._maybe_monitors_changed)

    def on_device_changed_message(self, _what_changed: native_funcs.WPARAM) -> None:
        """Callback for device_changed_message hook"""
        self.__executor.submit(self._maybe_monitors_changed)

    def get_virtual_screen_for_monitors(
            self, active: Sequence[WindowsMonitor],
    ) -> virtual_screen.VirtualScreen:
        return windows_vs.to_petronia_screen(active)

    def _maybe_monitors_changed(self) -> None:
        """Did the monitors change at all?  Should be run outside the message loop."""
        if native_funcs.WINDOWS_FUNCTIONS.monitor.find_monitors:
            new_monitors = native_funcs.WINDOWS_FUNCTIONS.monitor.find_monitors()  # pylint:disable=not-callable
            with self.__lock:
                if are_monitors_different(self.__old_monitors, new_monitors):
                    self.__old_monitors = new_monitors
                    # Trigger the chain of events.
                    user_messages.report_send_receive_problems(
                        self.detected_monitor_changed(new_monitors),
                    )


class WindowsWindowScreenMapper(monitor_screen.WindowScreenMapper[windows_vs.WindowsMonitor]):
    """Windows specific version of the monitor.

    This is intended to be a 1-for-1 mapping of the native monitor to the screen space.
    """

    def screen_to_window_pos(
            self, screen_pos: defs.ScreenPosition,
    ) -> Optional[defs.OsScreenPosition]:
        # 1-for-1 mapping...
        return (
            screen_pos[defs.SCREEN_POSITION_X],
            screen_pos[defs.SCREEN_AREA_Y],
        )

    def window_to_screen_pos(
            self, window_pos: defs.OsScreenPosition,
    ) -> Optional[defs.ScreenPosition]:
        # 1-for-1 mapping...
        return (
            defs.ScreenUnit(window_pos[defs.OS_SCREEN_POSITION_X]),
            defs.ScreenUnit(window_pos[defs.OS_SCREEN_POSITION_Y]),
        )
