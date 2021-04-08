"""
Special event target handlers for interaction between the foreman process and
other loaders.
"""

from typing import Optional, Dict, Any
from petronia_common.event_stream import BaseEventForwarderTarget
from petronia_common.util import PetroniaReturnError
from ..events import foreman
from ..user_message import trace_channel

CONSUMED_EXTENSION_LOADER_EVENT_IDS = (
    foreman.LauncherStartExtensionRequestEvent.FULL_EVENT_NAME,
    foreman.ExtensionAddEventListenerEvent.FULL_EVENT_NAME,
    foreman.ExtensionRemoveEventListenerEvent.FULL_EVENT_NAME,
)

CONSUMED_INTERNAL_EVENT_IDS = (
    foreman.StopEvent.FULL_EVENT_NAME,
    foreman.RestartEvent.FULL_EVENT_NAME,
)


class TargetHandlerRuntimeContext:
    """Abstract class used by the event targets to communicate events back to
    the router."""
    __slots__ = ()

    def do_shutdown(self) -> None:
        """Signal that the shutdown process should begin."""
        raise NotImplementedError()

    def do_restart(
            self,
            requested: bool,
            error: Optional[PetroniaReturnError],
    ) -> None:
        """Signal that the restart process should begin.  If this is an explicit call
        to perform the restart, then set the requested value to True."""
        raise NotImplementedError()

    def start_extension(
            self, source_id: str, target_id: str, event: foreman.LauncherStartExtensionRequestEvent,
    ) -> None:
        """Signal to load an extension."""
        raise NotImplementedError()

    def add_event_listener(
            self, target_id: str, event: foreman.ExtensionAddEventListenerEvent,
    ) -> None:
        """Signal to allow consuming events."""
        raise NotImplementedError()

    def remove_event_listener(
            self, target_id: str, event: foreman.ExtensionRemoveEventListenerEvent,
    ) -> None:
        """Signal to stop consuming events."""
        raise NotImplementedError()


class ExtensionLoaderTarget(BaseEventForwarderTarget):
    """The event target added to the channel for direct communication between the extension
    loader and the foreman router."""

    __slots__ = ('_context',)

    def __init__(self, context: TargetHandlerRuntimeContext) -> None:
        self._context = context

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        return event_id in CONSUMED_EXTENSION_LOADER_EVENT_IDS

    def on_error(self, error: PetroniaReturnError) -> bool:
        # Errors in the communication with the extension loader are really bad.
        # Restart Petronia.
        self._context.do_restart(False, error)
        return False

    def on_eof(self) -> None:
        # If the EOF is not expected, then this is really bad and we should restart Petronia.
        # If restart or shutdown is already happening, then this should be a no-op.
        self._context.do_restart(False, None)

    def consume_object(
            self, event_id: str, source_id: str, target_id: str, event_data: Dict[str, Any],
    ) -> bool:
        if event_id == foreman.LauncherStartExtensionRequestEvent.FULL_EVENT_NAME:
            lse_event = foreman.LauncherStartExtensionRequestEvent.parse_data(event_data)
            if lse_event.ok:
                self._context.start_extension(source_id, target_id, lse_event.result)
            return False

        if event_id == foreman.ExtensionAddEventListenerEvent.FULL_EVENT_NAME:
            eal_event = foreman.ExtensionAddEventListenerEvent.parse_data(event_data)
            if eal_event.ok:
                # NOTE: there's a severe bug here.
                # The "target_id" comes from the extension loader, and that is the extension
                # name.  However, this needs to be the handler id, which is stored differently
                # internally.  This calls into EventRouter.add_handler_listener()
                trace_channel(
                    'foreman-ext-loader',
                    f'++++++ adding listener on {target_id} / {eal_event.result.events} ++++++',
                )
                self._context.add_event_listener(target_id, eal_event.result)
            return False

        if event_id == foreman.ExtensionRemoveEventListenerEvent.FULL_EVENT_NAME:
            rel_event = foreman.ExtensionRemoveEventListenerEvent.parse_data(event_data)
            if rel_event.ok:
                self._context.remove_event_listener(target_id, rel_event.result)
            return False

        return False


class InternalTarget(BaseEventForwarderTarget):
    """Handles events sent from the internal extensions ('send-access' == 'internal')."""

    __slots__ = ('_context',)

    def __init__(self, context: TargetHandlerRuntimeContext) -> None:
        self._context = context

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        return event_id in CONSUMED_INTERNAL_EVENT_IDS

    def on_error(self, error: PetroniaReturnError) -> bool:
        # Errors in the communication with the internal extensions are bad, but not super
        # dire.  For now, the right solution is to restart Petronia.
        self._context.do_restart(False, error)
        return False

    def on_eof(self) -> None:
        # If the EOF is not expected, then this is really bad and we should restart Petronia.
        # If restart or shutdown is already happening, then this should be a no-op.
        self._context.do_restart(False, None)

    def consume_object(
            self, event_id: str, source_id: str, target_id: str, event_data: Dict[str, Any],
    ) -> bool:
        if event_id == foreman.StopEvent.FULL_EVENT_NAME:
            self._context.do_shutdown()
            return False

        if event_id == foreman.RestartEvent.FULL_EVENT_NAME:
            self._context.do_restart(True, None)
            return False

        return False
