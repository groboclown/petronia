"""Register and unregister event listeners."""

from typing import Iterable, Tuple, Optional
from petronia_common.util import StdRet
from ..events import extension_loader
from ..runner.registry import EventRegistryContext


def send_register_listeners(
        context: EventRegistryContext,
        listening_extension_name: str,
        listeners: Iterable[Tuple[Optional[str], Optional[str]]],
) -> StdRet[None]:
    """Send the request to add listeners.  This must be done before starting the
    event loop.

    The listeners are pairs of (event_id, target_id).
    """
    return context.send_event(
        listening_extension_name,
        extension_loader.RegisterExtensionListenersEvent.UNIQUE_TARGET_FQN,
        extension_loader.RegisterExtensionListenersEvent([
            extension_loader.EventListener(eid, tid)
            for eid, tid in listeners
        ]),
    )


def send_remove_listeners(
        context: EventRegistryContext,
        listening_extension_name: str,
        listeners: Iterable[Tuple[Optional[str], Optional[str]]],
) -> StdRet[None]:
    """Send the request to remove listeners.  This must be done before starting the
    event loop.

    The listeners are pairs of (event_id, target_id).
    """
    return context.send_event(
        listening_extension_name,
        extension_loader.RemoveExtensionListenersEvent.UNIQUE_TARGET_FQN,
        extension_loader.RemoveExtensionListenersEvent([
            extension_loader.EventListener(eid, tid)
            for eid, tid in listeners
        ]),
    )
