"""Windows Error Message handling"""

from typing import Sequence, Optional
import ctypes
import ctypes.wintypes
from petronia_common.util import StdRet, PetroniaReturnError, UserMessage, T, RET_OK_NONE
from petronia_common.util import i18n as _
from petronia_native.common import user_messages


FORMAT_MESSAGE_ALLOCATE_BUFFER = 0x00000100
FORMAT_MESSAGE_FROM_SYSTEM = 0x00001000
FORMAT_MESSAGE_IGNORE_INSERTS = 0x00000200

LANG_NEUTRAL = 0
SUBLANG_NEUTRAL = 0
SUBLANG_DEFAULT = 1

# See https://docs.microsoft.com/en-us/windows/win32/intl/language-identifiers
# macro MAKELANGID(int p, int s) == (s << 10) | p

LANGID_NEUTRAL_DEFAULT = (LANG_NEUTRAL << 10) | SUBLANG_DEFAULT


MAX_ERROR_LENGTH = 128 * 1024


class WindowsReturnError(PetroniaReturnError):
    """Common windows error message."""
    __slots__ = (
        '__called',
        '__errno', '__errmsg',
        '__msgs',
    )

    def __init__(self, called_function: str, last_error: Optional[int] = None):
        self.__called = called_function
        if last_error is None:
            self.__errno = ctypes.GetLastError()
        else:
            self.__errno = last_error

        buff = ctypes.create_unicode_buffer(MAX_ERROR_LENGTH + 1)
        char_count = ctypes.windll.kernel32.FormatMessageW(
            FORMAT_MESSAGE_FROM_SYSTEM |
            FORMAT_MESSAGE_IGNORE_INSERTS,
            None,
            self.__errno,
            LANGID_NEUTRAL_DEFAULT,  # MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT)
            ctypes.byref(buff),
            MAX_ERROR_LENGTH, None,
        )
        if char_count == 0:
            # format message failed.
            self.__msgs = (UserMessage(
                user_messages.TRANSLATION_CATALOG,
                _('{called}: caused unknown error {errno} (caused by {newerr})'),
                called=called_function,
                errno=self.__errno,
                newerr=ctypes.GetLastError(),
            ),)
        else:
            self.__msgs = (UserMessage(
                user_messages.TRANSLATION_CATALOG,
                _('{called}: caused {err} ({errno})'),
                called=called_function,
                err=buff.value,
            ),)

    @staticmethod
    def stdret(called_function: str, last_error: Optional[int] = None) -> StdRet[T]:
        """Create a StdRet error for a windows function call that failed."""
        return StdRet.pass_error(WindowsReturnError(called_function, last_error))

    @staticmethod
    def checked_stdret(called_function: str, result: int) -> StdRet[None]:
        """For StdRet[None] return types, this is used as a simple check for errors."""
        if result == 0:
            return StdRet.pass_error(WindowsReturnError(called_function))
        return RET_OK_NONE

    @property
    def errno(self) -> int:
        """The windows error code."""
        return self.__errno

    @property
    def called_function(self) -> str:
        """What the function called was named."""
        return self.__called

    def messages(self) -> Sequence[UserMessage]:
        return self.__msgs

    def __repr__(self) -> str:
        return 'WindowsErrorMessage(called={0}, errno={1})'.format(
            repr(self.__called),
            repr(self.__errno)
        )
