"""Routes events based on event IDs to handlers."""

from typing import List, Sequence, Tuple, Callable, Optional
from petronia_ext_lib.runner import EventRegistryContext
from petronia_common.util import StdRet
from .setup import get_extension_handler_id
from .shared_state import ExtLoaderSharedState
from .handlers.outside_handler import register_load_extension_handler
from .handlers.foreman_complete_handler import register_load_complete_handlers
from .handlers.request_listener_change_handler import register_listener_change_handlers
from .initial_extensions import boot_extensions
from .handlers.send import send_add_event_listener_event
from .events.impl import foreman, extension_loader


def create_startup_handlers() -> List[
    Callable[[ExtLoaderSharedState, EventRegistryContext], StdRet[None]]
]:
    """Create the event forwarder with the default event handlers registered."""
    return [
        add_event_listeners,
        register_load_extension_handler,
        register_load_complete_handlers,
        register_listener_change_handlers,
        boot_extensions,
    ]


def add_event_listeners(
        _shared_state: ExtLoaderSharedState,
        context: EventRegistryContext,
) -> StdRet[None]:
    """Get all events that the extension loader can listen to."""
    return send_add_event_listener_event(context, get_extension_handler_id(), MONITORING_EVENTS)


MONITORING_EVENTS: Sequence[Tuple[Optional[str], Optional[str]]] = (
        (foreman.LauncherStartExtensionSuccessEvent.FULL_EVENT_NAME, None),
        (foreman.LauncherStartExtensionFailedEvent.FULL_EVENT_NAME, None),
        (extension_loader.LoadExtensionRequestEvent.FULL_EVENT_NAME, None),
        (extension_loader.RegisterExtensionListenersEvent.FULL_EVENT_NAME, None),
        (extension_loader.RemoveExtensionListenersEvent.FULL_EVENT_NAME, None),

        # Extension loader does not listen to data store events; just sends them.
        # (datastore.DataUpdateEvent.FULL_EVENT_NAME, None),
)
