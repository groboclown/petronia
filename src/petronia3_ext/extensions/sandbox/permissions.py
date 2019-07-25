
"""
All the allowable permissions that a sandbox can be granted.
By default, none of the permissions are granted.

The permissions are of a
"""

from typing import NewType, Tuple, Union

SandboxPermissionCategory = NewType('SandboxPermissionCategory', str)
SandboxPermission = NewType('SandboxPermission', Tuple[
    SandboxPermissionCategory, Union[str, int]
])

SPCAT_IO_FILE_READ = SandboxPermissionCategory('io-file-read')
SPCAT_IO_FILE_WRITE = SandboxPermissionCategory('io-file-write')
