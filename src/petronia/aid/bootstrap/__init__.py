
"""
Common Petronia imports for bootstrap parts of an extension.

This should be imported along with the `simp` module.
"""


from ...base.bus import (
    EventBus,

    ListenerRegistrar,
    ListenerSetup,
    QueuePriority,
    ExtensionMetadataStruct,

    register_event,
    EVENT_WILDCARD,
    TARGET_WILDCARD,

    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_HIGH,
    QUEUE_EVENT_IO,
    QUEUE_EVENT_TYPES
)

from ...base.participant import (
    create_singleton_identity,

    NOT_PARTICIPANT,
)

from ...base.events import (
    # These are generally just bootstrap events.
    DisposeCompleteEvent,
    as_dispose_complete_listener,

    RequestDisposeEvent,
    as_request_dispose_listener,

    SystemStartedEvent,
    as_system_started_listener,
)
from ...base.events.bus import (
    EventProtectionModel,
    GLOBAL_EVENT_PROTECTION,
    INTERNAL_EVENT_PROTECTION,
    PRODUCE_EVENT_PROTECTION,
    CONSUME_EVENT_PROTECTION,
    REQUEST_EVENT_PROTECTION,
    RESPONSE_EVENT_PROTECTION,
)

from ...core.extensions.api import ANY_VERSION

from ...core.shutdown.api import (
    SystemShutdownEvent,
    as_system_shutdown_listener,

    SystemShutdownFinalizeEvent,
    as_system_shutdown_finalize_listener,

    TARGET_ID_SYSTEM_SHUTDOWN,
)
