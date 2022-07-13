"""
Finds options specific to the in-memory launcher.
"""

from typing import List, Sequence, Dict, Callable, Optional, Union, Any
import os
import sys
import types
import threading
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from petronia_common.event_stream import BinaryReader, BinaryWriter
from .importer import load_module_from_path
from ...constants import TRANSLATION_CATALOG
from ...configuration import RuntimeConfig

ENTRYPOINT_OPTION = 'entrypoint'
DEFAULT_ENTRYPOINT = 'extension_entrypoint'
PYTHON_PATH_OPTION = 'extra-path'


def import_module(
        extension_name: str,
        extension_version: Sequence[int],
        locations: Sequence[str],
        options: RuntimeConfig,
) -> StdRet[types.ModuleType]:
    """Load the module defined in the options."""
    res_module_name = get_module_name(extension_name, extension_version, options)
    if res_module_name.has_error:
        return res_module_name.forward()

    path = get_python_path(locations, options)
    return load_module_from_path(res_module_name.result, path)


class DelayedStartThread:
    """Waits for either a timeout or a signal to start the thread processing."""
    __slots__ = ('__callback', '__thread', '__cond',  '__signal', '__timeout')

    def __init__(
            self, name: str, target: Callable[[], None], timeout: Optional[float] = None,
    ) -> None:
        self.__callback = target
        self.__signal = 0
        self.__cond = threading.Condition()
        self.__timeout = timeout
        self.__thread = threading.Thread(target=self.runner, daemon=True, name=name)

    def start(self) -> None:
        """Call the thread's start function."""
        self.__thread.start()

    def join(self, timeout: float) -> None:
        """Call the thread's join function."""
        self.__thread.join(timeout)

    def is_alive(self) -> bool:
        """Call the thread's is-alive function."""
        return self.__thread.is_alive()

    def begin_ok(self) -> None:
        """Start the runner in normal mode."""
        with self.__cond:
            self.__signal = 1
            self.__cond.notify_all()

    def abort_start(self) -> None:
        """Stop the runner."""
        with self.__cond:
            self.__signal = 2
            self.__cond.notify_all()

    def runner(self) -> None:
        """Wait for the condition to be signaled, then start running."""
        with self.__cond:
            self.__cond.wait_for(lambda: self.__signal != 0, timeout=self.__timeout)
            if self.__signal == 2:
                return
        self.__callback()


def connect_launcher(  # pylint:disable=too-many-arguments
        entrypoint_name: str, module: types.ModuleType,
        error_callback: Callable[[str, str, Union[BaseException, StdRet[None]]], None],
        completed_callback: Callable[[str, str], None],
        arguments: Sequence[str],
        reader: BinaryReader,
        writer: BinaryWriter,
        config: Dict[str, Any],
) -> StdRet[DelayedStartThread]:
    """Call the module's entrypoint function with the reader, writer, config, and arguments.
    This is done in another thread."""
    if not hasattr(module, entrypoint_name):
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('No such entrypoint {entrypoint} in module {module}'),
            entrypoint=entrypoint_name,
            module=module.__name__,
        )
    entrypoint = getattr(module, entrypoint_name)
    if not callable(entrypoint):
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('Entrypoint {entrypoint} in module {module} is not a function'),
            entrypoint=entrypoint_name,
            module=module.__name__,
        )

    def runner() -> None:
        res_val: Union[BaseException, StdRet[None], None] = None
        try:
            res = entrypoint(reader, writer, config, arguments)
            if isinstance(res, StdRet):
                res_val = res
            else:
                res_val = StdRet.pass_errmsg(
                    TRANSLATION_CATALOG,
                    _('Extension in Python module {name} returned with invalid return value {ret}'),
                    name=module.__name__,
                    ret=repr(res)
                )
        except BaseException as err:  # pylint:disable=broad-except
            res_val = err
        if res_val is None:
            # Should not happen, but...
            completed_callback(module.__name__, entrypoint_name)
        if isinstance(res_val, StdRet):
            if res_val.has_error:
                error_callback(module.__name__, entrypoint_name, res_val)
            else:
                completed_callback(module.__name__, entrypoint_name)
        else:
            assert isinstance(res_val, BaseException)  # nosec  # for mypy
            error_callback(module.__name__, entrypoint_name, res_val)

    ret = DelayedStartThread(name=_next_thread_id(), target=runner)
    ret.start()
    return StdRet.pass_ok(ret)


def get_module_name(
        extension_name: str,
        _extension_version: Sequence[int],
        _options: RuntimeConfig,
) -> StdRet[str]:
    """Get the Python module name.  See the __init__ file for the standard."""
    return StdRet.pass_ok(extension_name)


def get_entrypoint_name(options: RuntimeConfig) -> str:
    """Get the entrypoint function name within the module.
    The entrypoint function must take a BinaryReader, BinaryWriter
    as arguments, and return None."""
    return options.options.get(ENTRYPOINT_OPTION, DEFAULT_ENTRYPOINT)


def get_python_path(locations: Sequence[str], options: RuntimeConfig) -> List[str]:
    """Get the path for the module's required libraries."""
    current_path = list(sys.path)
    for location in locations:
        if location not in current_path:
            current_path.append(location)
    res_extra_path = options.get_option(PYTHON_PATH_OPTION)
    if res_extra_path.ok:
        for path in res_extra_path.result.split(os.pathsep):
            if path not in current_path:
                current_path.append(path)
    return current_path


THREAD_INDEX = [0]


def _next_thread_id() -> str:
    THREAD_INDEX[0] += 1
    return 'memory-launcher-' + str(THREAD_INDEX[0])
