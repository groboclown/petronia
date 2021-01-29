
"""
Basic Petronia configuration loader.  The loaded configuration can be used
for multiple parts of Petronia, but, here, it's only read for the foreman
configuration.

This is the end-user's first view into configuring Petronia.  It should be
straight-forward and simple.  If something has complex behavior, that should
be simplified into referencing a file name, so the user can choose the
configuration that best suits their needs.
"""

from . import platform
from .foreman import ForemanConfig
from .platform import find_data_file, find_data_dir
from .runtime import RuntimeConfig
from .runtime_parameters import RuntimeLauncherOptions
from .reader import read_configuration_file, read_boot_extension_file
from .find_file import get_boot_extension_file
from .boot_extension import BootExtensionMetadata
