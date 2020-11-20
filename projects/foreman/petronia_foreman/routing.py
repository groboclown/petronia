
"""
Routing between launchers + internal routing for foreman.
"""

# TODO this is very complicated and should be split up.

from typing import Dict, List, Iterable, Coroutine, Callable, Optional, Any
import asyncio
from petronia_common.util import (
    PetroniaReturnError, StdRet, UserMessage, error_message,
    RET_OK_NONE,
)
from petronia_common.util import i18n as _
from petronia_common.event_stream import (
    RawEvent,
    EventForwarderTarget,
    to_raw_event_object,
    is_raw_event_object,
    raw_event_id,
    raw_event_source_id,
    raw_event_target_id,
    as_raw_event_object_data,
    BinaryWriter,
)
from .configuration import PlatformSettings
from .event_router import EventRouter
from .event_router.handler import EventTargetHandle
from .launcher import AbcLauncherCategory, RuntimeContext
from .events.foreman import EXTENSION_NAME as FOREMAN_NAME
from .events.foreman import (
    StartLauncherRequestEvent,
    StartLauncherFailedEvent,
    StartLauncherSuccessEvent,
    Error,
    Arguments,
    RestartEvent,
    StopEvent,
)
from .events.extension_loader import (
    LauncherLoadExtensionEvent,
)
from .user_message import CATALOG, display_error, display_message, translate


CONSUMABLE_EVENTS = (
    StartLauncherRequestEvent.FULL_EVENT_NAME,
    RestartEvent.FULL_EVENT_NAME,
    StopEvent.FULL_EVENT_NAME,
)

PETRONIA_INTERNAL_EXTENSION_PREFIX = 'petronia.core.'
FOREMAN_IMPL_NAME = PETRONIA_INTERNAL_EXTENSION_PREFIX + '.impl.foreman'


class LauncherCategoryRuntime:
    """Runtime information about a launcher category.
    Used to keep track of what's live on a launcher.
    """
    __slots__ = ('__name', '__category',)

    def __init__(self, name: str, category: AbcLauncherCategory) -> None:
        self.__name = name
        self.__category = category

    @property
    def name(self) -> str:
        """Name of the category"""
        return self.__name

    @property
    def category(self) -> AbcLauncherCategory:
        """Underlying category."""
        return self.__category

    def allows_producing(self, channel_name: str, event_id: str) -> bool:
        """Channel name <-> extension name."""
        raise NotImplementedError()

    def allows_consuming(self, channel_name: str, handle: EventTargetHandle) -> bool:
        """Channel name <-> extension name."""
        raise NotImplementedError()


class ForemanRuntimeContext(RuntimeContext):
    """The runtime context for one launcher category."""
    __slots__ = ('__router', '__platform', '__category', '__loop',)

    def __init__(
            self,
            platform: PlatformSettings,
            category: LauncherCategoryRuntime,
            router: EventRouter,
            loop: asyncio.AbstractEventLoop,
    ) -> None:
        self.__platform = platform
        self.__router = router
        self.__category = category
        self.__loop = loop

    def get_platform(self) -> PlatformSettings:
        return self.__platform

    def create_channel(
            self, name: str, reader: asyncio.StreamReader, writer: BinaryWriter,
    ) -> StdRet[None]:
        return self.__loop.run_until_complete(self.async_create_channel(name, reader, writer))

    def close_channel(self, name: str) -> bool:
        return self.__loop.run_until_complete(self.async_close_channel(name))

    def add_handler(
            self, channel_name: str, handler_id: str, produces: Iterable[str],
            consumes: Iterable[EventTargetHandle],
    ) -> StdRet[None]:
        return self.__loop.run_until_complete(self.async_add_handler(
            channel_name, handler_id, produces, consumes,
        ))

    def remove_handler(self, handler_id: str) -> bool:
        return self.__loop.run_until_complete(self.async_remove_handler(handler_id))

    def add_handler_listener(self, handler_id: str, event_id: str, target_id: str) -> bool:
        return self.__loop.run_until_complete(self.async_add_handler_listener(
            handler_id, event_id, target_id,
        ))

    def remove_handler_listener(self, handler_id: str, event_id: str, target_id: str) -> bool:
        return self.__loop.run_until_complete(self.async_remove_handler_listener(
            handler_id, event_id, target_id,
        ))

    async def async_create_channel(
            self, name: str, reader: asyncio.StreamReader, writer: BinaryWriter,
    ) -> StdRet[None]:
        res = await self.__router.add_channel(name, reader, writer)
        if res.has_error:
            return res.forward()
        self.__loop.create_task(res.result)
        return RET_OK_NONE

    async def async_close_channel(self, name: str) -> bool:
        return await self.__router.close_channel(name)

    async def async_add_handler(
            self, channel_name: str, handler_id: str, produces: Iterable[str],
            consumes: Iterable[EventTargetHandle],
    ) -> StdRet[None]:
        # Security check
        errors = []
        for event_id in produces:
            if not self.__category.allows_producing(channel_name, event_id):
                errors.append(error_message(
                    CATALOG,
                    _('blah security error'),
                    category=self.__category.name,
                    channel_name=channel_name,
                    event_id=event_id,
                ))
        for handle in consumes:
            if not self.__category.allows_consuming(channel_name, handle):
                errors.append(error_message(
                    CATALOG,
                    _('blah security error'),
                    category=self.__category.name,
                    channel_name=channel_name,
                    event_id=handle[0],
                    target_id=handle[1],
                ))
        if errors:
            return StdRet.pass_error(*errors)

        return await self.__router.add_handler(channel_name, handler_id, produces, consumes)

    async def async_remove_handler(self, handler_id: str) -> bool:
        # No need for a security handler in this function.
        return await self.__router.remove_handler(handler_id)

    async def async_add_handler_listener(
            self, handler_id: str, event_id: str, target_id: str,
    ) -> bool:
        # Security check.
        # Note: the handler must be registered in order for the router to allow the call.
        # However, we'll add extra security check here to ensure it's allowed.
        channel = await self.__router.get_channel_for_handler(handler_id)
        if not channel or not self.__category.allows_consuming(channel, (event_id, target_id)):
            return False

        return await self.__router.add_handler_listener(handler_id, event_id, target_id)

    async def async_remove_handler_listener(
            self, handler_id: str, event_id: str, target_id: str,
    ) -> bool:
        # No need for a security handler in this function.
        return await self.__router.remove_handler_listener(handler_id, event_id, target_id)


class ForemanRouter:
    """Maintains the channel router and handles the events for foreman.

    This keeps track of the active launcher categories.
    """
    __slots__ = (
        '__launcher_categories',
        '__router', '__state_condition', '__state_lock', '__state', '__loop',
        '__exception_handler', '__on_shutdown', '__platform',
        '__on_startup',
    )

    def __init__(
            self,
            platform_settings: PlatformSettings,
            categories: Dict[str, AbcLauncherCategory],
    ) -> None:
        self.__platform = platform_settings
        self.__launcher_categories = dict(categories)
        self.__router: Optional[EventRouter] = None
        self.__loop: Optional[asyncio.AbstractEventLoop] = None
        self.__state_condition: Optional[asyncio.Condition] = None
        self.__state_lock: Optional[asyncio.Lock] = None
        self.__exception_handler: Optional[
            Callable[[Optional[BaseException], Dict[str, Any]], None]
        ] = None
        self.__on_startup: Optional[Callable[[], Coroutine[Any, Any, StdRet[None]]]] = None
        self.__on_shutdown: Optional[Coroutine[Any, Any, None]] = None
        self.__state = 0

    def run_async(
            self,
            on_startup: Callable[[], Coroutine[Any, Any, StdRet[None]]],
            on_shutdown: Coroutine[Any, Any, None],
            exception_handler: Callable[[Optional[BaseException], Dict[str, Any]], None],
            debug: bool = False,
    ) -> None:
        """Run the router stuff asynchronously.  This runs the loop and waits for it to
        complete."""
        assert self.__state == 0
        self.__on_startup = on_startup
        self.__on_shutdown = on_shutdown
        self.__exception_handler = exception_handler
        self.__loop = asyncio.new_event_loop()
        self.__loop.set_exception_handler(self._loop_exception_handler)
        try:
            self.__loop.set_debug(debug)
            self.__loop.run_until_complete(self._async_run())
        finally:
            try:
                running_tasks = asyncio.tasks.all_tasks(self.__loop)
                if running_tasks:
                    self.__loop.run_until_complete(asyncio.tasks.gather(
                        *running_tasks, loop=self.__loop, return_exceptions=True,
                    ))
                    for task in running_tasks:
                        if not task.cancelled() and task.exception() is not None:
                            exception_handler(task.exception(), {
                                'message': UserMessage(
                                    CATALOG,
                                    _('unhandled error during shutdown'),
                                ),
                            })
                self.__loop.run_until_complete(self.__loop.shutdown_asyncgens())
            finally:
                self.__loop.close()
                self.__loop = None
                self.__exception_handler = None
                self.__on_shutdown = None

    def _loop_exception_handler(
            self, _loop: asyncio.AbstractEventLoop, context: Dict[str, Any],
    ) -> Any:
        error: Optional[BaseException] = None
        err = context.get('exception')
        if isinstance(err, BaseException):
            error = err
        if self.__exception_handler:
            self.__exception_handler(error, context)

    async def _async_run(self) -> None:
        """The asynchronous processing.  This will only exit when the router has exited."""
        assert self.__state == 0
        assert self.__router is None
        assert self.__state_condition is None
        assert self.__state_lock is None
        assert self.__loop is not None

        # Initializing
        self.__state = 1
        self.__state_lock = asyncio.Lock()
        self.__state_condition = asyncio.Condition(lock=self.__state_lock)
        access_lock = asyncio.Semaphore()
        target = ForemanEventTarget(
            self.__loop,
            self._start_launcher,
            self._load_extension,
            self._restart,
            self._set_stopping_state,
        )
        # The event router handles everything asynchronously through the RuntimeContext
        self.__router = EventRouter(access_lock, target)

        has_startup_error = await self._setup_categories()
        await self._startup(has_startup_error)
        # Wait until everything's stopped.
        await self._wait_for_stopped_state()

    async def _setup_categories(self) -> bool:
        """Setup the categories for running inside the router.  Returns True if there
        was a startup error."""
        assert self.__router
        assert self.__loop
        has_startup_error = False
        for category_name, category in self.__launcher_categories.items():
            launcher_runtime = LauncherCategoryRuntime(category_name, category)
            context = ForemanRuntimeContext(
                self.__platform, launcher_runtime, self.__router, self.__loop,
            )
            res = await category.initialize(context)
            if res.has_error:
                display_error(res.valid_error)
                has_startup_error = True
        return has_startup_error

    async def _startup(self, has_startup_error: bool) -> None:
        """Run the routing until this is stopped."""
        # Running
        assert self.__state_lock
        async with self.__state_lock:
            self.__state = 2

        # Start up the external async requirements.
        if not has_startup_error:
            if self.__on_startup:
                res = await self.__on_startup()
                if res.has_error:
                    display_error(res.valid_error)
                    has_startup_error = True

        if has_startup_error:
            await self._set_stopping_state()

    def stop(self) -> None:
        """Stop the running processes, and wait for them to stop."""
        if self.is_active():
            assert self.__loop
            self.__loop.run_until_complete(self._set_stopping_state())
            self.__loop.run_until_complete(self._wait_for_stopped_state())

    def is_active(self) -> bool:
        """Is the router still active (running and not shutting down)"""
        return self.__state == 2

    def is_stopping(self) -> bool:
        """Is the router in the stopping state?"""
        return self.__state == 3

    def is_stopped(self) -> bool:
        """Has the router stopped?"""
        return self.__state == 4

    async def _internal_stop(self) -> None:
        """Shuts down the internals that run inside the router."""
        for category in self.__launcher_categories.values():
            res = await category.stop()
            if res.has_error:
                display_error(res.valid_error)
        if self.__on_shutdown:
            await self.__on_shutdown

    async def _set_state(self, state: int) -> None:
        assert self.__state_lock is not None
        assert self.__state_condition is not None
        async with self.__state_lock:
            assert self.__state <= state
            self.__state = state
            self.__state_condition.notify_all()

    async def _set_stopping_state(self) -> None:
        """Special handler for setting the state to stopping."""
        assert self.__state_lock is not None
        assert self.__state_condition is not None
        run_stop = False
        async with self.__state_lock:
            if self.__state == 3:
                # we're already in the stopping state.  Just send a notification.
                self.__state_condition.notify_all()
            if self.__state == 2:
                # we're in running mode.
                run_stop = True
                self.__state = 3
                self.__state_condition.notify_all()
        if run_stop:
            async with self.__state_condition:
                if self.__state == 3:
                    await self._internal_stop()
                    self.__state = 4
                    self.__state_condition.notify_all()

    async def _wait_for_stopped_state(self) -> None:
        """Wait for the state to change to stopped."""
        assert self.__state_lock is not None
        assert self.__state_condition is not None
        async with self.__state_lock:
            await self.__state_condition.wait_for(self.is_stopped)

    async def _start_launcher(self, source_id: str, event: StartLauncherRequestEvent) -> None:
        """Add a new launcher for a category."""
        assert self.__router
        category = self.__launcher_categories.get(event.launcher)
        if category is None:
            failed_event = StartLauncherFailedEvent(event.identifier, Error(
                'no-such-launcher-category',
                FOREMAN_NAME,
                'No such launcher category {category}', [Arguments('category', event.launcher)],
            ))
            await self.__router.inject_event(to_raw_event_object(
                StartLauncherFailedEvent.FULL_EVENT_NAME,
                StartLauncherRequestEvent.UNIQUE_TARGET_LAUNCHER,
                source_id,
                failed_event.export_data(),
            ))
            return
        permissions: Dict[str, List[str]] = {
            permission.action: permission.resources
            for permission in event.permissions
        }
        res = await category.start_launcher(event.identifier, permissions)
        if res.has_error:
            arguments = [Arguments('category', event.launcher)]
            full_message = ''
            i = 0
            for msg in res.valid_error.messages():
                arguments.append(
                    Arguments(f'message{i}', translate(msg.message, **msg.arguments)),
                )
                i += 1
            arguments.append(Arguments('message', full_message))
            failed_event = StartLauncherFailedEvent(event.identifier, Error(
                'launcher-create-failed',
                FOREMAN_NAME,
                'Failed to create launcher from category {category}; {message}',
                arguments,
            ))
            await self.__router.inject_event(to_raw_event_object(
                StartLauncherFailedEvent.FULL_EVENT_NAME,
                StartLauncherRequestEvent.UNIQUE_TARGET_LAUNCHER,
                source_id,
                failed_event.export_data(),
            ))
            return
        success_event = StartLauncherSuccessEvent(event.identifier)
        await self.__router.inject_event(to_raw_event_object(
            StartLauncherSuccessEvent.FULL_EVENT_NAME,
            StartLauncherRequestEvent.UNIQUE_TARGET_LAUNCHER,
            source_id,
            success_event.export_data(),
        ))

    async def _load_extension(self, target_id: str, event: LauncherLoadExtensionEvent) -> None:
        """Load the new extension inside a loaded launcher."""
        assert self.__router
        if not target_id.startswith(FOREMAN_IMPL_NAME + ':'):
            display_message(UserMessage(
                CATALOG,
                _('Attempted to load extension with bad target_id {target_id}'),
                target_id=target_id,
            ))
            return
        if len(event.version) != 3:
            display_message(UserMessage(
                CATALOG,
                _('Attempted to load extension {name} with bad version {version}'),
                name=event.name,
                version=event.version,
            ))
            return
        launcher_id = target_id[len(FOREMAN_IMPL_NAME) + 1:]
        for category in self.__launcher_categories.values():
            if launcher_id in category.get_active_launcher_ids():
                # Found the category that owns the requested launcher.
                res = await category.start_extension(
                    launcher_id, event.name,
                    (event.version[0], event.version[1], event.version[2]),
                    event.location,
                )
                if res.has_error:
                    display_error(res.valid_error, True)
                return
        return

    async def _restart(self) -> None:
        """Restart the launchers and begin the boot process again."""
        assert self.__loop
        assert self.__state_lock
        async with self.__state_lock:
            if self.__state != 2:
                display_message(UserMessage(
                    CATALOG,
                    _('invalid state for restart')
                ))
                return
            # Mark this as restarting, so we don't get other stop
            # requests coming in.
            # This doesn't actually enter a stop state, because that
            # will trigger other things we don't want.
            self.__state = 5
        await self._internal_stop()
        has_startup_error = await self._setup_categories()
        await self._startup(has_startup_error)


class ForemanEventTarget(EventForwarderTarget):
    """Processes events directed to the Foreman process."""
    __slots__ = (
        '__stop_func', '__start_launcher_func', '__restart_func', '__load_ext_func',
        '__loop',
    )

    def __init__(
            self,
            loop: asyncio.AbstractEventLoop,
            start_launcher_func: Callable[
                [str, StartLauncherRequestEvent], Coroutine[Any, Any, None],
            ],
            load_ext_func: Callable[
                [str, LauncherLoadExtensionEvent], Coroutine[Any, Any, None],
            ],
            restart_func: Callable[[], Coroutine[Any, Any, None]],
            stop_func: Callable[[], Coroutine[Any, Any, None]],
    ) -> None:
        self.__loop = loop
        self.__start_launcher_func = start_launcher_func
        self.__load_ext_func = load_ext_func
        self.__restart_func = restart_func
        self.__stop_func = stop_func

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        if event_id == StartLauncherRequestEvent.FULL_EVENT_NAME:
            return (
               target_id == StartLauncherRequestEvent.UNIQUE_TARGET_LAUNCHER
               and source_id.startswith(PETRONIA_INTERNAL_EXTENSION_PREFIX)
            )
        if event_id == RestartEvent.FULL_EVENT_NAME:
            return (
                target_id == RestartEvent.UNIQUE_TARGET_RESTART
                and source_id.startswith(PETRONIA_INTERNAL_EXTENSION_PREFIX)
            )
        if event_id == StopEvent.FULL_EVENT_NAME:
            return (
                target_id == StopEvent.UNIQUE_TARGET_STOP
                and source_id.startswith(PETRONIA_INTERNAL_EXTENSION_PREFIX)
            )
        if event_id == LauncherLoadExtensionEvent.FULL_EVENT_NAME:
            return (
                target_id.startswith(FOREMAN_IMPL_NAME + ':')
                and source_id.startswith(PETRONIA_INTERNAL_EXTENSION_PREFIX)
            )
        return False

    async def consume(self, event: RawEvent) -> bool:
        # To get to this method, it has already passed the can_consume, so the
        # source and targets are verified.
        # Remember: return True means de-register this listener.
        if not is_raw_event_object(event):
            return False
        if raw_event_id(event) == StartLauncherRequestEvent.FULL_EVENT_NAME:
            start_res = StartLauncherRequestEvent.parse_data(as_raw_event_object_data(event))
            if start_res.has_error:
                display_error(start_res.valid_error)
                return False
            self.__loop.create_task(self.__start_launcher_func(
                raw_event_source_id(event),
                start_res.result,
            ))
            return False
        if raw_event_id(event) == RestartEvent.FULL_EVENT_NAME:
            self.__loop.create_task(self.__restart_func())
            return False
        if raw_event_id(event) == StopEvent.FULL_EVENT_NAME:
            self.__loop.create_task(self.__stop_func())
            return False
        if raw_event_id(event) == LauncherLoadExtensionEvent.FULL_EVENT_NAME:
            load_res = LauncherLoadExtensionEvent.parse_data(as_raw_event_object_data(event))
            if load_res.has_error:
                display_error(load_res.valid_error)
                return False
            self.__loop.create_task(self.__load_ext_func(
                raw_event_target_id(event),
                load_res.result,
            ))
        return False

    def on_error(self, error: PetroniaReturnError) -> bool:
        # return true == de-register this target.
        return False

    def on_eof(self) -> None:
        pass
