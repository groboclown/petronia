"""Send different kinds of events."""

from typing import Iterable, Tuple, Mapping, Set, Optional
import os
import json
from petronia_common.util import StdRet
from .privileges import add_event_send_access
from ..context import EventHandlerContext
from ..defs import ExtensionInfo
from ..setup import get_extension_config
from ..events.impl.extension_loader import (
    SystemStartedEvent,
    ActiveExtensionsState,
    LoadExtensionRequestEvent,
    LoadExtensionFailedEvent,
    Extensions,
    Error,
    EXTENSION_NAME,
)
from ..events.impl.foreman import (
    ExtensionAddEventListenerEvent,
    ExtensionRemoveEventListenerEvent,
    Events,
    StartLauncherRequestEvent,
    LauncherLoadExtensionRequestEvent,
    Permissions,
)
from ..events.ext.datastore import StoreDataEvent


EXTENSION_LOADER_FOREMAN_SOURCE = EXTENSION_NAME + ':for-foreman'
EXTENSION_LOADER_STATE_SOURCE = EXTENSION_NAME + ':state'

EventTargetHandle = Tuple[Optional[str], Optional[str]]


def send_add_event_listener(
        context: EventHandlerContext,
        launcher_id: str,
        extension_name: str,
        events: Iterable[EventTargetHandle],
) -> StdRet[None]:
    """Request to add an event listener to foreman."""
    return context.writer.write_object_event(
        ExtensionAddEventListenerEvent.FULL_EVENT_NAME,
        EXTENSION_LOADER_FOREMAN_SOURCE,
        launcher_id,
        ExtensionAddEventListenerEvent(
            extension_name,
            [
                Events(event_id, target_id)
                for event_id, target_id in events
            ]
        ).export_data(),
    )


def send_remove_event_listener(
        context: EventHandlerContext,
        launcher_id: str,
        extension_name: str,
        events: Iterable[EventTargetHandle],
) -> StdRet[None]:
    """Request to remove an event listener to foreman."""
    return context.writer.write_object_event(
        ExtensionRemoveEventListenerEvent.FULL_EVENT_NAME,
        EXTENSION_LOADER_FOREMAN_SOURCE,
        launcher_id,
        ExtensionRemoveEventListenerEvent(
            extension_name,
            [
                Events(event_id, target_id)
                for event_id, target_id in events
            ]
        ).export_data(),
    )


def send_startup_complete(context: EventHandlerContext) -> StdRet[None]:
    """Send the Startup Complete event."""
    return context.writer.write_object_event(
        SystemStartedEvent.FULL_EVENT_NAME,
        SystemStartedEvent.UNIQUE_TARGET_FQN,
        SystemStartedEvent.UNIQUE_TARGET_FQN,
        SystemStartedEvent().export_data(),
    )


def send_loaded_extension_state(
        context: EventHandlerContext,
        loaded: Iterable[ExtensionInfo],
) -> StdRet[None]:
    """Send the data store event for the loaded extensions."""
    return context.writer.write_object_event(
        StoreDataEvent.FULL_EVENT_NAME,
        EXTENSION_LOADER_STATE_SOURCE,
        StoreDataEvent.UNIQUE_TARGET_FQN,
        StoreDataEvent(
            ActiveExtensionsState.UNIQUE_TARGET_FQN,
            json.dumps(ActiveExtensionsState([
                Extensions(
                    info.name,
                    list(info.version),
                    info.metadata.about,
                    info.metadata.description,
                    list(info.metadata.authors),
                    list(info.metadata.licenses),
                )
                for info in loaded
            ]).export_data()),
        ).export_data(),
    )


def send_start_launcher_request(
        context: EventHandlerContext,
        identifier: str,
        launcher: str,
        permissions: Mapping[str, Iterable[str]],
) -> StdRet[None]:
    """Send a request to start a launcher."""
    return context.writer.write_object_event(
        StartLauncherRequestEvent.FULL_EVENT_NAME,
        EXTENSION_LOADER_FOREMAN_SOURCE,
        StartLauncherRequestEvent.UNIQUE_TARGET_FQN,
        StartLauncherRequestEvent(
            identifier,
            launcher,
            [
                Permissions(key, list(req))
                for key, req in permissions.items()
            ],
        ).export_data(),
    )


def send_foreman_start_extension_request(
        context: EventHandlerContext,
        extension_info: ExtensionInfo,
        loaded_extensions: Iterable[ExtensionInfo],
) -> StdRet[None]:
    """Send a request to foreman to start an extension within a started launcher."""
    event_send_access: Set[str] = set()
    res = add_event_send_access(event_send_access, extension_info, True, set(), loaded_extensions)
    if res.has_error:
        return res
    config = get_extension_config(extension_info.name) or {}
    return context.writer.write_object_event(
        LauncherLoadExtensionRequestEvent.FULL_EVENT_NAME,
        EXTENSION_LOADER_FOREMAN_SOURCE,
        LauncherLoadExtensionRequestEvent.UNIQUE_TARGET_FQN,
        LauncherLoadExtensionRequestEvent(
            extension_info.name,
            list(extension_info.version),
            os.pathsep.join(extension_info.path),
            list(event_send_access),
            json.dumps(config),
        ).export_data(),
    )


def send_load_extension_failed(
        context: EventHandlerContext,
        request_source_id: str,
        extension_name: str,
        # error: PetroniaReturnError,
        error: Error,
) -> StdRet[None]:
    """Send a failure response that an extension failed to load."""
    return context.writer.write_object_event(
        LoadExtensionFailedEvent.FULL_EVENT_NAME,
        request_source_id,
        LoadExtensionRequestEvent.UNIQUE_TARGET_FQN,
        LoadExtensionFailedEvent(extension_name, error).export_data(),
    )
