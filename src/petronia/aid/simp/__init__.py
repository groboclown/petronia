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
)

from ...base.participant import (
    ParticipantId,
    ComponentId,
    SingletonId,

    is_valid_component_identity,
    is_valid_participant_identity,
    is_valid_singleton_identity,
)

from ...base.events import (
    # Most of these are bootstrap events, but they can leak out into the
    # extension in some cases.
    # However, those are uncommon (as considered at the current implementation)
    # and so aren't included in this file.
    send_dispose_complete_event,

    RequestDisposeEvent,
    as_request_dispose_listener,
)

from ...base.events.component_events import (
    RequestNewComponentEvent,
    as_request_new_component_listener,
    send_request_new_component,

    ComponentCreatedEvent,
    as_component_created_listener,
    send_component_created_event,
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

    T, V, K,
    ValueHolder,

    EMPTY_DICT,
    EMPTY_LIST,
    EMPTY_TUPLE,
    STRING_EMPTY_TUPLE,
)

from ...errors import *
