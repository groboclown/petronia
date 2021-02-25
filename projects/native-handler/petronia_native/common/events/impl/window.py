# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-24T16:41:12.256898+00:00

"""
Data structures and marshalling for extension petronia.core.api.native.window version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods


from typing import (
    SupportsInt,
    Dict,
    Any,
    List,
    Optional,
    cast,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    StdRet,
    STANDARD_PETRONIA_CATALOG,
    not_none,
)

EXTENSION_NAME = 'petronia.core.api.native.window'
EXTENSION_VERSION = (1, 0, 0)


class ScreenDimension:
    """
    The screen position and size of a component. Unless otherwise specified, these
    are in virtual screen position, meaning that it's spread across all monitors and
    scaled.
    """
    __slots__ = ('x', 'y', 'width', 'height',)

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ScreenDimension']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('x')
        f_x: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='x',
                name='ScreenDimension',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='x',
                    type='int',
                    name='ScreenDimension',
                )
            f_x = int(val)
        val = data.get('y')
        f_y: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='y',
                name='ScreenDimension',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='y',
                    type='int',
                    name='ScreenDimension',
                )
            f_y = int(val)
        val = data.get('width')
        f_width: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='width',
                name='ScreenDimension',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='width',
                    type='int',
                    name='ScreenDimension',
                )
            f_width = int(val)
        val = data.get('height')
        f_height: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='height',
                name='ScreenDimension',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='height',
                    type='int',
                    name='ScreenDimension',
                )
            f_height = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ScreenDimension(
            x=not_none(f_x),
            y=not_none(f_y),
            width=not_none(f_width),
            height=not_none(f_height),
        ))

    def __repr__(self) -> str:
        return "ScreenDimension(" + repr(self.export_data()) + ")"


class Meta:
    """
    (no description)
    """
    __slots__ = ('key', 'value',)

    def __init__(
        self,
        key: str,
        value: str,
    ) -> None:
        self.key = key
        self.value = value

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'key': self.key,
            'value': self.value,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Meta']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('key')
        f_key: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='key',
                name='Meta',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='key',
                    type='str',
                    name='Meta',
                )
            f_key = val
        val = data.get('value')
        f_value: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='value',
                name='Meta',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='value',
                    type='str',
                    name='Meta',
                )
            f_value = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Meta(
            key=not_none(f_key),
            value=not_none(f_value),
        ))

    def __repr__(self) -> str:
        return "Meta(" + repr(self.export_data()) + ")"


class WindowState:
    """
    The state of a window.
    """
    __slots__ = ('active', 'focus', 'parent_id', 'flashing', 'location', 'minimized', 'meta',)

    def __init__(
        self,
        active: bool,
        focus: int,
        parent_id: Optional[str],
        flashing: bool,
        location: ScreenDimension,
        minimized: bool,
        meta: List[Meta],
    ) -> None:
        self.active = active
        self.focus = focus
        self.parent_id = parent_id
        self.flashing = flashing
        self.location = location
        self.minimized = minimized
        self.meta = meta

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'active': self.active,
            'focus': self.focus,
            'parent_id': self.parent_id,
            'flashing': self.flashing,
            'location': self.location.export_data(),
            'minimized': self.minimized,
            'meta': [v.export_data() for v in self.meta],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('active')
        f_active: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='active',
                name='WindowState',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='active',
                    type='bool',
                    name='WindowState',
                )
            f_active = val
        val = data.get('focus')
        f_focus: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='focus',
                name='WindowState',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='focus',
                    type='int',
                    name='WindowState',
                )
            f_focus = int(val)
        val = data.get('parent_id')
        f_parent_id: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='parent_id',
                    type='str',
                    name='WindowState',
                )
            f_parent_id = val
        val = data.get('flashing')
        f_flashing: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='flashing',
                name='WindowState',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='flashing',
                    type='bool',
                    name='WindowState',
                )
            f_flashing = val
        val = data.get('location')
        f_location: ScreenDimension
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='location',
                name='WindowState',
            )
        else:
            parsed_location = ScreenDimension.parse_data(val)
            if parsed_location.has_error:
                return parsed_location.forward()
            if parsed_location.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='location',
                )
            f_location = parsed_location.result
        val = data.get('minimized')
        f_minimized: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='minimized',
                name='WindowState',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='minimized',
                    type='bool',
                    name='WindowState',
                )
            f_minimized = val
        val = data.get('meta')
        f_meta: List[Meta]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='meta',
                name='WindowState',
            )
        else:
            f_meta = []
            for item in val:
                parsed_meta = Meta.parse_data(item)
                if parsed_meta.has_error:
                    return parsed_meta.forward()
                f_meta.append(parsed_meta.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowState(
            active=not_none(f_active),
            focus=not_none(f_focus),
            parent_id=f_parent_id,
            flashing=not_none(f_flashing),
            location=not_none(f_location),
            minimized=not_none(f_minimized),
            meta=not_none(f_meta),
        ))

    def __repr__(self) -> str:
        return "WindowState(" + repr(self.export_data()) + ")"


class WindowCreatedEvent:
    """
    A UI window was created. The source ID can be used for sending requests to alter
    the window state. Additionally, this indicates that the corresponding state
    object has also been created, and updates to the window state are broadcast to
    that state object.
    """
    __slots__ = ('state',)
    FULL_EVENT_NAME = 'petronia.core.api.native.window:window-created'
    SHORT_EVENT_NAME = 'window-created'

    def __init__(
        self,
        state: WindowState,
    ) -> None:
        self.state = state

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return WindowCreatedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'state': self.state.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowCreatedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('state')
        f_state: WindowState
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='state',
                name='WindowCreatedEvent',
            )
        else:
            parsed_state = WindowState.parse_data(val)
            if parsed_state.has_error:
                return parsed_state.forward()
            if parsed_state.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='state',
                )
            f_state = parsed_state.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowCreatedEvent(
            state=not_none(f_state),
        ))

    def __repr__(self) -> str:
        return "WindowCreatedEvent(" + repr(self.export_data()) + ")"


class WindowDestroyedEvent:
    """
    A UI window was destroyed. In addition to this event, the corresponding state
    object for the window is also removed.
    """
    __slots__ = ('reason',)
    FULL_EVENT_NAME = 'petronia.core.api.native.window:window-destroyed'
    SHORT_EVENT_NAME = 'window-destroyed'

    def __init__(
        self,
        reason: str,
    ) -> None:
        self.reason = reason

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return WindowDestroyedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'reason': self.reason,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowDestroyedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('reason')
        f_reason: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='reason',
                name='WindowDestroyedEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='reason',
                    type='str',
                    name='WindowDestroyedEvent',
                )
            f_reason = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowDestroyedEvent(
            reason=not_none(f_reason),
        ))

    def __repr__(self) -> str:
        return "WindowDestroyedEvent(" + repr(self.export_data()) + ")"


class WindowIdPositions:
    """
    (no description)
    """
    __slots__ = ('window_id', 'location',)

    def __init__(
        self,
        window_id: str,
        location: Optional[ScreenDimension],
    ) -> None:
        self.window_id = window_id
        self.location = location

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'window_id': self.window_id,
            'location': None if self.location is None else self.location.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowIdPositions']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('window_id')
        f_window_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='window_id',
                name='WindowIdPositions',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='window_id',
                    type='str',
                    name='WindowIdPositions',
                )
            f_window_id = val
        val = data.get('location')
        f_location: Optional[ScreenDimension] = None
        if val is not None:
            parsed_location = ScreenDimension.parse_data(val)
            if parsed_location.has_error:
                return parsed_location.forward()
            # Value, not result, because it could be optional...
            f_location = parsed_location.value
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowIdPositions(
            window_id=not_none(f_window_id),
            location=f_location,
        ))

    def __repr__(self) -> str:
        return "WindowIdPositions(" + repr(self.export_data()) + ")"


class SetWindowPositionsEvent:
    """
    Request changes to zero or more window positions. This is useful for systems
    that rearrange the whole screen, or move between virtual desktops.
    """
    __slots__ = ('window_id_positions',)
    FULL_EVENT_NAME = 'petronia.core.api.native.window:set-window-positions'
    SHORT_EVENT_NAME = 'set-window-positions'

    def __init__(
        self,
        window_id_positions: List[WindowIdPositions],
    ) -> None:
        self.window_id_positions = window_id_positions

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetWindowPositionsEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'window_id_positions': [v.export_data() for v in self.window_id_positions],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SetWindowPositionsEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('window_id_positions')
        f_window_id_positions: List[WindowIdPositions]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='window_id_positions',
                name='SetWindowPositionsEvent',
            )
        else:
            f_window_id_positions = []
            for item in val:
                parsed_window_id_positions = WindowIdPositions.parse_data(item)
                if parsed_window_id_positions.has_error:
                    return parsed_window_id_positions.forward()
                f_window_id_positions.append(parsed_window_id_positions.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SetWindowPositionsEvent(
            window_id_positions=not_none(f_window_id_positions),
        ))

    def __repr__(self) -> str:
        return "SetWindowPositionsEvent(" + repr(self.export_data()) + ")"


class WindowFocusedEvent:
    """
    Sent when a different window receives keyboard focus.
    """
    __slots__ = ('window_id', 'keyboard_focus',)
    FULL_EVENT_NAME = 'petronia.core.api.native.window:window-focused'
    SHORT_EVENT_NAME = 'window-focused'

    def __init__(
        self,
        window_id: str,
        keyboard_focus: int,
    ) -> None:
        self.window_id = window_id
        self.keyboard_focus = keyboard_focus

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return WindowFocusedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'window_id': self.window_id,
            'keyboard_focus': self.keyboard_focus,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowFocusedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('window_id')
        f_window_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='window_id',
                name='WindowFocusedEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='window_id',
                    type='str',
                    name='WindowFocusedEvent',
                )
            f_window_id = val
        val = data.get('keyboard_focus')
        f_keyboard_focus: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='keyboard_focus',
                name='WindowFocusedEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='keyboard_focus',
                    type='int',
                    name='WindowFocusedEvent',
                )
            f_keyboard_focus = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowFocusedEvent(
            window_id=not_none(f_window_id),
            keyboard_focus=not_none(f_keyboard_focus),
        ))

    def __repr__(self) -> str:
        return "WindowFocusedEvent(" + repr(self.export_data()) + ")"


class FocusSettingsState:
    """
    How the window focus events are translated into Petronia events.
    """
    __slots__ = ('on_new_window_click', 'on_new_window_enter', 'on_window_event',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.native.window:focus-settings'
    UNIQUE_TARGET_REL = 'petronia.core.api.native.window:focus-settings'

    def __init__(
        self,
        on_new_window_click: bool,
        on_new_window_enter: bool,
        on_window_event: bool,
    ) -> None:
        self.on_new_window_click = on_new_window_click
        self.on_new_window_enter = on_new_window_enter
        self.on_window_event = on_window_event

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'on_new_window_click': self.on_new_window_click,
            'on_new_window_enter': self.on_new_window_enter,
            'on_window_event': self.on_window_event,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['FocusSettingsState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('on_new_window_click')
        f_on_new_window_click: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='on_new_window_click',
                name='FocusSettingsState',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='on_new_window_click',
                    type='bool',
                    name='FocusSettingsState',
                )
            f_on_new_window_click = val
        val = data.get('on_new_window_enter')
        f_on_new_window_enter: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='on_new_window_enter',
                name='FocusSettingsState',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='on_new_window_enter',
                    type='bool',
                    name='FocusSettingsState',
                )
            f_on_new_window_enter = val
        val = data.get('on_window_event')
        f_on_window_event: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='on_window_event',
                name='FocusSettingsState',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='on_window_event',
                    type='bool',
                    name='FocusSettingsState',
                )
            f_on_window_event = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(FocusSettingsState(
            on_new_window_click=not_none(f_on_new_window_click),
            on_new_window_enter=not_none(f_on_new_window_enter),
            on_window_event=not_none(f_on_window_event),
        ))

    def __repr__(self) -> str:
        return "FocusSettingsState(" + repr(self.export_data()) + ")"


class ActiveIds:
    """
    (no description)
    """
    __slots__ = ('window_id',)

    def __init__(
        self,
        window_id: str,
    ) -> None:
        self.window_id = window_id

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'window_id': self.window_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ActiveIds']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('window_id')
        f_window_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='window_id',
                name='ActiveIds',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='window_id',
                    type='str',
                    name='ActiveIds',
                )
            f_window_id = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ActiveIds(
            window_id=not_none(f_window_id),
        ))

    def __repr__(self) -> str:
        return "ActiveIds(" + repr(self.export_data()) + ")"


class ActiveWindowsState:
    """
    Information about the windows that are active in the system. For each window in
    this list, its window-id is a structure that conforms to the window-state
    structure in the reference section.
    """
    __slots__ = ('active_ids',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.native.window:active-windows'
    UNIQUE_TARGET_REL = 'petronia.core.api.native.window:active-windows'

    def __init__(
        self,
        active_ids: List[ActiveIds],
    ) -> None:
        self.active_ids = active_ids

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'active_ids': [v.export_data() for v in self.active_ids],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ActiveWindowsState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('active_ids')
        f_active_ids: List[ActiveIds]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='active_ids',
                name='ActiveWindowsState',
            )
        else:
            f_active_ids = []
            for item in val:
                parsed_active_ids = ActiveIds.parse_data(item)
                if parsed_active_ids.has_error:
                    return parsed_active_ids.forward()
                f_active_ids.append(parsed_active_ids.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ActiveWindowsState(
            active_ids=not_none(f_active_ids),
        ))

    def __repr__(self) -> str:
        return "ActiveWindowsState(" + repr(self.export_data()) + ")"


class FocusedWindowsState:
    """
    The windows that have focus. Focus in Petronia allows multiple input groups to
    have their own windows, though most underlying UI systems only have support for
    one user (all keyboards and mice are considered one). Each index represents that
    user group.
    """
    __slots__ = ('focused',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.native.window:focused-windows'
    UNIQUE_TARGET_REL = 'petronia.core.api.native.window:focused-windows'

    def __init__(
        self,
        focused: List[str],
    ) -> None:
        self.focused = focused

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'focused': list(self.focused),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['FocusedWindowsState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('focused')
        f_focused: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='focused',
                name='FocusedWindowsState',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='focused',
                    type='List[str]',
                    name='FocusedWindowsState',
                )
            f_focused = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='focused',
                        type='str',
                        name='FocusedWindowsState',
                    )
                f_focused.append(item)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(FocusedWindowsState(
            focused=not_none(f_focused),
        ))

    def __repr__(self) -> str:
        return "FocusedWindowsState(" + repr(self.export_data()) + ")"


class WindowDetailsState:
    """
    Details for a single window. Note: this is not a state object, but rather a
    template for the data structure that stores the distinct windows. There are one
    of these structures registered for each active window in Petronia.
    """
    __slots__ = ('state',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.native.window:window-details'
    UNIQUE_TARGET_REL = 'petronia.core.api.native.window:window-details'

    def __init__(
        self,
        state: WindowState,
    ) -> None:
        self.state = state

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'state': self.state.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowDetailsState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('state')
        f_state: WindowState
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='state',
                name='WindowDetailsState',
            )
        else:
            parsed_state = WindowState.parse_data(val)
            if parsed_state.has_error:
                return parsed_state.forward()
            if parsed_state.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='state',
                )
            f_state = parsed_state.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowDetailsState(
            state=not_none(f_state),
        ))

    def __repr__(self) -> str:
        return "WindowDetailsState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
