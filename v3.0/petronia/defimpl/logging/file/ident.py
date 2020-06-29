
"""
Identity Manager.
"""

from ....aid.bootstrap import (
    create_singleton_identity,
)

TARGET_ID_FILE_LOGGER = create_singleton_identity('default.logging.file')
STATE_ID_FILE_LOGGER = create_singleton_identity('default.logging.file/state')
CONFIG_ID_FILE_LOGGER = create_singleton_identity('default.logging.file/setup-configuration')
