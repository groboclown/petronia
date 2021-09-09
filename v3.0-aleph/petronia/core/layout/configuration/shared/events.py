

from petronia.aid.std import (
    EventId,
    create_singleton_identity,
)


TARGET_LAYOUT_CONFIGURATION = create_singleton_identity('core.layout.configuration.api/global')


EVENT_ID_REQUEST_RELOAD_CONFIGURATION = EventId('core.layout.configuration.api/request-reload-config')


# FIXME COMPLETE
