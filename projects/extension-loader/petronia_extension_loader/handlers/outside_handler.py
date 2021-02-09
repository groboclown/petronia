"""
Handles the full process that loads the extension.
"""

from petronia_common.extension.runner import (
    EventRegistryContext, EventObjectTarget, EventObjectParser,
)
from petronia_common.util import StdRet
from petronia_ext_lib.standard.error import create_error_data, ACCESS_RESTRICTION_ERROR_CATEGORY
from .extension_loader import initiate_load_extension
from .send import send_load_extension_succeeded, send_load_extension_failed
from ..shared_state import ExtLoaderSharedState
from ..events.impl import extension_loader
from ..messages import display_message


def register_load_extension_handler(
        shared_state: ExtLoaderSharedState,
        registry: EventRegistryContext,
) -> StdRet[None]:
    """Create the event target for loading extension requests."""
    res = registry.register_event(
        extension_loader.LoadExtensionRequestEvent.FULL_EVENT_NAME,
        EventObjectParser(extension_loader.LoadExtensionRequestEvent.parse_data),
    )
    if res.has_error:
        return res
    return registry.register_target(
        extension_loader.LoadExtensionRequestEvent.FULL_EVENT_NAME,
        extension_loader.LoadExtensionRequestEvent.UNIQUE_TARGET_FQN,
        LoadExtensionHandler(shared_state, registry),
    )


class LoadExtensionHandler(EventObjectTarget[extension_loader.LoadExtensionRequestEvent]):
    """
    Listens to the external requests to load an extension.  This begins a chain of
    events.
    """

    __slots__ = ('_state', '_context')

    def __init__(self, shared_state: ExtLoaderSharedState, context: EventRegistryContext) -> None:
        self._state = shared_state
        self._context = context

    def on_event(
            self, source: str, target: str, event: extension_loader.LoadExtensionRequestEvent,
    ) -> bool:
        res = initiate_load_extension(
            self._state, self._context,
            source, event.name, event.minimum_version, event.below_version, None,
        )
        error_data = create_error_data(
            extension_loader.Error, extension_loader.LocalizableMessage,
            extension_loader.MessageArgument, extension_loader.MessageArgumentValue,
            res,
            [ACCESS_RESTRICTION_ERROR_CATEGORY],
            'load-extension-initialization-error',
            extension_loader.EXTENSION_NAME,
        )
        if error_data:
            fail_res = send_load_extension_failed(
                self._context, source, event.name, error_data,
            )
            if fail_res.has_error:
                display_message(
                    fail_res,
                    f'Failed attempting to send a failure message '
                    f'for loading extension {event.name}'
                )
            return False
        if res.result is not None:
            # Already loaded, so send the load success message.
            success_res = send_load_extension_succeeded(
                self._context, source, event.name, res.result,
            )
            if success_res.has_error:
                display_message(
                    success_res,
                    f'Failed attempting to send a success message '
                    f'for loading extension {event.name}'
                )
        return False
