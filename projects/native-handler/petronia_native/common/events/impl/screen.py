# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia.core.api.native.screen version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name,consider-using-f-string

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Dict,
    SupportsInt,
    List,
    Union,
    cast,
    Any,
    Optional,
    SupportsFloat,
)
import datetime
from petronia_common.util import i18n as _
from petronia_common.util import (
    not_none,
    STANDARD_PETRONIA_CATALOG,
    collect_errors_from,
    StdRet,
)

EXTENSION_NAME = 'petronia.core.api.native.screen'
EXTENSION_VERSION = (1, 0, 0)


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


class SetScreenConfigurationRequestEvent:
    """
    Request to set the screen configuration. It will only be set if the
    configuration is valid. If the request is valid, then the screen configuration
    datastore is updated and a success message is sent. Additionally, the active
    virtual-screen datastore value may be updated if this caused a change.
    """
    __slots__ = ('request_id', 'mapped_screens_by_monitors',)
    FULL_EVENT_NAME = 'petronia.core.api.native.screen:set-screen-configuration:request'
    SHORT_EVENT_NAME = 'set-screen-configuration:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.native.screen:configuration'
    UNIQUE_TARGET_REL = 'configuration'

    def __init__(
        self,
        request_id: int,
        mapped_screens_by_monitors: List[ScreenMonitorMappingConfigGroup],
    ) -> None:
        self.request_id = request_id
        self.mapped_screens_by_monitors = mapped_screens_by_monitors

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetScreenConfigurationRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'request_id': self.request_id,
            'mapped_screens_by_monitors': [v.export_data() for v in self.mapped_screens_by_monitors],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SetScreenConfigurationRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('request_id')
        f_request_id: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='request_id',
                name='SetScreenConfigurationRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='request_id',
                    type='int',
                    name='SetScreenConfigurationRequestEvent',
                )
            f_request_id = int(val)
        val = data.get('mapped_screens_by_monitors')
        f_mapped_screens_by_monitors: List[ScreenMonitorMappingConfigGroup]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='mapped_screens_by_monitors',
                name='SetScreenConfigurationRequestEvent',
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
        return StdRet.pass_ok(SetScreenConfigurationRequestEvent(
            request_id=not_none(f_request_id),
            mapped_screens_by_monitors=not_none(f_mapped_screens_by_monitors),
        ))

    def __repr__(self) -> str:
        return "SetScreenConfigurationRequestEvent(" + repr(self.export_data()) + ")"


class SetScreenConfigurationSuccessEvent:
    """
    The screen configuration request was successful. The request_id will be set to
    the original configuration set request, and the event's target_id is set to the
    original source_id.
    """
    __slots__ = ('request_id',)
    FULL_EVENT_NAME = 'petronia.core.api.native.screen:set-screen-configuration:success'
    SHORT_EVENT_NAME = 'set-screen-configuration:success'

    def __init__(
        self,
        request_id: int,
    ) -> None:
        self.request_id = request_id

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetScreenConfigurationSuccessEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'request_id': self.request_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SetScreenConfigurationSuccessEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('request_id')
        f_request_id: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='request_id',
                name='SetScreenConfigurationSuccessEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='request_id',
                    type='int',
                    name='SetScreenConfigurationSuccessEvent',
                )
            f_request_id = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SetScreenConfigurationSuccessEvent(
            request_id=not_none(f_request_id),
        ))

    def __repr__(self) -> str:
        return "SetScreenConfigurationSuccessEvent(" + repr(self.export_data()) + ")"


class MessageArgumentValue:
    """
    A replacement value for a named argument in the message.
    """
    __slots__ = ('__name', '__value')

    def __init__(
        self,
        name: str,
        value: Union[
            int,
            List[bool],
            bool,
            List[str],
            List[datetime.datetime],
            str,
            datetime.datetime,
            List[float],
            List[int],
            float,
        ],
    ) -> None:
        self.__name = name
        self.__value = value

    @property
    def name(self) -> str:
        """Name of the selector type."""
        return self.__name

    @property
    def value(self) -> Union[
            int,
            List[bool],
            bool,
            List[str],
            List[datetime.datetime],
            str,
            datetime.datetime,
            List[float],
            List[int],
            float,
    ]:
        """The selector value."""
        return self.__value

    def __repr__(self) -> str:
        return 'MessageArgumentValue(type: {0}, value: {1})'.format(
            self.__name, repr(self.__value),
        )

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0912
        """Create the event data structure, ready for marshalling."""
        if self.__name == 'string':
            return {
                '^': self.__name,
                '$':
                    cast(str, self.__value),
            }
        if self.__name == 'int':
            return {
                '^': self.__name,
                '$':
                    cast(int, self.__value),
            }
        if self.__name == 'float':
            return {
                '^': self.__name,
                '$':
                    cast(float, self.__value),
            }
        if self.__name == 'bool':
            return {
                '^': self.__name,
                '$':
                    cast(bool, self.__value),
            }
        if self.__name == 'datetime':
            return {
                '^': self.__name,
                '$':
                    cast(datetime.datetime, self.__value).strftime('%Y%m%d:%H%M%S.%f:%z'),
            }
        if self.__name == 'string_list':
            return {
                '^': self.__name,
                '$':
                    list(cast(List[str], self.__value)),
            }
        if self.__name == 'int_list':
            return {
                '^': self.__name,
                '$':
                    list(cast(List[int], self.__value)),
            }
        if self.__name == 'float_list':
            return {
                '^': self.__name,
                '$':
                    list(cast(List[float], self.__value)),
            }
        if self.__name == 'bool_list':
            return {
                '^': self.__name,
                '$':
                    list(cast(List[bool], self.__value)),
            }
        if self.__name == 'datetime_list':
            return {
                '^': self.__name,
                '$':
                    [dtv.strftime('%Y%m%d:%H%M%S.%f:%z') for dtv in cast(List[datetime.datetime], self.__value)],
            }
        raise RuntimeError('invalid inner type: ' + repr(self.__name))  # pragma no cover

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['MessageArgumentValue']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        selector_name = data.get('^', data.get('type'))
        val = data.get('$', data.get('value'))
        if not isinstance(selector_name, str):
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('selector for {name} value must have ^ and $ keys, or "type" and "value" keys'),
                name='MessageArgumentValue',
            )
        if selector_name == 'string':
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='string',
                    type='str',
                    name='MessageArgumentValue',
                )
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                val,
            ))
        if selector_name == 'int':
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='int',
                    type='int',
                    name='MessageArgumentValue',
                )
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                int(val),
            ))
        if selector_name == 'float':
            if not isinstance(val, SupportsFloat):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='float',
                    type='float',
                    name='MessageArgumentValue',
                )
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                float(val),
            ))
        if selector_name == 'bool':
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='bool',
                    type='bool',
                    name='MessageArgumentValue',
                )
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                val,
            ))
        if selector_name == 'datetime':
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Value must be of type datetime for selector {name}'),
                    field_name='datetime',
                    name='MessageArgumentValue',
                )
            try:
                dt_val = datetime.datetime.strptime(val, '%Y%m%d:%H%M%S.%f:%z')
                return StdRet.pass_ok(MessageArgumentValue(
                    selector_name,
                    dt_val,
                ))
            except ValueError:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Invalid date-time format: {value}'),
                    value=val,
                )
        if selector_name == 'string_list':
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for selector {name}'),
                    field_name='string_list',
                    type='List[str]',
                    name='MessageArgumentValue',
                )
            ret_val_str: List[str] = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='string_list',
                        type='str',
                        name='MessageArgumentValue',
                    )
                ret_val_str.append(item)
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                ret_val_str,
            ))
        if selector_name == 'int_list':
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for selector {name}'),
                    field_name='int_list',
                    type='List[int]',
                    name='MessageArgumentValue',
                )
            ret_val_int: List[int] = []
            for item in val:
                if not isinstance(item, int):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='int_list',
                        type='int',
                        name='MessageArgumentValue',
                    )
                ret_val_int.append(item)
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                ret_val_int,
            ))
        if selector_name == 'float_list':
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for selector {name}'),
                    field_name='float_list',
                    type='List[float]',
                    name='MessageArgumentValue',
                )
            ret_val_float: List[float] = []
            for item in val:
                if not isinstance(item, float):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='float_list',
                        type='float',
                        name='MessageArgumentValue',
                    )
                ret_val_float.append(item)
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                ret_val_float,
            ))
        if selector_name == 'bool_list':
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for selector {name}'),
                    field_name='bool_list',
                    type='List[bool]',
                    name='MessageArgumentValue',
                )
            ret_val_bool: List[bool] = []
            for item in val:
                if not isinstance(item, bool):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='bool_list',
                        type='bool',
                        name='MessageArgumentValue',
                    )
                ret_val_bool.append(item)
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                ret_val_bool,
            ))
        if selector_name == 'datetime_list':
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for selector {name}'),
                    field_name='datetime_list',
                    type='List[datetime.datetime]',
                    name='MessageArgumentValue',
                )
            ret_val_datetime_datetime: List[datetime.datetime] = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='datetime_list',
                        type='datetime.datetime',
                        name='MessageArgumentValue',
                    )
                try:
                    ret_val_datetime_datetime.append(datetime.datetime.strptime(item, '%Y%m%d:%H%M%S.%f:%z'))
                except ValueError:
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _('Invalid date-time format: {value}'),
                        value=val,
                    )
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                ret_val_datetime_datetime,
            ))
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('Invalid selector name {name} for {nc}'),
            name=selector_name,
            nc='MessageArgumentValue',
        )


class MessageArgument:
    """
    An argument to be inserted into the localizable message.
    """
    __slots__ = ('name', 'value',)

    def __init__(
        self,
        name: str,
        value: MessageArgumentValue,
    ) -> None:
        self.name = name
        self.value = value

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'value': self.value.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['MessageArgument']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('name')
        f_name: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='MessageArgument',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='MessageArgument',
                )
            f_name = val
        val = data.get('value')
        f_value: MessageArgumentValue
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='value',
                name='MessageArgument',
            )
        else:
            parsed_value = MessageArgumentValue.parse_data(val)
            if parsed_value.has_error:
                return parsed_value.forward()
            if parsed_value.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='value',
                )
            f_value = parsed_value.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(MessageArgument(
            name=not_none(f_name),
            value=not_none(f_value),
        ))

    def __repr__(self) -> str:
        return "MessageArgument(" + repr(self.export_data()) + ")"


class LocalizableMessage:
    """
    A localizable message for user display.
    """
    __slots__ = ('catalog', 'message', 'arguments',)

    def __init__(
        self,
        catalog: str,
        message: str,
        arguments: Optional[List[MessageArgument]],
    ) -> None:
        self.catalog = catalog
        self.message = message
        self.arguments = arguments

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'catalog': self.catalog,
            'message': self.message,
            'arguments': None if self.arguments is None else [v.export_data() for v in self.arguments],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LocalizableMessage']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('catalog')
        f_catalog: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='catalog',
                name='LocalizableMessage',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='catalog',
                    type='str',
                    name='LocalizableMessage',
                )
            f_catalog = val
        val = data.get('message')
        f_message: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='message',
                name='LocalizableMessage',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='message',
                    type='str',
                    name='LocalizableMessage',
                )
            f_message = val
        val = data.get('arguments')
        f_arguments: Optional[List[MessageArgument]] = None
        if val is not None:
            f_arguments = []
            for item in val:
                parsed_arguments = MessageArgument.parse_data(item)
                if parsed_arguments.has_error:
                    return parsed_arguments.forward()
                f_arguments.append(parsed_arguments.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LocalizableMessage(
            catalog=not_none(f_catalog),
            message=not_none(f_message),
            arguments=f_arguments,
        ))

    def __repr__(self) -> str:
        return "LocalizableMessage(" + repr(self.export_data()) + ")"


class Error:
    """
    A description of a failure.
    """
    __slots__ = ('identifier', 'categories', 'source', 'messages',)

    def __init__(
        self,
        identifier: str,
        categories: List[str],
        source: Optional[str],
        messages: List[LocalizableMessage],
    ) -> None:
        self.identifier = identifier
        self.categories = categories
        self.source = source
        self.messages = messages

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'categories': list(self.categories),
            'source': self.source,
            'messages': [v.export_data() for v in self.messages],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Error']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('identifier')
        f_identifier: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='identifier',
                name='Error',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='str',
                    name='Error',
                )
            f_identifier = val
        val = data.get('categories')
        f_categories: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='categories',
                name='Error',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='categories',
                    type='List[str]',
                    name='Error',
                )
            f_categories = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='categories',
                        type='str',
                        name='Error',
                    )
                f_categories.append(item)
        val = data.get('source')
        f_source: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='source',
                    type='str',
                    name='Error',
                )
            f_source = val
        val = data.get('messages')
        f_messages: List[LocalizableMessage]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='messages',
                name='Error',
            )
        else:
            f_messages = []
            for item in val:
                parsed_messages = LocalizableMessage.parse_data(item)
                if parsed_messages.has_error:
                    return parsed_messages.forward()
                f_messages.append(parsed_messages.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Error(
            identifier=not_none(f_identifier),
            categories=not_none(f_categories),
            source=f_source,
            messages=not_none(f_messages),
        ))

    def __repr__(self) -> str:
        return "Error(" + repr(self.export_data()) + ")"


class SetScreenConfigurationFailureEvent:
    """
    The screen configuration request failed due to a problem with the request. The
    request_id will be set to the original configuration set request, and the
    event's target_id is set to the original source_id.
    """
    __slots__ = ('request_id', 'error',)
    FULL_EVENT_NAME = 'petronia.core.api.native.screen:set-screen-configuration:failure'
    SHORT_EVENT_NAME = 'set-screen-configuration:failure'

    def __init__(
        self,
        request_id: int,
        error: Error,
    ) -> None:
        self.request_id = request_id
        self.error = error

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetScreenConfigurationFailureEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'request_id': self.request_id,
            'error': self.error.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SetScreenConfigurationFailureEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('request_id')
        f_request_id: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='request_id',
                name='SetScreenConfigurationFailureEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='request_id',
                    type='int',
                    name='SetScreenConfigurationFailureEvent',
                )
            f_request_id = int(val)
        val = data.get('error')
        f_error: Error
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='error',
                name='SetScreenConfigurationFailureEvent',
            )
        else:
            parsed_error = Error.parse_data(val)
            if parsed_error.has_error:
                return parsed_error.forward()
            if parsed_error.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='error',
                )
            f_error = parsed_error.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SetScreenConfigurationFailureEvent(
            request_id=not_none(f_request_id),
            error=not_none(f_error),
        ))

    def __repr__(self) -> str:
        return "SetScreenConfigurationFailureEvent(" + repr(self.export_data()) + ")"


class VirtualScreenBlock:
    """
    A single block of virtual screen space, usually maps to a single monitor.
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
    def parse_data(data: Dict[str, Any]) -> StdRet['VirtualScreenBlock']:  # pylint: disable=R0912,R0911
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
                name='VirtualScreenBlock',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='nw_x_pixel',
                    type='int',
                    name='VirtualScreenBlock',
                )
            f_nw_x_pixel = int(val)
        val = data.get('nw_y_pixel')
        f_nw_y_pixel: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='nw_y_pixel',
                name='VirtualScreenBlock',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='nw_y_pixel',
                    type='int',
                    name='VirtualScreenBlock',
                )
            f_nw_y_pixel = int(val)
        val = data.get('width')
        f_width: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='width',
                name='VirtualScreenBlock',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='width',
                    type='int',
                    name='VirtualScreenBlock',
                )
            f_width = int(val)
        val = data.get('height')
        f_height: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='height',
                name='VirtualScreenBlock',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='height',
                    type='int',
                    name='VirtualScreenBlock',
                )
            f_height = int(val)
        val = data.get('ratio_x')
        f_ratio_x: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='ratio_x',
                name='VirtualScreenBlock',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='ratio_x',
                    type='int',
                    name='VirtualScreenBlock',
                )
            f_ratio_x = int(val)
        val = data.get('ratio_y')
        f_ratio_y: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='ratio_y',
                name='VirtualScreenBlock',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='ratio_y',
                    type='int',
                    name='VirtualScreenBlock',
                )
            f_ratio_y = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(VirtualScreenBlock(
            nw_x_pixel=not_none(f_nw_x_pixel),
            nw_y_pixel=not_none(f_nw_y_pixel),
            width=not_none(f_width),
            height=not_none(f_height),
            ratio_x=not_none(f_ratio_x),
            ratio_y=not_none(f_ratio_y),
        ))

    def __repr__(self) -> str:
        return "VirtualScreenBlock(" + repr(self.export_data()) + ")"


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
        area: List[VirtualScreenBlock],
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
        f_area: List[VirtualScreenBlock]
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
                parsed_area = VirtualScreenBlock.parse_data(item)
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


class ScreenSetupsState:
    """
    The virtual screen mapping for different screen sizes. Any call to set the
    current monitor mapping will change the current value in this configuration. If
    the monitor state changes, then this is used to reference the new virtual-screen
    setting. This is used as reference for other extensions for a platform-agnostic
    method for discovering existing, stored screen mapping configurations. The
    storage of the user-defined persistent values should be maintained by the
    implementing native handler.
    """
    __slots__ = ('mapped_screens_by_monitors',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.native.screen:screen-setups'
    UNIQUE_TARGET_REL = 'petronia.core.api.native.screen:screen-setups'

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
    def parse_data(data: Dict[str, Any]) -> StdRet['ScreenSetupsState']:  # pylint: disable=R0912,R0911
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
                name='ScreenSetupsState',
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
        return StdRet.pass_ok(ScreenSetupsState(
            mapped_screens_by_monitors=not_none(f_mapped_screens_by_monitors),
        ))

    def __repr__(self) -> str:
        return "ScreenSetupsState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
