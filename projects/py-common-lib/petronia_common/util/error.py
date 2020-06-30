
from typing import Generic, Tuple, Sequence, Iterable, List, Optional
from .memory import T
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


def as_error(*messages: UserMessage, errors: Iterable[PetroniaReturnError] = None) -> PetroniaReturnError:
    """Return a collection of messages and/or errors, and return a single error representation."""
    msgs = [*messages]
    if errors:
        for error in errors:
            msgs.extend(error.messages())
    return SimplePetroniaReturnError(*msgs)


def possible_error(
        messages: Iterable[UserMessage] = None, errors: Iterable[PetroniaReturnError] = None,
) -> Optional[PetroniaReturnError]:
    msgs: List[UserMessage] = []
    if messages:
        msgs.extend(messages)
    if errors:
        for error in errors:
            msgs.extend(error.messages())
    if not msgs:
        return None
    return SimplePetroniaReturnError(*msgs)


class StdRet(Generic[T]):
    """
    A return value that contains an optional error.
    This is a type-safe way to return an error value.
    """
    __slots__ = ('__value', '__error',)

    def __init__(
            self,
            value: Optional[T] = None,
            error: Optional[PetroniaReturnError] = None,
    ) -> None:
        # value can be None, so a valid use case is all arguments are None.
        assert (not error) or (error and not value)
        # ensure that errors have at least one message.
        assert not error or len(error.messages()) > 0
        self.__value = value
        self.__error = error

    def items(self) -> Tuple[Optional[T], Optional[PetroniaReturnError]]:
        """
        :return: a tuple of the values.
        """
        return self.__value, self.__error

    def __bool__(self) -> bool:
        """
        :return: False if there was an error, otherwise True.
        """
        return self.__error is not None

    @property
    def success(self) -> bool:
        return self.__error is not None

    @property
    def value(self) -> Optional[T]:
        return self.__value

    @property
    def error(self) -> Optional[PetroniaReturnError]:
        return self.__error

    def as_error(self) -> PetroniaReturnError:
        """If the code has ensured that this is indeed an error condition, then this
        method will return the error as non-None.  If the check wasn't performed
        correctly in the caller's code, then this will raise a runtime error."""
        assert self.__error is not None
        return self.__error


def with_message(
        message: I18n,
        **arguments: UserMessageData,
) -> StdRet[T]:
    """Create an error return type for an error condition."""
    return StdRet(error=as_error(UserMessage(message, **arguments)))


def with_errors(first_error: PetroniaReturnError, *other_errors: PetroniaReturnError) -> StdRet[T]:
    """Create an error return type for an error condition."""
    return StdRet(error=as_error(errors=[first_error, *other_errors]))


def no_error(value: T) -> StdRet[T]:
    """Create an error return type for a normal result."""
    return StdRet(value=value)
