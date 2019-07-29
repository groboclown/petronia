
"""
Initialization of Petronia.

Handles loading of the configuration files and starting up the platform-specific engine.

Has deep knowledge of the correct initialization ordering.
"""

from .bus import create_bus
from .core import load_core_extensions
