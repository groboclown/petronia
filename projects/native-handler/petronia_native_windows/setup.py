"""Set up the extension for running."""

from typing import Optional
from petronia_common.util import StdRet
from petronia_ext_lib.runner import EventRegistryContext
from petronia_native.common import handlers
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

    screen_handler = screen.WindowsScreen(context, config_handler)
    handlers.monitor_screen.register_screen_listener(context, screen_handler)
    if res.has_error:
        return res.forward()
    # Don't need to register the monitor listener, because it reports to the screen directly.

    if res.has_error:
        return res.forward()

    loop = message_loop.WindowsMessageLoop()
    hotkey_handler.register_with_loop(loop)
    screen_handler.register_with_loop(loop)

    return StdRet.pass_ok(loop)
