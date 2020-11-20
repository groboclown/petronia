"""
The foreman execution handler.
"""

from typing import Dict, Optional
import os
from petronia_common.util import UserMessage, UserMessageData, I18n, StdRet
from petronia_common.util import i18n as _
from petronia_common.util.error import ExceptionPetroniaReturnError
from .configuration import PlatformSettings, ForemanConfig
from .routing import ForemanRouter
from .launcher import AbcLauncherCategory, create_launcher_category
from .os_hooks import OsHooks
from .user_message import display_error, CATALOG


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
        res = self.boot()
        if res != 0:
            return res
        # try:
        # except KeyboardInterrupt:
        self.shutdown()
        return 0

    def initialize(self) -> int:
        """Initialize the states."""
        assert self.__state == 0, 'can only be run before initialization'
        self.__state = 1
        log_file = self._config.get_root_log_file()
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
        self.__os_hooks.register_root_fd(self.__root_logger_fd)
        self.__os_hooks.register_on_shutdown(self.start_shutdown)
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

        # TODO create launch configurations.

        return 0

    def start_restart(self) -> None:
        """Stops all but the core boot stuff."""
        raise NotImplementedError()

    def start_shutdown(self) -> None:
        """Should be called due to a user request (ctrl-c, SIGINT 15, etc) to
        start shutdown."""
        self.shutdown()

    def shutdown(self) -> None:
        """
        Terminates the Foreman process nicely.

        Idempotent.
        """
        self.__os_hooks.stop()
        if self.__root_logger_fd is not None:
            try:
                os.close(self.__root_logger_fd)
            except OSError as err:
                _display_error(
                    err, self.debug,
                    _('Failed to close root log file {filename}'),
                    filename=self._config.get_root_log_file(),
                )
            self.__root_logger_fd = None

    def _get_launcher_categories(self) -> StdRet[Dict[str, AbcLauncherCategory]]:
        ret: Dict[str, AbcLauncherCategory] = {}
        for launcher_name in self._config.get_registered_launcher_config_names():
            config = self._config.get_launcher_config(launcher_name)
            if config.has_error:
                return config.forward()
            category = create_launcher_category(config.result.launcher_name, config.result.options)
            if category.has_error:
                return category.forward()
            ret[config.result.launcher_name] = category.result
        return StdRet.pass_ok(ret)


def _display_error(
        err: BaseException,
        debug: bool,
        message: I18n, **kvargs: UserMessageData,
) -> None:
    display_error(ExceptionPetroniaReturnError(
        UserMessage(CATALOG, message, **kvargs),
        err,
    ), debug)
