
"""
Structural definition for the contents of the Foreman configuration.
"""

from typing import Dict
from .launcher import LauncherConfig


class ForemanConfig:
    """
    The Foreman Process configuration.
    """

    # A map between a launcher type and the details for how
    # to run it.
    launcher_mapper: Dict[str, LauncherConfig]

    def __init__(self) -> None:
        self.launcher_mapper = {}
        self.native_handler_extension = ''
