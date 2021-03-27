# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia_native_windows version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Any,
    Optional,
    Dict,
    List,
    SupportsInt,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    STANDARD_PETRONIA_CATALOG,
    StdRet,
    not_none,
)

EXTENSION_NAME = 'petronia_native_windows'
EXTENSION_VERSION = (1, 0, 0)


class Hotkeys:
    """
    Basic hotkey behavior definitions. This does not define the hotkey bindings, but
    rather how Petronia handles certain kinds of events.
    """
    __slots__ = ('own_super_key',)

    def __init__(
        self,
        own_super_key: bool,
    ) -> None:
        self.own_super_key = own_super_key

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'own_super_key': self.own_super_key,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Hotkeys']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('own_super_key')
        f_own_super_key: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='own_super_key',
                name='Hotkeys',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='own_super_key',
                    type='bool',
                    name='Hotkeys',
                )
            f_own_super_key = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Hotkeys(
            own_super_key=not_none(f_own_super_key),
        ))

    def __repr__(self) -> str:
        return "Hotkeys(" + repr(self.export_data()) + ")"


class SourceMonitor:
    """
    A source monitor to match the virtual screen configuration against.
    """
    __slots__ = ('identifier', 'width', 'height',)

    def __init__(
        self,
        identifier: int,
        width: int,
        height: int,
    ) -> None:
        self.identifier = identifier
        self.width = width
        self.height = height

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'width': self.width,
            'height': self.height,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SourceMonitor']:  # pylint: disable=R0912,R0911
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
                name='SourceMonitor',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='int',
                    name='SourceMonitor',
                )
            f_identifier = int(val)
        val = data.get('width')
        f_width: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='width',
                name='SourceMonitor',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='width',
                    type='int',
                    name='SourceMonitor',
                )
            f_width = int(val)
        val = data.get('height')
        f_height: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='height',
                name='SourceMonitor',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='height',
                    type='int',
                    name='SourceMonitor',
                )
            f_height = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SourceMonitor(
            identifier=not_none(f_identifier),
            width=not_none(f_width),
            height=not_none(f_height),
        ))

    def __repr__(self) -> str:
        return "SourceMonitor(" + repr(self.export_data()) + ")"


class ScreenMonitorMapping:
    """
    A description of a virtual screen, and how it maps to an underlying monitor.
    It's possible to define multiple of these mappings per monitor, but serves no
    real purpose.
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


class ScreenMonitorMappingConfigGroup:
    """
    A single configuration defining how all the virtual screen sections are mapped
    into the monitor space.
    """
    __slots__ = ('description', 'monitors', 'screen',)

    def __init__(
        self,
        description: Optional[str],
        monitors: List[SourceMonitor],
        screen: List[ScreenMonitorMapping],
    ) -> None:
        self.description = description
        self.monitors = monitors
        self.screen = screen

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'description': self.description,
            'monitors': [v.export_data() for v in self.monitors],
            'screen': [v.export_data() for v in self.screen],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ScreenMonitorMappingConfigGroup']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('description')
        f_description: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='description',
                    type='str',
                    name='ScreenMonitorMappingConfigGroup',
                )
            f_description = val
        val = data.get('monitors')
        f_monitors: List[SourceMonitor]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='monitors',
                name='ScreenMonitorMappingConfigGroup',
            )
        else:
            f_monitors = []
            for item in val:
                parsed_monitors = SourceMonitor.parse_data(item)
                if parsed_monitors.has_error:
                    return parsed_monitors.forward()
                f_monitors.append(parsed_monitors.result)
        val = data.get('screen')
        f_screen: List[ScreenMonitorMapping]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='screen',
                name='ScreenMonitorMappingConfigGroup',
            )
        else:
            f_screen = []
            for item in val:
                parsed_screen = ScreenMonitorMapping.parse_data(item)
                if parsed_screen.has_error:
                    return parsed_screen.forward()
                f_screen.append(parsed_screen.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ScreenMonitorMappingConfigGroup(
            description=f_description,
            monitors=not_none(f_monitors),
            screen=not_none(f_screen),
        ))

    def __repr__(self) -> str:
        return "ScreenMonitorMappingConfigGroup(" + repr(self.export_data()) + ")"


class VirtualScreens:
    """
    The virtual screen mapping for different screen sizes. Any call to set the
    current monitor mapping will change the current value in this configuration. If
    the monitor state changes, then this is used to reference the new virtual-screen
    setting.
    """
    __slots__ = ('mapped_screens_by_monitors',)

    def __init__(
        self,
        mapped_screens_by_monitors: List[ScreenMonitorMappingConfigGroup],
    ) -> None:
        self.mapped_screens_by_monitors = mapped_screens_by_monitors

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'mapped_screens_by_monitors': [v.export_data() for v in self.mapped_screens_by_monitors],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['VirtualScreens']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('mapped_screens_by_monitors')
        f_mapped_screens_by_monitors: List[ScreenMonitorMappingConfigGroup]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='mapped_screens_by_monitors',
                name='VirtualScreens',
            )
        else:
            f_mapped_screens_by_monitors = []
            for item in val:
                parsed_mapped_screens_by_monitors = ScreenMonitorMappingConfigGroup.parse_data(item)
                if parsed_mapped_screens_by_monitors.has_error:
                    return parsed_mapped_screens_by_monitors.forward()
                f_mapped_screens_by_monitors.append(parsed_mapped_screens_by_monitors.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(VirtualScreens(
            mapped_screens_by_monitors=not_none(f_mapped_screens_by_monitors),
        ))

    def __repr__(self) -> str:
        return "VirtualScreens(" + repr(self.export_data()) + ")"


class ConfigurationState:
    """
    Configuration for all the components of the Windows native handler.
    """
    __slots__ = ('hotkeys', 'virtual_screens',)

    UNIQUE_TARGET_FQN = 'petronia_native_windows:configuration'
    UNIQUE_TARGET_REL = 'petronia_native_windows:configuration'

    def __init__(
        self,
        hotkeys: Hotkeys,
        virtual_screens: VirtualScreens,
    ) -> None:
        self.hotkeys = hotkeys
        self.virtual_screens = virtual_screens

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'hotkeys': self.hotkeys.export_data(),
            'virtual_screens': self.virtual_screens.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ConfigurationState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('hotkeys')
        f_hotkeys: Hotkeys
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='hotkeys',
                name='ConfigurationState',
            )
        else:
            parsed_hotkeys = Hotkeys.parse_data(val)
            if parsed_hotkeys.has_error:
                return parsed_hotkeys.forward()
            if parsed_hotkeys.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='hotkeys',
                )
            f_hotkeys = parsed_hotkeys.result
        val = data.get('virtual_screens')
        f_virtual_screens: VirtualScreens
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='virtual_screens',
                name='ConfigurationState',
            )
        else:
            parsed_virtual_screens = VirtualScreens.parse_data(val)
            if parsed_virtual_screens.has_error:
                return parsed_virtual_screens.forward()
            if parsed_virtual_screens.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='virtual_screens',
                )
            f_virtual_screens = parsed_virtual_screens.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ConfigurationState(
            hotkeys=not_none(f_hotkeys),
            virtual_screens=not_none(f_virtual_screens),
        ))

    def __repr__(self) -> str:
        return "ConfigurationState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
