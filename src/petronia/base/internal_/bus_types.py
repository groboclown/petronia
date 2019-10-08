
"""
Type definitions for the event bus.
"""

from typing import Callable, Tuple, NewType, Union, Sequence, Generic, Dict
from .identity_types import ParticipantId, ComponentId
from ..util.memory import T

EventId = NewType('EventId', str)
QueuePriority = NewType('QueuePriority', str)
ListenerId = NewType('ListenerId', int)

EventCallback = Callable[[EventId, ParticipantId, T], None]

# TODO figure out the right way to declare these as being generic for PyCharm.
#   Could make this a generic class, but that's a waste of memory for something that
#   has such a short lifecycle.
#   But Python and MyPy is just fine with the generic tuple, so keep it that way for now.
ListenerSetup = Tuple[EventId, EventCallback[T]]
ListenerRegistrar = Callable[[EventCallback[T]], ListenerSetup[T]]

ExtensionVersionStruct = Tuple[Union[int, float], Union[int, float], Union[int, float]]
ExtensionCompatibilityStruct = Dict[str, Union[
    str, ExtensionVersionStruct
]]

# This is very carefully constructed.  Take care modifying this.
# In particular, only one sequence can be contained inside of a
# Union.
ExtensionMetadataStruct = Dict[str, Union[
    str,
    ExtensionVersionStruct,
    ExtensionCompatibilityStruct,
    Sequence[Union[
        str,
        ExtensionCompatibilityStruct
    ]],
]]


class EventBus:
    """
    The EventBus common API.
    """

    def add_listener(
            self,
            target_id: ParticipantId,
            listener_setup: ListenerRegistrar[T],
            listener: EventCallback[T]
    ) -> ListenerId:
        """
        Registers a type-safe event listener.  Cannot work with a wildcard event ID.

        Each event type should have a custom call function to wrap this.
        """
        raise NotImplementedError()

    def remove_listener(self, listener_id: ListenerId) -> bool:
        """De-register the listener."""
        raise NotImplementedError()

    def trigger(self, event_id: EventId, target_id: ParticipantId, event_obj: T) -> None:
        """
        Triggers an event to fire.  The event priority is based upon the
        event id registration.
        """
        raise NotImplementedError()

    def create_component_id(self, component_category: str) -> ComponentId:
        """
        Creates a unique component ID for a new component in the given
        category.

        Due to the coupling between the implementation of the event bus and
        the uniqueness guarantees of the component ID generation, the
        component ID generation is included in the event bus definition.
        """
        raise NotImplementedError()
