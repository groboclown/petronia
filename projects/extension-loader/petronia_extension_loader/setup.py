"""Loads and processes the user's setup."""

from typing import Sequence, List, Dict, Optional, Any
import os
import sys
from petronia_common.util import (
    load_structured_file, join_errors, join_none_results, StdRet, UserMessage, RET_OK_NONE,
)
from petronia_common.util import i18n as _
from .defs import TRANSLATION_CATALOG
from .finder import find_config_files, find_extension_dirs
# from . import messages


_EXTENSION_DIRS: List[str] = []
_BOOT_EXTENSIONS: List[str] = []
_EXTENSIONS_CONFIGS: Dict[str, Dict[str, Any]] = {}
_LAUNCHER_ID = ['extension-loader']


def get_extension_dirs() -> Sequence[str]:
    """Get the extension dirs found during initialize."""
    return tuple(_EXTENSION_DIRS)


def get_boot_extensions() -> Sequence[str]:
    """Get the list of raw boot extension names declared in the initialize."""
    return tuple(_BOOT_EXTENSIONS)


def get_extension_config(name: str) -> Dict[str, Any]:
    """Get the extension configuration, if it was declared during
    initialize.  The name must not include the version information.

    This does not refresh from disk, they are cached at startup time.

    Note: the data returned is not read-only.  Be careful with this, please.
    """
    # Note: return new dict if not exist, rather than the read-only empty singleton.
    return _EXTENSIONS_CONFIGS.get(name) or {}


def get_extension_handler_id() -> str:
    """Get the extension handler ID registered for this launcher."""
    return _LAUNCHER_ID[0]


def initialize(  # pylint:disable=keyword-arg-before-vararg
        user_config_path: Optional[str] = None,
        data_path: Optional[str] = None,
        _temp_dir: Optional[str] = None,
        launcher_id: Optional[str] = None,
        *_others: str,
) -> StdRet[None]:
    """Initialize the user settings.  Can be called multiple times."""
    _EXTENSION_DIRS.clear()
    _BOOT_EXTENSIONS.clear()
    _EXTENSIONS_CONFIGS.clear()
    errors: List[UserMessage] = []
    user_config: List[Dict[str, Any]] = []

    if launcher_id:
        _LAUNCHER_ID[0] = launcher_id

    if data_path:
        # This must be done before user config parsing.  System
        # extensions are always first.
        _EXTENSION_DIRS.extend(find_extension_dirs(data_path))

    if user_config_path:
        # messages.low_println(f'Scanning for user config files in {user_config_path}')
        for user_config_file in find_config_files(user_config_path):
            # messages.low_println(f'Loading user config file {user_config_file}')
            config_res = load_config_file(user_config_file)
            if config_res.has_error:
                # messages.low_println(
                #     f' - has error(s): {[s.debug() for s in config_res.error_messages()]}'
                # )
                errors.extend(config_res.error_messages())
            else:
                # messages.low_println(f' - has configuration {config_res.result}')
                user_config.extend(config_res.result)

    res = parse_configuration(user_config, data_path or '')
    if res.has_error:
        errors.extend(res.error_messages())

    if not _EXTENSION_DIRS:
        errors.append(UserMessage(
            TRANSLATION_CATALOG,
            _('No extension directory found.'),
        ))

    if errors:
        return StdRet.pass_error(join_errors(*errors))
    return RET_OK_NONE


def load_config_file(filename: str) -> StdRet[Sequence[Dict[str, Any]]]:
    """Read in a user configuration file."""
    config_res = load_structured_file(filename)
    if config_res.has_error:
        return config_res.forward()
    cfg = config_res.result
    if isinstance(cfg, dict):
        return StdRet.pass_ok([cfg])
    if isinstance(cfg, (list, tuple)):
        return StdRet.pass_ok(cfg)
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _('Configuration file ({file}) must be a proper json or yaml document.'),
        file=filename,
    )


def parse_configuration(
        configs: Sequence[Dict[str, Any]], data_path: str,
) -> StdRet[None]:
    """
    Parse the user configurations and load the data into this module's
    static structures.  This appends to, not replaces, the static structures.
    """
    data_dirs: List[str] = []
    if data_path:
        data_dirs = data_path.split(os.pathsep)

    errors: List[UserMessage] = []
    for config in configs:
        for key, settings in config.items():
            if settings is None:
                continue
            if not isinstance(settings, dict):
                errors.append(UserMessage(
                    TRANSLATION_CATALOG,
                    _('Configurations include section {key}, but it must be a key-value entry'),
                    key=key,
                ))
                continue

            # Extension Loader configuration options...
            if key == 'startup':
                res = parse_startup_config(settings, data_dirs)
                errors.extend(res.error_messages())
                continue

            # This is assumed to be an extension configuration.
            res = load_extension_settings(key, settings)
            errors.extend(res.error_messages())

    if errors:
        return StdRet.pass_error(join_errors(*errors))
    return RET_OK_NONE


def parse_startup_config(config: Dict[str, Any], data_dirs: Sequence[str]) -> StdRet[None]:
    """Parse the configuration entry for the startup settings."""
    errors: List[UserMessage] = []

    ext_val = config.get('priority-extensions')
    if ext_val:
        if isinstance(ext_val, (tuple, list)) and not isinstance(ext_val, str):
            # These are always added first.
            for ext in ext_val:
                _BOOT_EXTENSIONS.insert(0, ext)
        else:
            errors.append(UserMessage(
                TRANSLATION_CATALOG,
                _(
                    'Configuration value for startup -> extensions '
                    'must be a list of extension names'
                ),
            ))

    ext_val = config.get('extensions')
    if ext_val:
        if isinstance(ext_val, (tuple, list)) and not isinstance(ext_val, str):
            _BOOT_EXTENSIONS.extend(ext_val)
        else:
            errors.append(UserMessage(
                TRANSLATION_CATALOG,
                _(
                    'Configuration value for startup -> extensions '
                    'must be a list of extension names'
                ),
            ))

    ext_dirs = config.get('extension-dirs')
    if ext_dirs:
        if isinstance(ext_dirs, (tuple, list)) and not isinstance(ext_dirs, str):
            for dir_name in ext_dirs:
                _EXTENSION_DIRS.extend(get_extension_dirs_for_name(dir_name, data_dirs))
        else:
            errors.append(UserMessage(
                TRANSLATION_CATALOG,
                _(
                    'Configuration value for startup -> extension-dirs '
                    'must be a list of directories to search for extensions'
                ),
            ))

    if errors:
        return StdRet.pass_error(join_errors(*errors))
    return RET_OK_NONE


def load_extension_settings(key: str, settings: Dict[str, Any]) -> StdRet[None]:
    """Load a single extension setting key."""
    errs: List[StdRet[None]] = []
    ext_name: Optional[str] = None
    is_boot = False
    config: Dict[str, Any] = {}

    if not isinstance(settings.get('extension'), str):
        errs.append(StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('Configuration file has problem in section {key}: no "extension" value'),
            key=key,
        ))
    else:
        ext_name = str(settings['extension'])

    if settings.get('enabled') is True:
        is_boot = True

    if isinstance(settings.get('properties'), dict):
        config = settings['properties']

    res = join_none_results(*errs)
    if res.ok and ext_name:
        _EXTENSIONS_CONFIGS[ext_name] = config
        if is_boot:
            _BOOT_EXTENSIONS.append(ext_name)

    return res


def get_extension_dirs_for_name(name: str, data_dirs: Sequence[str]) -> Sequence[str]:
    """Get the extension directories for the given name."""
    if os.path.isdir(name):
        return [name]
    ret: List[str] = [name]
    if '${DATA_DIR}' in name:
        for data_dir in data_dirs:
            ret.append(name.replace('${DATA_DIR}', data_dir))
    if '${SYS_PATH}' in name:
        for data_dir in sys.path:
            ret.append(name.replace('${SYS_PATH}', data_dir))
    return ret


def for_unittest_backup() -> Dict[str, Any]:
    """For unit testing only."""
    return {
        'b': tuple(_BOOT_EXTENSIONS),
        'x': tuple(_EXTENSION_DIRS),
        'l': _LAUNCHER_ID[0],
        'c': dict(_EXTENSIONS_CONFIGS),
    }


def for_unittest_restore(orig: Dict[str, Any]) -> None:
    """For unit testing only."""
    _BOOT_EXTENSIONS.clear()
    _BOOT_EXTENSIONS.extend(orig['b'])
    _EXTENSION_DIRS.clear()
    _EXTENSION_DIRS.extend(orig['x'])
    _LAUNCHER_ID[0] = orig['l']
    _EXTENSIONS_CONFIGS.clear()
    _EXTENSIONS_CONFIGS.update(orig['c'])
