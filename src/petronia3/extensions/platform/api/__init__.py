
"""
API that the platform components must implement.

This defines what is expected from the platform runtime implementation.
"""

from .bootstrap import bootstrap_platform_api as start_extension
from .bootstrap import EXTENSION_METADATA
