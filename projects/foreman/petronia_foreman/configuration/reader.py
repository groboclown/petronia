
"""
Reads the configuration file, and puts the data into the correct objects.
"""

from typing import Optional, Any, Iterable, Tuple, List, Dict
import configparser
import collections.abc
from petronia_common.extension.config.event_loader import load_dict_str_value
from petronia_common.extension.config.extension_loader import (
    load_extension_version_value, load_extension_runtime,
    load_extension_list_value,
)
from petronia_common.util import StdRet, collect_errors_from, load_structured_file
from petronia_common.util import i18n as _
from .foreman import ForemanConfig
from .boot_extension import BootExtensionMetadata
from .find_file import get_config_file
from ..constants import TRANSLATION_CATALOG


def read_configuration_file(filename: Optional[str]) -> StdRet[ForemanConfig]:
    """
    Parses the configuration file into the configuration.  If the filename is
    not provided, then the default file is searched for (using OS dependent
    path defaults).  If no configuration can be found, then the internal default
    values are returned.

    :param filename:
    :return:
    """
    config_file = get_config_file(filename)
    if config_file.has_error:
        return config_file.forward()

    parser = configparser.ConfigParser()
    try:
        parser.read(config_file.result)
    except configparser.ParsingError as err:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('Error parsing ini file {filename}: {msg}'),
            filename=config_file.result,
            msg=[f'Line {line_no}: {msg}' for line_no, msg in err.errors],
        )

    ret = ForemanConfig()
    res = ret.load_config(parser)
    if res.has_error:
        return res.forward()

    if not ret.get_boot_config().boot_file_order:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _(
                'No boot-file-order defined in the foreman configuration, so foreman cannot start.'
                '  Did you install Petronia correctly?  Please check the instructions again.  '
                'Petronia expects a file named petronia.ini in an OS-specific location.'
            ),
        )

    return StdRet.pass_ok(ret)


def read_boot_extension_file(filename: str) -> StdRet[BootExtensionMetadata]:
    """Parse the boot extension file."""
    res = load_structured_file(filename)
    if res.has_error:
        return res.forward()
    if isinstance(res.result, dict):
        raw = res.result
    else:
        if len(res.result) != 1:
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG,
                _('Boot extension file must have exactly 1 document: {filename}'),
                filename=filename,
            )
        raw = res.result[0]
    ret_name = load_dict_str_value('name', raw)
    ret_version = load_extension_version_value(raw.get('version'))
    ret_runtime = load_extension_runtime(raw.get('runtime'))
    ret_produces = load_extension_list_value('produces', raw)
    ret_consumes = load_consumes_list(raw.get('consumes'))
    ret_config = load_boot_extension_configuration(raw.get('configuration'))
    error = collect_errors_from(
        ret_name, ret_version, ret_runtime, ret_produces,
        ret_consumes, ret_config,
    )
    if error:
        return StdRet.pass_error(error)
    return StdRet.pass_ok(
        BootExtensionMetadata(
            name=ret_name.result,
            version=ret_version.result,
            runtime=ret_runtime.result.launcher,
            produces=ret_produces.result,
            consumes=ret_consumes.result,
            permissions=ret_runtime.result.requested_permissions,
            configuration=ret_config.result,
            locations=(),
        )
    )


def load_consumes_list(raw: Any) -> StdRet[Iterable[Tuple[Optional[str], Optional[str]]]]:
    """Loads a list of string values."""
    ret: List[Tuple[Optional[str], Optional[str]]] = []
    if not isinstance(raw, collections.abc.Iterable):
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG, _('must be a list of event-id/target-id values'),
        )
    for value in raw:
        if not isinstance(value, dict):
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG, _('must be a list of event-id/target-id values'),
            )
        event_id = value.get('event-id')
        if event_id is not None and not isinstance(event_id, str):
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG, _('must be a list of event-id/target-id values'),
            )
        target_id = value.get('target-id')
        if target_id is not None and not isinstance(target_id, str):
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG, _('must be a list of event-id/target-id values'),
            )
        ret.append((event_id, target_id))
    return StdRet.pass_ok(ret)


def load_boot_extension_configuration(raw: Any) -> StdRet[Dict[str, Any]]:
    """Turns a raw into a dict."""
    if not isinstance(raw, dict):
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG, _('configurations must be a dictionary'),
        )
    return StdRet.pass_ok(raw)
