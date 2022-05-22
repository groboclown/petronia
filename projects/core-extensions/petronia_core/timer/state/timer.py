# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia_core.timer version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name,consider-using-f-string

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Dict,
    Any,
    List,
    SupportsFloat,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    STANDARD_PETRONIA_CATALOG,
    StdRet,
    not_none,
)

EXTENSION_NAME = 'petronia_core.timer'
EXTENSION_VERSION = (1, 0, 0)


class ConfigurationState:
    """
    Configuration for the timer.
    """
    __slots__ = ('seconds',)

    UNIQUE_TARGET_FQN = 'petronia_core.timer:configuration'
    UNIQUE_TARGET_REL = 'petronia_core.timer:configuration'

    def __init__(
        self,
        seconds: float,
    ) -> None:
        self.seconds = seconds

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'seconds': self.seconds,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ConfigurationState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('seconds')
        f_seconds: float
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='seconds',
                name='ConfigurationState',
            )
        else:
            if not isinstance(val, SupportsFloat):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='seconds',
                    type='float',
                    name='ConfigurationState',
                )
            f_seconds = float(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ConfigurationState(
            seconds=not_none(f_seconds),
        ))

    def __repr__(self) -> str:
        return "ConfigurationState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
