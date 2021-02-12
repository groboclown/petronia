# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-12T16:50:56.795372+00:00

"""
Data structures and marshalling for extension petronia.core.api.native.monitor version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods


from typing import (
    Dict,
    SupportsInt,
    Any,
    List,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    StdRet,
    not_none,
    collect_errors_from,
    STANDARD_PETRONIA_CATALOG,
)

EXTENSION_NAME = 'petronia.core.api.native.monitor'
EXTENSION_VERSION = (1, 0, 0)


class Monitors:
    """
    (no description)
    """
    __slots__ = ('identifier', 'description', 'real_pixel_width', 'real_pixel_height', 'dpi_x', 'dpi_y', 'supports_rotation',)

    def __init__(
        self,
        identifier: int,
        description: str,
        real_pixel_width: int,
        real_pixel_height: int,
        dpi_x: int,
        dpi_y: int,
        supports_rotation: bool,
    ) -> None:
        self.identifier = identifier
        self.description = description
        self.real_pixel_width = real_pixel_width
        self.real_pixel_height = real_pixel_height
        self.dpi_x = dpi_x
        self.dpi_y = dpi_y
        self.supports_rotation = supports_rotation

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'description': self.description,
            'real_pixel_width': self.real_pixel_width,
            'real_pixel_height': self.real_pixel_height,
            'dpi_x': self.dpi_x,
            'dpi_y': self.dpi_y,
            'supports_rotation': self.supports_rotation,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Monitors']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('identifier')
        f_identifier: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='identifier',
                name='Monitors',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='int',
                    name='Monitors',
                )
            f_identifier = int(val)
        val = data.get('description')
        f_description: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='description',
                name='Monitors',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='description',
                    type='str',
                    name='Monitors',
                )
            f_description = val
        val = data.get('real_pixel_width')
        f_real_pixel_width: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='real_pixel_width',
                name='Monitors',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='real_pixel_width',
                    type='int',
                    name='Monitors',
                )
            f_real_pixel_width = int(val)
        val = data.get('real_pixel_height')
        f_real_pixel_height: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='real_pixel_height',
                name='Monitors',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='real_pixel_height',
                    type='int',
                    name='Monitors',
                )
            f_real_pixel_height = int(val)
        val = data.get('dpi_x')
        f_dpi_x: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='dpi_x',
                name='Monitors',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='dpi_x',
                    type='int',
                    name='Monitors',
                )
            f_dpi_x = int(val)
        val = data.get('dpi_y')
        f_dpi_y: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='dpi_y',
                name='Monitors',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='dpi_y',
                    type='int',
                    name='Monitors',
                )
            f_dpi_y = int(val)
        val = data.get('supports_rotation')
        f_supports_rotation: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='supports_rotation',
                name='Monitors',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='supports_rotation',
                    type='bool',
                    name='Monitors',
                )
            f_supports_rotation = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Monitors(
            identifier=not_none(f_identifier),
            description=not_none(f_description),
            real_pixel_width=not_none(f_real_pixel_width),
            real_pixel_height=not_none(f_real_pixel_height),
            dpi_x=not_none(f_dpi_x),
            dpi_y=not_none(f_dpi_y),
            supports_rotation=not_none(f_supports_rotation),
        ))

    def __repr__(self) -> str:
        return "Monitors(" + repr(self.export_data()) + ")"


class ActiveMonitorsState:
    """
    Information about the user's monitors. In nearly all cases, a virtual screen
    layout should be used instead of this low-level detail, so that low-level
    scaling can be properly used.
    """
    __slots__ = ('monitors',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.native.monitor:active-monitors'
    UNIQUE_TARGET_REL = 'petronia.core.api.native.monitor:active-monitors'

    def __init__(
        self,
        monitors: List[Monitors],
    ) -> None:
        self.monitors = monitors

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'monitors': [v.export_data() for v in self.monitors],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ActiveMonitorsState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('monitors')
        f_monitors: List[Monitors]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='monitors',
                name='ActiveMonitorsState',
            )
        else:
            f_monitors = []
            for item in val:
                parsed_monitors = Monitors.parse_data(item)
                if parsed_monitors.has_error:
                    return parsed_monitors.forward()
                f_monitors.append(parsed_monitors.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ActiveMonitorsState(
            monitors=not_none(f_monitors),
        ))

    def __repr__(self) -> str:
        return "ActiveMonitorsState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
