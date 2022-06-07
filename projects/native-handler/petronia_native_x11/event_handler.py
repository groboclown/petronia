"""Handle xcb events."""

from typing import Sequence, List, Dict, Literal, Callable, Optional, Type
import ctypes
import threading
import time
from concurrent.futures import Future, Executor, ThreadPoolExecutor
from queue import Queue, Empty
from petronia_common.util import StdRet, T
from petronia_native.common import user_messages
from . import common_data
from .libs import libc, libxcb_types, libxcb_consts, ct_util


IGNORED_EVENT_STAY_ALIVE_SECONDS = 5.0


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
    [libxcb_types.XcbGenericEventP],
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


# These callbacks take the contents of the pointer, rather than the pointer itself.
# ctypes makes a copy of the contents every time you call ".contents", so this allows
# the pointer to be freed immediately, and the data to not be re-copied every time it's
# called.  It also means that the handler can use the data in any thread, and not need
# to worry about the data being freed.
# The only danger is for events that pass more data than explicitly remarked
# by the structure.  However, that only happens for the request/response style xcb calls,
# not for the event data.
KeyPressEventCallback = Callable[[libxcb_types.XcbKeyPressEventP], Optional[bool]]
KeyReleaseEventCallback = Callable[[libxcb_types.XcbKeyReleaseEventP], Optional[bool]]
KeymapEventCallback = Callable[[libxcb_types.XcbKeymapNotifyEventP], Optional[bool]]
ButtonPressEventCallback = Callable[[libxcb_types.XcbButtonPressEventP], Optional[bool]]
ButtonReleaseEventCallback = Callable[[libxcb_types.XcbButtonReleaseEventP], Optional[bool]]
MotionEventCallback = Callable[[libxcb_types.XcbMotionNotifyEventP], Optional[bool]]
EnterEventCallback = Callable[[libxcb_types.XcbEnterNotifyEventP], Optional[bool]]
LeaveEventCallback = Callable[[libxcb_types.XcbLeaveNotifyEventP], Optional[bool]]
FocusInEventCallback = Callable[[libxcb_types.XcbFocusInEventP], Optional[bool]]
FocusOutEventCallback = Callable[[libxcb_types.XcbFocusOutEventP], Optional[bool]]
WinCreateEventCallback = Callable[[libxcb_types.XcbCreateNotifyEventP], Optional[bool]]
WinDestroyEventCallback = Callable[[libxcb_types.XcbDestroyNotifyEventP], Optional[bool]]
MapRequestEventCallback = Callable[[libxcb_types.XcbMapRequestEventP], Optional[bool]]
UnmapEventCallback = Callable[[libxcb_types.XcbUnmapNotifyEventP], Optional[bool]]
ConfigureRequestEventCallback = Callable[[libxcb_types.XcbConfigureRequestEventP], Optional[bool]]


class EventRegistrar:
    """register handlers for specific X events."""
    def register_keypress_callback(self, callback: KeyPressEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_keyrelease_callback(self, callback: KeyReleaseEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_keymap_callback(self, callback: KeymapEventCallback) -> None:
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

    def register_motion_callback(self, callback: MotionEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_enter_callback(self, callback: EnterEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_leave_callback(self, callback: LeaveEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_focus_in_callback(self, callback: FocusInEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_focus_out_callback(self, callback: FocusOutEventCallback) -> None:
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

    def register_unmap_callback(self, callback: UnmapEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_map_request_callback(self, callback: MapRequestEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError

    def register_configure_request_callback(self, callback: ConfigureRequestEventCallback) -> None:
        """Registers a callback that takes the event as an argument.
        It should return True to cancel other callbacks from running."""
        raise NotImplementedError


class LowEvents(EventRegistrar):
    """Handles event fetching, type casting, and calling."""

    __slots__ = (
        '__api', '__error_callback',
        '__callbacks',
        '__keypress', '__keyrelease', '__keymap',
        '__buttonpress', '__buttonrelease', '__motion', '__enter', '__leave',
        '__focusin', '__focusout',

        '__win_create', '__win_destroy',
        '__unmap', '__map_req', '__configure_req',
    )

    def __init__(
            self,
            on_error: Callable[[BaseException], None],
    ) -> None:
        self.__error_callback = on_error
        self.__keypress: List[KeyPressEventCallback] = []
        self.__keyrelease: List[KeyReleaseEventCallback] = []
        self.__keymap: List[KeymapEventCallback] = []
        self.__buttonpress: List[ButtonPressEventCallback] = []
        self.__buttonrelease: List[ButtonReleaseEventCallback] = []
        self.__motion: List[MotionEventCallback] = []
        self.__enter: List[EnterEventCallback] = []
        self.__leave: List[LeaveEventCallback] = []
        self.__focusin: List[FocusInEventCallback] = []
        self.__focusout: List[FocusOutEventCallback] = []
        self.__win_create: List[WinCreateEventCallback] = []
        self.__win_destroy: List[WinDestroyEventCallback] = []
        self.__unmap: List[UnmapEventCallback] = []
        self.__map_req: List[MapRequestEventCallback] = []
        self.__configure_req: List[ConfigureRequestEventCallback] = []

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
            libxcb_consts.XCB_MOTION_NOTIFY:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbMotionNotifyEventP, self.__motion,
                ),
            libxcb_consts.XCB_ENTER_NOTIFY:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbEnterNotifyEventP, self.__enter,
                ),
            libxcb_consts.XCB_LEAVE_NOTIFY:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbLeaveNotifyEventP, self.__leave,
                ),
            libxcb_consts.XCB_FOCUS_IN:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbFocusInEventP, self.__focusin,
                ),
            libxcb_consts.XCB_FOCUS_OUT:
                # Do we need to check this?
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbFocusOutEventP, self.__focusout,
                ),
            libxcb_consts.XCB_KEYMAP_NOTIFY:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbKeymapNotifyEventP, self.__keymap,
                ),
            # libxcb_consts.XCB_EXPOSE:  # TODO need to check
            # libxcb_consts.XCB_GRAPHICS_EXPOSURE:  # Do we need to check this?
            # libxcb_consts.XCB_NO_EXPOSURE:  # Do we need to check this?
            # libxcb_consts.XCB_VISIBILITY_NOTIFY:  # Do we need to check this?
            libxcb_consts.XCB_CREATE_NOTIFY:
                # Do we need to check this?
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbCreateNotifyEventP, self.__win_create,
                ),
            libxcb_consts.XCB_DESTROY_NOTIFY:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbDestroyNotifyEventP, self.__win_destroy,
                ),
            libxcb_consts.XCB_UNMAP_NOTIFY:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbUnmapNotifyEventP, self.__unmap,
                ),
            # libxcb_consts.XCB_MAP_NOTIFY:  # Do we need to check this?
            libxcb_consts.XCB_MAP_REQUEST:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbMapRequestEventP, self.__map_req,
                ),
            # libxcb_consts.XCB_REPARENT_NOTIFY:   # TODO need to check
            # libxcb_consts.XCB_CONFIGURE_NOTIFY:  # TODO need to check
            libxcb_consts.XCB_CONFIGURE_REQUEST:
                lambda e: self._handle_runner(
                    e, libxcb_types.XcbConfigureRequestEventP, self.__configure_req,
                ),
            # libxcb_consts.XCB_GRAVITY_NOTIFY:  # Do we need to check this?
            # libxcb_consts.XCB_RESIZE_REQUEST:  # Do we need to check this?
            # libxcb_consts.XCB_CIRCULATE_NOTIFY:  # Do we need to check this?
            # libxcb_consts.XCB_CIRCULATE_REQUEST:  # Do we need to check this?
            # libxcb_consts.XCB_PROPERTY_NOTIFY:   # TODO need to check
            # libxcb_consts.XCB_SELECTION_CLEAR:  # TODO need to check
            # libxcb_consts.XCB_SELECTION_REQUEST:  # TODO need to check
            # libxcb_consts.XCB_SELECTION_NOTIFY:  # TODO need to check
            # libxcb_consts.XCB_COLORMAP_NOTIFY:  # Do we need to check this?
            # libxcb_consts.XCB_CLIENT_MESSAGE:   # TODO need to check
            # libxcb_consts.XCB_MAPPING_NOTIFY:  # Do we need to check this?
            # libxcb_consts.XCB_GE_GENERIC:  # Do we need to check this?

            # XCB_RANDR_SCREEN_CHANGE_NOTIFY
            # XCB_RANDR_NOTIFY
            # XCB_SHAPE_NOTIFY
            # XCB_XFIXES_SELECTION_NOTIFY
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

    def register_configure_request_callback(self, callback: ConfigureRequestEventCallback) -> None:
        self.__configure_req.append(callback)

    def register_motion_callback(self, callback: MotionEventCallback) -> None:
        self.__motion.append(callback)

    def register_enter_callback(self, callback: EnterEventCallback) -> None:
        self.__enter.append(callback)

    def register_leave_callback(self, callback: LeaveEventCallback) -> None:
        self.__leave.append(callback)

    def register_focus_in_callback(self, callback: FocusInEventCallback) -> None:
        self.__focusin.append(callback)

    def register_focus_out_callback(self, callback: FocusOutEventCallback) -> None:
        self.__focusout.append(callback)

    def register_unmap_callback(self, callback: UnmapEventCallback) -> None:
        self.__unmap.append(callback)

    def on_event(
            self,
            event: libxcb_types.XcbGenericEventP,
    ) -> None:
        """Handle the event.  The event must be valid.  It is freed outside this call."""
        # TODO look at the sequence on the event, and ignore sequences that have been handled.
        #   Without this, subtle bugs can slip into the event handling.

        response_type = ct_util.as_py_int(event.contents.response_type) & ~0x80
        callback = self.__callbacks.get(response_type)
        if callback:
            user_messages.low_println(f"Processing X event response {response_type}")
            callback(event)
        else:
            user_messages.low_println(f"Ignoring X event response {response_type}")

    def _handle_runner(
            self,
            event,  # type: ctypes.pointer[T]
            real_type,  # type: Type[ctypes.pointer[T]]
            runners,  # type: Sequence[Callable[[ctypes.pointer[T]], Optional[bool]]]
    ) -> None:
        """Handle the runner list calls."""
        for runner in runners:
            try:
                if runner(ctypes.cast(event, real_type)) is True:
                    # Stop other events from running.
                    return
            except BaseException as err:
                print(f"src: {type(event)}, real type: {real_type}")
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
        '__ignored_events',
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
        self.__ignored_events = IgnorableEventList()

    def get_event_registrar(self) -> EventRegistrar:
        """Get the per-event type registration."""
        return self.__handlers

    def ignore_event(self, sequence: int, response_type: Optional[int]) -> None:
        """Mark the event response type and sequence as ignored."""
        with self.__lock:
            self.__ignored_events.add_event(sequence, response_type)

    def add_missed_events(
            self,
            events: Sequence[libc.Pointer[libxcb_types.XcbGenericEventP]],
    ) -> None:
        """Add X server events that were read outside the loop but that should be
        processed inside the loop.  The events must be freed after calling this."""
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

                # Make a copy of the ignorable events that aren't expired, so
                #   that we don't need to worry about locking another silliness.
                ignorable_events = self.__ignored_events.manage()

                # Handle improperly managed events.
                for pending_event in self.__pending_events:
                    if (
                            pending_event
                            and ignorable_events.is_ok(
                                pending_event.contents.sequence,
                                pending_event.contents.response_type,
                            )
                    ):
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
                    if ignorable_events.is_ok(
                        event.contents.sequence,
                        event.contents.response_type,
                    ):
                        # Note: X doesn't send the window manager a stop request.
                        user_messages.low_println(
                            f" - X loop: handling X event {event.contents.response_type}"
                        )
                        self.__handlers.on_event(event.value)
                    else:
                        user_messages.low_println(
                            f" - X loop: ignoring X event {event.contents.response_type}"
                        )
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


class IgnoredEvent:
    """An event to ignore.  These time out eventually.
    Even on a match for an ignored event, these should only be removed at the timeout,
    due to issues with multiple events being triggered for the same initial request."""
    __slots__ = ('__sequence', '__expires_at', '__response_type')

    def __init__(self, sequence: int, response_type: Optional[int]) -> None:
        self.__sequence = sequence
        self.__response_type = -1 if response_type is None else response_type
        self.__expires_at = time.time() + IGNORED_EVENT_STAY_ALIVE_SECONDS

    def is_expired(self) -> bool:
        """Is this ignored event expired?"""
        return time.time() > self.__expires_at

    def is_match(self, *, sequence: int, response_type: int) -> bool:
        """Is this a match?  Does not check expiration."""
        if sequence != self.__sequence:
            return False

        # Sequence numbers match.
        if response_type != -1 and response_type != self.__response_type:
            return False

        # response type matches or this is an event with a non-response type value.
        return True


class IgnorableEventList:
    """List of ignorable events."""
    __slots__ = ('__events',)

    def __init__(self) -> None:
        self.__events: List[IgnoredEvent] = []

    def add_event(self, sequence: int, response_type: Optional[int]) -> None:
        """Add the ignored event"""
        evt = IgnoredEvent(sequence, response_type)
        self.__events.append(evt)

    def is_ok(self, sequence: int, response_type: int) -> bool:
        """Is the event okay to handle (e.g. not ignored)?"""
        for evt in self.__events:
            if evt.is_match(sequence=sequence, response_type=response_type):
                return False
        return True

    def manage(self) -> 'IgnorableEventList':
        """Manage the event list for expired events, and return a copy for easy
        ignore checking."""
        events: List[IgnoredEvent] = []
        for evt in self.__events:
            if not evt.is_expired():
                events.append(evt)
        self.__events = events
        ret = IgnorableEventList()
        ret.__events = list(events)
        return ret
