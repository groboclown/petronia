
"""
Configuration related events.

The configuration sub-system provides a few extra events on top of the state
storage mechanisms.
"""

from ....system.participant import ParticipantId
from ....system.bus import (
    EventId, EventBus, EventCallback, ListenerSetup,
)

# User-generated event to trigger writing the configuration to disk, for the
# parts that are setup to permit writing the current state.
EVENT_ID_PERSIST_CONFIGURATION = EventId('core.config_persistence.api persist')


class PersistConfigurationEvent:
    """
    A signal to persist a single configuration piece.  Only those write-enabled
    participants need to listen to this, and those that write a complete unit of
    configuration (for example, a configuration file or a registry sub-tree),
    which are called by this system "configuration collection".
    """
    __slots__ = ('__initiator',)

    def __init__(self, initiator: ParticipantId) -> None:
        self.__initiator = initiator

    @property
    def initiator(self) -> ParticipantId:
        """The participant that requested the persistence."""
        return self.__initiator

def as_persist_configuration_listener(
        callback: EventCallback[PersistConfigurationEvent]
) -> ListenerSetup[PersistConfigurationEvent]:
    return (EVENT_ID_PERSIST_CONFIGURATION, callback,)

def send_persist_configuration(
        bus: EventBus,
        target_id: ParticipantId,
        initiator_id: ParticipantId
) -> None:
    bus.trigger(
        EVENT_ID_PERSIST_CONFIGURATION,
        target_id,
        PersistConfigurationEvent(initiator_id)
    )
