
"""
Sets up the logger in the system.
"""

from ....aid.std import (
    EventBus,
    ListenerSet,
)
from ....aid.bootstrap import (
    send_participant_started_event,
    ANY_VERSION,
)
from ....base.internal_.internal_extension import petronia_extension
from .ident import TARGET_ID_FILE_LOGGER
from .handler import startup_file_logger


def bootstrap_file_logger(bus: EventBus) -> None:
    """
    Sets up the file logger.  It doesn't ever explicitly shut down.
    """
    listeners = ListenerSet(bus)
    startup_file_logger(bus, listeners)
    send_participant_started_event(
        bus,
        TARGET_ID_FILE_LOGGER
    )


EXTENSION_METADATA = petronia_extension({
    'type': 'standalone',
    'depends': ({
        'extension': 'core.state.api',
        'minimum': ANY_VERSION,
    },),
    'name': 'default.logging.file',
    'version': (1, 0, 0,),
})
