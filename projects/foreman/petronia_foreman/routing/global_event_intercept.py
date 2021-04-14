"""The global event intercept.  All events are copied into this."""

from typing import Dict, Optional, Any
from petronia_common.event_stream import (
    EventForwarderTarget, RawBinaryReader,
    to_raw_event_object,
)
from petronia_common.util import PetroniaReturnError
from .handler_id import create_handler_id
from .router_loop import ExtensionLaunchWatcher
from ..event_router import EventRouter
from ..events import foreman, foreman_announcement


ALLOWED_EVENT_IDS = (
    foreman_announcement.ExtensionStartupCompleteEvent.FULL_EVENT_NAME,
)


class GlobalEventIntercept(EventForwarderTarget, ExtensionLaunchWatcher):
    """Intercepts all events sent by all extensions."""

    __slots__ = ('__router', '__pending_extensions')

    def __init__(self) -> None:
        self.__router: Optional[EventRouter] = None

        # handle_id -> extension loader id
        self.__pending_extensions: Dict[str, str] = {}

    def set_router(self, router: EventRouter) -> None:
        """Set the event router."""
        self.__router = router

    def extension_launching(self, source_id: str, handler_id: str) -> None:
        """Mark an extension as launching"""
        self.__pending_extensions[handler_id] = source_id

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        return self.__router is not None and event_id in ALLOWED_EVENT_IDS

    def on_error(self, error: PetroniaReturnError) -> bool:
        return False

    def on_eof(self) -> None:
        self.__router = None

    def consume_object(
            self, event_id: str, source_id: str, target_id: str, event_data: Dict[str, Any],
    ) -> bool:
        if self.__router:
            if event_id == foreman_announcement.ExtensionStartupCompleteEvent.FULL_EVENT_NAME:
                extension_name = get_extension_name_from_source_id(source_id)
                handler_id = create_handler_id(extension_name)
                extension_loader_id = self.__pending_extensions.get(handler_id)
                if extension_loader_id:
                    del self.__pending_extensions[handler_id]
                    # The extension reported itself as started, so send an event
                    # back to the extension loader to report that it has started
                    # successfully.
                    # print(f"Telling {extension_loader_id} that extension {extension_name} loaded")
                    self.__router.inject_event(to_raw_event_object(
                        foreman.LauncherStartExtensionSuccessEvent.FULL_EVENT_NAME,
                        handler_id,
                        extension_loader_id,
                        foreman.LauncherStartExtensionSuccessEvent(extension_name).export_data(),
                    ))
                # else:
                #     print(f"{extension_name} said it loaded, but it is not known")
                return False
        return False

    def consume_binary(
            self, event_id: str, source_id: str, target_id: str, size: int,
            data_reader: RawBinaryReader,
    ) -> bool:
        return False


def get_extension_name_from_source_id(source_id: str) -> str:
    """Get the extension name for the source id."""
    if ':' in source_id:
        return source_id[:source_id.index(':')]
    return source_id
