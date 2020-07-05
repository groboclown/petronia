
"""
Loads extension information from a simple data structure.

Simple data structures means list, dict, int, float, bool, str, None
"""

from typing import List, Dict, Optional, Any, cast
from . import event_schema, extension_schema
from .event_loader import load_full_event_schema
from .version import ExtensionVersion
from ...util import StdRet, collect_errors_from, EMPTY_TUPLE
from ...util import i18n as _


def load_extension(raw: Dict[str, Any]) -> StdRet[extension_schema.AbcExtensionMetadata]:
    """Returns the extension defined in the dictionary.  If the data does not have the
    basic information or does not conform to the standard, then an error is returned."""
    extension_type = raw.get('type')
    if type == 'api':
        return validate_extension(load_api_extension(raw))
    if type == 'impl':
        return validate_extension(load_impl_extension(raw))
    if type == 'standalone':
        return validate_extension(load_standalone_extension(raw))
    return StdRet.pass_errmsg(
        _('invalid extension type ({extension_type})'),
        extension_type=extension_type,
    )


def validate_extension(
        value: StdRet[extension_schema.AbcExtensionMetadata],
) -> StdRet[extension_schema.AbcExtensionMetadata]:
    if not value.ok:
        return value.forward()
    validation = value.result.validate_type()
    if validation:
        return StdRet.pass_error(validation)
    return value


def load_api_extension(raw: Dict[str, Any]) -> StdRet[extension_schema.ApiExtensionMetadata]:
    ret_name = load_extension_str_value('name', raw)
    ret_version = load_extension_version_value(raw.get('version'))
    ret_about = load_extension_str_value('about', raw)
    ret_description = load_extension_str_value('description', raw)
    ret_depends = load_extension_dependencies('depends', raw)
    ret_licenses = load_extension_list_value('licenses', raw)
    ret_authors = load_extension_list_value('authors', raw)
    ret_events = load_events(raw)
    error = collect_errors_from(
        ret_name, ret_version, ret_about, ret_description,
        ret_depends, ret_licenses, ret_authors, ret_events,
    )
    if error:
        return StdRet.pass_error(error)
    return StdRet.pass_ok(extension_schema.ApiExtensionMetadata(
        name=ret_name.result,
        version=ret_version.result,
        about=ret_about.result,
        description=ret_description.result,
        depends=ret_depends.result,
        licenses=ret_licenses.result,
        authors=ret_authors.result,
        events=ret_events.result,
    ))


def load_impl_extension(raw: Dict[str, Any]) -> StdRet[extension_schema.ImplExtensionMetadata]:
    ret_name = load_extension_str_value('name', raw)
    ret_version = load_extension_version_value(raw.get('version'))
    ret_about = load_extension_str_value('about', raw)
    ret_description = load_extension_str_value('description', raw)
    ret_depends = load_extension_dependencies('depends', raw)
    ret_licenses = load_extension_list_value('licenses', raw)
    ret_authors = load_extension_list_value('authors', raw)
    ret_implements = load_extension_dependencies('implements', raw)
    error = collect_errors_from(
        ret_name, ret_version, ret_about, ret_description,
        ret_depends, ret_licenses, ret_authors, ret_implements,
    )
    if error:
        return StdRet.pass_error(error)
    return StdRet.pass_ok(extension_schema.ImplExtensionMetadata(
        name=ret_name.result,
        version=ret_version.result,
        about=ret_about.result,
        description=ret_description.result,
        depends=ret_depends.result,
        licenses=ret_licenses.result,
        authors=ret_authors.result,
        implements=ret_implements.result,
    ))


def load_standalone_extension(raw: Dict[str, Any]) -> StdRet[extension_schema.StandAloneExtensionMetadata]:
    ret_name = load_extension_str_value('name', raw)
    ret_version = load_extension_version_value(raw.get('version'))
    ret_about = load_extension_str_value('about', raw)
    ret_description = load_extension_str_value('description', raw)
    ret_depends = load_extension_dependencies('depends', raw)
    ret_licenses = load_extension_list_value('licenses', raw)
    ret_authors = load_extension_list_value('authors', raw)
    error = collect_errors_from(
        ret_name, ret_version, ret_about, ret_description,
        ret_depends, ret_licenses, ret_authors,
    )
    if error:
        return StdRet.pass_error(error)
    return StdRet.pass_ok(extension_schema.StandAloneExtensionMetadata(
        name=ret_name.result,
        version=ret_version.result,
        about=ret_about.result,
        description=ret_description.result,
        depends=ret_depends.result,
        licenses=ret_licenses.result,
        authors=ret_authors.result,
    ))


def load_extension_str_value(key: str, raw: Dict[str, Any]) -> StdRet[str]:
    raw_value = raw.get(key)
    if not raw_value:
        return StdRet.pass_errmsg(
            _('no `{key}` found in extension definition'),
            key=key,
        )
    if not isinstance(raw_value, str):
        return StdRet.pass_errmsg(
            _('`{key}` must be a string value'),
            key=key,
        )
    return StdRet.pass_ok(raw_value)


def load_extension_list_value(key: str, raw: Dict[str, Any]) -> StdRet[List[str]]:
    raw_value = raw.get(key)
    if raw_value is None or not isinstance(raw_value, list):
        return StdRet.pass_errmsg(
            _('`{key}` must be a list of strings'),
            key=key,
        )
    ret: List[str] = []
    for raw_item in raw_value:
        if not isinstance(raw_item, str):
            return StdRet.pass_errmsg(
                _('`{key}` must be a list of strings'),
                key=key,
            )
        ret.append(raw_item)
    return StdRet.pass_ok(ret)


def load_extension_version_value(value: Any) -> StdRet[ExtensionVersion]:
    if (
            not isinstance(value, list) or
            len(value) != 3 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            not isinstance(value[2], int)
    ):
        return StdRet.pass_errmsg(
            _('version ({version}) must be in the format [major, minor, patch]'),
            version=value
        )
    return StdRet.pass_ok((value[0], value[1], value[2]))


def load_extension_dependencies(
        key: str, raw: Dict[str, Any],
) -> StdRet[List[extension_schema.ExtensionDependency]]:
    raw_depends = raw.get(key)
    if not raw_depends:
        return StdRet.pass_ok(cast(List[extension_schema.ExtensionDependency], EMPTY_TUPLE))
    if not isinstance(raw_depends, list):
        return StdRet.pass_errmsg(
            _('`{key}` must be a list of dictionaries'),
            key=key
        )
    ret: List[extension_schema.ExtensionDependency] = []
    for dep in raw_depends:
        ret_dep = load_extension_dependency(dep)
        if not ret_dep.ok:
            return ret_dep.forward()
        ret.append(ret_dep.result)
    return StdRet.pass_ok(ret)


def load_extension_dependency(value: Any) -> StdRet[extension_schema.ExtensionDependency]:
    if not isinstance(value, dict):
        return StdRet.pass_errmsg(
            _('dependency must be a dictionary containing the keys `name`, `minimum`, and possibly `below`'),
        )
    ret_name = load_extension_str_value('name', value)
    if not ret_name.ok:
        return ret_name.forward()
    ret_minimum = load_extension_version_value(value.get('minimum'))
    if not ret_minimum.ok:
        return ret_minimum.forward()
    raw_below = value.get('below')
    below: Optional[ExtensionVersion] = None
    if raw_below:
        ret_below = load_extension_version_value(raw_below)
        if not ret_below.ok:
            return ret_below.forward()
        below = ret_below.value
    return StdRet.pass_ok(extension_schema.ExtensionDependency(
        ret_name.result,
        ret_minimum.result,
        below,
    ))


def load_events(raw: Optional[Dict[str, Any]]) -> StdRet[List[event_schema.EventType]]:
    raw_events = raw.get('events')
    if not raw_events:
        return StdRet.pass_ok(cast(List[event_schema.EventType], EMPTY_TUPLE))
    if not isinstance(raw_events, dict):
        return StdRet.pass_errmsg(
            _('`events` must be a dictionary of event schemas'),
        )
    raw_references = raw.get('references')
    if raw_references and not isinstance(raw_events, dict):
        return StdRet.pass_errmsg(
            _('`references` must be a dictionary of event data type schemas'),
        )
    return load_full_event_schema(raw_events, raw_references or {})
