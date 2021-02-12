# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-11T17:55:50.534545+00:00

"""
Data structures and marshalling for extension petronia.core.api.native.screen version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods


from typing import (
    SupportsInt,
    Dict,
    List,
    Any,
    Optional,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    StdRet,
    not_none,
    STANDARD_PETRONIA_CATALOG,
)

EXTENSION_NAME = 'petronia.core.api.native.screen'
EXTENSION_VERSION = (1, 0, 0)


class ScreenMonitorMapping:
    """
    A description of a virtual screen, and how it maps to an underlying monitor.
    """
    __slots__ = ('source_monitor', 'source_nw_x_pixel', 'source_nw_y_pixel', 'source_pixel_width', 'source_pixel_height', 'rotation', 'virtual_nw_x_pixel', 'virtual_nw_y_pixel', 'virtual_width', 'virtual_height',)

    def __init__(
        self,
        source_monitor: Optional[int],
        source_nw_x_pixel: int,
        source_nw_y_pixel: int,
        source_pixel_width: int,
        source_pixel_height: int,
        rotation: int,
        virtual_nw_x_pixel: int,
        virtual_nw_y_pixel: int,
        virtual_width: int,
        virtual_height: int,
    ) -> None:
        self.source_monitor = source_monitor
        self.source_nw_x_pixel = source_nw_x_pixel
        self.source_nw_y_pixel = source_nw_y_pixel
        self.source_pixel_width = source_pixel_width
        self.source_pixel_height = source_pixel_height
        self.rotation = rotation
        self.virtual_nw_x_pixel = virtual_nw_x_pixel
        self.virtual_nw_y_pixel = virtual_nw_y_pixel
        self.virtual_width = virtual_width
        self.virtual_height = virtual_height

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'source_monitor': self.source_monitor,
            'source_nw_x_pixel': self.source_nw_x_pixel,
            'source_nw_y_pixel': self.source_nw_y_pixel,
            'source_pixel_width': self.source_pixel_width,
            'source_pixel_height': self.source_pixel_height,
            'rotation': self.rotation,
            'virtual_nw_x_pixel': self.virtual_nw_x_pixel,
            'virtual_nw_y_pixel': self.virtual_nw_y_pixel,
            'virtual_width': self.virtual_width,
            'virtual_height': self.virtual_height,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ScreenMonitorMapping']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('source_monitor')
        f_source_monitor: Optional[int] = None
        if val is not None:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='source_monitor',
                    type='int',
                    name='ScreenMonitorMapping',
                )
            f_source_monitor = int(val)
        val = data.get('source_nw_x_pixel')
        f_source_nw_x_pixel: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='source_nw_x_pixel',
                name='ScreenMonitorMapping',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='source_nw_x_pixel',
                    type='int',
                    name='ScreenMonitorMapping',
                )
            f_source_nw_x_pixel = int(val)
        val = data.get('source_nw_y_pixel')
        f_source_nw_y_pixel: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='source_nw_y_pixel',
                name='ScreenMonitorMapping',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='source_nw_y_pixel',
                    type='int',
                    name='ScreenMonitorMapping',
                )
            f_source_nw_y_pixel = int(val)
        val = data.get('source_pixel_width')
        f_source_pixel_width: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='source_pixel_width',
                name='ScreenMonitorMapping',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='source_pixel_width',
                    type='int',
                    name='ScreenMonitorMapping',
                )
            f_source_pixel_width = int(val)
        val = data.get('source_pixel_height')
        f_source_pixel_height: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='source_pixel_height',
                name='ScreenMonitorMapping',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='source_pixel_height',
                    type='int',
                    name='ScreenMonitorMapping',
                )
            f_source_pixel_height = int(val)
        val = data.get('rotation')
        f_rotation: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='rotation',
                name='ScreenMonitorMapping',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='rotation',
                    type='int',
                    name='ScreenMonitorMapping',
                )
            f_rotation = int(val)
        val = data.get('virtual_nw_x_pixel')
        f_virtual_nw_x_pixel: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='virtual_nw_x_pixel',
                name='ScreenMonitorMapping',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='virtual_nw_x_pixel',
                    type='int',
                    name='ScreenMonitorMapping',
                )
            f_virtual_nw_x_pixel = int(val)
        val = data.get('virtual_nw_y_pixel')
        f_virtual_nw_y_pixel: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='virtual_nw_y_pixel',
                name='ScreenMonitorMapping',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='virtual_nw_y_pixel',
                    type='int',
                    name='ScreenMonitorMapping',
                )
            f_virtual_nw_y_pixel = int(val)
        val = data.get('virtual_width')
        f_virtual_width: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='virtual_width',
                name='ScreenMonitorMapping',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='virtual_width',
                    type='int',
                    name='ScreenMonitorMapping',
                )
            f_virtual_width = int(val)
        val = data.get('virtual_height')
        f_virtual_height: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='virtual_height',
                name='ScreenMonitorMapping',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='virtual_height',
                    type='int',
                    name='ScreenMonitorMapping',
                )
            f_virtual_height = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ScreenMonitorMapping(
            source_monitor=f_source_monitor,
            source_nw_x_pixel=not_none(f_source_nw_x_pixel),
            source_nw_y_pixel=not_none(f_source_nw_y_pixel),
            source_pixel_width=not_none(f_source_pixel_width),
            source_pixel_height=not_none(f_source_pixel_height),
            rotation=not_none(f_rotation),
            virtual_nw_x_pixel=not_none(f_virtual_nw_x_pixel),
            virtual_nw_y_pixel=not_none(f_virtual_nw_y_pixel),
            virtual_width=not_none(f_virtual_width),
            virtual_height=not_none(f_virtual_height),
        ))

    def __repr__(self) -> str:
        return "ScreenMonitorMapping(" + repr(self.export_data()) + ")"


class MapMonitorsRequestEvent:
    """
    Maps monitor identifier numbers to a virtual screen space. This implicitly
    includes the scaling factor. The map request must be valid. That means: no
    pixels are shared between virtual spaces, and requested monitors must exist at
    the time of the request. The implementation may have its own additional
    requirements.
    """
    __slots__ = ('sceens',)
    FULL_EVENT_NAME = 'petronia.core.api.native.screen:map-monitors:request'
    SHORT_EVENT_NAME = 'map-monitors:request'

    def __init__(
        self,
        sceens: List[ScreenMonitorMapping],
    ) -> None:
        self.sceens = sceens

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return MapMonitorsRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'sceens': [v.export_data() for v in self.sceens],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['MapMonitorsRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('sceens')
        f_sceens: List[ScreenMonitorMapping]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='sceens',
                name='MapMonitorsRequestEvent',
            )
        else:
            f_sceens = []
            for item in val:
                parsed_sceens = ScreenMonitorMapping.parse_data(item)
                if parsed_sceens.has_error:
                    return parsed_sceens.forward()
                f_sceens.append(parsed_sceens.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(MapMonitorsRequestEvent(
            sceens=not_none(f_sceens),
        ))

    def __repr__(self) -> str:
        return "MapMonitorsRequestEvent(" + repr(self.export_data()) + ")"


class Area:
    """
    (no description)
    """
    __slots__ = ('nw_x_pixel', 'nw_y_pixel', 'width', 'height', 'ratio_x', 'ratio_y',)

    def __init__(
        self,
        nw_x_pixel: int,
        nw_y_pixel: int,
        width: int,
        height: int,
        ratio_x: int,
        ratio_y: int,
    ) -> None:
        self.nw_x_pixel = nw_x_pixel
        self.nw_y_pixel = nw_y_pixel
        self.width = width
        self.height = height
        self.ratio_x = ratio_x
        self.ratio_y = ratio_y

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'nw_x_pixel': self.nw_x_pixel,
            'nw_y_pixel': self.nw_y_pixel,
            'width': self.width,
            'height': self.height,
            'ratio_x': self.ratio_x,
            'ratio_y': self.ratio_y,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Area']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('nw_x_pixel')
        f_nw_x_pixel: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='nw_x_pixel',
                name='Area',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='nw_x_pixel',
                    type='int',
                    name='Area',
                )
            f_nw_x_pixel = int(val)
        val = data.get('nw_y_pixel')
        f_nw_y_pixel: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='nw_y_pixel',
                name='Area',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='nw_y_pixel',
                    type='int',
                    name='Area',
                )
            f_nw_y_pixel = int(val)
        val = data.get('width')
        f_width: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='width',
                name='Area',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='width',
                    type='int',
                    name='Area',
                )
            f_width = int(val)
        val = data.get('height')
        f_height: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='height',
                name='Area',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='height',
                    type='int',
                    name='Area',
                )
            f_height = int(val)
        val = data.get('ratio_x')
        f_ratio_x: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='ratio_x',
                name='Area',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='ratio_x',
                    type='int',
                    name='Area',
                )
            f_ratio_x = int(val)
        val = data.get('ratio_y')
        f_ratio_y: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='ratio_y',
                name='Area',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='ratio_y',
                    type='int',
                    name='Area',
                )
            f_ratio_y = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Area(
            nw_x_pixel=not_none(f_nw_x_pixel),
            nw_y_pixel=not_none(f_nw_y_pixel),
            width=not_none(f_width),
            height=not_none(f_height),
            ratio_x=not_none(f_ratio_x),
            ratio_y=not_none(f_ratio_y),
        ))

    def __repr__(self) -> str:
        return "Area(" + repr(self.export_data()) + ")"


class VirtualScreenState:
    """
    Layout of the monitors mapped into a virtual space. Index 0 is considered the
    primary screen, and must have a virtual North-West corner pixel set to (0, 0).
    Note that there isn't necessarily a 1-to-1 screen area to monitor here. Each
    screen area is a rectangle.
    """
    __slots__ = ('area',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.native.screen:virtual-screen'
    UNIQUE_TARGET_REL = 'petronia.core.api.native.screen:virtual-screen'

    def __init__(
        self,
        area: List[Area],
    ) -> None:
        self.area = area

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'area': [v.export_data() for v in self.area],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['VirtualScreenState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('area')
        f_area: List[Area]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='area',
                name='VirtualScreenState',
            )
        else:
            f_area = []
            for item in val:
                parsed_area = Area.parse_data(item)
                if parsed_area.has_error:
                    return parsed_area.forward()
                f_area.append(parsed_area.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(VirtualScreenState(
            area=not_none(f_area),
        ))

    def __repr__(self) -> str:
        return "VirtualScreenState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
