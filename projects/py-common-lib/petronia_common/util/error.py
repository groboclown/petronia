
"""
General error handling in Petronia.  Returned errors are preferred over exceptions.
"""

from __future__ import annotations
from typing import Sequence, Iterable, List, Optional, Generic, cast, TYPE_CHECKING
# These typing functions are in Python 3.8, but MyPy doesn't recognize them.
if TYPE_CHECKING:  # pragma: no cover
    from typing_extensions import Final, final
else:
    from typing import Final, final
from .memory import T, V, EMPTY_TUPLE
from .message import I18n, UserMessage, UserMessageData


class PetroniaReturnError:
    """
    A marker for a recoverable Petronia error.  Sometimes, these can
    extend exception types.
    """
    def messages(self) -> Sequence[UserMessage]:
        """Error messages associated with this error.  There MUST be at least one."""
        raise NotImplementedError()


class SimplePetroniaReturnError(PetroniaReturnError):
    """Just a message."""
    __slots__ = ('__messages',)

    def __init__(self, *messages: UserMessage) -> None:
        self.__messages = tuple(messages)

    def messages(self) -> Sequence[UserMessage]:
        return self.__messages

    def __repr__(self) -> str:
        return f'SimplePetroniaReturnError({", ".join([repr(msg) for msg in self.__messages])})'


class StdRet(Generic[T]):
    """
    StdRet the standard return type.  It could be a standard Tuple type, but
    this runs into typing issues (alias of generics has lots of bugs in different
    systems), but also forces the user of the returned value to write a bunch of
    boilerplate.

    Note that it's possible to return an error AND a value.  There are valid use
    cases where this can simplify code.

    The helper constructors can enforce different rules.
    """
    __slots__ = ('__error', '__value',)

    def __init__(
            self,
            error: Optional[PetroniaReturnError],
            value: Optional[T],
    ) -> None:
        self.__error: Final[Optional[PetroniaReturnError]] = error
        self.__value: Final[Optional[T]] = value

    @staticmethod
    def pass_error(
            *errors: PetroniaReturnError,
    ) -> StdRet[T]:
        """Constructor that generates a forced error with no value."""
        return StdRet(join_errors(errors=errors), None)

    @staticmethod
    def pass_errmsg(
            message: I18n,
            **arguments: UserMessageData,
    ) -> StdRet[T]:
        """Constructor that generates a forced error with no value."""
        return StdRet(error_message(message, **arguments), None)

    @staticmethod
    def pass_ok(ret: T) -> StdRet[T]:
        """Constructor that generates a forced value with no error."""
        return StdRet(None, ret)

    @property
    @final
    def ok(self) -> bool:
        """Checks whether an error exists, and returns True if there is
        no error.  Note that the value can be None as well as no
        error."""
        return self.__error is None

    @property
    @final
    def has_error(self) -> bool:
        """Returns whether an error exists in this return.  The
        presence of an error does not preclude the existence of a
        value; that is, even if there is an error, the value
        can be non-None."""
        return self.__error is not None

    @property
    @final
    def error(self) -> Optional[PetroniaReturnError]:
        """Return the error, which can be None."""
        return self.__error

    @property
    @final
    def value(self) -> Optional[T]:
        """Return the value.  This can be non-None and the error can be present."""
        return self.__value

    @property
    @final
    def not_none(self) -> bool:
        """Check if the value is non-None."""
        return self.__value is not None

    @final
    def forward(self) -> StdRet[V]:
        """Forward this error as another type.  It doesn't allocate a
        new value.  This can ONLY be used if the value is known to be None."""
        assert self.__value is None
        return cast(StdRet[V], self)

    @property
    @final
    def valid_error(self) -> PetroniaReturnError:
        """Return a non-null version of the error.  Only call if you know it to
        be non-null."""
        assert self.__error
        return self.__error

    @property
    @final
    def result(self) -> T:
        """The non-None version of the value.  If the type itself is optional,
        this will still fail if the value is not None, but the returned type will
        still be Optional."""
        assert self.__value is not None
        return self.__value

    @final
    def error_messages(self) -> Sequence[UserMessage]:
        """Returns a list of error messages associated with the error, or
        an empty list if there is no error.  This is valid to call in any
        circumstance."""
        if self.__error:
            return self.__error.messages()
        return cast(Sequence[UserMessage], EMPTY_TUPLE)


def error_message(
        message: I18n,
        **arguments: UserMessageData,
) -> PetroniaReturnError:
    """Returns an error object with a single message."""
    return SimplePetroniaReturnError(UserMessage(message, **arguments))


def join_errors(
        *messages: UserMessage,
        errors: Optional[Iterable[PetroniaReturnError]] = None
) -> PetroniaReturnError:
    """Return a collection of messages and/or errors, and return a single error representation."""
    msgs = [*messages]
    if errors:
        for error in errors:
            msgs.extend(error.messages())
    return SimplePetroniaReturnError(*msgs)


def possible_error(
        messages: Optional[Iterable[UserMessage]] = None,
        errors: Optional[Iterable[PetroniaReturnError]] = None,
) -> Optional[PetroniaReturnError]:
    """Creates an optional message, based on whether any errors were passed in."""
    msgs: List[UserMessage] = []
    if messages:
        msgs.extend(messages)
    if errors:
        for error in errors:
            msgs.extend(error.messages())
    if not msgs:
        return None
    return SimplePetroniaReturnError(*msgs)