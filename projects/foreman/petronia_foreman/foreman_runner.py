"""
The foreman execution handler.
"""

from typing import List, Sequence, Optional
import os
from petronia_common.util import UserMessage, UserMessageData, I18n, StdRet, join_results
from petronia_common.util import i18n as _
from petronia_common.util.error import ExceptionPetroniaReturnError
from .configuration import (
    ForemanConfig, RuntimeConfig, BootExtensionMetadata,
    read_boot_extension_file, get_boot_extension_file,
)
from .routing import ForemanRouter
from .os_hooks import OsHooks
from .user_message import local_display, display_error, CATALOG


class ForemanRunner:
    """
    This handles boot up, runtime, and shutdown.  This includes handling external OS events to the
    process.
    """

    __slots__ = (
        '_config', '__root_logger_fd', '__os_hooks', 'debug', '__state',
        '__router', '_boot_configs',
    )

    def __init__(
            self,
            foreman_config: ForemanConfig,
    ) -> None:
        self.__state = 0
        self.debug = False
        self._config = foreman_config
        self._boot_configs: List[BootExtensionMetadata] = []
        self.__root_logger_fd: Optional[int] = None
        self.__router: Optional[ForemanRouter] = None
        self.__os_hooks = OsHooks()

    def run(self) -> int:
        """Run the while Foreman process."""
        res = self.initialize()
        if res != 0:
            return res
        local_display(_('Starting up Petronia.'))
        res = self.boot()
        if res != 0:
            return res
        self.join()
        local_display(_('Petronia shutting down.'))
        self.shutdown()
        return 0

    def initialize(self) -> int:
        """Initialize the states."""
        self._ensure_state(0, 'can only be run before initialization')
        self.__state = 1
        log_file = self._config.get_boot_config().root_log_file
        if log_file:
            try:
                self.__root_logger_fd = os.open(
                    log_file, flags=os.O_WRONLY | os.O_APPEND | os.O_CREAT, mode=0o644,
                )
            except OSError as err:
                _display_error(
                    err, self.debug,
                    _('Failed to open root log file {filename}'),
                    filename=log_file,
                )
                return 1
        if self._config.get_boot_config().is_signals_enabled():
            self.__os_hooks.register_root_fd(self.__root_logger_fd)
            self.__os_hooks.register_on_shutdown(self.start_shutdown)
            self.__os_hooks.register_on_restart(self.start_restart)
            self.__os_hooks.start()
        launcher_categories = self._get_launcher_categories()
        if launcher_categories.has_error:
            display_error(launcher_categories.valid_error)
            return 1
        extensions = load_boot_extensions(self._config)
        if extensions.has_error:
            display_error(extensions.valid_error)
            return 2
        self._boot_configs = list(extensions.result)
        self.__router = ForemanRouter(launcher_categories.result)
        return 0

    def boot(self) -> int:
        """Boot up the dependent services."""
        self._ensure_state(1, 'can only be run after initialization')
        self.__state = 2

        # MyPy required check
        assert self.__router  # nosec
        # print("DEBUG ForemanRunner starting the router")
        self.__router.start()
        # print("DEBUG ForemanRunner router is running")

        # start launchers.
        for boot_config in self._boot_configs:
            # local_display(_('Starting boot launcher {name}'), name=name)
            self.__router.start_boot_extension(boot_config)

        return 0

    def join(self) -> None:
        """Wait for the processing to end.  This must be done in a way that is safe for
        signal handlers to run."""
        if self.__router:
            self.__router.join()

    def start_restart(self) -> None:
        """Stops all but the core initialized stuff."""
        local_display(_('Starting the restart process.'))
        self._ensure_state(2, 'can only be run after booted and not stopping')

        # MyPy required check.
        assert self.__router  # nosec
        self.__router.stop()
        self.__state = 1
        self.boot()

    def start_shutdown(self) -> None:
        """Should be called due to a user request (ctrl-c, SIGINT 15, etc) to
        start shutdown."""
        self.shutdown()

    def shutdown(self) -> None:
        """
        Terminates the Foreman process nicely.

        Idempotent.
        """
        local_display(_('Starting the shut down process.'))
        self.__state = 4
        if self.__router:
            self.__router.stop()
            # Do not empty out the router; we may need to join with it.
            # self.__router = None
        self.__os_hooks.stop()
        if self.__root_logger_fd is not None:
            try:
                os.close(self.__root_logger_fd)
            except OSError as err:
                _display_error(
                    err, self.debug,
                    _('Failed to close root log file {filename}'),
                    filename=self._config.get_boot_config().root_log_file,
                )
            self.__root_logger_fd = None

    def _get_launcher_categories(self) -> StdRet[List[RuntimeConfig]]:
        ret: List[RuntimeConfig] = []
        for launcher_name in self._config.get_registered_runtime_config_names():
            config = self._config.get_runtime_config(launcher_name)
            if config.has_error:
                # Should consolidate the errors...
                return config.forward()
            ret.append(config.result)
        return StdRet.pass_ok(ret)

    def _ensure_state(self, expected_state: int, error: str) -> None:
        if self.__state != expected_state:
            raise AttributeError(error)


def load_boot_extensions(config: ForemanConfig) -> StdRet[Sequence[BootExtensionMetadata]]:
    """Load the boot extension metadata."""
    ret: List[StdRet[BootExtensionMetadata]] = []
    for filename in config.get_boot_config().boot_file_order:
        fqn = get_boot_extension_file(filename)
        if fqn.has_error:
            ret.append(fqn.forward())
        else:
            ret.append(read_boot_extension_file(fqn.result))
    return join_results(tuple, *ret)


def _display_error(
        err: BaseException,
        debug: bool,
        message: I18n, **kwargs: UserMessageData,
) -> None:
    display_error(ExceptionPetroniaReturnError(
        UserMessage(CATALOG, message, **kwargs),
        err,
    ), debug)
