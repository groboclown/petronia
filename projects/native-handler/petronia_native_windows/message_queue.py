"""A custom queue-like structure for passing messages to the message loop."""

from typing import List, Tuple, Dict, Callable, Optional, Any
import time
import threading
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from petronia_native.common import user_messages
from . import hook_messages
from .arch.native_funcs import windows_common
from .message_loop import WindowsMessageLoop


class UserMessageQueue:
    """A custom queue-like structure for sending messages into the message loop, and handling
    them.

    Messages are associated with an ID that is passed in as the WPARAM.  Messages are removed
    when the loop receives them."""

    __slots__ = (
        '__queued_messages', '__handlers', '__loop', '__message_id', '__lock', '__next_index',
    )

    def __init__(self, loop: WindowsMessageLoop, custom_user_message: int) -> None:
        self.__lock = threading.Lock()
        self.__next_index = 0
        self.__queued_messages: Dict[int, Tuple[float, Any]] = {}
        self.__handlers: Dict[int, Callable[[Any], None]] = {}
        self.__loop = loop
        self.__message_id = custom_user_message
        loop.add_message_handler(
            hook_messages.custom_user_message(custom_user_message, self.message_loop_callback),
        )

    def cleanup_messages(self, timeout: float) -> int:
        """Removes messages that are older than `timeout` seconds.  This may take a while,
        so it may block the message handling.

        Returns the number of messages removed."""

        remove: List[int] = []
        expired_at = time.time() - timeout

        with self.__lock:
            for key, message in self.__queued_messages.items():
                if message[0] > expired_at:
                    remove.append(key)
            for key in remove:
                del self.__queued_messages[key]

        return len(remove)

    def add_handler(self, handler_id: int, callback: Callable[[Any], None]) -> StdRet[None]:
        """Add a handler callback.  Only one handler can be registered to an ID at a time."""
        with self.__lock:
            if handler_id in self.__handlers:
                return StdRet.pass_errmsg(
                    user_messages.TRANSLATION_CATALOG,
                    _('handler id {handler_id} already registered'),
                    handler_id=handler_id,
                )
            self.__handlers[handler_id] = callback
        return RET_OK_NONE

    def remove_handler(self, handler_id: int) -> None:
        """Remove the registered handler.  If it's not registered,
        this does not report an issue."""
        with self.__lock:
            if handler_id in self.__handlers:
                del self.__handlers[handler_id]

    def queue_message(self, handler_id: int, message: Any) -> StdRet[None]:
        """Send a message to the message loop.  If the loop has stopped, this won't be delivered."""
        message_entry: Tuple[float, Any] = (time.time(), message)
        handler_lparam = windows_common.LPARAM(handler_id)
        with self.__lock:
            if handler_id not in self.__handlers:
                return StdRet.pass_errmsg(
                    user_messages.TRANSLATION_CATALOG,
                    _('no such handler id {handler_id}'),
                    handler_id=handler_id,
                )
            this_index = self.__next_index
            wparam = windows_common.WPARAM(self.__next_index)
            self.__next_index += 1
            self.__queued_messages[this_index] = message_entry
        return self.__loop.send_custom_message_to_self(self.__message_id, wparam, handler_lparam)

    def message_loop_callback(
            self, wparam: windows_common.WPARAM, lparam: windows_common.LPARAM,
    ) -> None:
        """Callback used as the parameter for the custom_user_message call."""
        handler: Optional[Callable[[Any], None]] = None
        message_id = wparam.value
        handle_id = lparam.value

        with self.__lock:
            message = self.__queued_messages.get(message_id)
            if message:
                del self.__queued_messages[message_id]
                handler = self.__handlers.get(handle_id)

        if not message:
            # FIXME make this a real boy
            print(
                f'custom message {self.__message_id} called with unknown queue entry {message_id}'
            )
            return
        if not handler:
            # FIXME make this a real boy
            print(f'custom message handler {handle_id} not registered')
            return

        handler(message[1])
