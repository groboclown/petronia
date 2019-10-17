
# mypy: allow-any-expr
# mypy: allow-any-explicit

"""
Loads the contents of a parsed configuration file into deserialized
configuration objects.
"""

from typing import Dict, List, Iterable, Sequence, Tuple, Union, Optional, Any, cast
from numbers import Real
import locale
from ....base.util import (
    optional_key,
    V,
    EMPTY_DICT,
)
from ....base.util.simple_type import PersistType
from ....core.extensions.api import ExtensionVersion


_DEFAULT_CONFIGURATION_NAME = 'setup-configuration'
_CONFIGURATION_ID_FORMAT = '{0}/{1}'


class ExtensionConfigurationDetails:
    """
    Configuration of an extensions.
    """
    __slots__ = (
        '__src', '__mod', '__state_id', '__state', '__err',
        '__name', '__enabled',
    )

    def __init__(
            self,
            src: str,
            name: str,
            extension_name: Optional[str] = None,
            state_id: Optional[str] = None,
            # FIXME make the error a locale specific string.
            err: Optional[str] = None,
            state: Optional[PersistType] = None,
            enabled: bool = False
    ) -> None:
        self.__src = src
        self.__mod = extension_name
        self.__state_id = state_id
        self.__err = err
        self.__state = state
        self.__name = name
        self.__enabled = enabled

    # Derived value, so not a property.
    def is_error(self) -> bool:
        """Does this represent an error during load?"""
        return self.__err is not None

    @property
    def source_name(self) -> str:
        return self.__src

    @property
    def name(self) -> str:
        return self.__name

    @property
    def extension_name(self) -> Optional[str]:
        return self.__mod

    @property
    def err(self) -> Optional[str]:
        return self.__err

    @property
    def state_id(self) -> Optional[str]:
        return self.__state_id

    @property
    def state(self) -> Optional[PersistType]:
        return self.__state

    @property
    def is_enabled(self) -> bool:
        return self.__enabled

    def __repr__(self) -> str:
        return (
            'ExtensionConfigurationDetails('
            'src={src}, '
            'extension_name={extension_name}, '
            'state_id={state_id}, '
            'err={err}, '
            'state={state}, '
            'name={name}, '
            'enabled={enabled}'
            ')'
        ).format(
            src=repr(self.__src),
            extension_name=repr(self.__mod),
            state_id=repr(self.__state_id),
            err=repr(self.__err),
            state=repr(self.__state),
            name=repr(self.__name),
            enabled=repr(self.__enabled)
        )


def deserialize_contents(
        file_contents: Any, source_name: str
) -> Sequence[ExtensionConfigurationDetails]:
    """
    Converts the contents into objects.

    Contents are simple JSON style data structures only.

    Format is expected to be either a list of configuration definitions, or
    a dictionary of user names mapped to configuration definitions.
    """
    ret: List[ExtensionConfigurationDetails] = []
    named_configs: Dict[str, Dict[str, Any]] = {}
    if isinstance(file_contents, dict):
        for key, value in file_contents.items():
            if not isinstance(value, dict):
                ret.append(ExtensionConfigurationDetails(
                    source_name, str(key),
                    # TODO Localise
                    err='key must reference a configuration mapping'
                ))
            else:
                named_configs[str(key)] = value
    else:
        if isinstance(file_contents, str) or not isinstance(file_contents, Iterable):
            ret.append(ExtensionConfigurationDetails(
                source_name, '',
                # TODO Localise
                err='Contents must be either a key-value map to '
                'configuration values, or a list of configuration values'
            ))
        else:
            fcl = tuple(file_contents)
            for index in range(len(fcl)):
                config = fcl[index]
                if (
                        isinstance(config, dict) and
                        'ext' not in config and
                        'extension' not in config and
                        'config' not in config
                ):
                    for key, val in config.items():
                        named_configs[key] = val
                else:
                    named_configs[str(index)] = fcl[index]

    for key, raw in named_configs.items():
        ret.append(decode_value(source_name, key, raw))

    return ret


def decode_value(
        src: str, key: str, raw: Dict[str, Any]
) -> ExtensionConfigurationDetails:
    """
    Extract out the details of the value.
    """
    extension_name = _safe_key(raw, 'extension', str) or _safe_key(raw, 'ext', str)
    configuration_name = _safe_key(raw, 'config', str) or _DEFAULT_CONFIGURATION_NAME
    # If "config" is given, then this describes a configuration.
    # If "extension" and "config" are given, then this is considered to be
    # a configuration for that extension.
    # If "config" is not given, then this is the default configuration for the
    # extension.
    # If none are given, then this is the default configuration for the
    # extension named in the key.
    if not extension_name:
        extension_name = key.replace('-', '.')
    raw_enabled = _safe_key(raw, 'enabled', bool)
    if raw_enabled is None:
        enabled = True
    else:
        enabled = raw_enabled

    # Version and below.version are currently not used.
    # Using them will require changes to the extension load request code.
    # raw_version = _safe_key(raw, 'version', (str, Iterable,))
    # if raw_version:
    #     version = decode_version(raw_version)
    # else:
    #     version = ANY_VERSION
    # raw_below = _safe_key(raw, 'below.version', (str, Iterable,))
    # below: Optional[ExtensionVersion] = None
    # if raw_below:
    #     below = decode_version(raw_below)

    # Properties are allowed to be empty, if no configuration is given
    properties: Dict[str, Any] = _safe_key(raw, 'properties', dict) or EMPTY_DICT

    state_id = _CONFIGURATION_ID_FORMAT.format(extension_name, configuration_name)
    state: PersistType = enforce_persist_type(properties)
    return ExtensionConfigurationDetails(
        src, key,
        extension_name=extension_name,
        state_id=state_id,
        state=state,
        enabled=enabled
    )


def _safe_key(
        con: Dict[str, Any], key: str,
        oftype: Union[type, Tuple[Union[type, Tuple[V, ...]], ...]]
) -> Optional[V]:
    """key: lower case, using `.` instead of `_` or `-`"""
    if key in con:
        return optional_key(con, key, oftype)
    for conkey, val in con.items():
        conkey = conkey.strip().lower().replace('_', '.').replace('-', '.')
        if conkey == key:
            if oftype and isinstance(val, oftype):
                return cast(V, val)
            return None
    return None


def decode_version(version: Union[str, Iterable[Any]]) -> Union[str, ExtensionVersion]:
    if isinstance(version, str):
        parts = version.split('.')[:3]
    else:
        parts = list(version)

    # Default version values.
    ret: List[int] = [0, 0, 0]

    for idx in range(len(parts)):
        part = parts[idx]
        if isinstance(part, str):
            try:
                ret[idx] = locale.atoi(parts[idx])
            except ValueError:
                # TODO localize
                return 'invalid value `{0}` in version `{1}`'.format(parts[idx], version)
        elif isinstance(part, Real):
            ret[idx] = int(part.real)
        else:
            # TODO localize
            return 'invalid value `{0}` in version `{1}`'.format(parts[idx], version)
    return (ret[0], ret[1], ret[2],)


def enforce_persist_type(properties: Dict[str, Any]) -> PersistType:
    # TODO validate, but that means returning a possible error.
    return cast(PersistType, properties)
