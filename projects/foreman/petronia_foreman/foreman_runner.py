"""
The foreman execution handler.
"""

from typing import List, Optional
import os
from petronia_common.util import UserMessage, UserMessageData, I18n, StdRet
from petronia_common.util import i18n as _
from petronia_common.util.error import ExceptionPetroniaReturnError
from .configuration import PlatformSettings, ForemanConfig, LauncherConfig
from .routing import ForemanRouter
from .os_hooks import OsHooks
from .user_message import local_display, display_error, CATALOG


class ForemanRunner:
    """
    This handles boot up, runtime, and shutdown.  This includes handling external OS events to the
    process.
    """

    __slots__ = (
        '_platform', '_config', '__root_logger_fd', '__os_hooks', 'debug', '__state',
        '__router',
    )

    def __init__(
            self,
            platform_settings: PlatformSettings,
            foreman_config: ForemanConfig,
    ) -> None:
        self.__state = 0
        self.debug = False
        self._platform = platform_settings
        self._config = foreman_config
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
        assert self.__state == 0, 'can only be run before initialization'
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
        self.__router = ForemanRouter(self._platform, launcher_categories.result)
        return 0

    def boot(self) -> int:
        """Boot up the dependent services."""
        assert self.__state == 1, 'can only be run after initialization'
        self.__state = 2

        assert self.__router
        # print("DEBUG ForemanRunner starting the router")
        self.__router.start()
        # print("DEBUG ForemanRunner router is running")

        # start launchers.

        # Native is always started first.
        # local_display(
        #     _('Starting native launcher {name}'),
        #     name=self._get_native_launcher_category_name(),
        # )
        self.__router.boot_launcher(self._get_native_launcher_category_name())

        # Then the others.
        for name in self._config.get_boot_config().boot_order:
            # local_display(_('Starting boot launcher {name}'), name=name)
            self.__router.boot_launcher(name)

        return 0

    def join(self) -> None:
        """Wait for the processing to end.  This must be done in a way that is safe for
        signal handlers to run."""
        if self.__router:
            self.__router.join()

    def start_restart(self) -> None:
        """Stops all but the core initialized stuff."""
        local_display(_('Starting the restart process.'))
        assert self.__state == 2, 'can only be run after booted and not stopping'

        assert self.__router
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

    def _get_launcher_categories(self) -> StdRet[List[LauncherConfig]]:
        ret: List[LauncherConfig] = []
        for launcher_name in self._config.get_registered_launcher_config_names():
            config = self._config.get_launcher_config(launcher_name)
            if config.has_error:
                # Should consolidate the errors...
                return config.forward()
            ret.append(config.result)
        return StdRet.pass_ok(ret)

    def _get_native_launcher_category_name(self) -> str:
        return self._config.get_boot_config().get_native_launcher(self._platform)


def _display_error(
        err: BaseException,
        debug: bool,
        message: I18n, **kwargs: UserMessageData,
) -> None:
    display_error(ExceptionPetroniaReturnError(
        UserMessage(CATALOG, message, **kwargs),
        err,
    ), debug)
