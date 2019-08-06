
"""
List of directories that the preboot API must provide.
"""

from typing import Iterable, Tuple, Optional
from ....base.security import SandboxPermission
from ....base.util import (
    STRING_EMPTY_TUPLE,
    EMPTY_TUPLE,
)

SandboxPath = Tuple[str, Iterable[SandboxPermission]]

class ExtensionPaths:
    """
    Definition of where to load extensions.  This is static at boot time, and
    cannot be changed later.
    """
    __slots__ = (
        'secure_paths',
        'sandbox_paths',
        'secure_zip_dirs',
        'sandbox_zip_dirs',
    )

    secure_paths: Iterable[str]
    sandbox_paths: Iterable[SandboxPath]
    secure_zip_dirs: Iterable[str]
    sandbox_zip_dirs: Iterable[SandboxPath]

    def __init__(
            self,
            secure_paths: Optional[Iterable[str]] = None,
            sandbox_paths: Optional[Iterable[SandboxPath]] = None,
            secure_zip_dirs: Optional[Iterable[str]] = None,
            sandbox_zip_dirs: Optional[Iterable[SandboxPath]] = None
    ):
        self.secure_paths = secure_paths or STRING_EMPTY_TUPLE
        self.sandbox_paths = sandbox_paths or EMPTY_TUPLE # type: ignore
        self.secure_zip_dirs = secure_zip_dirs or STRING_EMPTY_TUPLE
        self.sandbox_zip_dirs = sandbox_zip_dirs or EMPTY_TUPLE # type: ignore
