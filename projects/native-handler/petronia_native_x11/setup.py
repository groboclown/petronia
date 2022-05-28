"""Set up the extension for running."""

from typing import Optional
import time
from petronia_common.util import StdRet, UserMessage, join_none_results, join_errors, RET_OK_NONE
from petronia_common.util import i18n as _
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget
from petronia_native.common import handlers, user_messages
from petronia_native.common.events.impl import screen as screen_event
from .datastore.petronia_native_x11 import ConfigurationState
from . import configuration
from .libs.setup import setup_x11, X11Access
from .pet_evt.setup import setup_petronia_events, PetroniaEventHandlers


class X11Runner:
    """Simple return type that performs the start process in the right order."""

    __slots__ = (
        '__post_start', '__loop', '__disposed',
        '__use_argb_visual', '__replace_existing_wm',
    )

    def __init__(
            self, *,
            peh: PetroniaEventHandlers,
            use_argb_visual: bool,
            replace_existing_wm: bool,
    ) -> None:
        self.__post_start = peh
        self.__use_argb_visual = use_argb_visual
        self.__replace_existing_wm = replace_existing_wm
        self.__loop: Optional[X11Access] = None
        self.__disposed = False

    def start(self) -> StdRet[None]:
        """Start the loop and run the callbacks."""
        if self.__disposed:
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('Already disposed'),
            )
        if self.__loop is not None:
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('X11 already running'),
            )
        loop_res = setup_x11(
            use_argb_visual=self.__use_argb_visual,
            replace_existing_wm=self.__replace_existing_wm,
        )
        if loop_res.has_error:
            return loop_res.forward()
        self.__loop = loop_res.result
        res = self.__post_start.connect_to_x11(self.__loop)
        if res.has_error:
            return res.forward()

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

        # print("** WINDOWS INITIALIZING STATE **")
        return join_none_results(*(
            c()
            for c in self.__post_start.post_start_handlers()
        ))

    def dispose(self, timeout: float) -> StdRet[None]:
        """Dispose of the runner."""
        ret = RET_OK_NONE
        if not self.__disposed:
            self.__disposed = True
            if self.__loop:
                ret = self.__loop.dispose(timeout)
                self.__loop = None
        return ret


def setup_context(
        context: EventRegistryContext,
        config: Optional[ConfigurationState],
) -> StdRet[X11Runner]:
    """Set up the context for the extension."""
    config_handler = configuration.ConfigurationStore(config)
    event_res = setup_petronia_events(context, config_handler)
    if event_res.has_error:
        return event_res.forward()

    x11_runner = X11Runner(
        peh=event_res.result,
        use_argb_visual=config_handler.get_config().connection.use_argb_visual,
        replace_existing_wm=config_handler.get_config().connection.replace_existing_wm,
    )

    return StdRet.pass_ok(x11_runner)


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
