"""The routing mechanism specific to foreman, with all the foreman logic."""

from typing import Dict, List, Tuple, Iterable, Callable, Optional
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from queue import Queue, Empty
from petronia_common.event_stream import (
    EventForwarderTarget, BinaryWriter, RawEventObject, BinaryReader,
)
from petronia_common.util import StdRet, UserMessage, collect_errors_from, RET_OK_NONE
from petronia_common.util import i18n as _
from .event_handlers import ExtensionLoaderTarget, InternalTarget
from .router_context import RouterContext
from ..configuration import PlatformSettings, LauncherConfig
from ..constants import EXTENSION_LOADER_CHANNEL, INTERNAL_CHANNEL_PATTERN, TRANSLATION_CATALOG
from ..event_router import EventRouter
from ..event_router.handler import EventTargetHandle
from ..launcher import AbcLauncherCategory, RuntimeContext, create_launcher_category
from ..user_message import display_error, display_message

_REQUEST_STOP = 'stop'
_REQUEST_LAUNCH = 'launch:'
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
        '__platform', '__category_states', '__executor', '__state', '__queue', '__lock',
        '__state_condition', '__thread', 'stop_timeout',
    )

    def __init__(
            self,
            platform: PlatformSettings,
            categories: List[LauncherConfig],
    ) -> None:
        self.__platform = platform
        self.__category_states: Dict[str, LauncherCategoryState] = {
            config.launcher_name: LauncherCategoryState(config)
            for config in categories
        }
        self.__executor: Optional[ThreadPoolExecutor] = None
        self.__state = 0
        self.__lock = threading.RLock()
        self.__queue = Queue()  # type: Queue[str]
        self.__state_condition = threading.Condition(self.__lock)
        self.__thread: Optional[threading.Thread] = None
        self.stop_timeout = 10.0

    def start(self, timeout: Optional[float] = None) -> bool:
        """Starts up the router.  If it is already running, then this is a no-op.  If it
        is currently shutting down, then this will wait for the shutdown to complete, then
        start the router.  If the router is starting, then this will wait for the start to
        complete.  Returns False if the timeout is exceeded."""
        with self.__lock:
            while self.__state != _STATE_RUNNING:
                # Capture the current state inside the loop, because the if statements
                # wait for the state to change.
                current_state = self.__state
                if current_state in (_STATE_BOOTING, _STATE_STARTING, _STATE_STOPPING):
                    res = self.__state_condition.wait_for(
                        lambda: self.__state != current_state,
                        timeout,
                    )
                    if not res:
                        # Timeout.
                        return False
                    continue
                if self.__state == _STATE_STOPPED:
                    # Start the thread + router.
                    assert self.__thread is None, 'Did not stop router thread correctly'
                    # This + constructor is the only time outside the thread loop the state changes.
                    # It can only be done while the thread is stopped.
                    self.__state = _STATE_BOOTING
                    self.__thread = threading.Thread(target=self._thread_runner, daemon=False)
                    self.__thread.start()
                    # Keep looping until it's started.
                    continue
        return True

    def join(self, timeout: Optional[float] = None) -> bool:
        """Wait for the state to be stopped."""
        end_time = time.time() + (timeout or 0.0)
        while True:
            if timeout is not None and end_time > time.time():
                return False
            with self.__lock:
                if self.__state == _STATE_STOPPED:
                    return True
            current_thread = self.__thread
            if current_thread:
                # Signal friendly join.
                current_thread.join(1)

    def stop(self, timeout: Optional[float] = None) -> bool:
        """Stops the router and waits for it to stop.  If the router is not running, then this
        is a no-op.  If the router is currently starting, then this will interrupt the startup
        and stop whatever has already started.  If the router is stopping, then this will wait
        for the stop to complete.

        Returns False if the timeout is exceeded."""
        with self.__lock:
            while self.__state != _STATE_STOPPED:
                current_state = self.__state
                if current_state in (_STATE_BOOTING, _STATE_STARTING, _STATE_STOPPING):
                    res = self.__state_condition.wait_for(
                        lambda: self.__state != current_state,
                        timeout,
                    )
                    if not res:
                        # Timeout.
                        return False
                    continue
                if current_state == _STATE_RUNNING:
                    self.__queue.put(_REQUEST_STOP)
                    res = self.__state_condition.wait_for(
                        lambda: self.__state != current_state,
                        timeout,
                    )
                    if not res:
                        # Timeout.
                        return False
        return True

    def boot_launcher(self, launcher_config_name: str) -> None:
        """Starts up a boot-time launcher.  The launcher config name will be used as the
        channel name."""
        with self.__lock:
            assert self.__state == _STATE_RUNNING, 'router not running'
            self.__queue.put(_REQUEST_LAUNCH + launcher_config_name)

    def _thread_runner(self) -> None:
        """A thread runnable method that monitors the queue for actions to perform on the
        asyncio items in the loop."""

        # Start up the thread.
        with self.__lock:
            assert self.__state == _STATE_BOOTING, 'Not in correct state to start thread'

        sem = threading.Semaphore()
        executor = ThreadPoolExecutor()
        router, categories = self._create_router_launchers(sem, executor)

        with self.__lock:
            self.__state = _STATE_RUNNING
            self.__state_condition.notify_all()

        while True:
            event = self.__queue.get(block=True)
            # print(f"Foreman processing request `{event}`")
            if event.startswith(_REQUEST_LAUNCH):
                launcher_config_name = event[len(_REQUEST_LAUNCH):]
                executor.submit(ForemanRouter._add_boot_launcher, launcher_config_name, categories)
            elif event == _REQUEST_STOP:
                # TODO there should be two requests:
                #   a "nice" stop, which goes through the nice shutdown process for all the
                #   extensions,
                #   and a "hard" stop, which ignores extensions.
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

                ForemanRouter._stop_launchers(categories)
                ForemanRouter._stop_channels(router)

                with self.__lock:
                    self.__state = _STATE_STOPPED
                    self.__state_condition.notify_all()
                    self.__thread = None
                return

    @staticmethod
    def _add_boot_launcher(
            launcher_category: str, categories: Dict[str, AbcLauncherCategory],
    ) -> None:
        """Add a new launcher to the router.
        This must be called from in the thread's event loop."""
        category = categories.get(launcher_category)
        if category is None:
            display_message(UserMessage(
                TRANSLATION_CATALOG,
                _('Requested to boot launch a non-existent category ({category})'),
                category=launcher_category,
            ))
            return
        if category.config.boot_channel is None:
            display_message(UserMessage(
                TRANSLATION_CATALOG,
                _('Requested to boot launch a non-bootable category ({category})'),
                category=launcher_category,
            ))
            return

        res = category.start_launcher(category.config.boot_channel, {'boot': []})
        if res.has_error:
            display_error(res.valid_error)

    @staticmethod
    def _stop_launchers(categories: Dict[str, AbcLauncherCategory]) -> None:
        """Stop all running launchers.  Errors are displayed but not returned."""
        errors: List[StdRet[None]] = []
        for launcher_category in categories.values():
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
        self.stop()
        self.start()

    def _stop(self) -> None:
        """Internal stop callback."""
        self.stop()

    def _create_router_launchers(
            self, sem: threading.Semaphore, executor: ThreadPoolExecutor,
    ) -> Tuple[EventRouter, Dict[str, AbcLauncherCategory]]:
        """Create the router specifically for foreman interaction.
        """

        router = EventRouter(sem, executor=executor)

        launcher_context = LauncherRuntimeContext(self.__platform, router, executor)

        # Create launcher categories based on this router.
        # They all need to be initialized.  Which means they need to be created.
        categories: Dict[str, AbcLauncherCategory] = {}
        for state in self.__category_states.values():
            cat_res = state.create_category(launcher_context, executor)
            if cat_res.has_error:
                display_error(cat_res.valid_error)
            else:
                categories[state.name] = cat_res.result

        def send_event_to_extension_loader(event: RawEventObject) -> None:
            assert self.__executor is not None, 'loop stopped'
            self.__executor.submit(
                router.inject_event_to_channel,
                EXTENSION_LOADER_CHANNEL, event,
            )

        def add_handler_listener(
                handler_id: str, event_id: Optional[str], target_id: Optional[str],
        ) -> None:
            assert self.__executor is not None, 'loop stopped'
            self.__executor.submit(router.add_handler_listener, handler_id, event_id, target_id)

        def remove_handler_listener(
                handler_id: str, event_id: Optional[str], target_id: Optional[str],
        ) -> None:
            assert self.__executor is not None, 'loop stopped'
            self.__executor.submit(router.remove_handler_listener, handler_id, event_id, target_id)

        context = RouterContext(
            categories=categories,
            shutdown=self._stop,
            restart=self._restart,
            generate_event=send_event_to_extension_loader,
            add_handler_listener=add_handler_listener,
            remove_handler_listener=remove_handler_listener,
            executor=executor,
        )
        router.add_reservation_callback(
            EXTENSION_LOADER_CHANNEL,
            ExtensionLoaderCallback(ExtensionLoaderTarget(context, executor)),
        )

        internal_target = InternalTarget(context, executor)

        def internal_channel_callback(name: str) -> StdRet[Optional[EventForwarderTarget]]:
            if INTERNAL_CHANNEL_PATTERN.match(name):
                return StdRet.pass_ok(internal_target)
            return RET_OK_NONE

        router.add_reservation_callback(
            INTERNAL_CHANNEL_PATTERN,
            internal_channel_callback,
        )

        return router, categories


class ExtensionLoaderCallback:
    """A callback that conforms to the ChannelReservationCallback"""
    __slots__ = ('__target',)

    def __init__(self, target: ExtensionLoaderTarget) -> None:
        self.__target: Optional[ExtensionLoaderTarget] = target

    def __call__(self, name: str) -> StdRet[Optional[EventForwarderTarget]]:
        if name != EXTENSION_LOADER_CHANNEL:
            return RET_OK_NONE
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
    __slots__ = ('_router', '_platform', '_executor')

    def __init__(
            self, platform: PlatformSettings, router: EventRouter, executor: ThreadPoolExecutor,
    ) -> None:
        self._router = router
        self._platform = platform
        self._executor = executor

    def get_platform(self) -> PlatformSettings:
        return self._platform

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
    ) -> StdRet[None]:
        return self._router.add_handler(channel_name, handler_id, produces, consumes)

    def remove_handler(self, handler_id: str) -> bool:
        return self._router.remove_handler(handler_id)


class LauncherCategoryState:
    """Launcher category state."""
    __slots__ = ('config', 'category',)

    def __init__(self, config: LauncherConfig) -> None:
        self.config = config

    @property
    def name(self) -> str:
        """The launcher category name."""
        return self.config.launcher_name

    def create_category(
            self, context: LauncherRuntimeContext, executor: ThreadPoolExecutor,
    ) -> StdRet[AbcLauncherCategory]:
        """Create the launcher category."""
        category_res = create_launcher_category(self.config)
        if category_res.has_error:
            return category_res.forward()
        init_res = executor.submit(category_res.result.initialize, context).result()
        if init_res.has_error:
            return init_res.forward()
        return category_res
