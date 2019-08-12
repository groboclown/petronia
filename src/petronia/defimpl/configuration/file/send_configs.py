
"""
Send the configuration files to all the necessary parties.
"""

from .contents import ExtensionConfigurationDetails
from ....aid.simp import (
    EventBus,
    log, NOTICE,
    set_state,
)
from ....aid.bootstrap import create_singleton_identity
from ....core.config_persistence.api import PersistType


def send_config(bus: EventBus, config: ExtensionConfigurationDetails) -> None:
    if config.is_error():
        log(
            NOTICE, send_config,
            'Problem loading {0} {1}: {2}'.format(
                config.source_name, config.name,
                config.err
            )
        )

        # FIXME do something smart.
        # Send a platform Notification?
        return
    if config.state_id:
        set_state(bus, create_singleton_identity(config.state_id), PersistType, config.state)
