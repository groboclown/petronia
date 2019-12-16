
"""
Send the configuration files to all the necessary parties.
"""

from .contents import ExtensionConfigurationDetails
from ....aid.std import (
    EventBus,
    log, NOTICE, DEBUG, ERROR,
    set_state,
)
from ....aid.std.error import report_user_error
from ....aid.bootstrap import create_singleton_identity
from ....core.config_persistence.api import PersistentConfigurationState
from ....core.extensions.api import send_request_load_extension_event


def send_config(bus: EventBus, config: ExtensionConfigurationDetails) -> None:
    if config.err:
        log(
            NOTICE, send_config,
            'Problem loading {0} {1}: {2}'.format(
                config.source_name, config.name,
                config.err
            )
        )
        report_user_error(
            bus, "default.configuration.file",
            config.err.message, **config.err.arguments
        )
        return
    if config.state_id and config.is_enabled:
        # Note: version information is not used.
        if config.extension_name:
            log(
                DEBUG, send_config,
                "config is sending load extension request for {0} ({1} / {2})",
                config.name, config.extension_name, config.state_id
            )
            send_request_load_extension_event(bus, config.extension_name)

        # Note that the configuration MUST be a PersistType; without it, it
        # requires importing the configuration object.  This cannot be done
        # due to security restraints around the extension.

        set_state(
            bus, create_singleton_identity(config.state_id),
            PersistentConfigurationState,
            PersistentConfigurationState(config.state)  # type: ignore
        )
