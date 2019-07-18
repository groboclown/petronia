
"""
Type definitions for the type-safe implementation.

Split out for separate dependency import ordering.
"""

from typing import Callable, Tuple
from .event_bus import EventId
from ..participant import ParticipantId
from ...util.memory import T

TypeSafeEventCallback = Callable[[EventId, ParticipantId, T], None]
ListenerSetup = Tuple[EventId, TypeSafeEventCallback[T]]
ListenerRegistrator = Callable[[TypeSafeEventCallback[T]], ListenerSetup[T]]
