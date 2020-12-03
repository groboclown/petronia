"""
Special event target handlers for interaction between the foreman process and
other loaders.
"""

from typing import Optional
import asyncio
from petronia_common.event_stream import (
    EventForwarderTarget, RawEvent,
    raw_event_id, raw_event_source_id, raw_event_target_id,
    is_raw_event_object, as_raw_event_object_data,
)
from petronia_common.util import PetroniaReturnError
from ..events import foreman

CONSUMED_EXTENSION_LOADER_EVENT_IDS = (
    foreman.StartLauncherRequestEvent.FULL_EVENT_NAME,
    foreman.LauncherLoadExtensionRequestEvent.FULL_EVENT_NAME,
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

    async def do_shutdown(self) -> None:
        """Signal that the shutdown process should begin."""
        raise NotImplementedError()

    async def do_restart(
            self,
            requested: bool,
            error: Optional[PetroniaReturnError],
    ) -> None:
        """Signal that the restart process should begin.  If this is an explicit call
        to perform the restart, then set the requested value to True."""
        raise NotImplementedError()

    async def start_launcher(
            self, source_id: str, event: foreman.StartLauncherRequestEvent,
    ) -> None:
        """Signal that a launcher should be started."""
        raise NotImplementedError()

    async def load_extension(
            self, source_id: str, target_id: str, event: foreman.LauncherLoadExtensionRequestEvent,
    ) -> None:
        """Signal to load an extension."""
        raise NotImplementedError()

    async def add_event_listener(
            self, target_id: str, event: foreman.ExtensionAddEventListenerEvent,
    ) -> None:
        """Signal to allow consuming events."""
        raise NotImplementedError()

    async def remove_event_listener(
            self, target_id: str, event: foreman.ExtensionRemoveEventListenerEvent,
    ) -> None:
        """Signal to stop consuming events."""
        raise NotImplementedError()


class ExtensionLoaderTarget(EventForwarderTarget):
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
        asyncio.create_task(self._context.do_restart(False, error))
        return False

    def on_eof(self) -> None:
        # If the EOF is not expected, then this is really bad and we should restart Petronia.
        # If restart or shutdown is already happening, then this should be a no-op.
        asyncio.create_task(self._context.do_restart(False, None))

    async def consume(self, event: RawEvent) -> bool:
        if not is_raw_event_object(event):
            return False
        event_id = raw_event_id(event)
        target_id = raw_event_target_id(event)
        raw_data = as_raw_event_object_data(event)

        if event_id == foreman.StartLauncherRequestEvent.FULL_EVENT_NAME:
            slr_event = foreman.StartLauncherRequestEvent.parse_data(raw_data)
            if slr_event.ok:
                asyncio.create_task(self._context.start_launcher(
                    raw_event_source_id(event),
                    slr_event.result,
                ))
            return False

        if event_id == foreman.LauncherLoadExtensionRequestEvent.FULL_EVENT_NAME:
            lle_event = foreman.LauncherLoadExtensionRequestEvent.parse_data(raw_data)
            if lle_event.ok:
                asyncio.create_task(self._context.load_extension(
                    raw_event_source_id(event), target_id, lle_event.result,
                ))
            return False

        if event_id == foreman.ExtensionAddEventListenerEvent.FULL_EVENT_NAME:
            eal_event = foreman.ExtensionAddEventListenerEvent.parse_data(raw_data)
            if eal_event.ok:
                asyncio.create_task(self._context.add_event_listener(
                    target_id, eal_event.result,
                ))
            return False

        if event_id == foreman.ExtensionRemoveEventListenerEvent.FULL_EVENT_NAME:
            rel_event = foreman.ExtensionRemoveEventListenerEvent.parse_data(raw_data)
            if rel_event.ok:
                asyncio.create_task(self._context.remove_event_listener(
                    target_id, rel_event.result,
                ))
            return False

        return False


class InternalTarget(EventForwarderTarget):
    """Handles events sent from the internal extensions ('send-access' == 'internal')."""
    __slots__ = ('_context',)

    def __init__(self, context: TargetHandlerRuntimeContext) -> None:
        self._context = context

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        return event_id in CONSUMED_INTERNAL_EVENT_IDS

    def on_error(self, error: PetroniaReturnError) -> bool:
        # Errors in the communication with the internal extensions are bad, but not super
        # dire.  For now, the right solution is to restart Petronia.
        asyncio.create_task(self._context.do_restart(False, error))
        return False

    def on_eof(self) -> None:
        # If the EOF is not expected, then this is really bad and we should restart Petronia.
        # If restart or shutdown is already happening, then this should be a no-op.
        asyncio.create_task(self._context.do_restart(False, None))

    async def consume(self, event: RawEvent) -> bool:
        if not is_raw_event_object(event):
            return False
        event_id = raw_event_id(event)

        if event_id == foreman.StopEvent.FULL_EVENT_NAME:
            asyncio.create_task(self._context.do_shutdown())
            return False

        if event_id == foreman.RestartEvent.FULL_EVENT_NAME:
            asyncio.create_task(self._context.do_restart(True, None))
            return False

        return False
