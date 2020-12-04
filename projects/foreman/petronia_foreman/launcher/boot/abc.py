"""
The base boot launcher class.
"""

from typing import Tuple
from abc import ABC
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from ..abc import AbcLauncherCategory
from ...constants import TRANSLATION_CATALOG


class AbcBootLauncherCategory(AbcLauncherCategory, ABC):
    """The boot launcher categories have extra methods for the boot time,
    because they are not loaded from the extension loader."""

    def get_channel_name(self) -> str:
        """The channel name for this boot launcher.  The name is highly specific
        to the task of the launcher."""
        raise NotImplementedError()

    def start_extension(
            self, launcher_id: str, handler_id: str, extension_name: str,
            extension_version: Tuple[int, int, int], location: str,
    ) -> StdRet[None]:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('Boot launcher {launcher_id} cannot start extensions.'),
            launcher_id=launcher_id,
        )
