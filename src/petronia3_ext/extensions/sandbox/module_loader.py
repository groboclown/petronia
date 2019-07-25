
"""
Module loader implementations that run a module in a sandbox environment.
"""

from typing import Sequence
from petronia3.system.bus import EventBus
from .permissions import SandboxPermission
from ..defs import ModuleLoader

def create_sandbox_module_loader(
        paths: Sequence[str],
        permissions: Sequence[SandboxPermission]
) -> ModuleLoader:
    """
    Create a sandbox loader that runs in its own protected space, using
    the current python path + the given paths, which may be local directories
    or zip files.
    """
    def loader(bus: EventBus) -> None:
        raise NotImplementedError()

    return loader
