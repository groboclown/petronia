
"""
Structural definition for the contents of the Foreman configuration.
"""

from typing import Dict, List, Sequence, Optional
from configparser import ConfigParser, DEFAULTSECT
from petronia_common.util import StdRet, RET_OK_NONE, collect_errors_from
from petronia_common.util import i18n as _
from .runtime import RuntimeConfig
from ..constants import TRANSLATION_CATALOG as CATALOG

# Must be lower-case
BOOT_SECTION = 'foreman'


class BootConfig:
    """
    Boot-up options for Foreman.
    """
    __slots__ = (
        '_root_log_file', '_use_signals', '_boot_file_order', '_boot_extension_dir',
    )

    def __init__(self, section_name: str, config: ConfigParser) -> None:
        self._root_log_file = config.get(section_name, 'root-log-file', fallback=None) or None
        boot_order_str = config.get(section_name, 'boot-file-order', fallback=None) or ''
        boot_order: List[str] = []
        for name in boot_order_str.split(','):
            name = name.strip()
            if name:
                boot_order.append(name)
        self._boot_file_order = tuple(boot_order)
        self._boot_extension_dir = config.get(section_name, 'boot-extension-dir', fallback='.')
        self._use_signals = True

    @property
    def root_log_file(self) -> Optional[str]:
        """The root log file, for low-level errors."""
        return self._root_log_file

    @property
    def boot_extension_dir(self) -> str:
        """The boot extension directory."""
        return self._boot_extension_dir

    @property
    def boot_file_order(self) -> Sequence[str]:
        """Order of the boot-time extension metadata files to read and load."""
        return self._boot_file_order

    def is_signals_enabled(self) -> bool:
        """Should foreman wire up the OS signals at boot time?"""
        return self._use_signals

    def set_signals_enabled(self, enabled: bool) -> None:
        """Set the OS signal state."""
        self._use_signals = enabled


class ForemanConfig:
    """
    The Foreman Process configuration.

    This contains:
        - The "launcher" types.  Each launcher type describes a method for setting up and
            running a particular extension type.
        - Boot-up options.  This is contained in the 'boot' section.
    """
    __slots__ = ('_runtime_mapper', '_boot',)

    def __init__(self) -> None:
        self._runtime_mapper: Dict[str, RuntimeConfig] = {}
        self._boot: Optional[BootConfig] = None

    def get_boot_config(self) -> BootConfig:
        """Get the configuration for foreman.  This is expected to be called after load_config."""
        if self._boot is None:
            raise ValueError('Load config failed.')
        return self._boot

    def load_config(self, *configs: ConfigParser) -> StdRet[None]:
        """Load the configurations.
        These are ordered in priority order - least important is first.
        """
        self._runtime_mapper.clear()
        boot_config = ConfigParser()
        boot_section_name: str = DEFAULTSECT

        for config in configs:
            for section_name in config.sections():
                inner_section_name = section_name.lower()
                if inner_section_name == BOOT_SECTION:
                    boot_config = config
                    boot_section_name = section_name
                else:
                    self._runtime_mapper[inner_section_name] = RuntimeConfig(
                        section_name, config,
                    )

        self._boot = BootConfig(boot_section_name, boot_config)
        errs = collect_errors_from(
            [launcher.validate() for launcher in self._runtime_mapper.values()],
        )
        if errs:
            return StdRet.pass_error(errs)

        return RET_OK_NONE

    def get_registered_runtime_config_names(self) -> List[str]:
        """Get all registered launcher configuration names."""
        return list(self._runtime_mapper.keys())

    def get_runtime_config(self, name: str) -> StdRet[RuntimeConfig]:
        """Fetch the boot launcher configurations."""
        inner_name = name.lower()
        if inner_name not in self._runtime_mapper:
            return StdRet.pass_errmsg(
                CATALOG,
                _('No launcher named {name}.'),
                name=name,
            )
        ret = self._runtime_mapper[inner_name]
        valid = ret.validate()
        if valid.has_error:
            return valid.forward()
        return StdRet.pass_ok(ret)
