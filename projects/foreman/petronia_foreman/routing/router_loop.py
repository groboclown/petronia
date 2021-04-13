"""
Handles the inner-loop execution of requests.
"""

from typing import Dict, Iterable, Tuple, Literal, Optional
from queue import Queue
from petronia_common.event_stream import to_raw_event_object
from petronia_common.util import UserMessage, PetroniaReturnError, not_none
from petronia_common.util import i18n as _
from petronia_ext_lib.standard.error import (
    ACCESS_RESTRICTION_ERROR_CATEGORY, CONFIGURATION_ERROR_CATEGORY,
)
from .event_handlers import TargetHandlerRuntimeContext
from .handler_id import create_handler_id
from .. import event_util
from ..configuration import BootExtensionMetadata
from ..event_router import EventRouter
from ..events import foreman
from ..launcher import AbcLauncherCategory
from ..user_message import display_error, display_message, CATALOG


class ExtensionLaunchWatcher:
    """Watches extension launches."""
    __slots__ = ()

    def extension_launching(
            self, source_id: str, handler_id: str,
    ) -> None:
        """Called when an extension is just about to be launched."""
        raise NotImplementedError


class QueueRequest:
    """Basic queue request."""
    __slots__ = ()


class BootExtensionQueueRequest(QueueRequest):
    """Boot extension request."""
    __slots__ = ('metadata',)

    def __init__(self, metadata: BootExtensionMetadata) -> None:
        self.metadata = metadata

    def __repr__(self) -> str:
        return f'BootExtensionMetadata({self.metadata.to_start_event().name})'


class ExtensionQueueRequest(QueueRequest):
    """Standard extension request."""
    __slots__ = ('source', 'request',)

    def __init__(self, source: str, request: foreman.LauncherStartExtensionRequestEvent) -> None:
        self.source = source
        self.request = request

    def __repr__(self) -> str:
        return f'ExtensionQueueRequest({self.source}, {self.request.name})'


class AddEventListenersQueueRequest(QueueRequest):
    """Add event listeners request."""
    __slots__ = ('target', 'request',)

    def __init__(self, target: str, request: foreman.ExtensionAddEventListenerEvent) -> None:
        self.target = target
        self.request = request

    def __repr__(self) -> str:
        return f'AddEventListenersQueueRequest({self.target}, {self.request.events})'


class RemoveEventListenersQueueRequest(QueueRequest):
    """Remove event listeners request."""
    __slots__ = ('target', 'request',)

    def __init__(self, target: str, request: foreman.ExtensionRemoveEventListenerEvent) -> None:
        self.target = target
        self.request = request

    def __repr__(self) -> str:
        return f'RemoveEventListenersQueueRequest({self.target}, {self.request.events})'


SOFT_STOP_REQUEST = QueueRequest()
HARD_STOP_REQUEST = QueueRequest()
RESTART_REQUEST = QueueRequest()

LoopAction = Literal['none', 'hard-stop', 'soft-stop', 'restart']
HARD_STOP_LOOP_ACTION: LoopAction = 'hard-stop'
SOFT_STOP_LOOP_ACTION: LoopAction = 'soft-stop'
RESTART_LOOP_ACTION: LoopAction = 'restart'
NONE_LOOP_ACTION: LoopAction = 'none'


class RouterLoopLogic:
    """The inner logic that runs in a thread.  It manages the execution in a single thread,
    based on a queue to inject requests."""
    __slots__ = ('__categories', '__router', '__launch_watcher')

    def __init__(
            self,
            categories: Dict[str, AbcLauncherCategory],
            router: EventRouter,
            launch_watcher: Optional[ExtensionLaunchWatcher] = None,
    ) -> None:
        self.__categories = dict(categories)
        self.__router = router
        self.__launch_watcher = launch_watcher

    def get_categories(self) -> Iterable[AbcLauncherCategory]:
        """Get the known category list."""
        return tuple(self.__categories.values())

    def get_router(self) -> EventRouter:
        """Get the event router."""
        return self.__router

    def handle_request(self, request: QueueRequest) -> LoopAction:  # pylint:disable=too-many-return-statements
        """Handle the next queued request.  If the request is for an action on the looping
        behavior, that is returned."""
        if request == SOFT_STOP_REQUEST:
            return SOFT_STOP_LOOP_ACTION
        if request == HARD_STOP_REQUEST:
            return HARD_STOP_LOOP_ACTION
        if request == RESTART_REQUEST:
            return RESTART_LOOP_ACTION

        if isinstance(request, BootExtensionQueueRequest):
            self._handle_boot_extension(request.metadata)
            return NONE_LOOP_ACTION

        if isinstance(request, ExtensionQueueRequest):
            self._handle_extension(request.source, request.request)
            return NONE_LOOP_ACTION

        if isinstance(request, AddEventListenersQueueRequest):
            self._handle_add_listeners(request.target, request.request)
            return NONE_LOOP_ACTION

        if isinstance(request, RemoveEventListenersQueueRequest):
            self._handle_remove_listeners(request.target, request.request)
            return NONE_LOOP_ACTION

        display_message(
            UserMessage(
                CATALOG, _('unknown router queue request: {request}'),
                request=repr(request),
            )
        )
        return NONE_LOOP_ACTION

    def _handle_boot_extension(self, metadata: BootExtensionMetadata) -> None:
        event = metadata.to_start_event()
        handler_id = create_handler_id(event.name)
        # print(f'********** BOOT EXTENSION METADATA {event.name} - handler {handler_id}')
        if self._start_extension(None, handler_id, event):
            self._add_listeners(handler_id, metadata.consumes)

    def _handle_extension(
            self,
            source: str, request: foreman.LauncherStartExtensionRequestEvent,
    ) -> None:
        handler_id = create_handler_id(request.name)
        self._start_extension(source, handler_id, request)
        # The launch watcher should send any events when it's fully loaded.

    def _handle_add_listeners(
            self, target: str, request: foreman.ExtensionAddEventListenerEvent,
    ) -> None:
        handler_id = create_handler_id(target)
        # print(f'********** ADD LISTENERS: target {target} ; handler {handler_id}')
        self._add_listeners(handler_id, [
            (event.event_id, event.target_id)
            for event in request.events
        ])

    def _handle_remove_listeners(
            self, target: str, request: foreman.ExtensionRemoveEventListenerEvent,
    ) -> None:
        self._remove_listeners(target, [
            (event.event_id, event.target_id)
            for event in request.events
        ])

    def _start_extension(
            self,
            source: Optional[str],
            handler_id: str, request: foreman.LauncherStartExtensionRequestEvent,
    ) -> bool:
        """Start the extension, and return True if it started fine, or False if there
        was a problem."""
        launcher = self.__categories.get(request.runtime)
        if launcher is None:
            error_msg = UserMessage(
                CATALOG,
                _(
                    'Runtime {runtime} defined in extension {name}-{version} '
                    'but not defined in petronia.ini'
                ),
                runtime=request.runtime,
                name=request.name,
                version=request.version,
            )
            corrective_msg = UserMessage(
                CATALOG,
                _(
                    'Do not load the extension, or add the correct runtime '
                    'configuration in your petronia.ini file.'
                ),
            )
            if source:
                # send error
                send_res = self.__router.inject_event(to_raw_event_object(
                    foreman.LauncherStartExtensionFailedEvent.FULL_EVENT_NAME,
                    handler_id,
                    source,
                    foreman.LauncherStartExtensionFailedEvent(
                        request.name,
                        not_none(event_util.create_std_ret_errors(
                            error_msg,
                            'foreman-runtime-not-known',
                            [CONFIGURATION_ERROR_CATEGORY],
                        )),
                    ).export_data(),
                ))
                for msg in send_res.error_messages():
                    display_message(msg)
            else:
                display_message(error_msg)
                display_message(corrective_msg)
            return False
        if self.__launch_watcher:
            self.__launch_watcher.extension_launching(source, handler_id)
        res = launcher.start_extension(handler_id, request)
        if res.has_error:
            if source:
                self.__router.inject_event(to_raw_event_object(
                    foreman.LauncherStartExtensionFailedEvent.FULL_EVENT_NAME,
                    handler_id,
                    source,
                    foreman.LauncherStartExtensionFailedEvent(
                        request.name,
                        not_none(event_util.create_std_ret_errors(
                            res.valid_error,
                            'start-extension-failed',
                            [CONFIGURATION_ERROR_CATEGORY, ACCESS_RESTRICTION_ERROR_CATEGORY],
                        )),
                    ).export_data(),
                ))
            else:
                display_error(res.valid_error, True)
            return False
        # Success message is sent by the caller.
        display_message(UserMessage(
            CATALOG, _('Started extension {name}-{version}'),
            name=request.name, version=request.version,
        ))
        return True

    def _add_listeners(
            self, handler_id: str, events: Iterable[Tuple[Optional[str], Optional[str]]],
    ) -> bool:
        """Add listeners to the event handler."""
        ret = True
        for event_id, target_id in events:
            # Need to call this for all events.
            added = self.__router.add_handler_listener(handler_id, event_id, target_id)
            ret = ret and added
        return ret

    def _remove_listeners(
            self, handler_id: str, events: Iterable[Tuple[Optional[str], Optional[str]]],
    ) -> bool:
        """Remove listeners to the event handler."""
        ret = True
        for event_id, target_id in events:
            ret = ret and self.__router.remove_handler_listener(handler_id, event_id, target_id)
        return ret


class QueuedContext(TargetHandlerRuntimeContext):
    """Adds the requests to a queue."""
    __slots__ = ('__queue',)

    def __init__(self, queue):
        # type: (Queue[QueueRequest]) -> None
        self.__queue = queue

    def do_shutdown(self) -> None:
        self.__queue.put(SOFT_STOP_REQUEST)

    def do_restart(self, requested: bool, error: Optional[PetroniaReturnError]) -> None:
        self.__queue.put(RESTART_REQUEST)

    def start_extension(
            self, source_id: str, target_id: str,
            event: foreman.LauncherStartExtensionRequestEvent,
    ) -> None:
        self.__queue.put(ExtensionQueueRequest(source_id, event))

    def add_event_listener(
            self, target_id: str, event: foreman.ExtensionAddEventListenerEvent,
    ) -> None:
        # print(f"**** ADD LISTENERS FOR {target_id}")
        self.__queue.put(AddEventListenersQueueRequest(target_id, event))

    def remove_event_listener(
            self, target_id: str, event: foreman.ExtensionRemoveEventListenerEvent,
    ) -> None:
        self.__queue.put(RemoveEventListenersQueueRequest(target_id, event))
