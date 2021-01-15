"""Routes events based on event IDs to handlers."""

from typing import List
from petronia_common.event_stream import EventForwarder, BinaryReader, BinaryWriter
from petronia_common.event_stream.thread_stream import ThreadedStreamForwarder
from petronia_common.util import StdRet
from .setup import get_launcher_id
from .context import EventHandlerContext
from .handlers.factory import register_load_extension_handler
from .initial_extensions import boot_extensions
from .handlers.send import EventTargetHandle, send_add_event_listener
from .events.impl import foreman, extension_loader


def create_router(reader: BinaryReader, outp: BinaryWriter) -> StdRet[EventForwarder]:
    """Create the event forwarder with the default event handlers registered."""
    ret = EventForwarder(
        reader,
        ThreadedStreamForwarder(),
        None,
    )

    context = EventHandlerContext(ret, outp)

    res = send_add_event_listener(
        context, get_launcher_id(), get_launcher_id(),
        get_listeners(),
    )
    if res.has_error:
        return res.forward()

    res = register_load_extension_handler(context)
    if res.has_error:
        return res.forward()

    res = boot_extensions(context)
    if res.has_error:
        return res.forward()

    return StdRet.pass_ok(ret)


def get_listeners() -> List[EventTargetHandle]:
    """Get all events that the extension loader can listen to."""
    return [
        (foreman.LauncherLoadExtensionSuccessEvent.FULL_EVENT_NAME, None),
        (foreman.LauncherLoadExtensionFailedEvent.FULL_EVENT_NAME, None),
        (foreman.StartLauncherSuccessEvent.FULL_EVENT_NAME, None),
        (foreman.StartLauncherFailedEvent.FULL_EVENT_NAME, None),
        (extension_loader.LoadExtensionRequestEvent.FULL_EVENT_NAME, None),
        (extension_loader.RegisterExtensionListenersEvent.FULL_EVENT_NAME, None),
        (extension_loader.RemoveExtensionListenersEvent.FULL_EVENT_NAME, None),

        # Does not listen to data store events; just sends them.
        # (datastore.DataUpdateEvent.FULL_EVENT_NAME, None),
    ]
