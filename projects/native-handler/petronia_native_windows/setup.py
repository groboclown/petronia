"""Set up the extension for running."""

from petronia_common.util import StdRet, RET_OK_NONE
from petronia_ext_lib.runner import EventRegistryContext
from petronia_native.common import handlers
from . import windows_vs


def setup_context(context: EventRegistryContext) -> StdRet[None]:
    """Setup the context for the extension."""
    res = windows_vs.bootstrap_screens()
    if res.has_error:
        return res

    hotkey_handler = handlers.hotkey.HotkeyHandler()
    res = handlers.hotkey.register_hotkey_listeners(context, hotkey_handler)
    if res.has_error:
        return res
    screen_handler = handlers.monitor_screen.AbstractScreenHandler(context)
    handlers.monitor_screen.register_screen_listener(context, screen_handler)
    if res.has_error:
        return res
    # Don't need to register the monitor listener, because it reports to the screen directly.

    # FIXME start the Windows message loop.
    # The message loop runs in a separate thread.  Where possible, all Windows native commands
    # should be run in the message loop.  The event stream is thread safe, so events can be
    # sent from the message loop.

    return RET_OK_NONE
