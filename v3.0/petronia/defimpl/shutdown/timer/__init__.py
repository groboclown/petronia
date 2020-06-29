
"""
Sends a halt message after a time is exceeded in either a total time or
a quiet period with no events.
"""

from .bootstrap import bootstrap_shutdown_timer as start_extension
from .bootstrap import EXTENSION_METADATA
