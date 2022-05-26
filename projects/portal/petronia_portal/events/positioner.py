# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia.core.api.ui.positioner version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name,consider-using-f-string

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    List,
    SupportsInt,
    Dict,
    Optional,
    cast,
    Any,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    StdRet,
    collect_errors_from,
    STANDARD_PETRONIA_CATALOG,
    not_none,
)

EXTENSION_NAME = 'petronia.core.api.ui.positioner'
EXTENSION_VERSION = (1, 0, 0)


class VirtualWindow:
    """
    A window and its position in the virtual desktop.
    """
    __slots__ = ('window_id', 'desktop_id', 'pos_x', 'pos_y', 'width', 'height', 'chrome_west', 'chrome_east', 'chrome_north', 'chrome_south', 'minimized', 'keyboard_focus',)

    def __init__(
        self,
        window_id: str,
        desktop_id: str,
        pos_x: int,
        pos_y: int,
        width: int,
        height: int,
        chrome_west: int,
        chrome_east: int,
        chrome_north: int,
        chrome_south: int,
        minimized: bool,
        keyboard_focus: int,
    ) -> None:
        self.window_id = window_id
        self.desktop_id = desktop_id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.chrome_west = chrome_west
        self.chrome_east = chrome_east
        self.chrome_north = chrome_north
        self.chrome_south = chrome_south
        self.minimized = minimized
        self.keyboard_focus = keyboard_focus

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'window_id': self.window_id,
            'desktop_id': self.desktop_id,
            'pos_x': self.pos_x,
            'pos_y': self.pos_y,
            'width': self.width,
            'height': self.height,
            'chrome_west': self.chrome_west,
            'chrome_east': self.chrome_east,
            'chrome_north': self.chrome_north,
            'chrome_south': self.chrome_south,
            'minimized': self.minimized,
            'keyboard_focus': self.keyboard_focus,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['VirtualWindow']:  # pylint: disable=R0912,R0911
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
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='window_id',
                    type='str',
                    name='VirtualWindow',
                )
            f_window_id = val
        val = data.get('desktop_id')
        f_desktop_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='desktop_id',
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='desktop_id',
                    type='str',
                    name='VirtualWindow',
                )
            f_desktop_id = val
        val = data.get('pos_x')
        f_pos_x: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='pos_x',
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='pos_x',
                    type='int',
                    name='VirtualWindow',
                )
            f_pos_x = int(val)
        val = data.get('pos_y')
        f_pos_y: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='pos_y',
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='pos_y',
                    type='int',
                    name='VirtualWindow',
                )
            f_pos_y = int(val)
        val = data.get('width')
        f_width: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='width',
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='width',
                    type='int',
                    name='VirtualWindow',
                )
            f_width = int(val)
        val = data.get('height')
        f_height: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='height',
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='height',
                    type='int',
                    name='VirtualWindow',
                )
            f_height = int(val)
        val = data.get('chrome_west')
        f_chrome_west: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_west',
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_west',
                    type='int',
                    name='VirtualWindow',
                )
            f_chrome_west = int(val)
        val = data.get('chrome_east')
        f_chrome_east: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_east',
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_east',
                    type='int',
                    name='VirtualWindow',
                )
            f_chrome_east = int(val)
        val = data.get('chrome_north')
        f_chrome_north: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_north',
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_north',
                    type='int',
                    name='VirtualWindow',
                )
            f_chrome_north = int(val)
        val = data.get('chrome_south')
        f_chrome_south: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_south',
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_south',
                    type='int',
                    name='VirtualWindow',
                )
            f_chrome_south = int(val)
        val = data.get('minimized')
        f_minimized: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='minimized',
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='minimized',
                    type='bool',
                    name='VirtualWindow',
                )
            f_minimized = val
        val = data.get('keyboard_focus')
        f_keyboard_focus: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='keyboard_focus',
                name='VirtualWindow',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='keyboard_focus',
                    type='int',
                    name='VirtualWindow',
                )
            f_keyboard_focus = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(VirtualWindow(
            window_id=not_none(f_window_id),
            desktop_id=not_none(f_desktop_id),
            pos_x=not_none(f_pos_x),
            pos_y=not_none(f_pos_y),
            width=not_none(f_width),
            height=not_none(f_height),
            chrome_west=not_none(f_chrome_west),
            chrome_east=not_none(f_chrome_east),
            chrome_north=not_none(f_chrome_north),
            chrome_south=not_none(f_chrome_south),
            minimized=not_none(f_minimized),
            keyboard_focus=not_none(f_keyboard_focus),
        ))

    def __repr__(self) -> str:
        return "VirtualWindow(" + repr(self.export_data()) + ")"


class WindowUpdatedEvent:
    """
    The state for one or more existing windows has changed.
    """
    __slots__ = ('settings',)
    FULL_EVENT_NAME = 'petronia.core.api.ui.positioner:window-updated'
    SHORT_EVENT_NAME = 'window-updated'

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:positioner'
    UNIQUE_TARGET_REL = 'positioner'

    def __init__(
        self,
        settings: List[VirtualWindow],
    ) -> None:
        self.settings = settings

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return WindowUpdatedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'settings': [v.export_data() for v in self.settings],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowUpdatedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('settings')
        f_settings: List[VirtualWindow]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='settings',
                name='WindowUpdatedEvent',
            )
        else:
            f_settings = []
            for item in val:
                parsed_settings = VirtualWindow.parse_data(item)
                if parsed_settings.has_error:
                    return parsed_settings.forward()
                f_settings.append(parsed_settings.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowUpdatedEvent(
            settings=not_none(f_settings),
        ))

    def __repr__(self) -> str:
        return "WindowUpdatedEvent(" + repr(self.export_data()) + ")"


class WindowCreatedEvent:
    """
    A new window was created.
    """
    __slots__ = ('window',)
    FULL_EVENT_NAME = 'petronia.core.api.ui.positioner:window-created'
    SHORT_EVENT_NAME = 'window-created'

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:positioner'
    UNIQUE_TARGET_REL = 'positioner'

    def __init__(
        self,
        window: VirtualWindow,
    ) -> None:
        self.window = window

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return WindowCreatedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'window': self.window.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowCreatedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('window')
        f_window: VirtualWindow
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='window',
                name='WindowCreatedEvent',
            )
        else:
            parsed_window = VirtualWindow.parse_data(val)
            if parsed_window.has_error:
                return parsed_window.forward()
            if parsed_window.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='window',
                )
            f_window = parsed_window.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowCreatedEvent(
            window=not_none(f_window),
        ))

    def __repr__(self) -> str:
        return "WindowCreatedEvent(" + repr(self.export_data()) + ")"


class WindowDestroyedEvent:
    """
    An existing window was removed from the system.
    """
    __slots__ = ('window_id', 'desktop_id',)
    FULL_EVENT_NAME = 'petronia.core.api.ui.positioner:window-destroyed'
    SHORT_EVENT_NAME = 'window-destroyed'

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:positioner'
    UNIQUE_TARGET_REL = 'positioner'

    def __init__(
        self,
        window_id: str,
        desktop_id: str,
    ) -> None:
        self.window_id = window_id
        self.desktop_id = desktop_id

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return WindowDestroyedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'window_id': self.window_id,
            'desktop_id': self.desktop_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowDestroyedEvent']:  # pylint: disable=R0912,R0911
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
                name='WindowDestroyedEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='window_id',
                    type='str',
                    name='WindowDestroyedEvent',
                )
            f_window_id = val
        val = data.get('desktop_id')
        f_desktop_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='desktop_id',
                name='WindowDestroyedEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='desktop_id',
                    type='str',
                    name='WindowDestroyedEvent',
                )
            f_desktop_id = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowDestroyedEvent(
            window_id=not_none(f_window_id),
            desktop_id=not_none(f_desktop_id),
        ))

    def __repr__(self) -> str:
        return "WindowDestroyedEvent(" + repr(self.export_data()) + ")"


class FocusWindowRequestEvent:
    """
    Request for a window to gain keyboard focus. If this succeeds, a window update
    is posted, along with a state change.
    """
    __slots__ = ('desktop_id', 'keyboard_focus',)
    FULL_EVENT_NAME = 'petronia.core.api.ui.positioner:focus-window:request'
    SHORT_EVENT_NAME = 'focus-window:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:positioner'
    UNIQUE_TARGET_REL = 'positioner'

    def __init__(
        self,
        desktop_id: str,
        keyboard_focus: int,
    ) -> None:
        self.desktop_id = desktop_id
        self.keyboard_focus = keyboard_focus

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return FocusWindowRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'desktop_id': self.desktop_id,
            'keyboard_focus': self.keyboard_focus,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['FocusWindowRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('desktop_id')
        f_desktop_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='desktop_id',
                name='FocusWindowRequestEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='desktop_id',
                    type='str',
                    name='FocusWindowRequestEvent',
                )
            f_desktop_id = val
        val = data.get('keyboard_focus')
        f_keyboard_focus: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='keyboard_focus',
                name='FocusWindowRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='keyboard_focus',
                    type='int',
                    name='FocusWindowRequestEvent',
                )
            f_keyboard_focus = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(FocusWindowRequestEvent(
            desktop_id=not_none(f_desktop_id),
            keyboard_focus=not_none(f_keyboard_focus),
        ))

    def __repr__(self) -> str:
        return "FocusWindowRequestEvent(" + repr(self.export_data()) + ")"


class MoveWindowRequestEvent:
    """
    Request to move a window. This may cause other windows to adjust accordingly. If
    this succeeds, a window update is posted, along with a state change. This is
    used for both moving and resizing a window.
    """
    __slots__ = ('desktop_id', 'pos_x', 'pos_y', 'width', 'height',)
    FULL_EVENT_NAME = 'petronia.core.api.ui.positioner:move-window:request'
    SHORT_EVENT_NAME = 'move-window:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:positioner'
    UNIQUE_TARGET_REL = 'positioner'

    def __init__(
        self,
        desktop_id: str,
        pos_x: int,
        pos_y: int,
        width: int,
        height: int,
    ) -> None:
        self.desktop_id = desktop_id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return MoveWindowRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'desktop_id': self.desktop_id,
            'pos_x': self.pos_x,
            'pos_y': self.pos_y,
            'width': self.width,
            'height': self.height,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['MoveWindowRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('desktop_id')
        f_desktop_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='desktop_id',
                name='MoveWindowRequestEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='desktop_id',
                    type='str',
                    name='MoveWindowRequestEvent',
                )
            f_desktop_id = val
        val = data.get('pos_x')
        f_pos_x: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='pos_x',
                name='MoveWindowRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='pos_x',
                    type='int',
                    name='MoveWindowRequestEvent',
                )
            f_pos_x = int(val)
        val = data.get('pos_y')
        f_pos_y: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='pos_y',
                name='MoveWindowRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='pos_y',
                    type='int',
                    name='MoveWindowRequestEvent',
                )
            f_pos_y = int(val)
        val = data.get('width')
        f_width: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='width',
                name='MoveWindowRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='width',
                    type='int',
                    name='MoveWindowRequestEvent',
                )
            f_width = int(val)
        val = data.get('height')
        f_height: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='height',
                name='MoveWindowRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='height',
                    type='int',
                    name='MoveWindowRequestEvent',
                )
            f_height = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(MoveWindowRequestEvent(
            desktop_id=not_none(f_desktop_id),
            pos_x=not_none(f_pos_x),
            pos_y=not_none(f_pos_y),
            width=not_none(f_width),
            height=not_none(f_height),
        ))

    def __repr__(self) -> str:
        return "MoveWindowRequestEvent(" + repr(self.export_data()) + ")"


class CloseWindowRequestEvent:
    """
    Request to close a window. This may cause other windows to adjust accordingly.
    If this succeeds, a "window-destroyed" event is posted; if windows are then
    adjusted, a window-updated event is posted.
    """
    __slots__ = ('desktop_id',)
    FULL_EVENT_NAME = 'petronia.core.api.ui.positioner:close-window:request'
    SHORT_EVENT_NAME = 'close-window:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:positioner'
    UNIQUE_TARGET_REL = 'positioner'

    def __init__(
        self,
        desktop_id: str,
    ) -> None:
        self.desktop_id = desktop_id

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return CloseWindowRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'desktop_id': self.desktop_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['CloseWindowRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('desktop_id')
        f_desktop_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='desktop_id',
                name='CloseWindowRequestEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='desktop_id',
                    type='str',
                    name='CloseWindowRequestEvent',
                )
            f_desktop_id = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(CloseWindowRequestEvent(
            desktop_id=not_none(f_desktop_id),
        ))

    def __repr__(self) -> str:
        return "CloseWindowRequestEvent(" + repr(self.export_data()) + ")"


class SetWindowChromeRequestEvent:
    """
    Request to set one or more windows' chrome space. All affected windows will be
    sent in a window update event.
    """
    __slots__ = ('desktop_ids', 'chrome_west', 'chrome_east', 'chrome_north', 'chrome_south',)
    FULL_EVENT_NAME = 'petronia.core.api.ui.positioner:set-window-chrome:request'
    SHORT_EVENT_NAME = 'set-window-chrome:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:positioner'
    UNIQUE_TARGET_REL = 'positioner'

    def __init__(
        self,
        desktop_ids: List[str],
        chrome_west: int,
        chrome_east: int,
        chrome_north: int,
        chrome_south: int,
    ) -> None:
        self.desktop_ids = desktop_ids
        self.chrome_west = chrome_west
        self.chrome_east = chrome_east
        self.chrome_north = chrome_north
        self.chrome_south = chrome_south

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetWindowChromeRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'desktop_ids': list(self.desktop_ids),
            'chrome_west': self.chrome_west,
            'chrome_east': self.chrome_east,
            'chrome_north': self.chrome_north,
            'chrome_south': self.chrome_south,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SetWindowChromeRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('desktop_ids')
        f_desktop_ids: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='desktop_ids',
                name='SetWindowChromeRequestEvent',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='desktop_ids',
                    type='List[str]',
                    name='SetWindowChromeRequestEvent',
                )
            f_desktop_ids = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='desktop_ids',
                        type='str',
                        name='SetWindowChromeRequestEvent',
                    )
                f_desktop_ids.append(item)
        val = data.get('chrome_west')
        f_chrome_west: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_west',
                name='SetWindowChromeRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_west',
                    type='int',
                    name='SetWindowChromeRequestEvent',
                )
            f_chrome_west = int(val)
        val = data.get('chrome_east')
        f_chrome_east: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_east',
                name='SetWindowChromeRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_east',
                    type='int',
                    name='SetWindowChromeRequestEvent',
                )
            f_chrome_east = int(val)
        val = data.get('chrome_north')
        f_chrome_north: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_north',
                name='SetWindowChromeRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_north',
                    type='int',
                    name='SetWindowChromeRequestEvent',
                )
            f_chrome_north = int(val)
        val = data.get('chrome_south')
        f_chrome_south: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_south',
                name='SetWindowChromeRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_south',
                    type='int',
                    name='SetWindowChromeRequestEvent',
                )
            f_chrome_south = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SetWindowChromeRequestEvent(
            desktop_ids=not_none(f_desktop_ids),
            chrome_west=not_none(f_chrome_west),
            chrome_east=not_none(f_chrome_east),
            chrome_north=not_none(f_chrome_north),
            chrome_south=not_none(f_chrome_south),
        ))

    def __repr__(self) -> str:
        return "SetWindowChromeRequestEvent(" + repr(self.export_data()) + ")"


class SetGlobalChromeRequestEvent:
    """
    Request to set the global chrome values. Optionally, it can affect all existing
    windows, too. The global state will be updated on success, and any affected
    windows will be included in a window update event.
    """
    __slots__ = ('affect_all', 'chrome_west', 'chrome_east', 'chrome_north', 'chrome_south',)
    FULL_EVENT_NAME = 'petronia.core.api.ui.positioner:set-global-chrome:request'
    SHORT_EVENT_NAME = 'set-global-chrome:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:positioner'
    UNIQUE_TARGET_REL = 'positioner'

    def __init__(
        self,
        affect_all: Optional[bool],
        chrome_west: int,
        chrome_east: int,
        chrome_north: int,
        chrome_south: int,
    ) -> None:
        self.affect_all = affect_all
        self.chrome_west = chrome_west
        self.chrome_east = chrome_east
        self.chrome_north = chrome_north
        self.chrome_south = chrome_south

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetGlobalChromeRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'affect_all': self.affect_all,
            'chrome_west': self.chrome_west,
            'chrome_east': self.chrome_east,
            'chrome_north': self.chrome_north,
            'chrome_south': self.chrome_south,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SetGlobalChromeRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('affect_all')
        f_affect_all: Optional[bool] = None
        if val is not None:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='affect_all',
                    type='bool',
                    name='SetGlobalChromeRequestEvent',
                )
            f_affect_all = val
        val = data.get('chrome_west')
        f_chrome_west: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_west',
                name='SetGlobalChromeRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_west',
                    type='int',
                    name='SetGlobalChromeRequestEvent',
                )
            f_chrome_west = int(val)
        val = data.get('chrome_east')
        f_chrome_east: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_east',
                name='SetGlobalChromeRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_east',
                    type='int',
                    name='SetGlobalChromeRequestEvent',
                )
            f_chrome_east = int(val)
        val = data.get('chrome_north')
        f_chrome_north: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_north',
                name='SetGlobalChromeRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_north',
                    type='int',
                    name='SetGlobalChromeRequestEvent',
                )
            f_chrome_north = int(val)
        val = data.get('chrome_south')
        f_chrome_south: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_south',
                name='SetGlobalChromeRequestEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_south',
                    type='int',
                    name='SetGlobalChromeRequestEvent',
                )
            f_chrome_south = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SetGlobalChromeRequestEvent(
            affect_all=f_affect_all,
            chrome_west=not_none(f_chrome_west),
            chrome_east=not_none(f_chrome_east),
            chrome_north=not_none(f_chrome_north),
            chrome_south=not_none(f_chrome_south),
        ))

    def __repr__(self) -> str:
        return "SetGlobalChromeRequestEvent(" + repr(self.export_data()) + ")"


class SetWindowSizeStateRequestEvent:
    """
    Requests that one or more windows have a simple, relative set for them.
    """
    __slots__ = ('desktop_ids', 'relative_size',)
    FULL_EVENT_NAME = 'petronia.core.api.ui.positioner:set-window-size-state:request'
    SHORT_EVENT_NAME = 'set-window-size-state:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:positioner'
    UNIQUE_TARGET_REL = 'positioner'

    def __init__(
        self,
        desktop_ids: List[str],
        relative_size: str,
    ) -> None:
        self.desktop_ids = desktop_ids
        self.relative_size = relative_size

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetWindowSizeStateRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'desktop_ids': list(self.desktop_ids),
            'relative_size': self.relative_size,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SetWindowSizeStateRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('desktop_ids')
        f_desktop_ids: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='desktop_ids',
                name='SetWindowSizeStateRequestEvent',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='desktop_ids',
                    type='List[str]',
                    name='SetWindowSizeStateRequestEvent',
                )
            f_desktop_ids = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='desktop_ids',
                        type='str',
                        name='SetWindowSizeStateRequestEvent',
                    )
                f_desktop_ids.append(item)
        val = data.get('relative_size')
        f_relative_size: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='relative_size',
                name='SetWindowSizeStateRequestEvent',
            )
        else:
            if val not in ('minimize','maximize','restore', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='relative_size',
                    type='str',
                    name='SetWindowSizeStateRequestEvent',
                )
            f_relative_size = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SetWindowSizeStateRequestEvent(
            desktop_ids=not_none(f_desktop_ids),
            relative_size=not_none(f_relative_size),
        ))

    def __repr__(self) -> str:
        return "SetWindowSizeStateRequestEvent(" + repr(self.export_data()) + ")"


class FocusState:
    """
    The currently focused window.
    """
    __slots__ = ('window_id',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:focus'
    UNIQUE_TARGET_REL = 'petronia.core.api.ui.positioner:focus'

    def __init__(
        self,
        window_id: Optional[str],
    ) -> None:
        self.window_id = window_id

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'window_id': self.window_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['FocusState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('window_id')
        f_window_id: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='window_id',
                    type='str',
                    name='FocusState',
                )
            f_window_id = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(FocusState(
            window_id=f_window_id,
        ))

    def __repr__(self) -> str:
        return "FocusState(" + repr(self.export_data()) + ")"


class DefaultChromeState:
    """
    The default chrome size to place around windows. Requests for individual windows
    can be done separately.
    """
    __slots__ = ('chrome_west', 'chrome_east', 'chrome_north', 'chrome_south',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:default-chrome'
    UNIQUE_TARGET_REL = 'petronia.core.api.ui.positioner:default-chrome'

    def __init__(
        self,
        chrome_west: int,
        chrome_east: int,
        chrome_north: int,
        chrome_south: int,
    ) -> None:
        self.chrome_west = chrome_west
        self.chrome_east = chrome_east
        self.chrome_north = chrome_north
        self.chrome_south = chrome_south

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'chrome_west': self.chrome_west,
            'chrome_east': self.chrome_east,
            'chrome_north': self.chrome_north,
            'chrome_south': self.chrome_south,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['DefaultChromeState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('chrome_west')
        f_chrome_west: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_west',
                name='DefaultChromeState',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_west',
                    type='int',
                    name='DefaultChromeState',
                )
            f_chrome_west = int(val)
        val = data.get('chrome_east')
        f_chrome_east: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_east',
                name='DefaultChromeState',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_east',
                    type='int',
                    name='DefaultChromeState',
                )
            f_chrome_east = int(val)
        val = data.get('chrome_north')
        f_chrome_north: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_north',
                name='DefaultChromeState',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_north',
                    type='int',
                    name='DefaultChromeState',
                )
            f_chrome_north = int(val)
        val = data.get('chrome_south')
        f_chrome_south: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_south',
                name='DefaultChromeState',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_south',
                    type='int',
                    name='DefaultChromeState',
                )
            f_chrome_south = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(DefaultChromeState(
            chrome_west=not_none(f_chrome_west),
            chrome_east=not_none(f_chrome_east),
            chrome_north=not_none(f_chrome_north),
            chrome_south=not_none(f_chrome_south),
        ))

    def __repr__(self) -> str:
        return "DefaultChromeState(" + repr(self.export_data()) + ")"


class Windows:
    """
    A window position in the virtual desktop.
    """
    __slots__ = ('window_id', 'desktop_id', 'pos_x', 'pos_y', 'width', 'height', 'chrome_west', 'chrome_east', 'chrome_north', 'chrome_south', 'minimized', 'keyboard_focus',)

    def __init__(
        self,
        window_id: str,
        desktop_id: str,
        pos_x: int,
        pos_y: int,
        width: int,
        height: int,
        chrome_west: int,
        chrome_east: int,
        chrome_north: int,
        chrome_south: int,
        minimized: bool,
        keyboard_focus: int,
    ) -> None:
        self.window_id = window_id
        self.desktop_id = desktop_id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.chrome_west = chrome_west
        self.chrome_east = chrome_east
        self.chrome_north = chrome_north
        self.chrome_south = chrome_south
        self.minimized = minimized
        self.keyboard_focus = keyboard_focus

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'window_id': self.window_id,
            'desktop_id': self.desktop_id,
            'pos_x': self.pos_x,
            'pos_y': self.pos_y,
            'width': self.width,
            'height': self.height,
            'chrome_west': self.chrome_west,
            'chrome_east': self.chrome_east,
            'chrome_north': self.chrome_north,
            'chrome_south': self.chrome_south,
            'minimized': self.minimized,
            'keyboard_focus': self.keyboard_focus,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Windows']:  # pylint: disable=R0912,R0911
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
                name='Windows',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='window_id',
                    type='str',
                    name='Windows',
                )
            f_window_id = val
        val = data.get('desktop_id')
        f_desktop_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='desktop_id',
                name='Windows',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='desktop_id',
                    type='str',
                    name='Windows',
                )
            f_desktop_id = val
        val = data.get('pos_x')
        f_pos_x: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='pos_x',
                name='Windows',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='pos_x',
                    type='int',
                    name='Windows',
                )
            f_pos_x = int(val)
        val = data.get('pos_y')
        f_pos_y: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='pos_y',
                name='Windows',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='pos_y',
                    type='int',
                    name='Windows',
                )
            f_pos_y = int(val)
        val = data.get('width')
        f_width: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='width',
                name='Windows',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='width',
                    type='int',
                    name='Windows',
                )
            f_width = int(val)
        val = data.get('height')
        f_height: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='height',
                name='Windows',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='height',
                    type='int',
                    name='Windows',
                )
            f_height = int(val)
        val = data.get('chrome_west')
        f_chrome_west: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_west',
                name='Windows',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_west',
                    type='int',
                    name='Windows',
                )
            f_chrome_west = int(val)
        val = data.get('chrome_east')
        f_chrome_east: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_east',
                name='Windows',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_east',
                    type='int',
                    name='Windows',
                )
            f_chrome_east = int(val)
        val = data.get('chrome_north')
        f_chrome_north: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_north',
                name='Windows',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_north',
                    type='int',
                    name='Windows',
                )
            f_chrome_north = int(val)
        val = data.get('chrome_south')
        f_chrome_south: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='chrome_south',
                name='Windows',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='chrome_south',
                    type='int',
                    name='Windows',
                )
            f_chrome_south = int(val)
        val = data.get('minimized')
        f_minimized: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='minimized',
                name='Windows',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='minimized',
                    type='bool',
                    name='Windows',
                )
            f_minimized = val
        val = data.get('keyboard_focus')
        f_keyboard_focus: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='keyboard_focus',
                name='Windows',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='keyboard_focus',
                    type='int',
                    name='Windows',
                )
            f_keyboard_focus = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Windows(
            window_id=not_none(f_window_id),
            desktop_id=not_none(f_desktop_id),
            pos_x=not_none(f_pos_x),
            pos_y=not_none(f_pos_y),
            width=not_none(f_width),
            height=not_none(f_height),
            chrome_west=not_none(f_chrome_west),
            chrome_east=not_none(f_chrome_east),
            chrome_north=not_none(f_chrome_north),
            chrome_south=not_none(f_chrome_south),
            minimized=not_none(f_minimized),
            keyboard_focus=not_none(f_keyboard_focus),
        ))

    def __repr__(self) -> str:
        return "Windows(" + repr(self.export_data()) + ")"


class VirtualDesktopWindowsState:
    """
    List of window IDs and their position in the virtual desktops.
    """
    __slots__ = ('windows',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.ui.positioner:virtual_desktop_windows'
    UNIQUE_TARGET_REL = 'petronia.core.api.ui.positioner:virtual_desktop_windows'

    def __init__(
        self,
        windows: List[Windows],
    ) -> None:
        self.windows = windows

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'windows': [v.export_data() for v in self.windows],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['VirtualDesktopWindowsState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('windows')
        f_windows: List[Windows]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='windows',
                name='VirtualDesktopWindowsState',
            )
        else:
            f_windows = []
            for item in val:
                parsed_windows = Windows.parse_data(item)
                if parsed_windows.has_error:
                    return parsed_windows.forward()
                f_windows.append(parsed_windows.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(VirtualDesktopWindowsState(
            windows=not_none(f_windows),
        ))

    def __repr__(self) -> str:
        return "VirtualDesktopWindowsState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
