"""
Simplified imports for extensions, so you don't need to go probing everywhere
for the right location of things.

The stuff related to bootstrapping extensions
"""

from ...base.bus import (
    EventId,
    EventBus,
    ListenerId,
    EventCallback,
    ListenerSetup,

    TARGET_WILDCARD,
    EVENT_WILDCARD,
)

from ...base.participant import (
    ParticipantId,
    ComponentId,
    SingletonId,

    is_valid_component_identity,
    is_valid_participant_identity,
    is_valid_singleton_identity,

    create_singleton_identity,
)

from ...base.events import (
    # Most of these are bootstrap events, but they can leak out into the
    # extension in some cases.
    # However, those are uncommon (as considered at the current implementation)
    # and so aren't included in this file.
    send_dispose_complete_event,

    RequestDisposeEvent,
    as_request_dispose_listener,

    ParticipantStartedEvent,
    as_participant_started_listener,
    send_participant_started_event,

    TARGET_ID_SYSTEM,

    ErrorEvent,
    send_error_event,
    as_error_listener,
)

from ...base.events.component_events import (
    RequestNewComponentEvent,
    as_request_new_component_listener,
    send_request_new_component,

    ComponentCreatedEvent,
    as_component_created_listener,
    send_component_created_event,

    ComponentCreationFailedEvent,
    as_component_creation_failed_listener,
    send_component_creation_failed_event,
)

from ...base.logging import *

from ...base.validation import *

from ...base.security import (
    SandboxPermission,
    SandboxPermissionCategory,
)

from ...base.util import (
    in_or,
    optional_key,
    optional_list_key,
    readonly_dict,

    T, V, K,
    ValueHolder,

    EMPTY_DICT,
    EMPTY_LIST,
    EMPTY_TUPLE,
    STRING_EMPTY_TUPLE,
)

from ...errors import *

from ...core.state.api import (
    StateStoreUpdatedEvent,
    set_state,
    as_state_change_listener,
)

from ...core.timer.api import (
    TimerEvent,
    as_timer_listener,
    TARGET_TIMER,
)

from .error import report_error
