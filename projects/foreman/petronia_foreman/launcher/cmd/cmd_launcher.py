"""
Launch extensions from a child process.
"""

from typing import Sequence, Tuple, List, Dict, Optional
import os
import tempfile

from petronia_common.event_stream import BinaryWriter, BinaryReader
from petronia_common.extension.config.extension_schema import ExtensionRuntime
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from .run_native import get_native_exec_args
from .run_python import get_python_exec_args
from ..abc import AbcLauncherCategory, RuntimeContext
from ..util import (
    launcher_not_loaded, launcher_category_not_initialized, launcher_already_registered,
    LaunchedInstance,
)
from ...configuration import RuntimeConfig, platform
from ...constants import TRANSLATION_CATALOG
from ...events import foreman
from ...process_mgmt import ManagedProcess, run_launcher
from ...user_message import local_display


def create_cmd_launcher(options: RuntimeConfig) -> AbcLauncherCategory:
    """Create a command launcher category"""
    return CmdLauncherCategory(options)


class CmdLauncherCategory(AbcLauncherCategory):
    """Launches processes."""

    __slots__ = ('_processes', '_context')

    def __init__(self, options: RuntimeConfig) -> None:
        AbcLauncherCategory.__init__(self, options)
        self._processes: Dict[str, LaunchedProcess] = {}
        self._context: Optional[RuntimeContext] = None

    def is_valid(self) -> StdRet[None]:
        return RET_OK_NONE

    def initialize(self, context: RuntimeContext) -> StdRet[None]:
        self._context = context
        return RET_OK_NONE

    def start_extension(
            self, handler_id: str, start_event: foreman.LauncherStartExtensionRequestEvent,
    ) -> StdRet[None]:
        if not self._context:
            return launcher_category_not_initialized()
        exec_res = get_runtime_settings(self.config, start_event.location)
        if exec_res.has_error:
            return exec_res.forward()
        if handler_id in self._processes:
            return launcher_already_registered(handler_id)
        launcher_runtime = ExtensionRuntime(handler_id, {
            permission.action: tuple(permission.resources)
            for permission in start_event.permissions
        })
        command, env = exec_res.result

        def register_callback() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            temp_dir = tempfile.mkdtemp()
            res_process = run_launcher(
                handler_id,
                self._create_params(start_event, temp_dir),
                temp_dir,
                launcher_runtime,
                command, env,
            )
            if res_process.has_error:
                return res_process.forward()

            process = LaunchedProcess(
                handler_id, self.config, launcher_runtime, res_process.result,
            )
            self._processes[handler_id] = process

            return StdRet.pass_ok((process.reader, process.writer))

        res = self._context.register_channel(handler_id, register_callback)
        if res.ok:
            self._context.add_handler(
                handler_id, handler_id,
                start_event.send_access.event_ids, [], start_event.send_access.source_id_prefixes,
            )
        return res

    def get_active_handler_ids(self) -> Sequence[str]:
        return tuple(self._processes.keys())

    def stop_extension(self, handler_id: str) -> StdRet[None]:
        launcher = self._get_launcher(handler_id)
        if launcher.has_error:
            return launcher.forward()
        res = launcher.result.stop()
        if res.ok:
            del self._processes[handler_id]
        return res

    def _get_launcher(self, launcher_id: str) -> StdRet['LaunchedProcess']:
        launcher = self._processes.get(launcher_id)
        if not launcher:
            return launcher_not_loaded(launcher_id)
        return StdRet.pass_ok(launcher)

    @staticmethod
    def _create_params(
            start_event: foreman.LauncherStartExtensionRequestEvent, temp_dir: str,
    ) -> Dict[str, str]:
        config_file = os.path.join(temp_dir, 'config.json')
        with open(config_file, 'w') as f:
            f.write(start_event.configuration or '{}')
        return {
            'EXTENSION_NAME': start_event.name,
            'EXTENSION_VERSION': '.'.join([str(v) for v in start_event.version]),
            'CONFIGURATION_FILE': config_file,
        }

    def stop(self) -> StdRet[None]:
        ret = []
        # Could do this in parallel.
        for launcher in self._processes.values():
            res = launcher.stop()
            if res.has_error:
                ret.append(res.valid_error)
        if ret:
            return StdRet.pass_error(*ret)
        return RET_OK_NONE


class LaunchedProcess(LaunchedInstance):
    """Information about a launched process"""
    __slots__ = ('extension_runtime', 'process',)

    def __init__(
            self,
            launcher_id: str,
            options: RuntimeConfig,
            extension_runtime: ExtensionRuntime,
            process: ManagedProcess,
    ) -> None:
        LaunchedInstance.__init__(
            self, launcher_id, options, process.reader, process, self._local_stop,
        )
        self.extension_runtime = extension_runtime
        self.process = process

    def _local_stop(self, timeout: float) -> StdRet[None]:
        """Try to nicely, then forcefully, stop the process."""
        self.process.close_writer()
        if not self.process.wait_for_stop(timeout):
            self.process.stop()
            if not self.process.wait_for_stop(timeout * 4.0):
                return StdRet.pass_errmsg(
                    TRANSLATION_CATALOG,
                    _('Could not stop launcher {launcher_id} within {timeout} seconds.'),
                    launcher_id=self.extension_runtime.launcher,
                    timeout=timeout * 5.0,
                )
        return RET_OK_NONE


def get_runtime_settings(
        options: RuntimeConfig,
        location: Sequence[str],
) -> StdRet[Tuple[Sequence[str], Dict[str, str]]]:
    """Get the executable settings for the options: the
    executable arguments and the environment variables and temporary directories.
    """
    abs_locations = safe_location_convert(location)
    executable = options.get_option('exe')
    if executable.has_error:
        return executable.forward()
    if executable.result == 'py':
        return get_python_runtime_settings(options, abs_locations)
    return get_native_exec_args(executable.result, abs_locations)


def safe_location_convert(location: Sequence[str]) -> Sequence[str]:
    """Safely convert the location strings passed from the extension load request.
    These must all be relative to the data path or the config path."""
    ret: List[str] = []
    for loc in location:
        search_path: Sequence[str]
        relative: str
        if loc.startswith('${DATA_PATH}/') or loc.startswith('${DATA_PATH}\\'):
            search_path = platform.data_paths
            relative = loc[13:]
        elif loc.startswith('${CONFIG_PATH}/') or loc.startswith('${CONFIG_PATH}\\'):
            search_path = platform.configuration_paths
            relative = loc[15:]
        else:
            local_display(
                _('Extension load request included non-relative location path: {path}'),
                path=loc,
            )
            continue
        for path in search_path:
            attempt = os.path.join(path, relative)
            if os.path.exists(attempt):
                # The attempt may be a zip file, in which case it's allowed as a location.
                ret.append(attempt)

    return tuple(ret)


def get_python_runtime_settings(
        options: RuntimeConfig,
        location: Sequence[str],
) -> StdRet[Tuple[Sequence[str], Dict[str, str]]]:
    """Get the runtime settings for a python executable."""
    res_module = options.get_option('module')
    if res_module.has_error:
        return res_module.forward()
    res_module_path = options.get_option('path')
    if res_module_path.ok:
        module_path = res_module_path.result.split(os.path.pathsep)
    else:
        module_path = []
    module_path.extend(location)
    res_py_exec = get_python_exec_args(
        res_module.result, module_path, False,
        options.options.get('args', None),
    )
    return res_py_exec
