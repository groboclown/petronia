
"""
Sets up the logger in the system.
"""

from ....aid.std import (
    EventBus,
)
from ....aid.bootstrap import (
    send_participant_started_event,
    ExtensionMetadataStruct,
    ANY_VERSION,
)
from ....aid.lifecycle import (
    setup_dispose_handler,
)
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
    send_participant_started_event(
        bus,
        TARGET_ID_CONSOLE_LOGGER
    )


EXTENSION_METADATA: ExtensionMetadataStruct = {
    'type': 'standalone',
    'depends': [{
        'extension': 'core.state.api',
        'minimum': ANY_VERSION,
    }],
    'name': 'default.logging.console',
    'version': (1, 0, 0,),
    'authors': ['Petronia'],
}
