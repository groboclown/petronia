"""
Windows Native Launcher.
"""
from typing import Sequence, Mapping, List
import platform
from petronia_common.util import StdRet, RET_OK_NONE
from .abc import AbcBootLauncherCategory
from ..abc import RuntimeContext, AbcLauncherCategory
from ...constants import NATIVE_CHANNEL


def create_windows_native_launcher(options: Mapping[str, str]) -> AbcLauncherCategory:
    """Factory for the launcher."""
    return WindowsNativeLauncher(options)


class WindowsNativeLauncher(AbcBootLauncherCategory):
    """Native launcher for Windows."""

    def get_channel_name(self) -> str:
        return NATIVE_CHANNEL

    def is_valid(self) -> StdRet[None]:
        return StdRet.pass_ok(platform.system() == 'Windows')

    def initialize(self, context: RuntimeContext) -> StdRet[None]:
        return RET_OK_NONE

    def start_launcher(self, launcher_id: str, permissions: Mapping[str, List[str]]) -> StdRet[None]:
        print(f"TODO start native launcher {launcher_id}")
        return RET_OK_NONE

    def get_active_launcher_ids(self) -> Sequence[str]:
        return []

    def stop_launcher(self, launcher_id: str) -> StdRet[None]:
        return RET_OK_NONE

    def stop(self) -> StdRet[None]:
        return RET_OK_NONE
