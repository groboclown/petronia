"""
Context for the router target handlers.
"""

from typing import Dict, Callable, Union, Optional
from concurrent.futures import ThreadPoolExecutor
from petronia_common.event_stream import RawEventObject, to_raw_event_object
from petronia_common.util import PetroniaReturnError, UserMessage
from petronia_common.util import i18n as _
from .event_handlers import TargetHandlerRuntimeContext
from ..launcher import AbcLauncherCategory
from ..events import foreman
from ..user_message import display_error, display_message, CATALOG


class RouterContext(TargetHandlerRuntimeContext):
    """Runtime context for the target handlers.  Note that all async calls happen within the
    event thread, so special care must be taken to ensure that they do not cause a deadlock
    with the thread loop."""
    __slots__ = (
        '__categories', '__shutdown', '__restart', '__generate_event',
        '__add_handler_listener', '__remove_handler_listener',
        '__executor',
    )

    def __init__(  # pylint: disable=too-many-arguments
            self,
            categories: Dict[str, AbcLauncherCategory],
            shutdown: Callable[[], None],
            restart: Callable[[], None],
            generate_event: Callable[[RawEventObject], None],
            add_handler_listener: Callable[[str, Optional[str], Optional[str]], None],
            remove_handler_listener: Callable[[str, Optional[str], Optional[str]], None],
            executor: ThreadPoolExecutor,
    ) -> None:
        self.__categories = dict(categories)
        self.__shutdown = shutdown
        self.__restart = restart
        self.__generate_event = generate_event
        self.__add_handler_listener = add_handler_listener
        self.__remove_handler_listener = remove_handler_listener
        self.__executor = executor

    def do_shutdown(self) -> None:
        self.__executor.submit(self.__shutdown)

    def do_restart(self, requested: bool, error: Optional[PetroniaReturnError]) -> None:
        self.__executor.submit(self.__restart)

    def _async_inject_event(
            self, event_id: str, source_id: str, target_id: str,
            event: Union[
                foreman.StartLauncherSuccessEvent,
                foreman.StartLauncherFailedEvent,
                foreman.LauncherLoadExtensionSuccessEvent,
                foreman.LauncherLoadExtensionFailedEvent,
            ],
    ) -> None:
        """Runs the event in the background of the current loop."""
        self.__executor.submit(
            self.__generate_event,
            to_raw_event_object(event_id, source_id, target_id, event.export_data()),
        )

    def _inject_event(
            self, event_id: str, source_id: str, target_id: str,
            event: Union[
                foreman.StartLauncherSuccessEvent,
                foreman.StartLauncherFailedEvent,
                foreman.LauncherLoadExtensionSuccessEvent,
                foreman.LauncherLoadExtensionFailedEvent,
            ],
    ) -> None:
        """Generates the event right now."""
        self.__generate_event(
            to_raw_event_object(event_id, source_id, target_id, event.export_data())
        )

    def start_launcher(
            self, source_id: str, event: foreman.StartLauncherRequestEvent,
    ) -> None:
        category_name = event.launcher
        category = self.__categories.get(category_name)
        if category is None:
            display_message(UserMessage(
                CATALOG,
                _('Requested to start unknown launcher category ({name})'),
                name=category_name,
            ))
            self._async_inject_event(
                event_id=foreman.StartLauncherFailedEvent.FULL_EVENT_NAME,
                source_id=foreman.StartLauncherRequestEvent.UNIQUE_TARGET_FQN,
                target_id=source_id,
                event=foreman.StartLauncherFailedEvent(
                    event.identifier,
                    foreman.Error(
                        'no-such-launcher-category',
                        foreman.EXTENSION_NAME,
                        'requested category {category} is not registered.',
                        [foreman.Arguments('category', category_name)],
                    ),
                ),
            )
            return
        launcher_id = event.identifier
        permissions = {
            p.action: list(p.resources)
            for p in event.permissions
        }

        def in_parallel() -> None:
            assert category is not None  # mypy requirement
            res = category.start_launcher(launcher_id, permissions)
            if res.ok:
                target_id = launcher_id_as_target_id(launcher_id)
                # Run in parallel, so let the generate just run.
                self._inject_event(
                    event_id=foreman.StartLauncherSuccessEvent.FULL_EVENT_NAME,
                    source_id=foreman.StartLauncherRequestEvent.UNIQUE_TARGET_FQN,
                    target_id=source_id,
                    event=foreman.StartLauncherSuccessEvent(
                        launcher_id,
                        target_id,
                    ),
                )
                return

            # Run in parallel, so let the generate just run.
            self._inject_event(
                event_id=foreman.StartLauncherFailedEvent.FULL_EVENT_NAME,
                source_id=foreman.StartLauncherRequestEvent.UNIQUE_TARGET_FQN,
                target_id=source_id,
                event=foreman.StartLauncherFailedEvent(
                    launcher_id,
                    create_event_error(
                        'launcher-failed-to-start', category_name, res.valid_error,
                    ),
                ),
            )

        self.__executor.submit(in_parallel)

    def load_extension(
            self, source_id: str, target_id: str, event: foreman.LauncherLoadExtensionRequestEvent,
    ) -> None:
        launcher_id = target_id_as_launcher_id(target_id)
        if launcher_id is None:
            display_message(UserMessage(
                CATALOG,
                _('Requested to load extension ({name}) for non-launcher target ({target})'),
                name=event.name, target=target_id,
            ))
            self._async_inject_event(
                event_id=foreman.LauncherLoadExtensionFailedEvent.FULL_EVENT_NAME,
                source_id=target_id,
                target_id=source_id,
                event=foreman.LauncherLoadExtensionFailedEvent(
                    name=event.name,
                    error=foreman.Error(
                        'invalid-launcher-id',
                        None,
                        'requested target id {target_id} must be a valid launcher target',
                        [foreman.Arguments('target_id', target_id)],
                    ),
                ),
            )
            return

        def start_extension(cat: AbcLauncherCategory, cat_name: str) -> None:
            assert launcher_id is not None  # mypy requirement
            res = cat.start_extension(
                launcher_id,
                create_handler_id(cat_name, launcher_id, event.name),
                event.name,
                (event.version[0], event.version[1], event.version[2]),
                event.location,
                event.configuration,
            )
            if res.ok:
                self._inject_event(
                    event_id=foreman.LauncherLoadExtensionSuccessEvent.FULL_EVENT_NAME,
                    source_id=target_id,
                    target_id=source_id,
                    event=foreman.LauncherLoadExtensionSuccessEvent(
                        name=event.name,
                    ),
                )
                return
            self._inject_event(
                event_id=foreman.LauncherLoadExtensionFailedEvent.FULL_EVENT_NAME,
                source_id=target_id,
                target_id=source_id,
                event=foreman.LauncherLoadExtensionFailedEvent(
                    name=event.name,
                    error=create_event_error(
                        'failed-to-load-extension', target_id, res.valid_error,
                    ),
                ),
            )

        # note that launcher id == channel name.
        for category_name, category in self.__categories.items():
            if launcher_id in category.get_active_launcher_ids():
                self.__executor.submit(start_extension, category, category_name)
                return

        # No such launcher_id active.
        display_message(UserMessage(
            CATALOG,
            _(
                'Requested to load extension ({name}) for unknown launcher '
                '{launcher} (target {target})'
            ),
            launcher=launcher_id, target=target_id, name=event.name,
        ))
        self._async_inject_event(
            event_id=foreman.LauncherLoadExtensionFailedEvent.FULL_EVENT_NAME,
            source_id=target_id,
            target_id=source_id,
            event=foreman.LauncherLoadExtensionFailedEvent(
                name=event.name,
                error=foreman.Error(
                    'unknown-launcher-id',
                    None,
                    'requested target id {target_id} references a launcher that does not exist',
                    [foreman.Arguments('target_id', target_id)],
                ),
            ),
        )

    def add_event_listener(
            self, target_id: str, event: foreman.ExtensionAddEventListenerEvent,
    ) -> None:
        launcher_id = target_id_as_launcher_id(target_id)
        if launcher_id is None:
            # No error event to send.
            display_message(UserMessage(
                CATALOG,
                _('Requested to add event listener for non-launcher target ({target})'),
                target=target_id,
            ))
            return
        for category_name, category in self.__categories.items():
            if launcher_id in category.get_active_launcher_ids():
                for listen_to in event.events:
                    self.__add_handler_listener(
                        create_handler_id(category_name, launcher_id, event.extension_name),
                        listen_to.event_id, listen_to.target_id,
                    )
                return
        # launcher not found, but no error to send.
        display_message(UserMessage(
            CATALOG,
            _(
                'Requested to add event listeners for unknown launcher '
                '{launcher} (target {target})'
            ),
            launcher=launcher_id, target=target_id,
        ))

    def remove_event_listener(
            self, target_id: str, event: foreman.ExtensionRemoveEventListenerEvent,
    ) -> None:
        launcher_id = target_id_as_launcher_id(target_id)
        if launcher_id is None:
            # No error event to send.
            display_message(UserMessage(
                CATALOG,
                _('Requested to remove event listener for non-launcher target ({target})'),
                target=target_id,
            ))
            return
        for category_name, category in self.__categories.items():
            if launcher_id in category.get_active_launcher_ids():
                for listen_to in event.events:
                    self.__remove_handler_listener(
                        create_handler_id(category_name, launcher_id, event.extension_name),
                        listen_to.event_id, listen_to.target_id,
                    )
                return
        # launcher not found, but no error to send.
        display_message(UserMessage(
            CATALOG,
            _(
                'Requested to remove event listeners for unknown launcher '
                '{launcher} (target {target})'
            ),
            launcher=launcher_id, target=target_id,
        ))


LAUNCHER_TARGET_PREFIX = foreman.EXTENSION_NAME + ':launcher:'


def launcher_id_as_target_id(launcher_id: str) -> str:
    """Convert the requested launcher id into an appropriate target id."""
    return LAUNCHER_TARGET_PREFIX + launcher_id


def target_id_as_launcher_id(target_id: str) -> Optional[str]:
    """Convert the target id into a launcher id, or None if it is not in the correct format."""
    if target_id.startswith(LAUNCHER_TARGET_PREFIX):
        return target_id[len(LAUNCHER_TARGET_PREFIX):]
    return None


def create_handler_id(category_name: str, launcher_id: str, extension_name: str) -> str:
    """Create a unique handler ID for the category's launcher."""
    return category_name + ':' + launcher_id + ':' + extension_name


def create_event_error(
        identifier: str, source: Optional[str], error: PetroniaReturnError,
) -> foreman.Error:
    """Create the event object based on this error value."""

    display_error(error)
    message = ''
    args: Dict[str, Union[str, int, float]] = {}
    for msg in error.messages():
        if message:
            message += '; '
        message += msg.message
        for key, val in msg.arguments.items():
            if isinstance(val, (str, int, float)):
                args[key] = val
            else:
                args[key] = repr(val)

    return foreman.Error(
        identifier, source, message, [
            foreman.Arguments(key, val)
            for key, val in args.items()
        ],
    )
