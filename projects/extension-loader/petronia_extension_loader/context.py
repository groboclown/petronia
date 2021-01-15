"""Runtime Context."""

from typing import Iterable, List
import threading
from petronia_common.event_stream import EventForwarder, EventForwarderTarget, BinaryWriter
from petronia_common.event_stream.thread_writer import ThreadSafeEventWriter
from petronia_common.util import StdRet, UserMessage, join_errors, RET_OK_NONE
from .order import LoadList, add_pending_extensions
from .defs import ExtensionInfo


class EventHandlerContext:
    """Simple context for an event handler."""
    __slots__ = ('__forwarder', '__writer', '__load', '__lock')

    def __init__(self, forwarder: EventForwarder, writer: BinaryWriter) -> None:
        self.__lock = threading.RLock()
        self.__forwarder = forwarder
        self.__writer = ThreadSafeEventWriter(writer, self.__lock)
        self.__load = LoadList()

    @property
    def writer(self) -> ThreadSafeEventWriter:
        """Get the writer."""
        return self.__writer

    def add_target(self, target: EventForwarderTarget) -> None:
        """Add a new target to the forwarder.  The target will receive new
        messages once the next event comes in, or if the stream is already
        at an end.  The `on_eof` function can be called immediately."""
        self.__forwarder.add_target(target)

    def load_list(self) -> LoadList:
        """Get the list of extensions to load."""
        return self.__load

    def start_ready_extensions(self) -> StdRet[None]:
        """Make a request to start all extensions that are ready to be run."""
        errors: List[UserMessage] = []
        with self.__lock:
            for ext in self.__load.get_ready_to_load():
                res = self._start_extension(ext)
                errors.extend(res.error_messages())
        if errors:
            return StdRet.pass_error(join_errors(*errors))
        return RET_OK_NONE

    def _start_extension(self, extension: ExtensionInfo) -> StdRet[None]:
        # Must be called from within a locked state.
        self.__load.mark_loading(extension.name)
        # FIXME add in the right listener to start the process.
        return RET_OK_NONE

    def add_pending_extensions(
            self,
            extensions: Iterable[ExtensionInfo],
            installed: Iterable[ExtensionInfo],
    ) -> StdRet[None]:
        """Add extensions to the list of those that should run.  If any are ready to be
        started, they will be requested to start during this call."""
        errors: List[UserMessage] = []
        with self.__lock:
            res = add_pending_extensions(self.__load, extensions, installed)
            errors.extend(res.error_messages())
            res = self.start_ready_extensions()
            errors.extend(res.error_messages())
        if errors:
            return StdRet.pass_error(join_errors(*errors))
        return RET_OK_NONE
