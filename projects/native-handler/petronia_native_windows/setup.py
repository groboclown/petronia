"""Set up the extension for running."""

from typing import Sequence, Callable, Optional
import time
from petronia_common.util import StdRet, UserMessage, join_none_results, join_errors
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
from . import window_handler


class WindowsRunner:
    """Simple return type that performs the start process in the right order."""

    __slots__ = ('__post_start', '__loop')

    def __init__(
            self,
            loop: message_loop.WindowsMessageLoop,
            callbacks: Sequence[Callable[[], StdRet[None]]],
    ) -> None:
        self.__loop = loop
        self.__post_start = tuple(callbacks)

    def start(self) -> StdRet[None]:
        """Start the loop and run the callbacks."""
        print("** WINDOWS STARTING MESSAGE LISTENER **")
        self.__loop.start()

        # Wait for the loop to start.
        end_time = time.time() + 60.0
        while time.time() < end_time and not self.__loop.is_running():
            time.sleep(1.0)
        if not self.__loop.is_running():
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('Native windows message handler did not start after {timeout} seconds.'),
                timeout=60.0,
            )

        print("** WINDOWS INITIALIZING STATE **")
        return join_none_results(*(
            c()
            for c in self.__post_start
        ))

    def dispose(self, timeout: float) -> None:
        """Dispose of the runner."""
        self.__loop.dispose(timeout)


def setup_context(
        context: EventRegistryContext,
        config: Optional[ConfigurationState],
) -> StdRet[WindowsRunner]:
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

    win_handler = window_handler.WindowsNativeHandler()
    win_handler.register_listeners(context)

    loop = message_loop.WindowsMessageLoop()
    hotkey_handler.register_with_loop(loop)
    screen_handler.register_with_loop(loop)
    win_handler.register_messages(loop)

    return StdRet.pass_ok(WindowsRunner(
        loop,
        [win_handler.initialize_system_state],
    ))


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
