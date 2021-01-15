"""Loads and processes the user's setup."""

from typing import Sequence, List, Dict, Optional, Any
import json
from petronia_common.util import load_yaml_documents, StdRet, UserMessage, join_errors, RET_OK_NONE
from petronia_common.util import i18n as _
from .defs import TRANSLATION_CATALOG
from .finder import find_config_files, find_extension_dirs


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


def get_extension_config(name: str) -> Optional[Dict[str, Any]]:
    """Get the extension configuration, if it was declared during
    initialize.  The name must not include the version information.

    Note: the data returned is not read-only.  Be careful with this, please.
    """
    return _EXTENSIONS_CONFIGS.get(name)


def get_launcher_id() -> str:
    """Get the launcher ID registered for this launcher."""
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
        for user_config_file in find_config_files(user_config_path):
            config_res = load_config_file(user_config_file)
            if config_res.has_error:
                errors.extend(config_res.error_messages())
            elif config_res.ok:
                user_config.extend(config_res.result)

    res = parse_configuration(user_config)
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
    try:
        if filename.lower().endswith('.json'):
            try:
                with open(filename, 'r') as f:
                    cfg = json.load(f)
            except json.JSONDecodeError as err:
                return StdRet.pass_exception(
                    _('Invalid JSON formatted'),
                    err,
                )
        else:
            with open(filename, 'r') as f:
                config_res = load_yaml_documents(f.read())
            if config_res.has_error:
                return config_res.forward()
            cfg = config_res.result
    except OSError as err:
        return StdRet.pass_exception(
            _('Failed to read file {filename}'),
            err,
            filename=filename,
        )
    if isinstance(cfg, dict):
        return StdRet.pass_ok([cfg])
    if isinstance(cfg, (list, tuple)):
        return StdRet.pass_ok(cfg)
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _(
            'Configuration file ({file}) must be a proper yaml '
            'document or list of yaml documents.'
        ),
        file=filename,
    )


def parse_configuration(configs: Sequence[Dict[str, Any]]) -> StdRet[None]:
    """
    Parse the user configurations and load the data into this module's
    static structures.  This appends to, not replaces, the static structures.
    """
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
                res = parse_startup_config(settings)
                errors.extend(res.error_messages())
                continue

            # This is assumed to be an extension configuration.
            _EXTENSIONS_CONFIGS[key] = settings

    if errors:
        return StdRet.pass_error(join_errors(*errors))
    return RET_OK_NONE


def parse_startup_config(config: Dict[str, Any]) -> StdRet[None]:
    """Parse the configuration entry for the startup settings."""
    errors: List[UserMessage] = []
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
            _EXTENSION_DIRS.extend(ext_dirs)
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
