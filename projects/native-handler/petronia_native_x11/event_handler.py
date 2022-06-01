"""Handle xcb events."""

from typing import Sequence, List, Dict, Literal, Callable, Optional, Type
import ctypes
import threading
from concurrent.futures import Future, Executor, ThreadPoolExecutor
from queue import Queue, Empty
from petronia_common.util import StdRet, T
from petronia_native.common import user_messages
from . import common_data
from .libs import libc, libxcb_types, libxcb_consts, ct_util


class EventResponse:
    """Response for an event."""


EventQueryCallback = Callable[[StdRet[EventResponse]], StdRet[None]]

EventQueryRegisterCookie = Callable[[libxcb_types.XcbVoidCookie], None]

EventQuery = Callable[[common_data.WindowManagerData, EventQueryRegisterCookie], None]

FutureEventQuery = Callable[
    [common_data.WindowManagerData, EventQueryRegisterCookie],
    StdRet[None],
]

EventResponseCallback = Callable[
    [libc.Pointer[libxcb_types.XcbGenericEventP]],
    None,
]

ServerRequest = Callable[[common_data.WindowManagerData], None]

_STOP_SERVER_REQUEST: ServerRequest = lambda x: None


EventStateEnum = Literal['init', 'starting', 'running', 'stop-request', 'stopping', 'stopped']

_STOP_STATES: Sequence[EventStateEnum] = ('stop-request', 'stopping', 'stopped')


class EventHandler:
    """Client API into the event handler."""

    def query(self, query_request: EventQuery, callback: EventQueryCallback) -> StdRet[None]:
        """Runs the query in the event queue.  The response is also handled in the event queue,
        in the queue by calling the callback.  The request must register the cookie that will
        signal the callback to run.

        If the cookie is not registered, then the callback is immediately called with an error."""
        raise NotImplemented

    def future_query(self, future_query: FutureEventQuery) -> Future[StdRet[EventResponse]]:
        """Calls the query callback in the loop, and the response is returned in the future.

        The callback must register a cookie to signal which response to return.  If the cookie
        isn't registered, then the future returns immediately with an error.
        """
        raise NotImplemented


KeyPressEventCallback = Callable[[libxcb_types.XcbKeyPressEventP], Optional[bool]]
KeyReleaseEventCallback = Callable[[libxcb_types.XcbKeyReleaseEventP], Optional[bool]]
ButtonPressEventCallback = Callable[[libxcb_types.XcbButtonPressEventP], Optional[bool]]
ButtonReleaseEventCallback = Callable[[libxcb_types.XcbButtonReleaseEventP], Optional[bool]]
KeymapEventCallback = Callable[[libxcb_types.XcbKeymapNotifyEventP], Optional[bool]]
WinCreateEventCallback = Callable[[libxcb_types.XcbCreateNotifyEventP], Optional[bool]]
WinDestroyEventCallback = Callable[[libxcb_types.XcbDestroyNotifyEventP], Optional[bool]]
MapRequestEventCallback = Callable[[libxcb_types.XcbMapRequestEventP], Optional[bool]]
ConfigureEventCallback = Callable[[libxcb_types.XcbConfigureRequestEventP], Optional[bool]]


class EventRegistrar:
    """register handlers for specific X events."""
    def register_keymap_callback(self, callback: KeymapEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_keypress_callback(self, callback: KeyPressEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_keyrelease_callback(self, callback: KeyReleaseEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_buttonpress_callback(self, callback: ButtonPressEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_buttonrelease_callback(self, callback: ButtonReleaseEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_window_create_callback(self, callback: WinCreateEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_window_destroy_callback(self, callback: WinDestroyEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_map_request_callback(self, callback: MapRequestEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_configure_request_callback(self, callback: ConfigureEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError


class LowEvents(EventRegistrar):
    """Handles event fetching, type casting, and calling."""

    __slots__ = (
        '__api', '__error_callback',
        '__callbacks',
        '__keypress', '__keyrelease',
        '__buttonpress', '__buttonrelease',
        '__keymap',

        '__win_create', '__win_destroy',
        '__map_req', '__configure_req',
    )

    def __init__(
            self,
            on_error: Callable[[BaseException], None],
    ) -> None:
        self.__error_callback = on_error
        self.__keypress: List[KeyPressEventCallback] = []
        self.__keyrelease: List[KeyReleaseEventCallback] = []
        self.__buttonpress: List[ButtonPressEventCallback] = []
        self.__buttonrelease: List[ButtonReleaseEventCallback] = []
        self.__keymap: List[KeymapEventCallback] = []
        self.__win_create: List[WinCreateEventCallback] = []
        self.__win_destroy: List[WinDestroyEventCallback] = []
        self.__map_req: List[MapRequestEventCallback] = []
        self.__configure_req: List[ConfigureEventCallback] = []

        self.__callbacks: Dict[int, EventResponseCallback] = {
            libxcb_consts.XCB_KEY_PRESS:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbKeyPressEventP, self.__keypress,
                ),
            libxcb_consts.XCB_KEY_RELEASE:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbKeyReleaseEventP, self.__keyrelease,
                ),
            libxcb_consts.XCB_BUTTON_PRESS:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbButtonPressEventP, self.__buttonpress,
                ),
            libxcb_consts.XCB_BUTTON_RELEASE:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbButtonReleaseEventP, self.__buttonrelease,
                ),
            # libxcb_consts.XCB_MOTION_NOTIFY:
            # libxcb_consts.XCB_ENTER_NOTIFY:
            # libxcb_consts.XCB_LEAVE_NOTIFY:
            # libxcb_consts.XCB_FOCUS_IN:
            # libxcb_consts.XCB_FOCUS_OUT:
            libxcb_consts.XCB_KEYMAP_NOTIFY:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbKeymapNotifyEventP, self.__keymap,
                ),
            # libxcb_consts.XCB_EXPOSE:
            # libxcb_consts.XCB_GRAPHICS_EXPOSURE:
            # libxcb_consts.XCB_NO_EXPOSURE = 14
            # libxcb_consts.XCB_VISIBILITY_NOTIFY = 15
            libxcb_consts.XCB_CREATE_NOTIFY:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbCreateNotifyEventP, self.__win_create,
                ),
            libxcb_consts.XCB_DESTROY_NOTIFY:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbDestroyNotifyEventP, self.__win_destroy,
                ),
            # libxcb_consts.XCB_UNMAP_NOTIFY = 18
            # libxcb_consts.XCB_MAP_NOTIFY = 19
            libxcb_consts.XCB_MAP_REQUEST:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbMapRequestEventP, self.__map_req,
                ),
            # libxcb_consts.XCB_REPARENT_NOTIFY = 21
            # libxcb_consts.XCB_CONFIGURE_NOTIFY = 22
            libxcb_consts.XCB_CONFIGURE_REQUEST:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbConfigureRequestEvent, self.__configure_req,
                ),
            # libxcb_consts.XCB_GRAVITY_NOTIFY = 24
            # libxcb_consts.XCB_RESIZE_REQUEST = 25
            # libxcb_consts.XCB_CIRCULATE_NOTIFY = 26
            # libxcb_consts.XCB_CIRCULATE_REQUEST = 27
            # libxcb_consts.XCB_PROPERTY_NOTIFY = 28
            # libxcb_consts.XCB_SELECTION_CLEAR = 29
            # libxcb_consts.XCB_SELECTION_REQUEST = 30
            # libxcb_consts.XCB_SELECTION_NOTIFY = 31
            # libxcb_consts.XCB_COLORMAP_NOTIFY = 32
            # libxcb_consts.XCB_CLIENT_MESSAGE = 33
            # libxcb_consts.XCB_MAPPING_NOTIFY = 34
            # libxcb_consts.XCB_GE_GENERIC = 35
        }

    def register_keymap_callback(self, callback: KeymapEventCallback) -> None:
        self.__keymap.append(callback)

    def register_keypress_callback(self, callback: KeyPressEventCallback) -> None:
        self.__keypress.append(callback)

    def register_keyrelease_callback(self, callback: KeyReleaseEventCallback) -> None:
        self.__keyrelease.append(callback)

    def register_buttonpress_callback(self, callback: ButtonPressEventCallback) -> None:
        self.__buttonpress.append(callback)

    def register_buttonrelease_callback(self, callback: ButtonReleaseEventCallback) -> None:
        self.__buttonrelease.append(callback)

    def register_window_create_callback(self, callback: WinCreateEventCallback) -> None:
        self.__win_create.append(callback)

    def register_window_destroy_callback(self, callback: WinDestroyEventCallback) -> None:
        self.__win_destroy.append(callback)

    def register_map_request_callback(self, callback: MapRequestEventCallback) -> None:
        self.__map_req.append(callback)

    def register_configure_request_callback(self, callback: ConfigureEventCallback) -> None:
        self.__configure_req.append(callback)

    def on_event(
            self,
            event: libc.Pointer[libxcb_types.XcbGenericEventP],
    ) -> None:
        """Handle the event.  The event must be valid.  It is freed outside this call."""
        response_type = ct_util.as_py_int(event.contents.response_type) & ~0x80
        callback = self.__callbacks.get(response_type)
        if callback:
            user_messages.low_println(f"Processing X event response {response_type}")
            callback(event)
        else:
            user_messages.low_println(f"Ignoring X event response {response_type}")

    def _handle_runner(
            self,
            event: libc.Pointer[T],
            real_type: Type[T],
            runners: Sequence[Callable[[T], Optional[bool]]],
    ) -> None:
        """Handle the runner list calls."""
        for runner in runners:
            try:
                if runner(ctypes.cast(event.value, real_type)) is True:
                    # Stop other events from running.
                    return
            except BaseException as err:
                self.__error_callback(err)


class EventHandlerLoop:
    """Handles events posted to and from the X server.

    This is intended to be asynchronous from the execution of the Petronia events,
    so special care is taken to be thread safe.

    All public APIs are for calling into the thread.
    """
    __slots__ = (
        '__lock', '__state', '__cxt', '__thread',
        '__request_queue', '__queue_wait_time', '__handlers',
        '__error_callback', '__executor', '__pending_events',
    )

    def __init__(
            self, *,
            cxt: common_data.WindowManagerData,
            on_error: Callable[[BaseException], None],
            queue_wait_time: float = 0.1,
            executor: Optional[Executor] = None,
    ) -> None:
        self.__lock = threading.RLock()
        self.__executor = executor or ThreadPoolExecutor(16)
        self.__state: EventStateEnum = 'init'
        self.__cxt = cxt
        self.__thread: Optional[threading.Thread] = None
        self.__request_queue = Queue()  # type: Queue[ServerRequest]
        self.__queue_wait_time = queue_wait_time
        self.__handlers = LowEvents(on_error)
        self.__error_callback = on_error
        self.__pending_events: List[libc.Pointer[libxcb_types.XcbGenericEventP]] = []

    def get_event_registrar(self) -> EventRegistrar:
        """Get the per-event type registration."""
        return self.__handlers

    def add_missed_events(
            self,
            events: Sequence[libc.Pointer[libxcb_types.XcbGenericEventP]],
    ) -> None:
        """Add X server events that were read outside the loop but that should be
        processed inside the loop."""
        with self.__lock:
            self.__pending_events.extend(events)

    def enqueue(self, callback: ServerRequest) -> None:
        """Add the simple callback to the pending queue."""
        self.__request_queue.put(callback)

    def is_running(self) -> bool:
        """Is the thread running at all?"""
        return self.__thread is not None and self.__thread.is_alive()

    def stop(self, timeout: float) -> None:
        """Send a signal to the running thread to stop running."""
        with self.__lock:
            if self.__state not in _STOP_STATES:
                user_messages.low_println("Stopping X Server Event Loop")
                self.__state = 'stop-request'
                self.__request_queue.put(_STOP_SERVER_REQUEST)
        if timeout > 0 and self.__thread is not None and self.__thread.is_alive():
            user_messages.low_println("Joining X Server Event Loop")
            self.__thread.join(timeout)

    def start(self) -> None:
        """Start the loop."""
        with self.__lock:
            if self.is_running() or self.__state != 'init':
                raise ValueError('Already running')  # programmer error
            user_messages.low_println("Launching X Server Event Loop")
            self.__state = 'starting'
            self.__thread = threading.Thread(
                target=self._loop,
                daemon=True,
            )
            self.__thread.start()

    def _loop(self) -> None:
        """The thread execution loop.

        This takes turns performing a non-blocking event get then a request queue get.
        """
        with self.__lock:
            if self.__state in _STOP_STATES:
                # Already stopped.  This can happen if a stop request happens before the
                # thread has a chance to start.
                self.__state = 'stopped'
                return

            if self.__state != 'starting':
                raise ValueError(
                    f'Incorrect usage: started loop outside starting state: {self.__state}'
                )
            self.__state = 'running'
        user_messages.low_println("Running X Server Event Loop")

        while True:
            stop_now = False
            with self.__lock:
                if self.__state in _STOP_STATES:
                    # regardless of the state, we need to stop.
                    self.__state = 'stopping'
                    stop_now = True
                    break

            # First, handle improperly managed events.
            with self.__lock:
                for pending_event in self.__pending_events:
                    if pending_event:
                        user_messages.low_println(f" - X loop: pending event {pending_event}")
                        self.__handlers.on_event(pending_event.value)
                        pending_event.close()
                self.__pending_events.clear()

            # read requests out to the server while requests are immediately ready.
            keep_pulling = True
            while keep_pulling:
                try:
                    request = self.__request_queue.get_nowait()
                    if request == _STOP_SERVER_REQUEST:
                        user_messages.low_println(" - X loop: petronia request to stop loop")
                        stop_now = True
                        break
                    user_messages.low_println(f" - X loop: petronia request {request}")
                    with self.__lock:
                        request(self.__cxt)
                except Empty:
                    # Nothing in the request queue
                    keep_pulling = False
            if stop_now:
                break

            # Non-blocking event fetch from the X server until there is nothing pending.
            # user_messages.low_println(" - X loop: poll start")
            keep_pulling = True
            while keep_pulling:
                event_ptr = self.__cxt.libs.xcb.xcb_poll_for_event(self.__cxt.connection)
                if not event_ptr:
                    # user_messages.low_println(" - X loop: end of events to poll")
                    # TODO check for error.
                    # No event.  Nothing else is pending at this moment.
                    keep_pulling = False
                else:
                    event = self.__cxt.libs.clib.freeable(event_ptr, self.__lock)
                    # TODO check for quit event?
                    user_messages.low_println(
                        f" - X loop: handling X event {event.contents.response_type}"
                    )
                    self.__handlers.on_event(event)
                    event.close()

            # Now that the immediately available requests are handled and the pending
            #   events from the X server are handled, wait a bit for requests
            #   from inside our program.  This will give a bit of time before the next
            #   batch of events are handled.
            # user_messages.low_println(" - X loop: pet event poll")
            try:
                request = self.__request_queue.get(block=True, timeout=self.__queue_wait_time)
                if request == _STOP_SERVER_REQUEST:
                    user_messages.low_println(" - X loop: petronia request to stop server (2)")
                    stop_now = True
                    break
                user_messages.low_println(f" - X loop: petronia request {request} (2)")
                with self.__lock:
                    request(self.__cxt)
            except Empty:
                # Nothing in the request
                pass

        # Finished running.  Set the state.
        with self.__lock:
            self.__state = 'stopped'
        user_messages.low_println("X Loop Stopped")
