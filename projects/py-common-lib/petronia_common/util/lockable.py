"""Simple wrappers for lockable types."""

from typing import Type, Protocol, Optional
from types import TracebackType


class Lockable(Protocol):
    """Base class for all lockable types.."""
    def __enter__(self) -> None:
        pass

    def __exit__(
            self, __exc_type: Optional[Type[BaseException]], __exc_value: Optional[BaseException],
            __traceback: Optional[TracebackType]
    ) -> Optional[bool]:
        pass


class NoopLockable:
    """Acts like a lock."""
    def __enter__(self) -> None:
        pass

    def __exit__(
            self, __exc_type: Optional[Type[BaseException]], __exc_value: Optional[BaseException],
            __traceback: Optional[TracebackType]
    ) -> Optional[bool]:
        pass
