"""
The base boot launcher class.
"""
from abc import ABC

from petronia_foreman.launcher import AbcLauncherCategory


class AbcBootLauncherCategory(AbcLauncherCategory, ABC):
    """The boot launcher categories have extra methods for the boot time,
    because they are not loaded from the extension loader."""

    def get_channel_name(self) -> str:
        """The channel name for this boot launcher.  The name is highly specific
        to the task of the launcher."""
        raise NotImplementedError()
