"""Handlers for the monitor and screen events."""

from typing import Sequence, List, Set, Generic, TypeVar, Optional, cast
import threading
from petronia_common.util import (
    StdRet, PetroniaReturnError, RET_OK_TRUE, RET_OK_FALSE,
    not_none, join_results,
)
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget
from petronia_ext_lib import datastore
from petronia_ext_lib.standard.error import create_error_data, INVALID_USER_ACTION_ERROR_CATEGORY
from .. import defs
from .. import virtual_screen
from ..events.impl import monitor
from ..events.impl import screen


def create_monitor_state(
        identifier: int,
        description: str,
        size: defs.MonitorSize,
        dpi_x: int,
        dpi_y: int,
        supports_rotation: bool,
) -> monitor.Monitor:
    """Create a monitor event structure from native-common structures."""
    return monitor.Monitor(
        identifier=identifier,
        description=description,
        real_pixel_width=size[defs.MONITOR_SIZE_WIDTH],
        real_pixel_height=size[defs.MONITOR_SIZE_HEIGHT],
        dpi_x=dpi_x, dpi_y=dpi_y,
        supports_rotation=supports_rotation,
    )


def store_monitor_state(
        context: EventRegistryContext,
        monitors: Sequence[monitor.Monitor],
) -> StdRet[None]:
    """Set the current monitor state in the datastore.
    This should be called at startup and when the low-level monitor
    configuration changes."""
    return datastore.send_store_data(
        context,
        monitor.ActiveMonitorsState.UNIQUE_TARGET_FQN,
        monitor.ActiveMonitorsState(list(monitors)),
    )


def store_virtual_screen_state(
        context: EventRegistryContext,
        v_screen: virtual_screen.VirtualScreen,
) -> StdRet[None]:
    """Set the virtual screen state in the datastore."""
    return datastore.send_store_data(
        context,
        screen.VirtualScreenState.UNIQUE_TARGET_FQN,
        screen.VirtualScreenState([
            screen.VirtualScreenBlock(
                b.screen_l, b.screen_t, b.screen_w, b.screen_h,
                # NOTE: get the real ratio here.  This should take into account the monitor's
                # native DPI and the screen-to-monitor mapping distortion.
                1, 1,
            )
            for b in v_screen.blocks
        ]),
    )


def send_screen_configuration_bad(
        context: EventRegistryContext,
        original_source_id: str,
        original_request_id: int,
        error: PetroniaReturnError,
) -> StdRet[None]:
    """Send a set-configuration failed message."""
    return context.send_event(
        screen.SetScreenConfigurationRequestEvent.UNIQUE_TARGET_FQN,
        original_source_id,
        screen.SetScreenConfigurationFailureEvent(
            original_request_id,
            not_none(create_error_data(
                screen.Error,
                screen.LocalizableMessage,
                screen.MessageArgument,
                screen.MessageArgumentValue,
                error,
                [INVALID_USER_ACTION_ERROR_CATEGORY],
                'bad-config', 'native-screen',
            )),
        ),
    )


class NativeMonitor:
    """Describes a kind of native monitor."""

    def get_petronia_monitor(self) -> monitor.Monitor:
        """Get the Petronia monitor structure."""
        raise NotImplementedError


NativeMonitorType = TypeVar('NativeMonitorType', bound=NativeMonitor, covariant=True)


class WindowScreenMapper(Generic[NativeMonitorType]):
    """A mapping between native windows, the screen, and the configuration.

    This is thread safe.

    By default, the window position is 1-for-1 to the screen layout."""

    __slots__ = ('_monitors', '_screen', '_native', '_lock')

    def __init__(
            self,
            native_monitors: Sequence[NativeMonitorType],
            active_screen: virtual_screen.VirtualScreen,
            lock: Optional[threading.RLock] = None,
    ) -> None:
        self._native = tuple(native_monitors)
        self._monitors = tuple((m.get_petronia_monitor() for m in native_monitors))
        self._screen = active_screen
        self._lock = lock or threading.RLock()

    @property
    def monitors(self) -> Sequence[monitor.Monitor]:
        """Get the active monitors"""
        with self._lock:
            return self._monitors

    @property
    def native(self) -> Sequence[NativeMonitorType]:
        """Get the active native monitors"""
        with self._lock:
            return self._native

    @property
    def screen(self) -> virtual_screen.VirtualScreen:
        """Get the active screen layout."""
        with self._lock:
            return self._screen

    def on_monitor_change(self, active: Sequence[NativeMonitorType]) -> bool:
        """Called by the native code when a change to the monitors is
        detected.  If the monitors have actually changed, then True is returned."""
        monitors = [m.get_petronia_monitor() for m in active]
        with self._lock:
            if virtual_screen.are_monitors_same(self._monitors, monitors):
                return False
            self._monitors = tuple(monitors)
            self._native = tuple(active)
            return True

    def on_screen_change(self, active_screen: virtual_screen.VirtualScreen) -> bool:
        """Called by either a configuration event or native monitor change."""
        with self._lock:
            if self._screen == active_screen:
                return False
            self._screen = active_screen
            return True

    def screen_to_window_pos(
            self, screen_pos: defs.ScreenPosition,
    ) -> Optional[defs.OsScreenPosition]:
        """Converts the screen position (which user events should use) to a monitor position.

        Implementations must be careful about lock state."""
        raise NotImplementedError

    def window_to_screen_pos(
            self, window_pos: defs.OsScreenPosition,
    ) -> Optional[defs.ScreenPosition]:
        """Converts the window position (native UI reporting) to a screen position (which the
        user events should contain).

        Implementations must be careful about lock state."""
        raise NotImplementedError

    def screen_to_window_area(
            self, screen_area: defs.ScreenArea,
    ) -> Optional[defs.OsScreenRect]:
        """Converts a screen area to a native rectangle."""
        with self._lock:
            window_xy = self.screen_to_window_pos((
                screen_area[defs.SCREEN_AREA_X], screen_area[defs.SCREEN_AREA_Y],
            ))
            window_hw = self.screen_to_window_pos((
                screen_area[defs.SCREEN_AREA_WIDTH], screen_area[defs.SCREEN_AREA_HEIGHT],
            ))
            if window_xy is None or window_hw is None:
                return None
        return defs.OsScreenRect.from_size(
            x=window_xy[defs.OS_SCREEN_POSITION_X], y=window_xy[defs.OS_SCREEN_POSITION_Y],
            width=window_hw[defs.OS_SCREEN_POSITION_X], height=window_hw[defs.OS_SCREEN_POSITION_Y],
        )


class AbstractMonitorHandler(Generic[NativeMonitorType]):
    """Callback class for handling events based on the native implementation's detection of
    monitor state changes.  Changes should be passed to this handler, which will then pass
    those changes on to the WindowScreenMapper.

    Because of the `close` function, implementations shouldn't keep a copy of the
    context.  Instead, when the handlers' functions are called, the valid (non-None)
    context is passed."""

    __slots__ = ('_mapper', '_context')

    def __init__(
            self, context: EventRegistryContext, mapper: WindowScreenMapper[NativeMonitorType],
    ) -> None:
        self._mapper = mapper
        self._context: Optional[EventRegistryContext] = context

    def close(self) -> None:
        """Called when the target listener closes."""
        self._context = None

    def get_virtual_screen_for_monitors(
            self, active: Sequence[NativeMonitorType],
    ) -> virtual_screen.VirtualScreen:
        """Finds the correct virtual screen for the monitor setup."""
        raise NotImplementedError

    def detected_monitor_changed(self, active: Sequence[NativeMonitorType]) -> StdRet[bool]:
        """Called by the native implementation when a change to the monitors happened.
        This triggers many other actions to happen.  Returns True if the monitors are
        considered changed."""
        if not self._context:
            # Closed
            return RET_OK_FALSE

        if self._mapper.on_monitor_change(active):
            # Monitors changed
            errors: List[StdRet[None]] = [store_monitor_state(self._context, self._mapper.monitors)]

            new_screen = self.get_virtual_screen_for_monitors(self._mapper.native)
            # Screen configuration may have changed.
            res = self.detected_screen_changed(new_screen)
            if res.has_error:
                errors.append(res.forward())
            return join_results(lambda x: True, *errors)
        return RET_OK_FALSE

    def detected_screen_changed(self, active: virtual_screen.VirtualScreen) -> StdRet[bool]:
        """Called if the virtual screen has changed."""
        if self._context and self._mapper.on_screen_change(active):
            # screen configuration switched.
            res = store_virtual_screen_state(self._context, self._mapper.screen)
            if res.has_error:
                return res.forward()
            return RET_OK_TRUE
        return RET_OK_FALSE


def register_set_screen_configuration_listener(
        context: EventRegistryContext,
        handler: EventObjectTarget[screen.SetScreenConfigurationRequestEvent],
) -> StdRet[None]:
    """Register the screen event listeners.  If the implementation does not directly send
    monitor change requests to the handler (by calling `detected_monitor_changed`), then
    a separate monitor datastore change event listener must be registered, by calling
    `register_monitor_state_change_listener`."""
    res = context.register_event_parser(
        screen.SetScreenConfigurationRequestEvent.FULL_EVENT_NAME,
        screen.SetScreenConfigurationRequestEvent.parse_data,
    )
    if res.has_error:
        return res

    return context.register_target(
        screen.SetScreenConfigurationRequestEvent.FULL_EVENT_NAME,
        screen.SetScreenConfigurationRequestEvent.UNIQUE_TARGET_FQN,
        handler,
    )


# When a good example of using this comes up, this can be uncommented.
# class AbstractVirtualScreenHandler:
#     """Callback class for allowing users to define the virtual screen layout.
#
#     Because of the `close` function, implementations shouldn't keep a copy of the
#     context.  Instead, when the handlers' functions are called, the valid (non-None)
#     context is passed."""
#
#     __slots__ = ('__configs', '_mapper', '_context')
#
#     def __init__(self, context: EventRegistryContext, mapper: WindowScreenMapper) -> None:
#         self.__configs = virtual_screen.VirtualScreenConfigurationSet()
#         self._mapper = mapper
#         self._context: Optional[EventRegistryContext] = context
#
#     def close(self) -> None:
#         """Called when the target listener closes."""
#         self._context = None
#
#     def get_virtual_screen_for_monitors(self) -> virtual_screen.VirtualScreen:
#         """Finds the correct virtual screen for the monitor setup."""
#         index, _arrangement = self.__configs.choose_best_config_index(self._mapper.monitors)
#         if index >= 0:
#             return self.__configs.get_config_list()[index].screen
#         default_config = virtual_screen.VirtualScreenConfig.create_default(self._mapper.monitors)
#         self.__configs.set_config_list([default_config, *self.__configs.get_config_list()])
#         return default_config.screen
#
#     def on_monitors_changed(self, active_monitors: Sequence[monitor.Monitor]) -> StdRet[bool]:
#         """Called when the monitors changed, which might alter the active screen.  This
#         instance's underlying window/screen mapper instance may be shared with the monitor
#         """
#         self._mapper.on_monitor_change(active_monitors)
#
#     def on_configuration_update(
#             self,
#             original_source_id: Optional[str],
#             original_request_id: int,
#             new_configs: Sequence[virtual_screen.VirtualScreenConfig],
#     ) -> StdRet[bool]:
#         "Called by an event listener or implementation startup when the configuration changes."
#         if not self._context:
#             # closed
#             return RET_OK_FALSE
#
#         # First, check if the configurations are valid.
#         errors: List[StdRet[None]] = []
#         for config in new_configs:
#             res = config.validate()
#             if res.has_error:
#                 errors.append(res)
#
#         if errors:
#             # The configuration had problems.
#             if original_source_id:
#                 errors.append(send_screen_configuration_bad(
#                     self._context, original_source_id, original_request_id,
#                     # Ugly, because this returns an error that immediately is turned
#                     # into another error, but meh.  It works.
#                     join_none_results(*errors).valid_error,
#                 ))
#             return join_none_results(*errors).forward()
#
#         # Just assume the list of configs is different, rather than laboriously check it.
#
#         # Change our current settings to a copy of the old ones, so that
#         # any updates from the implementation can be easily reverted.
#         old_configs = self.__configs.get_config_list()
#         old_screen = self._mapper.screen
#         self.__configs.set_config_list(new_configs)
#         new_screen = self.get_virtual_screen_for_monitors()
#         screen_changed = False
#         if self._mapper.on_screen_change(new_screen):
#             # Screen changed.  Let the native implementation do its stuff.
#             res = self.callback_virtual_screen_update(self._context, self._mapper.screen)
#             if res.has_error:
#                 # Revert everything.
#                 self.__configs.set_config_list(old_configs)
#                 self._mapper.on_screen_change(old_screen)
#                 return res.forward()
#             screen_changed = True
#
#         # Configuration change okay.  Perform the notification chain.
#         # Note that there shouldn't be any errors at this point.
#
#         if screen_changed:
#             errors.append(store_virtual_screen_state(self._context, self._mapper.screen))
#
#         errors.append(store_screen_setups_state(self._context, self.__configs))
#
#         if original_source_id:
#             errors.append(self._context.send_event(
#                 screen.SetScreenConfigurationRequestEvent.UNIQUE_TARGET_FQN,
#                 original_source_id,
#                 screen.SetScreenConfigurationSuccessEvent(original_request_id),
#             ))
#
#         return join_results(lambda x: True, *errors)
#
#     def callback_virtual_screen_update(
#             self, context: EventRegistryContext, active_screen: virtual_screen.VirtualScreen,
#     ) -> StdRet[None]:
#         """Called when the virtual screen changed due to a user request.  It should already
#         be considered valid from an internal perspective, but the implementation may fail the
#         change due to its own reasoning.
#
#         If this returns an error, then the change to the configuration will be reverted."""
#         raise NotImplementedError  # pragma no cover
#
#
# def register_screen_listener(
#         context: EventRegistryContext, handler: AbstractVirtualScreenHandler,
# ) -> StdRet[None]:
#     """Register the screen event listeners.  If the implementation does not directly send
#     monitor change requests to the handler (by calling `detected_monitor_changed`), then
#     a separate monitor datastore change event listener must be registered, by calling
#     `register_monitor_state_change_listener`."""
#     res = context.register_event_parser(
#         screen.SetScreenConfigurationRequestEvent.FULL_EVENT_NAME,
#         screen.SetScreenConfigurationRequestEvent.parse_data,
#     )
#     if res.has_error:
#         return res
#
#     return context.register_target(
#         screen.SetScreenConfigurationRequestEvent.FULL_EVENT_NAME,
#         screen.SetScreenConfigurationRequestEvent.UNIQUE_TARGET_FQN,
#         ScreenConfigChangedEventListener(handler),
#     )
#
#
# def register_monitor_state_change_listener(
#         context: EventRegistryContext, handler: AbstractVirtualScreenHandler,
# ) -> StdRet[None]:
#     """Register a listener for changes to the monitor state via the datastore.  Only
#     add this if the implementation does not directly call `detected_monitor_changed`
#     on the handler."""
#
#     def on_update(value: Optional[monitor.ActiveMonitorsState]) -> None:
#         monitors: Sequence[monitor.Monitor]
#         if value:
#             monitors = value.monitors
#         else:
#             monitors = EMPTY_TUPLE
#         user_messages.report_send_receive_problems(
#             handler.detected_monitor_changed(monitors)
#         )
#
#     return datastore.register_datastore_target_listener(
#         context, monitor.ActiveMonitorsState.UNIQUE_TARGET_FQN,
#         datastore.CachedInstance(
#             EventObjectParser(monitor.ActiveMonitorsState.parse_data), on_update,
#         ),
#     )
#
#
# class ScreenConfigChangedEventListener(
#     EventObjectTarget[screen.SetScreenConfigurationRequestEvent]
# ):
#     """Handles change config events directed to the screen."""
#     __slots__ = ('_handler',)
#
#     def __init__(self, handler: AbstractVirtualScreenHandler) -> None:
#         self._handler: Optional[AbstractVirtualScreenHandler] = handler
#
#     def on_close(self) -> None:
#         self._handler = None
#
#     def on_event(
#             self, source: str, target: str, event: screen.SetScreenConfigurationRequestEvent,
#     ) -> bool:
#         if not self._handler:
#             # Closed, so remove this target.
#             return True
#         user_messages.report_send_receive_problems(self._handler.on_configuration_update(
#             source, event.request_id,
#             [
#                 create_screen_config_from_mapped_screen(sbm)
#                 for sbm in event.mapped_screens_by_monitors
#             ],
#         ))
#         return False


def create_screen_config_from_mapped_screen(
        sbm: screen.ScreenMonitorMappingConfigGroup,
) -> virtual_screen.VirtualScreenConfig:
    """Create a VirtualScreenConfig from an event's ScreenMonitorMappingConfigGroup"""
    last_id = [0]
    seen_ids: Set[int] = set()

    def next_id(mon_id: Optional[int]) -> int:
        if mon_id is None:
            while last_id[0] in seen_ids:
                last_id[0] += 1
            seen_ids.add(last_id[0])
            return last_id[0]
        seen_ids.add(mon_id)
        return mon_id

    return virtual_screen.VirtualScreenConfig(
        sbm.description or 'screen-config',
        [
            (
                mon.identifier,
                cast(defs.MonitorUnit, mon.width),
                cast(defs.MonitorUnit, mon.height),
            )
            for mon in sbm.monitors
        ],
        virtual_screen.VirtualScreen(
            [
                virtual_screen.VirtualScreenBlock(
                    (
                        next_id(scn.source_monitor),
                        cast(defs.MonitorUnit, scn.source_nw_x_pixel),
                        cast(defs.MonitorUnit, scn.source_nw_y_pixel),
                        cast(defs.MonitorUnit, scn.source_pixel_width),
                        cast(defs.MonitorUnit, scn.source_pixel_height),
                    ),
                    (
                        cast(defs.ScreenUnit, scn.virtual_nw_x_pixel),
                        cast(defs.ScreenUnit, scn.virtual_nw_y_pixel),
                        cast(defs.ScreenUnit, scn.virtual_width),
                        cast(defs.ScreenUnit, scn.virtual_height),
                    ),
                    scn.rotation,
                )
                for scn in sbm.screen
            ]
        ),
    )


def store_screen_setups_state(
        context: EventRegistryContext,
        config: virtual_screen.VirtualScreenConfigurationSet,
) -> StdRet[None]:
    """Send the store data request for the ScreenSetupsState value."""
    return datastore.send_store_data(
        context,
        screen.ScreenSetupsState.UNIQUE_TARGET_FQN,
        screen.ScreenSetupsState([
            screen.ScreenMonitorMappingConfigGroup(
                scg.name,
                [
                    screen.SourceMonitor(
                        smr[defs.MONITOR_POSITION_MONITOR_IDENTIFIER],
                        smr[defs.MONITOR_POSITION_X],
                        smr[defs.MONITOR_POSITION_Y],
                    )
                    for smr in scg.monitor_defs
                ],
                [
                    screen.ScreenMonitorMapping(
                        blk.monitor_id,
                        blk.monitor_l, blk.monitor_t, blk.monitor_w, blk.monitor_h,
                        blk.monitor_rotation,
                        blk.screen_l, blk.screen_t, blk.screen_w, blk.screen_h,
                    )
                    for blk in scg.screen.blocks
                ],
            )
            for scg in config.get_config_list()
        ]),
    )
