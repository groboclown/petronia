"""Screen and monitor connections between the message loop and the Petronia events."""

from typing import Sequence, Optional
import threading
from concurrent.futures.thread import ThreadPoolExecutor
from petronia_common.util import StdRet, EMPTY_TUPLE
from petronia_ext_lib.runner import EventRegistryContext
from petronia_native.common import virtual_screen, user_messages, defs
from petronia_native.common.handlers import monitor_screen
from . import configuration, message_loop, hook_messages
from .datastore.petronia_native_windows import (
    VirtualScreens, ScreenMonitorMappingConfigGroup,
    SourceMonitor, ScreenMonitorMapping,
)
from .arch import native_funcs
from .arch.native_funcs.monitor import WindowsMonitor, are_monitors_different


class WindowsScreen(monitor_screen.AbstractScreenHandler):
    """Windows state for the monitors and screens, tying the message loop and events together."""
    __slots__ = ('__config', '__old_monitors', '__executor', '__lock')

    def __init__(
            self, context: EventRegistryContext, config: configuration.ConfigurationStore,
            executor: Optional[ThreadPoolExecutor] = None,
    ) -> None:
        monitor_screen.AbstractScreenHandler.__init__(self, context)
        self.__config = config
        self.__lock = threading.Lock()
        self.__executor = executor or ThreadPoolExecutor(1)
        self.__old_monitors: Sequence[WindowsMonitor] = EMPTY_TUPLE
        if native_funcs.WINDOWS_FUNCTIONS.monitor.find_monitors:
            self.__old_monitors = native_funcs.WINDOWS_FUNCTIONS.monitor.find_monitors()

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

    def on_system_settings_changed_message(self, _what_changed: native_funcs.LPARAM) -> None:
        """Callback for system_settings_changed_message hook"""
        self.__executor.submit(self._maybe_monitors_changed)

    def on_device_changed_message(self, _what_changed: native_funcs.WPARAM) -> None:
        """Callback for device_changed_message hook"""
        self.__executor.submit(self._maybe_monitors_changed)

    def _maybe_monitors_changed(self) -> None:
        """Did the monitors change at all?  Should be run outside the message loop."""
        if native_funcs.WINDOWS_FUNCTIONS.monitor.find_monitors:
            new_monitors = native_funcs.WINDOWS_FUNCTIONS.monitor.find_monitors()
            with self.__lock:
                if are_monitors_different(self.__old_monitors, new_monitors):
                    self.__old_monitors = new_monitors
                    # Trigger the chain of events.
                    user_messages.report_send_receive_problems(self.detected_monitor_changed([
                        m.info for m in new_monitors
                    ]))

    def on_screen_configuration_settings_changed(
            self, context: EventRegistryContext,
            screen_configs: Sequence[virtual_screen.VirtualScreenConfig],
    ) -> StdRet[None]:
        self.__config.get_config().virtual_screens = VirtualScreens([
            ScreenMonitorMappingConfigGroup(
                scf.name,
                [
                    SourceMonitor(
                        smd[defs.MONITOR_POSITION_MONITOR_IDENTIFIER],
                        smd[defs.MONITOR_POSITION_X],
                        smd[defs.MONITOR_POSITION_Y],
                    )
                    for smd in scf.monitor_defs
                ],
                [
                    ScreenMonitorMapping(
                        sbk.monitor_id,
                        sbk.monitor_l, sbk.monitor_t, sbk.monitor_w, sbk.monitor_h,
                        sbk.monitor_rotation,
                        sbk.screen_l, sbk.screen_t, sbk.screen_w, sbk.screen_h,
                    )
                    for sbk in scf.screen.blocks
                ],
            )
            for scf in screen_configs
        ])
        return self.__config.put_in_datastore(context)

    def callback_virtual_screen_update(
            self, context: EventRegistryContext,
            active_screen: virtual_screen.VirtualScreen,
    ) -> StdRet[None]:
        # This can be called from within a lock state.  So don't do anything with the lock state.
        pass
