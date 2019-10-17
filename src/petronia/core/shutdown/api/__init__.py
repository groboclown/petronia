
"""
API for the system shutdown process.
"""

from .bootstrap import bootstrap_shutdown_api as start_extension
from .bootstrap import EXTENSION_METADATA

from .events import (
    SystemShutdownEvent,
    as_system_shutdown_listener,

    SystemShutdownCancelledEvent,
    as_system_shutdown_cancelled_listener,

    send_system_shutdown_request,

    SystemShutdownFinalizeEvent,
    as_system_shutdown_finalize_listener,

    TARGET_ID_SYSTEM_SHUTDOWN,
)
