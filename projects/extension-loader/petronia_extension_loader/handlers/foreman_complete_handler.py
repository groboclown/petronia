"""Handles the foreman extension load complete events."""

from petronia_common.extension.runner import (
    EventObjectTarget, EventRegistryContext, EventObjectParser,
)
from petronia_common.util import StdRet, RET_OK_NONE
from .send import EXTENSION_LOADER_FOREMAN_SOURCE
from ..events.impl import foreman
from ..shared_state import ExtLoaderSharedState


def register_load_complete_handlers(
        shared_state: ExtLoaderSharedState,
        registry: EventRegistryContext,
) -> StdRet[None]:
    """Create the event target for loading extension requests."""
    res = registry.register_event(
        foreman.LauncherStartExtensionSuccessEvent.FULL_EVENT_NAME,
        EventObjectParser(foreman.LauncherStartExtensionSuccessEvent.parse_data),
    )
    if res.has_error:
        return res
    res = registry.register_target(
        foreman.LauncherStartExtensionSuccessEvent.FULL_EVENT_NAME,
        EXTENSION_LOADER_FOREMAN_SOURCE,
        LoadSuccessHandler(shared_state, registry),
    )
    if res.has_error:
        return res.forward()
    res = registry.register_event(
        foreman.LauncherStartExtensionFailedEvent.FULL_EVENT_NAME,
        EventObjectParser(foreman.LauncherStartExtensionFailedEvent.parse_data),
    )
    if res.has_error:
        return res
    res = registry.register_target(
        foreman.LauncherStartExtensionFailedEvent.FULL_EVENT_NAME,
        EXTENSION_LOADER_FOREMAN_SOURCE,
        LoadFailedHandler(),
    )
    if res.has_error:
        return res.forward()
    return RET_OK_NONE


class LoadSuccessHandler(EventObjectTarget[foreman.LauncherStartExtensionSuccessEvent]):
    """Handles the load success event.  After the load, the shared state of next
    extensions to load needs to be processed.  If the loaded extension had a requested
    source_id, then the load success event is sent."""

    __slots__ = ('_state', '_registry',)

    def __init__(
        self,
        shared_state: ExtLoaderSharedState,
        registry: EventRegistryContext,
    ) -> None:
        self._state = shared_state
        self._registry = registry

    def on_event(
            self, source: str, target: str, event: foreman.LauncherStartExtensionSuccessEvent,
    ) -> bool:
        self._state.on_extension_loaded(
            event.name, self._registry,
        )
        return False


class LoadFailedHandler(EventObjectTarget[foreman.LauncherStartExtensionFailedEvent]):
    """Handles the load failed event.  All down-stream extensions that depend upon
    this event must be triggered as a failure, too.  If this extension or any
    down-stream extension has a requested source_id, then the failure is sent."""

    def on_event(
            self, source: str, target: str, event: foreman.LauncherStartExtensionFailedEvent,
    ) -> bool:
        print(event.export_data())
        raise NotImplementedError
