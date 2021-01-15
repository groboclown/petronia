"""
Creates the in-memory launcher category.
"""

from typing import Sequence, Tuple, Dict, Mapping, List, Optional
import types
import threading

from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, UserMessage, join_errors, RET_OK_NONE
from petronia_common.util import i18n as _
from .load_launcher import (
    get_entrypoint_name, get_module_name, connect_launcher, import_module,
)
from .stream import ReadWriteStream
from ..abc import AbcLauncherCategory, RuntimeContext
from ..util import (
    LaunchedInstance,
    request_extension_load,
    create_intercept_extension_loaded_event_handler,
    launcher_category_not_initialized,
    launcher_already_registered,
    no_such_launcher_id,
)
from ...process_mgmt.util import create_cmd_and_dirs
from ...configuration import LauncherConfig
from ...constants import TRANSLATION_CATALOG


WAIT_FOR_EXTENSION_LOAD_TIMEOUT_OPTION = 'extension-load-timeout'
WAIT_FOR_EXTENSION_LOAD_TIMEOUT_DEFAULT = '60.0'
ARGUMENT_OPTION_PREFIX = 'arg.'


def create_memory_launcher(options: LauncherConfig) -> AbcLauncherCategory:
    """Create a command launcher category"""
    return MemoryLauncherCategory(options)


class MemoryLauncherCategory(AbcLauncherCategory):
    """Launches launchers in-memory."""
    __slots__ = ('_module', '_launchers', '_context', '_start_timeout', '_args', '_alive')

    def __init__(self, options: LauncherConfig) -> None:
        AbcLauncherCategory.__init__(self, options)
        self._module: Optional[types.ModuleType] = None
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
        epn = get_entrypoint_name(self.config)
        if epn.has_error:
            return epn.forward()
        mdn = get_module_name(self.config)
        if mdn.has_error:
            return mdn.forward()
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
        assert self._alive, 'Stop already called.'
        res = import_module(self.config)
        if res.has_error:
            return res.forward()
        self._module = res.result
        self._context = context
        return RET_OK_NONE

    def start_launcher(
            self, launcher_id: str, permissions: Mapping[str, List[str]],
    ) -> StdRet[None]:
        print("[DEBUG MemoryLauncher] Starting launcher " + launcher_id)
        assert self._alive, 'Stop already called'
        if not self._context or not self._module:
            return launcher_category_not_initialized()
        if launcher_id in self._launchers:
            return launcher_already_registered(launcher_id)
        entrypoint_name = get_entrypoint_name(self.config)
        if entrypoint_name.has_error:
            return entrypoint_name.forward()
        cmd_args, _tmp_dirs = create_cmd_and_dirs(self._args, self._context.get_platform(), 0)

        # Ignore the permissions.  It's running in Foreman space, which means we can't limit
        # what it can do.

        loaded_launcher: List[LauncherData] = []

        # Create the launcher inside the registration process.
        def register_callback() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            # Re-do our assertions for completion; not really necessary,
            # but that's based on the current implementation details.
            if not self._context or not self._module:
                return launcher_category_not_initialized()
            to_launcher = ReadWriteStream(f'to_launcher {launcher_id}')
            from_launcher = ReadWriteStream(f'from_launcher {launcher_id}')
            thread_res = connect_launcher(
                entrypoint_name.result,
                self._module,
                self._on_error,
                self._on_complete,
                cmd_args,
                to_launcher,
                from_launcher,
            )
            if thread_res.has_error:
                return thread_res.forward()

            loaded_launcher.append(LauncherData(
                launcher_id, self.config, thread_res.result, to_launcher, from_launcher,
            ))
            launch_res = loaded_launcher[0].post_launch_processing(self._context)
            if launch_res.has_error:
                return launch_res.forward()
            self._launchers[launcher_id] = loaded_launcher[0]
            return loaded_launcher[0].as_channel_res()

        res = self._context.register_channel(launcher_id, register_callback)
        if res.has_error:
            if loaded_launcher:
                stop_res = loaded_launcher[0].stop()
                del self._launchers[launcher_id]
                if stop_res.has_error:
                    return StdRet.pass_error(res.valid_error, stop_res.valid_error)

        return res

    def start_extension(  # pylint:disable=too-many-arguments
            self, launcher_id: str, handler_id: str, extension_name: str,
            extension_version: Tuple[int, int, int], location: str,
            configuration: Optional[str],
    ) -> StdRet[None]:
        assert self._alive, 'Stop already called'
        if not self._context:
            return launcher_category_not_initialized()
        launcher = self._launchers.get(launcher_id)
        if not launcher:
            return no_such_launcher_id(launcher_id)

        def on_extension_loaded() -> None:
            # TODO implement
            pass

        def on_extension_load_failed(_errors: Sequence[UserMessage]) -> None:
            # TODO implement
            pass

        self._context.add_internal_event_handler(
            launcher_id,
            create_intercept_extension_loaded_event_handler(
                extension_name, extension_version,
                on_extension_loaded, on_extension_load_failed,
                float(self._start_timeout),
            ),
        )

        res = request_extension_load(
            launcher, handler_id, extension_name, extension_version, configuration,
        )
        return res

    def get_active_launcher_ids(self) -> Sequence[str]:
        return tuple(self._launchers.keys())

    def stop_launcher(self, launcher_id: str) -> StdRet[None]:
        launcher = self._launchers.get(launcher_id)
        if launcher is None:
            return no_such_launcher_id(launcher_id)
        res = launcher.stop()
        if res.ok:
            del self._launchers[launcher_id]
        return res

    def stop(self) -> StdRet[None]:
        # TODO make this parallel.
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

    def _on_error(self, module_name: str, extension_point: str, err: BaseException) -> None:
        # TODO implement
        pass

    def _on_complete(self, module_name: str, extension_point: str) -> None:
        # TODO implement
        pass


class LauncherData(LaunchedInstance):
    """Data container for an in-memory launcher."""
    __slots__ = ('thread', 'to_launcher', 'from_launcher',)

    def __init__(  # pylint:disable=too-many-arguments
            self,
            launcher_id: str,
            options: LauncherConfig,
            thread: threading.Thread,
            to_launcher: ReadWriteStream, from_launcher: ReadWriteStream,
    ) -> None:
        LaunchedInstance.__init__(
            self, launcher_id, options, from_launcher, to_launcher, self._local_stop,
        )
        self.thread = thread
        self.to_launcher = to_launcher
        self.from_launcher = from_launcher

    def _local_stop(self, timeout: float) -> StdRet[None]:
        print(f"==== Stopping {self.launcher_id} ====")
        # TODO writes are happening to this launcher after the stop.
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
