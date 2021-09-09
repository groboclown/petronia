
"""
Global functions for accessing the currently installed security implementation.
"""

from .file_signature import is_file_signature_validation_available
from .memory_crypto import is_memory_crypto_available
from .permissions import (
    SandboxPermissionCategory,
    SandboxPermission,

    SPCAT_IO_FILE_READ,
    SPCAT_IO_FILE_WRITE,
)