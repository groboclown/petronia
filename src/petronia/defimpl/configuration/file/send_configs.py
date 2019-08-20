
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
from ....core.extensions.api import send_request_load_extension_event

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
    if config.state_id and config.is_enabled:
        # Note: version information is not used.
        send_request_load_extension_event(bus, config.name)

        # Note that the configuration MUST be a PersistType; without it, it
        # requires importing the configuration object.  This cannot be done
        # due to security restraints around the extension.

        set_state(bus, create_singleton_identity(config.state_id), PersistType, config.state)
