"""Runtime Context."""

from typing import Iterable, List
import threading
from petronia_common.extension.runner import EventRegistryContext
from petronia_common.util import StdRet, UserMessage, join_errors, RET_OK_NONE
from .order import LoadList, add_pending_extensions
from .defs import ExtensionInfo
from .handlers import send


class ExtLoaderSharedState:
    """Simple context for an event handler."""
    __slots__ = ('__load', '__lock')

    def __init__(self) -> None:
        self.__lock = threading.RLock()
        self.__load = LoadList()

    def load_list(self) -> LoadList:
        """Get the list of extensions to load."""
        return self.__load

    def start_ready_extensions(self, context: EventRegistryContext) -> StdRet[None]:
        """Make a request to start all extensions that are ready to be run."""
        errors: List[UserMessage] = []
        with self.__lock:
            for ext in self.__load.get_ready_to_load():
                res = self._start_extension(ext, context)
                errors.extend(res.error_messages())
        if errors:
            return StdRet.pass_error(join_errors(*errors))
        return RET_OK_NONE

    def _start_extension(
            self, extension: ExtensionInfo, registry: EventRegistryContext,
    ) -> StdRet[None]:
        # Must be called from within a locked state.
        self.__load.mark_loading(extension.name)
        send.send_foreman_start_extension_request(
            registry,
            extension,
            self.__load.get_loaded(),
        )
        return RET_OK_NONE

    def add_pending_extensions(
            self,
            extensions: Iterable[ExtensionInfo],
            installed: Iterable[ExtensionInfo],
            registry: EventRegistryContext,
    ) -> StdRet[None]:
        """Add extensions to the list of those that should run.  If any are ready to be
        started, they will be requested to start during this call."""
        errors: List[UserMessage] = []
        with self.__lock:
            res = add_pending_extensions(self.__load, extensions, installed)
            errors.extend(res.error_messages())
            res = self.start_ready_extensions(registry)
            errors.extend(res.error_messages())
        if errors:
            return StdRet.pass_error(join_errors(*errors))
        return RET_OK_NONE
