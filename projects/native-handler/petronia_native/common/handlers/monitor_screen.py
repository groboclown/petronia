"""Handlers for the monitor and screen events."""

from typing import Sequence, List, Set, Optional, cast
from petronia_common.util import (
    StdRet, PetroniaReturnError, RET_OK_NONE, EMPTY_TUPLE, not_none, join_none_results,
)
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget, EventObjectParser
from petronia_ext_lib import datastore
from petronia_ext_lib.standard.error import create_error_data, INVALID_USER_ACTION_ERROR_CATEGORY
from .. import defs
from .. import virtual_screen
from .. import user_messages
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


class AbstractScreenHandler:
    """Callback class for handling events directed towards the native implementation.

    Because of the `close` function, implementations shouldn't keep a copy of the
    context.  Instead, when the handlers' functions are called, the valid (non-None)
    context is passed."""

    __slots__ = ('_settings', '__context')

    def __init__(self, context: EventRegistryContext) -> None:
        self._settings = virtual_screen.VirtualScreenSettings()
        self.__context: Optional[EventRegistryContext] = context

    def close(self) -> None:
        """Called when the target listener closes."""
        self.__context = None

    def detected_monitor_changed(self, active: Sequence[monitor.Monitor]) -> StdRet[None]:
        """Called by the implementation when a change to the monitors happened, or if the
        datastore value for the monitor is updated.  This triggers
        many other actions to happen, possibly also calling into
        callback_virtual_screen_update."""
        if not self.__context:
            # Closed
            return RET_OK_NONE

        errors: List[StdRet[None]] = [store_monitor_state(self.__context, active)]

        if self._settings.set_active_monitors(active):
            # The monitor state changed the virtual screen.
            errors.append(
                store_virtual_screen_state(self.__context, self._settings.active_screen)
            )
            errors.append(
                self.callback_virtual_screen_update(self.__context, self._settings.active_screen)
            )
        return join_none_results(*errors)

    def on_configuration_update(
            self,
            original_source_id: Optional[str],
            original_request_id: int,
            new_configs: Sequence[virtual_screen.VirtualScreenConfig],
    ) -> StdRet[None]:
        """Called by an event listener or implementation startup when the configuration changes."""
        if not self.__context:
            # closed
            return RET_OK_NONE

        # First, check if the configurations are valid.
        errors: List[StdRet[None]] = []
        for config in new_configs:
            errors.append(config.validate())

        if errors:
            # The configuration had problems.
            if original_source_id:
                errors.append(send_screen_configuration_bad(
                    self.__context, original_source_id, original_request_id,
                    # Ugly, but meh.
                    join_none_results(*errors).valid_error,
                ))
            return join_none_results(*errors)

        # Change our current settings to a copy of the old ones, so that
        # any updates from the implementation can be easily reverted.
        old_settings = self._settings
        self._settings = self._settings.copy()
        screen_changed = False
        if self._settings.update_configuration(new_configs):
            res = self.callback_virtual_screen_update(self.__context, self._settings.active_screen)
            if res.has_error:
                self._settings = old_settings
                return res
            screen_changed = True

        # Configuration change okay.  Perform the notification chain.
        # Note that there shouldn't be any errors at this point.

        if screen_changed:
            errors.append(store_virtual_screen_state(self.__context, self._settings.active_screen))

        errors.append(self.on_screen_configuration_settings_changed(
            self.__context, self._settings.screen_configurations,
        ))
        errors.append(store_screen_setups_state(self.__context, self._settings))

        if original_source_id:
            errors.append(self.__context.send_event(
                screen.SetScreenConfigurationRequestEvent.UNIQUE_TARGET_FQN,
                original_source_id,
                screen.SetScreenConfigurationSuccessEvent(original_request_id),
            ))

        return join_none_results(*errors)

    def on_screen_configuration_settings_changed(
            self, context: EventRegistryContext,
            screen_configs: Sequence[virtual_screen.VirtualScreenConfig],
    ) -> StdRet[None]:
        """Called when the configuration for the virtual screens has changed successfully.
        this should perform necessary steps to update the datastore configuration for the
        extension, if necessary.  Errors reported from this do not stop the configuration
        from being changed in this object."""
        raise NotImplementedError  # pragma no cover

    def callback_virtual_screen_update(
            self, context: EventRegistryContext, active_screen: virtual_screen.VirtualScreen,
    ) -> StdRet[None]:
        """Called when the virtual screen changed due to a user request.  It should already
        be considered valid from an internal perspective, but the implementation may fail the
        change due to its own reasoning.

        If this returns an error, then the change to the configuration will be reverted."""
        raise NotImplementedError  # pragma no cover


def register_screen_listener(
        context: EventRegistryContext, handler: AbstractScreenHandler,
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
        ScreenConfigChangedEventListener(handler),
    )


def register_monitor_state_change_listener(
        context: EventRegistryContext, handler: AbstractScreenHandler,
) -> StdRet[None]:
    """Register a listener for changes to the monitor state via the datastore.  Only
    add this if the implementation does not directly call `detected_monitor_changed`
    on the handler."""

    def on_update(value: Optional[monitor.ActiveMonitorsState]) -> None:
        monitors: Sequence[monitor.Monitor]
        if value:
            monitors = value.monitors
        else:
            monitors = EMPTY_TUPLE
        user_messages.report_send_receive_problems(
            handler.detected_monitor_changed(monitors)
        )

    return datastore.register_datastore_target_listener(
        context, monitor.ActiveMonitorsState.UNIQUE_TARGET_FQN,
        datastore.CachedInstance(
            EventObjectParser(monitor.ActiveMonitorsState.parse_data), on_update,
        ),
    )


class ScreenConfigChangedEventListener(
    EventObjectTarget[screen.SetScreenConfigurationRequestEvent]
):
    """Handles change config events directed to the screen."""
    __slots__ = ('_handler',)

    def __init__(self, handler: AbstractScreenHandler) -> None:
        self._handler: Optional[AbstractScreenHandler] = handler

    def on_close(self) -> None:
        self._handler = None

    def on_event(
            self, source: str, target: str, event: screen.SetScreenConfigurationRequestEvent,
    ) -> bool:
        if not self._handler:
            # Closed, so remove this target.
            return True
        user_messages.report_send_receive_problems(self._handler.on_configuration_update(
            source, event.request_id,
            [
                create_screen_config_from_mapped_screen(sbm)
                for sbm in event.mapped_screens_by_monitors
            ],
        ))
        return False


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
        config: virtual_screen.VirtualScreenSettings,
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
            for scg in config.screen_configurations
        ]),
    )
