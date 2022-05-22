# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia_core.binarystore version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name,consider-using-f-string

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Optional,
    Any,
    List,
    SupportsFloat,
    Dict,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    STANDARD_PETRONIA_CATALOG,
    not_none,
    StdRet,
)

EXTENSION_NAME = 'petronia_core.binarystore'
EXTENSION_VERSION = (1, 0, 0)


class ConfigurationState:
    """
    Configuration for the data store.
    """
    __slots__ = ('cachedir', 'request_timeout_seconds',)

    UNIQUE_TARGET_FQN = 'petronia_core.binarystore:configuration'
    UNIQUE_TARGET_REL = 'petronia_core.binarystore:configuration'

    def __init__(
        self,
        cachedir: Optional[str],
        request_timeout_seconds: Optional[float],
    ) -> None:
        self.cachedir = cachedir
        self.request_timeout_seconds = request_timeout_seconds

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'cachedir': self.cachedir,
            'request_timeout_seconds': self.request_timeout_seconds,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ConfigurationState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('cachedir')
        f_cachedir: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='cachedir',
                    type='str',
                    name='ConfigurationState',
                )
            f_cachedir = val
        val = data.get('request_timeout_seconds')
        f_request_timeout_seconds: Optional[float] = None
        if val is not None:
            if not isinstance(val, SupportsFloat):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='request_timeout_seconds',
                    type='float',
                    name='ConfigurationState',
                )
            f_request_timeout_seconds = float(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ConfigurationState(
            cachedir=f_cachedir,
            request_timeout_seconds=f_request_timeout_seconds,
        ))

    def __repr__(self) -> str:
        return "ConfigurationState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
