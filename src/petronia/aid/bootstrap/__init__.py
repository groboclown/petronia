
"""
Common Petronia imports for bootstrap parts of an extension.

This should be imported along with the `simp` module.
"""


from ...base.bus import (
    ListenerRegistrator,
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

    ParticipantStartedEvent,
    as_participant_started_listener,
    send_participant_started_event,
)

from ...core.extensions.api import ANY_VERSION

from ...core.shutdown.api import (
    SystemShutdownEvent,
    as_system_shutdown_listener,

    SystemShutdownFinalizeEvent,
    as_system_shutdown_finalize_listener,
)
