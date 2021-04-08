"""
Creates the in-memory launcher category.
"""

from typing import Sequence, Tuple, Dict, List, Optional
import json
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, UserMessage, join_errors, RET_OK_NONE, DelayedValueHolder
from petronia_common.util import i18n as _
from .load_launcher import (
    get_entrypoint_name, connect_launcher, import_module, DelayedStartThread,
)
from .stream import ReadWriteStream
from ..abc import AbcLauncherCategory, RuntimeContext
from ..util import (
    LaunchedInstance,
    launcher_category_not_initialized,
    launcher_already_registered,
    launcher_stopped, launcher_not_loaded,
)
from ... import user_message
from ...configuration import RuntimeConfig
from ...events import foreman
from ...process_mgmt.util import create_cmd
from ...constants import TRANSLATION_CATALOG
from ...user_message import trace_channel


WAIT_FOR_EXTENSION_LOAD_TIMEOUT_OPTION = 'extension-load-timeout'
WAIT_FOR_EXTENSION_LOAD_TIMEOUT_DEFAULT = '60.0'
ARGUMENT_OPTION_PREFIX = 'arg.'


def create_memory_launcher(options: RuntimeConfig) -> AbcLauncherCategory:
    """Create a command launcher category"""
    return MemoryLauncherCategory(options)


class MemoryLauncherCategory(AbcLauncherCategory):
    """Launches launchers in-memory."""

    __slots__ = ('_launchers', '_context', '_start_timeout', '_args', '_alive')

    def __init__(self, options: RuntimeConfig) -> None:
        AbcLauncherCategory.__init__(self, options)
        self._launchers: Dict[str, LauncherData] = {}
        self._context: Optional[RuntimeContext] = None
        self._start_timeout = options.options.get(
            WAIT_FOR_EXTENSION_LOAD_TIMEOUT_OPTION,
            WAIT_FOR_EXTENSION_LOAD_TIMEOUT_DEFAULT,
        )
        args: List[str] = []
        i = 1
        arg_name = ARGUMENT_OPTION_PREFIX + str(i)
        while arg_name in options.options:
            args.append(options.options[arg_name])
            i += 1
            arg_name = ARGUMENT_OPTION_PREFIX + str(i)
        self._args = tuple(args)
        self._alive = True

    def is_valid(self) -> StdRet[None]:
        try:
            float(self._start_timeout)
        except (ValueError, TypeError):
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG,
                _('Invalid option {option}; must be a number, found {value}'),
                option=WAIT_FOR_EXTENSION_LOAD_TIMEOUT_OPTION,
                value=self._start_timeout,
            )
        return RET_OK_NONE

    def initialize(self, context: RuntimeContext) -> StdRet[None]:
        if not self._alive:
            return launcher_stopped()
        self._context = context
        return RET_OK_NONE

    def start_extension(  # pylint:disable=too-many-return-statements
            self, handler_id: str, start_event: foreman.LauncherStartExtensionRequestEvent,
    ) -> StdRet[None]:
        trace_channel(handler_id, f"Starting launcher for extension {start_event.name}")
        if not self._alive:
            return launcher_stopped()
        if not self._context:
            return launcher_category_not_initialized()
        if handler_id in self._launchers:
            return launcher_already_registered(handler_id)
        module_res = import_module(
            start_event.name,
            start_event.version,
            start_event.location,
            self.config,
        )
        try:
            config_data = json.loads(start_event.configuration or '{}')
        except json.JSONDecodeError as err:
            return StdRet.pass_exception(
                TRANSLATION_CATALOG,
                _('extension {name}-{version} configuration data'),
                err,
                name=start_event.name,
                version=start_event.version,
            )
        if module_res.has_error:
            return module_res.forward()
        entrypoint_name = get_entrypoint_name(self.config)
        cmd_args = create_cmd(self._args, '.', -1, handler_id, {
            'EXTENSION_NAME': start_event.name,
        })

        # Ignore the permissions.  It's running in Foreman space, which means we can't limit
        # what it can do.

        loaded_launcher: DelayedValueHolder[LauncherData] = DelayedValueHolder()

        # Create the launcher inside the registration process.
        def register_callback() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            # Re-do our assertions for completion; not really necessary,
            # but that's based on the current implementation details.
            if not self._context:
                return launcher_category_not_initialized()
            to_launcher = ReadWriteStream(f'to_launcher {handler_id}')
            from_launcher = ReadWriteStream(f'from_launcher {handler_id}')
            thread_res = connect_launcher(
                entrypoint_name,
                module_res.result,
                MemoryLauncherCategory._on_error,
                MemoryLauncherCategory._on_complete,
                cmd_args,
                to_launcher,
                from_launcher,
                config_data,
            )
            if thread_res.has_error:
                return thread_res.forward()

            loaded_launcher.value = LauncherData(
                handler_id, self.config, thread_res.result, to_launcher, from_launcher,
            )
            self._launchers[handler_id] = loaded_launcher.non_none
            return loaded_launcher.non_none.as_channel_res()

        res = self._context.register_channel(handler_id, register_callback)
        if res.has_error:
            if loaded_launcher.has_value():
                stop_res = loaded_launcher.non_none.stop()
                del self._launchers[handler_id]
                if stop_res.has_error:
                    return StdRet.pass_error(res.valid_error, stop_res.valid_error)
            return res
        self._context.add_handler(
            handler_id, handler_id,
            start_event.send_access.event_ids, [], start_event.send_access.source_id_prefixes,
        )
        loaded_launcher.non_none.thread.begin_ok()

        return res

    def get_active_handler_ids(self) -> Sequence[str]:
        return tuple(self._launchers.keys())

    def stop_extension(self, handler_id: str) -> StdRet[None]:
        launcher = self._launchers.get(handler_id)
        if launcher is None or self._context is None:
            return launcher_not_loaded(handler_id)
        res = launcher.stop()
        if res.ok:
            del self._launchers[handler_id]
        self._context.remove_handler(handler_id)
        self._context.close_channel(handler_id)
        return res

    def stop(self) -> StdRet[None]:
        # Could make this parallel.
        self._alive = False
        errors: List[UserMessage] = []
        stopped: List[str] = []
        # Make a copy of the items, because there are scenarios
        # where a launcher can stop while trying to call stop.
        for name, launcher in list(self._launchers.items()):
            res = launcher.stop()
            if res.has_error:
                errors.extend(res.valid_error.messages())
            else:
                stopped.append(name)
        for name in stopped:
            if name in self._launchers:
                del self._launchers[name]
        if errors:
            return StdRet.pass_error(join_errors(*errors))
        return RET_OK_NONE

    @staticmethod
    def _on_error(module_name: str, extension_point: str, err: BaseException) -> None:
        user_message.display_error(
            StdRet.pass_exception(
                TRANSLATION_CATALOG,
                _('Encountered error running extension in module {mod_name}, function {func_name}'),
                err,
                mod_name=module_name,
                func_name=extension_point,
            ).valid_error, True,
        )

    @staticmethod
    def _on_complete(module_name: str, extension_point: str) -> None:
        user_message.display(
            TRANSLATION_CATALOG,
            _('Completed running extension in module {mod_name}, function {func_name}'),
            mod_name=module_name,
            func_name=extension_point,
        )


class LauncherData(LaunchedInstance):
    """Data container for an in-memory launcher."""
    __slots__ = ('thread', 'to_launcher', 'from_launcher',)

    def __init__(  # pylint:disable=too-many-arguments
            self,
            launcher_id: str,
            options: RuntimeConfig,
            thread: DelayedStartThread,
            to_launcher: ReadWriteStream, from_launcher: ReadWriteStream,
    ) -> None:
        LaunchedInstance.__init__(
            self, launcher_id, options, from_launcher, to_launcher, self._local_stop,
        )
        self.thread = thread
        self.to_launcher = to_launcher
        self.from_launcher = from_launcher

    def _local_stop(self, timeout: float) -> StdRet[None]:
        trace_channel(self.launcher_id, "==== Stopping ====")
        self.thread.abort_start()
        self.to_launcher.close()
        self.from_launcher.close()
        if self.thread.is_alive():
            self.thread.join(timeout)
            if self.thread.is_alive():
                return StdRet.pass_errmsg(
                    TRANSLATION_CATALOG,
                    _('Could not stop launcher {launcher} after {timeout} seconds'),
                    launcher=self.launcher_id,
                    timeout=timeout,
                )
        return RET_OK_NONE
