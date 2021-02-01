"""Runtime Context."""

from typing import Iterable, List
import threading
from petronia_common.extension.runner import EventRegistryContext
from petronia_common.util import StdRet, UserMessage, join_errors, RET_OK_NONE
from petronia_common.util import i18n as _
from .defs import TRANSLATION_CATALOG
from .order import LoadList, add_pending_extensions
from .defs import ExtensionInfo
from .handlers import send, boot_extension_handler


class ExtLoaderSharedState:
    """Simple context for the event handlers."""
    __slots__ = ('__load', '__lock',)

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
            # Perform possibly multiple passes over the ready-to-load,
            # in case the start extension request ends up being a no-op
            # and dependencies are then ready to load.
            to_load = self.__load.get_ready_to_load()
            while to_load:
                for ext in to_load:
                    res = self._start_extension(ext, context)
                    errors.extend(res.error_messages())
                to_load = self.__load.get_ready_to_load()
        if errors:
            return StdRet.pass_error(join_errors(*errors))
        return RET_OK_NONE

    def _start_extension(
            self, extension: ExtensionInfo, registry: EventRegistryContext,
    ) -> StdRet[None]:
        # Must be called from within a locked state.
        self.__load.mark_loading(extension.name)
        return send.send_foreman_start_extension_request(
            registry,
            extension,
            self.__load.get_loaded(),
        )

    def on_extension_loaded(
            self,
            extension_name: str, registry: EventRegistryContext,
    ) -> StdRet[None]:
        """Called when an extension has completed loading."""
        ext = self.__load.get_loading_extension(extension_name)
        if not ext:
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG,
                _('extension not in loading state: {name}'),
                name=extension_name,
            )
        errors: List[UserMessage] = []
        for source_id in ext.request_source_ids:
            res = send.send_load_extension_succeeded(
                registry, source_id, ext.name, ext.version,
            )
            errors.extend(res.error_messages())
        errors.extend(
            boot_extension_handler.on_extension_load_complete(
                registry, extension_name,
            ).error_messages()
        )
        if errors:
            return StdRet.pass_error(join_errors(*errors))
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
