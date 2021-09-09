# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia_core.datastore version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Any,
    List,
    Dict,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    not_none,
    StdRet,
    collect_errors_from,
    STANDARD_PETRONIA_CATALOG,
)

EXTENSION_NAME = 'petronia_core.datastore'
EXTENSION_VERSION = (1, 0, 0)


class ConfigurationState:
    """
    Configuration for the data store.
    """
    __slots__ = ('cachedir',)

    UNIQUE_TARGET_FQN = 'petronia_core.datastore:configuration'
    UNIQUE_TARGET_REL = 'petronia_core.datastore:configuration'

    def __init__(
        self,
        cachedir: str,
    ) -> None:
        self.cachedir = cachedir

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'cachedir': self.cachedir,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ConfigurationState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('cachedir')
        f_cachedir: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='cachedir',
                name='ConfigurationState',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='cachedir',
                    type='str',
                    name='ConfigurationState',
                )
            f_cachedir = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ConfigurationState(
            cachedir=not_none(f_cachedir),
        ))

    def __repr__(self) -> str:
        return "ConfigurationState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
