
"""
Identity Manager.
"""

from ....aid.bootstrap import (
    create_singleton_identity,
)

TARGET_ID_CONSOLE_LOGGER = create_singleton_identity('default.logger.console')
TARGET_ID_CONSOLE_LOGGER_STATE = create_singleton_identity('default.logger.console/state')
TARGET_ID_CONSOLE_LOGGER_CONFIG = create_singleton_identity('default.logger.console/config')
