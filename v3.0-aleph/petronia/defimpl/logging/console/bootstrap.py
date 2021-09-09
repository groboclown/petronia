
"""
Sets up the logger in the system.
"""

from ....aid.std import (
    EventBus,
)
from ....aid.bootstrap import (
    ANY_VERSION,
)
from ....aid.lifecycle import (
    setup_dispose_handler,
)
from ....base.internal_.internal_extension import petronia_extension
from .ident import TARGET_ID_CONSOLE_LOGGER
from .transition import LogStateTransitionHandler


def bootstrap_console_logger(bus: EventBus) -> None:
    """
    Sets up the console logger.
    """
    log_transition_handler = LogStateTransitionHandler(bus)
    setup_dispose_handler(
        bus,
        TARGET_ID_CONSOLE_LOGGER,
        log_transition_handler.dispose
    )


EXTENSION_METADATA = petronia_extension({
    'type': 'standalone',
    'depends': ({
        'extension': 'core.state.api',
        'minimum': ANY_VERSION,
    },),
    'name': 'default.logging.console',
    'version': (1, 0, 0,),
})
