
"""
Identity Manager.
"""

from ....aid.bootstrap import (
    create_singleton_identity,
)

TARGET_ID_FILE_LOGGER = create_singleton_identity('default.logger.file')
TARGET_ID_FILE_LOGGER_STATE = create_singleton_identity('default.logger.file/state')
TARGET_ID_FILE_LOGGER_CONFIG = create_singleton_identity('default.logger.file/config')
TARGET_ID_FILE_LOGGER_USER_CONFIG = create_singleton_identity('default.logger.file/setup-configuration')
