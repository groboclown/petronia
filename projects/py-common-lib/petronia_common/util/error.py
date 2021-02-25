
"""
General error handling in Petronia.  Returned errors are preferred over exceptions.

These errors are used by the validation framework, so the assertions done
here are the only exception to the assertion rules.
"""

# Future: Figure out a better way than using Any here...
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

from __future__ import annotations
from typing import (
    Sequence, Iterable, List, Callable, Union, Optional, Generic, Any, cast, TYPE_CHECKING,
)
import collections
import collections.abc
from .memory import T, T_co, V, EMPTY_TUPLE
from .message import (
    I18n, UserMessage, UserMessageData,
)

# These typing functions are in Python 3.8, but MyPy doesn't recognize them.
if TYPE_CHECKING:  # pragma: no cover
    from typing_extensions import Final, final
else:
    from typing import Final, final  # pylint: disable=ungrouped-imports


class PetroniaReturnError:
    """
    A marker for a recoverable Petronia error.  Sometimes, these can
    extend exception types.
    """
    def messages(self) -> Sequence[UserMessage]:
        """Error messages associated with this error.  There MUST be at least one."""
        raise NotImplementedError()  # pragma: no cover


class SimplePetroniaReturnError(PetroniaReturnError):
    """Just a message."""
    __slots__ = ('__messages',)

    def __init__(self, *messages: UserMessage) -> None:
        self.__messages = tuple(messages)

    def messages(self) -> Sequence[UserMessage]:
        return self.__messages

    def __repr__(self) -> str:
        return f'SimplePetroniaReturnError({", ".join([repr(msg) for msg in self.__messages])})'


class ExceptionPetroniaReturnError(PetroniaReturnError):
    """An error that came from a trapped exception.
    This is used to encapsulate third party library exceptions."""
    __slots__ = ('__messages', '__exception')

    def __init__(self, message: UserMessage, exception: BaseException) -> None:
        self.__messages = (message,)
        self.__exception = exception

    def messages(self) -> Sequence[UserMessage]:
        return self.__messages

    def exception(self) -> BaseException:
        """Exception that caused this error."""
        return self.__exception

    def __repr__(self) -> str:
        return f'ExceptionPetroniaReturnError({repr(self.__messages[0])}, {repr(self.__exception)})'


class StdRet(Generic[T_co]):
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
            value: Optional[T_co],
    ) -> None:
        self.__error: Final[Optional[PetroniaReturnError]] = error
        self.__value: Final[Optional[T_co]] = value

    @staticmethod
    def pass_error(
            *errors: PetroniaReturnError,
    ) -> StdRet[T_co]:
        """Constructor that generates a forced error with no value."""
        return StdRet(join_errors(errors=errors), None)

    @staticmethod
    def pass_errmsg(
            catalog: str,
            message: I18n,
            **arguments: UserMessageData,
    ) -> StdRet[T_co]:
        """Constructor that generates a forced error with no value."""
        return StdRet(error_message(catalog, message, **arguments), None)

    @staticmethod
    def pass_exception(
            catalog: str,
            cause: I18n,
            exception: BaseException,
            **details: UserMessageData,
    ) -> StdRet[T_co]:
        """Constructor that generates a forced error with no value.
        The 'cause' text can include an {exception} expression for
        replacement with the error itself."""
        return StdRet(ExceptionPetroniaReturnError(
            UserMessage(catalog, cause, **details, exception=exception),
            exception,
        ), None)

    @staticmethod
    def pass_ok(ret: T) -> StdRet[T]:
        """Constructor that generates a forced value with no error."""
        return StdRet(None, ret)

    @property
    @final
    def ok(self) -> bool:  # pylint: disable=C0103
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
    def value(self) -> Optional[T_co]:
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
    def result(self) -> T_co:
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
        catalog: str,
        message: I18n,
        **arguments: UserMessageData,
) -> PetroniaReturnError:
    """Returns an error object with a single message."""
    return SimplePetroniaReturnError(UserMessage(catalog, message, **arguments))


def join_errors(
        *messages: UserMessage,
        errors: Optional[Iterable[PetroniaReturnError]] = None,
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
    """Creates an optional message, based on whether any errors were passed in.
    If errors are passed in without messages, an error will still be generated.
    """
    msgs: List[UserMessage] = []
    has_messages = False
    if messages:
        msgs.extend(messages)
        has_messages = True
    if errors:
        for error in errors:
            msgs.extend(error.messages())
        has_messages = True
    # Allow for errors without messages.
    if not has_messages:
        return None
    return SimplePetroniaReturnError(*msgs)


ValidationType = Union[StdRet[Any], Callable[[], StdRet[Any]]]


def collect_errors_from(
        *values: Union[ValidationType, Iterable[ValidationType]],
) -> Optional[PetroniaReturnError]:
    """Collects the return objects, and if there are any errors or messages,
    including errors without messages, then an error object is returned.
    Otherwise, a None is returned."""
    messages: List[UserMessage] = []
    # value: ValidationType
    for validation_value in values:
        if isinstance(validation_value, collections.abc.Iterable):
            for value1 in validation_value:
                if callable(value1):
                    value1 = value1()
                assert isinstance(value1, StdRet)
                if value1.has_error:
                    messages.extend(value1.valid_error.messages())
        else:
            value2 = validation_value
            if callable(value2):
                value2 = value2()
            assert isinstance(value2, StdRet)
            if value2.has_error:
                messages.extend(value2.valid_error.messages())
    return possible_error(messages)


def join_results(
        joiner: Callable[[List[T]], V],
        *values: StdRet[T],
) -> StdRet[V]:
    """Use a separate joining function to collect the results into an output value.
    If any error is encountered, then an error is returned and the joining function is
    not called."""
    valid: List[T] = []
    errors: List[PetroniaReturnError] = []
    for value in values:
        if value.has_error:
            errors.append(value.valid_error)
        else:
            # T might be None, so we don't want null checking
            valid.append(value.value)  # type: ignore
    if errors:
        return StdRet.pass_error(join_errors(errors=errors))
    return StdRet.pass_ok(joiner(valid))


# A generic constant for return types that may have an error
# but no real return value.
RET_OK_NONE = StdRet.pass_ok(None)

# A generic constant for boolean return types.
RET_OK_TRUE = StdRet.pass_ok(True)
RET_OK_FALSE = StdRet.pass_ok(False)
