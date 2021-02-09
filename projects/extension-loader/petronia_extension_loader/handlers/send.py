"""Send different kinds of events."""

from typing import Iterable, Tuple, Set, Optional
import json
from petronia_ext_lib.runner import EventRegistryContext
from petronia_common.extension.config import ImplExtensionMetadata, StandAloneExtensionMetadata
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from .privileges import add_event_send_access, get_source_id_prefix_access
from ..defs import ExtensionInfo, TRANSLATION_CATALOG
from ..setup import get_extension_config
from ..events.impl import extension_loader, foreman
from ..events.ext.datastore import StoreDataEvent


EXTENSION_LOADER_FOREMAN_SOURCE = extension_loader.EXTENSION_NAME + ':for-foreman'

EventTargetHandle = Tuple[Optional[str], Optional[str]]


def send_add_event_listener_event(
        context: EventRegistryContext,
        extension_handler_id: str,
        events: Iterable[EventTargetHandle],
) -> StdRet[None]:
    """Request to add an event listener to foreman."""
    return context.send_event(
        EXTENSION_LOADER_FOREMAN_SOURCE,
        extension_handler_id,
        foreman.ExtensionAddEventListenerEvent(
            [
                foreman.EventTarget(event_id, target_id)
                for event_id, target_id in events
            ]
        ),
    )


def send_remove_event_listener(
        context: EventRegistryContext,
        extension_handler_id: str,
        events: Iterable[EventTargetHandle],
) -> StdRet[None]:
    """Request to remove an event listener to foreman."""
    return context.send_event(
        EXTENSION_LOADER_FOREMAN_SOURCE,
        extension_handler_id,
        foreman.ExtensionRemoveEventListenerEvent(
            [
                foreman.EventTarget(event_id, target_id)
                for event_id, target_id in events
            ]
        ),
    )


def send_startup_complete(context: EventRegistryContext) -> StdRet[None]:
    """Send the Startup Complete event."""
    return context.send_event(
        extension_loader.SystemStartedEvent.UNIQUE_TARGET_FQN,
        extension_loader.SystemStartedEvent.UNIQUE_TARGET_FQN,
        extension_loader.SystemStartedEvent(),
    )


def send_loaded_extension_state(
        context: EventRegistryContext,
        loaded: Iterable[ExtensionInfo],
) -> StdRet[None]:
    """Send the data store event for the loaded extensions."""
    return context.send_event(
        extension_loader.ActiveExtensionsState.UNIQUE_TARGET_FQN,
        StoreDataEvent.UNIQUE_TARGET_FQN,
        StoreDataEvent(
            json.dumps(extension_loader.ActiveExtensionsState([
                extension_loader.ExtensionInfo(
                    info.name,
                    list(info.version),
                    info.metadata.about,
                    info.metadata.description,
                    list(info.metadata.authors),
                    list(info.metadata.licenses),
                )
                for info in loaded
            ]).export_data()),
        ),
    )


def send_foreman_start_extension_request(
        context: EventRegistryContext,
        extension_info: ExtensionInfo,
        loaded_extensions: Iterable[ExtensionInfo],
) -> StdRet[None]:
    """Send a request to foreman to start an extension within a started launcher."""
    metadata = extension_info.metadata
    if not isinstance(metadata, (StandAloneExtensionMetadata, ImplExtensionMetadata)):
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('cannot send start request for non-implementable extension {name}'),
            name=extension_info.name,
        )
    event_source_id_access = get_source_id_prefix_access(extension_info)
    event_send_access: Set[str] = set()
    res = add_event_send_access(event_send_access, extension_info, True, set(), loaded_extensions)
    if res.has_error:
        return res
    config = get_extension_config(extension_info.name) or {}
    return context.send_event(
        EXTENSION_LOADER_FOREMAN_SOURCE,
        foreman.LauncherStartExtensionRequestEvent.UNIQUE_TARGET_FQN,
        foreman.LauncherStartExtensionRequestEvent(
            name=extension_info.name,
            version=list(extension_info.version),
            location=list(extension_info.path),
            runtime=metadata.runtime.launcher,
            send_access=foreman.SendEventAccess(
                list(event_send_access), list(event_source_id_access),
            ),
            configuration=json.dumps(config),
            permissions=[
                foreman.ExtensionPermission(action, list(resources))
                for action, resources in metadata.runtime.requested_permissions.items()
            ],
        ),
    )


def send_load_extension_failed(
        context: EventRegistryContext,
        request_source_id: str,
        extension_name: str,
        # error: PetroniaReturnError,
        error: extension_loader.Error,
) -> StdRet[None]:
    """Send a failure response that an extension failed to load."""
    return context.send_event(
        extension_loader.LoadExtensionRequestEvent.UNIQUE_TARGET_FQN,
        request_source_id,
        extension_loader.LoadExtensionFailedEvent(extension_name, error),
    )


def send_load_extension_succeeded(
        context: EventRegistryContext,
        request_source_id: str,
        extension_name: str,
        version: Iterable[int],
) -> StdRet[None]:
    """Send a failure response that an extension failed to load."""
    return context.send_event(
        extension_loader.LoadExtensionRequestEvent.UNIQUE_TARGET_FQN,
        request_source_id,
        extension_loader.LoadExtensionSuccessEvent(extension_name, list(version)),
    )
