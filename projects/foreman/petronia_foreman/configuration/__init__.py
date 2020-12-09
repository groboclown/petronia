
"""
Basic Petronia configuration loader.  The loaded configuration can be used
for multiple parts of Petronia, but, here, it's only read for the foreman
configuration.

This is the end-user's first view into configuring Petronia.  It should be
straight-forward and simple.  If something has complex behavior, that should
be simplified into referencing a file name, so the user can choose the
configuration that best suits their needs.
"""

from .foreman import ForemanConfig
from .platform import SUPPORTED_PLATFORMS, PlatformSettings, detect_platform
from .launcher import LauncherConfig
from .launcher_parameters import LauncherOptions
from .reader import read_configuration_file
