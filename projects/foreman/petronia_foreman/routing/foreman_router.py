"""The routing mechanism specific to foreman, with all the foreman logic."""

import threading
import time
from concurrent.futures import ThreadPoolExecutor
from queue import Queue, Empty
from typing import Dict, List, Tuple, Iterable, Callable, Optional, Any
from petronia_common.event_stream import (
    EventForwarderTarget, BinaryWriter, BinaryReader,
)
from petronia_common.util import StdRet, collect_errors_from, RET_OK_NONE
from petronia_common.util import i18n as _
from .event_handlers import ExtensionLoaderTarget, InternalTarget
from .router_loop import (
    QueueRequest, ExtensionQueueRequest, RouterLoopLogic, QueuedContext,
    BootExtensionQueueRequest,
    SOFT_STOP_REQUEST, SOFT_STOP_LOOP_ACTION, HARD_STOP_LOOP_ACTION, RESTART_LOOP_ACTION,
)
from ..configuration import RuntimeConfig, BootExtensionMetadata
from ..constants import (
    EXTENSION_LOADER_CHANNEL_PATTERN, INTERNAL_CHANNEL_PATTERN, TRANSLATION_CATALOG,
)
from ..event_router import EventRouter
from ..event_router.channel import InternalEventHandler
from ..event_router.handler import EventTargetHandle
from ..events import foreman
from ..launcher import AbcLauncherCategory, RuntimeContext, create_launcher_category
from ..launcher.internal import create_internal_launcher
from ..launcher.loader import INTERNAL_EXTENSION_RUNTIME
from ..user_message import display_error, low_println


DEBUG = False

_STATE_STOPPED = 0
_STATE_BOOTING = 1
_STATE_STARTING = 2
_STATE_RUNNING = 3
_STATE_STOPPING = 4


class ForemanRouter:  # pylint: disable=too-many-instance-attributes
    """
    Manages a running event router that runs in an event loop.
    The router can be started and stopped multiple times.

    The router itself performs the communication in another thread,
    so that the event loop does not interfere or cause contention with
    the main thread.
    """
    __slots__ = (
        '__category_states', '__executor', '__state', '__queue', '__lock',
        '__state_condition', '__thread', '__full_stop', 'stop_timeout',
    )

    def __init__(
            self,
            categories: List[RuntimeConfig],
    ) -> None:
        self.__category_states: Dict[str, LauncherCategoryState] = {
            config.runtime_name: LauncherCategoryState(config)
            for config in categories
        }
        self.__executor: Optional[ThreadPoolExecutor] = None
        self.__state = 0
        self.__lock = threading.RLock()
        self.__queue = Queue()  # type: Queue[QueueRequest]
        self.__state_condition = threading.Condition(self.__lock)
        self.__thread: Optional[threading.Thread] = None
        self.__full_stop = False
        self.stop_timeout = 10.0

    def is_running(self) -> bool:
        """Is this router running?"""
        with self.__lock:
            return self.__state == _STATE_RUNNING

    def start(self, timeout: Optional[float] = None) -> bool:
        """Starts up the router.  If it is already running, then this is a no-op.  If it
        is currently shutting down, then this will wait for the shutdown to complete, then
        start the router.  If the router is starting, then this will wait for the start to
        complete.  Returns False if the timeout is exceeded."""

        # Reset the stop request.
        self.__full_stop = False

        # timeout is a per-wait timeout, not entire start timeout.

        with self.__lock:
            while self.__state != _STATE_RUNNING:
                # Capture the current state inside the loop, because the if statements
                # wait for the state to change.
                current_state = self.__state
                if current_state in (_STATE_BOOTING, _STATE_STARTING, _STATE_STOPPING):
                    _debug(
                        'start', 'state is {state}, waiting on state change.', state=current_state,
                    )
                    res = self.__state_condition.wait_for(
                        lambda: self.__state != current_state,
                        timeout,
                    )
                    if not res:
                        # Timeout.
                        _debug(
                            'start', 'timed out waiting on start; state is {state}',
                            state=self.__state,
                        )
                        return False
                    continue
                if self.__state == _STATE_STOPPED:
                    # Start the thread + router.

                    # This is a basic state-machine validation, useful for unit tests and
                    # developers.
                    assert self.__thread is None, 'Did not stop router thread correctly'  # nosec

                    # This + constructor is the only time outside the thread loop the state changes.
                    # It can only be done while the thread is stopped.
                    _debug('start', 'Starting router thread')
                    thread_name = _next_thread_id()
                    self.__state = _STATE_BOOTING
                    self.__thread = threading.Thread(
                        target=self._thread_runner,
                        daemon=False,
                        name=thread_name,
                    )
                    self.__thread.start()
                    # Keep looping until it's started.
                    continue
        _debug('start', 'router thread is running')
        return True

    def join(self, timeout: Optional[float] = None) -> bool:
        """Wait for the state to be stopped."""
        end_time = time.time() + (timeout or 0.0)
        while True:
            if timeout is not None and end_time > time.time():
                _debug('join', 'timed out waiting for stop')
                return False
            with self.__lock:
                if self.__state == _STATE_STOPPED:
                    _debug('join', 'thread is stopped')
                    return True
                _debug('join', 'state is {state}', state=self.__state)
            current_thread = self.__thread
            if current_thread:
                if not current_thread.is_alive():
                    # Something killed it
                    with self.__lock:
                        self.__state = _STATE_STOPPED
                    _debug('join', 'thread died unexpectedly.  Forcing stopped state.')
                    return True
                # Signal friendly join.
                current_thread.join(min(1.0, time.time() - end_time))

    def stop(self, timeout: Optional[float] = None) -> bool:
        """Stops the router and waits for it to stop.  If the router is not running, then this
        is a no-op.  If the router is currently starting, then this will interrupt the startup
        and stop whatever has already started.  If the router is stopping, then this will wait
        for the stop to complete.

        Returns False if the timeout is exceeded."""

        # A real stop was requested.
        self.__full_stop = True
        _debug('stop', 'initiating stop sequence')

        with self.__lock:
            while self.__state != _STATE_STOPPED:
                current_state = self.__state
                if current_state in (_STATE_BOOTING, _STATE_STARTING, _STATE_STOPPING):
                    _debug(
                        'stop', 'state is {state}; waiting on state change.', state=current_state,
                    )
                    res = self.__state_condition.wait_for(
                        lambda: self.__state != current_state,
                        timeout,
                    )
                    if not res:
                        # Timeout.
                        _debug(
                            'stop', 'timed out waiting for stop; state is {state}',
                            state=self.__state,
                        )
                        return False
                    continue
                if current_state == _STATE_RUNNING:
                    _debug('stop', 'running state, sending stop request and waiting')
                    self.__queue.put(SOFT_STOP_REQUEST)
                    res = self.__state_condition.wait_for(
                        lambda: self.__state != current_state,
                        timeout,
                    )
                    if not res:
                        # Timeout.
                        _debug('stop', 'timed out waiting for state change')
                        return False
        _debug('stop', 'router thread is stopped')
        return True

    def start_extension(
            self, source_id: str, request: foreman.LauncherStartExtensionRequestEvent,
    ) -> None:
        """Starts up an extension after boot-time."""
        with self.__lock:
            self._ensure_running()
            self.__queue.put(ExtensionQueueRequest(source_id, request))

    def start_boot_extension(self, request: BootExtensionMetadata) -> None:
        """Starts up a boot-time extension."""
        with self.__lock:
            self._ensure_running()
            self.__queue.put(BootExtensionQueueRequest(request))

    def _thread_runner(self) -> None:
        """A thread runnable method that monitors the queue for actions to perform on the
        asyncio items in the loop."""

        # Start up the thread.

        with self.__lock:
            # This is intended to protect the state machine during unit tests, to ensure this
            # protected method isn't called in the wrong order.
            assert self.__state == _STATE_BOOTING, 'Not in correct state to start thread'  # nosec

        sem = threading.Semaphore()
        executor = ThreadPoolExecutor()
        loop_handler = self._setup_loop_logic(sem, executor)

        with self.__lock:
            self.__state = _STATE_RUNNING
            self.__state_condition.notify_all()

        while True:
            event = self.__queue.get(block=True)
            _debug('thread', "Foreman processing request `{event}`", event=event)
            special = loop_handler.handle_request(event)
            if special == RESTART_LOOP_ACTION:
                # Perform the restart outside the loop, as it's a ... weird activity.
                executor.submit(self._restart)
            elif special in (HARD_STOP_LOOP_ACTION, SOFT_STOP_LOOP_ACTION):
                # Changing the state requires acquiring the lock and sending a
                # notification.
                with self.__lock:
                    self.__state = _STATE_STOPPING
                    self.__state_condition.notify_all()
                    # Empty out the queue, so that the next execution doesn't pick up weird stuff.
                    # Only do this from within the lock.
                    try:
                        while True:
                            self.__queue.get_nowait()
                    except Empty:
                        pass

                # A "hard" stop ignores extensions.
                ForemanRouter._stop_launchers(loop_handler.get_categories())
                ForemanRouter._stop_channels(loop_handler.get_router())

                with self.__lock:
                    self.__state = _STATE_STOPPED
                    self.__state_condition.notify_all()
                    self.__thread = None
                return

    @staticmethod
    def _stop_launchers(categories: Iterable[AbcLauncherCategory]) -> None:
        """Stop all running launchers.  Errors are displayed but not returned."""
        errors: List[StdRet[None]] = []
        for launcher_category in categories:
            errors.append(launcher_category.stop())
        err = collect_errors_from(errors)
        if err:
            display_error(err)

    @staticmethod
    def _stop_channels(router: EventRouter) -> None:
        """Stop all the active channels in the router."""
        channel_names = router.get_registered_channel_names()
        for name in channel_names:
            router.close_channel(name)

    def _restart(self) -> None:
        """Restart the router."""
        _debug('_restart', 'Received restart signal')
        if self.__full_stop:
            _debug('_restart', 'Called after a stop request.')
            return
        self.stop()
        # Start will reset the stop request.
        self.start()

    def _stop(self) -> None:
        """Internal stop callback."""
        self.stop()

    def _setup_loop_logic(
            self, sem: threading.Semaphore, executor: ThreadPoolExecutor,
    ) -> RouterLoopLogic:
        """Create the router specifically for foreman interaction.
        """

        router = EventRouter(sem, executor=executor)

        launcher_context = LauncherRuntimeContext(router, executor)

        # Create launcher categories based on this router.
        # They all need to be initialized.  Which means they need to be created.
        categories: Dict[str, AbcLauncherCategory] = {
            # Hard-coded, always present launcher...
            INTERNAL_EXTENSION_RUNTIME: create_internal_launcher(),

        }
        for state in self.__category_states.values():
            cat_res = state.create_category(launcher_context, executor)
            if cat_res.has_error:
                display_error(cat_res.valid_error, debug=True)
            else:
                categories[state.name] = cat_res.result

        context = QueuedContext(self.__queue)

        internal_target = InternalTarget(context)

        def internal_channel_callback(name: str) -> StdRet[Optional[EventForwarderTarget]]:
            if INTERNAL_CHANNEL_PATTERN.match(name):
                return StdRet.pass_ok(internal_target)
            return RET_OK_NONE

        router.add_reservation_callback(
            INTERNAL_CHANNEL_PATTERN,
            internal_channel_callback,
        )

        # Extension loader reservation MUST be added after internal channel reservation.
        router.add_reservation_callback(
            EXTENSION_LOADER_CHANNEL_PATTERN,
            ExtensionLoaderCallback(ExtensionLoaderTarget(context)),
        )

        return RouterLoopLogic(categories, router)

    def _ensure_running(self) -> None:
        """MUST be called from within a lock."""
        if self.__state != _STATE_RUNNING:
            raise AttributeError('router not running')


class ExtensionLoaderCallback:
    """A callback that conforms to the ChannelReservationCallback"""
    __slots__ = ('__target',)

    def __init__(self, target: ExtensionLoaderTarget) -> None:
        self.__target: Optional[ExtensionLoaderTarget] = target

    def __call__(self, name: str) -> StdRet[Optional[EventForwarderTarget]]:
        # if name != EXTENSION_LOADER_CHANNEL:
        #     return RET_OK_NONE
        if self.__target is None:
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG,
                _('extension loader channel {channel} already registered.'),
                channel=name,
            )
        ret = StdRet.pass_ok(self.__target)
        self.__target = None
        return ret


class LauncherRuntimeContext(RuntimeContext):
    """Launcher category context."""

    __slots__ = ('_router', '_executor')

    def __init__(
            self, router: EventRouter, executor: ThreadPoolExecutor,
    ) -> None:
        self._router = router
        self._executor = executor

    def register_channel(
            self, name: str,
            channel_creator: Callable[
                [],
                StdRet[Tuple[BinaryReader, BinaryWriter]],
            ],
    ) -> StdRet[None]:
        return self._router.register_channel(name, channel_creator)

    def close_channel(self, name: str) -> bool:
        return self._router.close_channel(name)

    def add_handler(
            self, channel_name: str, handler_id: str, produces: Iterable[str],
            consumes: Iterable[EventTargetHandle],
            source_id_prefixes: Iterable[str],
    ) -> StdRet[None]:
        return self._router.add_handler(
            channel_name, handler_id, produces, consumes, source_id_prefixes,
        )

    def remove_handler(self, handler_id: str) -> bool:
        return self._router.remove_handler(handler_id)

    def add_internal_event_handler(self, channel_name: str, handler: InternalEventHandler) -> None:
        self._router.add_internal_event_handler(channel_name, handler)


class LauncherCategoryState:
    """Launcher category state."""
    __slots__ = ('config', 'category',)

    def __init__(self, config: RuntimeConfig) -> None:
        self.config = config

    @property
    def name(self) -> str:
        """The launcher category name."""
        return self.config.runtime_name

    def create_category(
            self, context: RuntimeContext, executor: ThreadPoolExecutor,
    ) -> StdRet[AbcLauncherCategory]:
        """Create the launcher category."""
        category_res = create_launcher_category(self.config)
        if category_res.has_error:
            return category_res.forward()
        try:
            init_res = executor.submit(category_res.result.initialize, context).result()
        except RuntimeError as err:
            return StdRet.pass_exception(
                TRANSLATION_CATALOG,
                _('failed creating launcher {name}'),
                err,
                name=self.config.runtime_name,
            )
        if init_res.has_error:
            return init_res.forward()
        return category_res


def _debug(action: str, msg: str, **kwargs: Any) -> None:
    if DEBUG:  # pragma no cover
        low_println(  # pragma no cover
            '[DEBUG ForemanRouter(' + action + ')] ' + (msg.format(**kwargs))
        )


NEXT_THREAD_ID = [0]


def _next_thread_id() -> str:
    NEXT_THREAD_ID[0] += 1
    return 'foreman-router-' + str(NEXT_THREAD_ID[0])


def create_handler_id(category_name: str, extension_name: str) -> str:
    """Create a unique handler ID for the extension."""
    return category_name + ':' + extension_name
