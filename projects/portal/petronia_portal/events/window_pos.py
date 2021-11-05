# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia.core.api.window_pos version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Dict,
    Optional,
    Any,
    SupportsInt,
    List,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    not_none,
    STANDARD_PETRONIA_CATALOG,
    StdRet,
)

EXTENSION_NAME = 'petronia.core.api.window_pos'
EXTENSION_VERSION = (1, 0, 0)


class FocusState:
    """
    The currently focused window.
    """
    __slots__ = ('window_id',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.window_pos:focus'
    UNIQUE_TARGET_REL = 'petronia.core.api.window_pos:focus'

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


class Windows:
    """
    A window position in the virtual desktop.
    """
    __slots__ = ('window_id', 'desktop_id', 'pos_x', 'pos_y', 'width', 'height', 'chrome_west', 'chrome_east', 'chrome_north', 'chrome_south', 'minimized',)

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
        ))

    def __repr__(self) -> str:
        return "Windows(" + repr(self.export_data()) + ")"


class VirtualDesktopWindowsState:
    """
    List of window IDs and their position in the virtual desktops.
    """
    __slots__ = ('windows',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.window_pos:virtual_desktop_windows'
    UNIQUE_TARGET_REL = 'petronia.core.api.window_pos:virtual_desktop_windows'

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
