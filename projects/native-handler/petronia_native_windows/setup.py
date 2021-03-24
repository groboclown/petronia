"""Set up the extension for running."""

from typing import Optional
from petronia_common.util import StdRet, UserMessage, join_errors
from petronia_common.util import i18n as _
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget
from petronia_native.common import handlers, user_messages
from petronia_native.common.events.impl import screen as screen_event
from .datastore.petronia_native_windows import ConfigurationState
from . import message_loop
from . import configuration
from . import key_handler
from . import screen
from . import windows_vs


def setup_context(
        context: EventRegistryContext,
        config: Optional[ConfigurationState],
) -> StdRet[message_loop.WindowsMessageLoop]:
    """Setup the context for the extension."""
    res = windows_vs.bootstrap_screens()
    if res.has_error:
        return res.forward()

    config_handler = configuration.ConfigurationStore(config)

    hotkey_handler = key_handler.WindowsKeyHandler(context, config_handler)
    res = handlers.hotkey.register_hotkey_listeners(context, hotkey_handler)
    if res.has_error:
        return res.forward()

    res = handlers.monitor_screen.register_set_screen_configuration_listener(
        context, ScreenConfigChangeEventListener(context),
    )
    if res.has_error:
        return res.forward()

    screen_handler = screen.WindowsScreen(context, config_handler)

    loop = message_loop.WindowsMessageLoop()
    hotkey_handler.register_with_loop(loop)
    screen_handler.register_with_loop(loop)

    return StdRet.pass_ok(loop)


class ScreenConfigChangeEventListener(
    EventObjectTarget[screen_event.SetScreenConfigurationRequestEvent]
):
    """Handles change config events directed to the screen."""
    __slots__ = ('_context',)

    def __init__(self, context: EventRegistryContext) -> None:
        self._context: Optional[EventRegistryContext] = context

    def on_close(self) -> None:
        self._context = None

    def on_event(
            self, source: str, target: str,
            event: screen_event.SetScreenConfigurationRequestEvent,
    ) -> bool:
        if not self._context:
            # Closed, so de-register this listener.
            return True

        # Does not allow manual screen config settings.
        user_messages.report_send_receive_problems(
            handlers.monitor_screen.send_screen_configuration_bad(
                self._context, source, event.request_id,
                join_errors(UserMessage(
                    user_messages.TRANSLATION_CATALOG,
                    _('native implementation does not support setting a screen configuration'),
                )),
            )
        )
        return False
