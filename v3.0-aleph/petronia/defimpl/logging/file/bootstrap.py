
"""
Sets up the logger in the system.
"""

from ....aid.std import (
    EventBus,
    ListenerSet,
)
from ....aid.bootstrap import (
    ANY_VERSION,
)
from ....base.internal_.internal_extension import petronia_extension
from .handler import startup_file_logger


def bootstrap_file_logger(bus: EventBus) -> None:
    """
    Sets up the file logger.  It doesn't ever explicitly shut down.
    """
    listeners = ListenerSet(bus)
    startup_file_logger(bus, listeners)


EXTENSION_METADATA = petronia_extension({
    'type': 'standalone',
    'depends': ({
        'extension': 'core.state.api',
        'minimum': ANY_VERSION,
    },),
    'name': 'default.logging.file',
    'version': (1, 0, 0,),
})
