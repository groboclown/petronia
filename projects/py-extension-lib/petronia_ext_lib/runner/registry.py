"""
An extension event listener registry.  This is a higher-level
system than the raw event stream.
"""
from abc import ABC
from typing import Dict, Callable, Generic, Protocol, Optional, Union, Any
from petronia_common.event_stream import RawBinaryReader
from petronia_common.util import StdRet, T


class EventObject(Protocol):
    """Protocol for all generated event objects."""
    @property
    def fully_qualified_event_name(self) -> str:
        """Get the full event name that this object encapsulates."""
        raise NotImplementedError  # pragma no cover

    def export_data(self) -> Dict[str, Any]:
        """Export the event object into a JSON-like structure for creating a raw event object."""
        raise NotImplementedError  # pragma no cover


class EventObjectParser(Generic[T]):
    """Extracts event objects.  Technically, should not be an object, but due to generics,
    it works best if wrapped by a simple object.  Generally, this is just wrapping the static
    parse function on the generated event object."""
    __slots__ = ('_parser',)

    def __init__(self, parser: Callable[[Dict[str, Any]], StdRet[T]]) -> None:
        self._parser = parser

    def parse(self, event: Dict[str, Any]) -> StdRet[T]:
        """Parse the event object."""
        return self._parser(event)


class EventObjectTarget(Generic[T]):
    """Handles the event object."""
    __slots__ = ()

    def on_close(self) -> None:
        """Called when the extension is terminated.  Does nothing by default."""

    def on_event(self, source: str, target: str, event: T) -> bool:
        """Called when the event is received and parsed.  Return True if
        the target should be removed from future event listening, False if
        it should continue listening."""
        raise NotImplementedError  # pragma no cover


class EventBinaryTarget:
    """Handles the event object."""
    __slots__ = ()

    def on_close(self) -> None:
        """Called when the extension is terminated.  Does nothing by default."""

    def on_event(self, source: str, target: str, size: int, reader: RawBinaryReader) -> bool:
        """Called when the event is received and parsed.  Return True if
        the target should be removed from future event listening, False if
        it should continue listening."""
        raise NotImplementedError  # pragma no cover


class EventRegistryContext:
    """An interface for registering and sending events."""

    def register_event_parser(
            self,
            event_id: str,
            parser: Callable[[Dict[str, Any]], StdRet[T]],
    ) -> StdRet[None]:
        """Register the parser function."""
        return self.register_event(event_id, EventObjectParser(parser))

    def register_event(self, event_id: str, parser: EventObjectParser) -> StdRet[None]:
        """Registers a new parser for the event."""
        raise NotImplementedError  # pragma no cover

    def register_target(  # pylint:disable=too-many-arguments
            self,
            event_id: str,
            target_id: Optional[str],
            target: EventObjectTarget[T],
            source_id: Optional[str] = None,
            timeout: float = -1.0,
    ) -> StdRet[None]:
        """Register a new event target."""
        raise NotImplementedError  # pragma no cover

    def register_binary_target(  # pylint:disable=too-many-arguments
            self,
            event_id: str,
            target_id: Optional[str],
            target: EventBinaryTarget,
            source_id: Optional[str] = None,
            timeout: float = -1.0,
    ) -> StdRet[None]:
        """Register a new binary event target.

        The target_id can be None for cases like setting the background image for a single
        window."""
        raise NotImplementedError  # pragma no cover

    def register_eof_target(self, callback: Callable[[], None]) -> StdRet[None]:
        """Register a new target that is called on EOF."""
        raise NotImplementedError  # pragma no cover

    def send_event(self, source_id: str, target_id: str, event: EventObject) -> StdRet[None]:
        """Send the event object safely."""
        raise NotImplementedError  # pragma no cover

    def send_binary_event(
            self, source_id: str, target_id: str, event_id: str, data: Union[bytes, bytearray],
    ) -> StdRet[None]:
        """Send the binary event safely."""
        raise NotImplementedError  # pragma no cover


class ContextEventObjectTarget(EventObjectTarget[T], ABC):
    """Handles the event object while being context aware."""
    __slots__ = ('__context',)

    def __init__(self, context: EventRegistryContext) -> None:
        self.__context: Optional[EventRegistryContext] = context

    def on_close(self) -> None:
        self.__context = None

    def on_event(self, source: str, target: str, event: T) -> bool:
        context = self.__context
        if not context:
            # Closed, so do not handle this event anymore.
            return True
        return self.on_context_event(context, source, target, event)

    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: T,
    ) -> bool:
        """Called when the event is received and the target is not closed."""
        raise NotImplementedError

    @property
    def get_context(self) -> Optional[EventRegistryContext]:
        """Get the context; None if closed."""
        return self.__context
