"""Event handlers for changing the list of listeners allowed by a loaded
extension."""

from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.runner import EventRegistryContext, ContextEventObjectTarget
from petronia_extension_loader.shared_state import ExtLoaderSharedState
from . import privileges
from ..events.impl import extension_loader as extension_loader_event
from ..events.impl import foreman as foreman_event
from ..messages import display_messages


def register_listener_change_handlers(
        shared_state: ExtLoaderSharedState,
        registry: EventRegistryContext,
) -> StdRet[None]:
    """Register the listeners for adding and removing listeners."""
    return join_none_results(
        registry.register_event_parser(
            extension_loader_event.RegisterExtensionListenersEvent.FULL_EVENT_NAME,
            extension_loader_event.RegisterExtensionListenersEvent.parse_data,
        ),
        registry.register_target(
            extension_loader_event.RegisterExtensionListenersEvent.FULL_EVENT_NAME,
            extension_loader_event.RegisterExtensionListenersEvent.UNIQUE_TARGET_FQN,
            RegisterExtensionListenersHandler(shared_state, registry),
        ),

        registry.register_event_parser(
            extension_loader_event.RemoveExtensionListenersEvent.FULL_EVENT_NAME,
            extension_loader_event.RemoveExtensionListenersEvent.parse_data,
        ),
        registry.register_target(
            extension_loader_event.RemoveExtensionListenersEvent.FULL_EVENT_NAME,
            extension_loader_event.RemoveExtensionListenersEvent.UNIQUE_TARGET_FQN,
            RemoveExtensionListenersHandler(shared_state, registry),
        ),
    )


class RegisterExtensionListenersHandler(
    ContextEventObjectTarget[extension_loader_event.RegisterExtensionListenersEvent]
):
    """Handles RegisterExtensionListenersEvent"""
    __slots__ = ('state',)

    def __init__(
            self,
            shared_state: ExtLoaderSharedState,
            registry: EventRegistryContext,
    ) -> None:
        ContextEventObjectTarget.__init__(self, registry)
        self.state = shared_state

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: extension_loader_event.RegisterExtensionListenersEvent,
    ) -> bool:
        # The source must have originated from the source extension.
        ext_name = get_extension_name(source)
        ext_info = self.state.load_list().get_loaded_info(ext_name)
        if not ext_info:
            # It might be loading...
            ext_info = self.state.load_list().get_loading_extension(ext_name)
        if ext_info:
            valid_pairs = privileges.get_valid_listen_event_pairs(
                [
                    (e.event_id, e.target_id)
                    for e in event.events
                ],
                ext_info, True, set(), self.state.load_list().get_loaded(),
            )
            res = context.send_event(
                extension_loader_event.RegisterExtensionListenersEvent.UNIQUE_TARGET_FQN,
                # Interesting event.  The target is the source extension.
                ext_name,
                foreman_event.ExtensionAddEventListenerEvent([
                    foreman_event.EventTarget(event_id, target_id)
                    for event_id, target_id in valid_pairs
                ]),
            )
            if res.has_error:
                display_messages('send event failed', *res.error_messages())

        return False


class RemoveExtensionListenersHandler(
    ContextEventObjectTarget[extension_loader_event.RemoveExtensionListenersEvent]
):
    """Handles RemoveExtensionListenersEvent"""
    __slots__ = ('state',)

    def __init__(
            self,
            shared_state: ExtLoaderSharedState,
            registry: EventRegistryContext,
    ) -> None:
        ContextEventObjectTarget.__init__(self, registry)
        self.state = shared_state

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: extension_loader_event.RemoveExtensionListenersEvent,
    ) -> bool:
        # The source must have originated from the source extension.
        ext_name = get_extension_name(source)
        ext_info = self.state.load_list().get_loaded_info(ext_name)
        if not ext_info:
            # It might be loading...
            ext_info = self.state.load_list().get_loading_extension(ext_name)
        if ext_info:
            res = context.send_event(
                extension_loader_event.RemoveExtensionListenersEvent.UNIQUE_TARGET_FQN,
                # Interesting event.  The target is the source extension.
                ext_name,
                foreman_event.ExtensionAddEventListenerEvent([
                    foreman_event.EventTarget(event_details.event_id, event_details.target_id)
                    for event_details in event.events
                ]),
            )
            if res.has_error:
                display_messages('send event failed', *res.error_messages())

        return False


def get_extension_name(event_source: str) -> str:
    """Get the name of the extension based on the source id from an event."""
    pos = event_source.find(':')
    if pos > 0:
        return event_source[:pos]
    return event_source
