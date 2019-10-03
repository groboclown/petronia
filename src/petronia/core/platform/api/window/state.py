
"""
State definition for window objects.
"""

from typing import Sequence, Mapping, Dict, Iterable, List, Union
from .....aid.simp import (
    EventBus,
    set_state,
    create_singleton_identity,
    ComponentId,
    readonly_dict,
)
from ..defs import (
    ScreenRect,
)


STATE_ID_ACTIVE_WINDOWS = create_singleton_identity('petronia.core.platform.api/windows')


class NativeWindowState:
    """
    State for a specific window.
    """
    __slots__ = (
        '__cid',
        '__title',
        '__process_id',
        '__names',
        '__bordered_rect',
        '__client_rect',
        '__is_visible',
        '__is_focused',
        '__is_active',
        '__style',
    )

    def __init__(
            self,
            component_id: ComponentId,
            title: str,
            process_id: int,
            names: Dict[str, str],
            bordered_rect: ScreenRect,
            client_rect: ScreenRect,
            style: Mapping[str, Union[str, float, bool]],
            is_visible: bool,
            is_active: bool,
            is_focused: bool
    ) -> None:
        self.__cid = component_id
        self.__title = title
        self.__process_id = process_id
        self.__names = dict(names)
        self.__bordered_rect = bordered_rect
        self.__client_rect = client_rect
        self.__style = readonly_dict(style)
        self.__is_visible = is_visible
        self.__is_active = is_active
        self.__is_focused = is_focused

    @property
    def component_id(self) -> ComponentId:
        return self.__cid

    @property
    def title(self) -> str:
        return self.__title

    @property
    def process_id(self) -> int:
        return self.__process_id

    @property
    def names(self) -> Dict[str, str]:
        return dict(self.__names)

    @property
    def bordered_rect(self) -> ScreenRect:
        return self.__bordered_rect

    @property
    def client_rect(self) -> ScreenRect:
        return self.__client_rect

    @property
    def is_visible(self) -> bool:
        return self.__is_visible

    @property
    def is_active(self) -> bool:
        return self.__is_active

    @property
    def is_focused(self) -> bool:
        return self.__is_focused

    @property
    def style(self) -> Mapping[str, Union[str, float, bool]]:
        return self.__style

    def get_style_flags(self) -> Sequence[str]:
        """All style settings which have a boolean 'True' value."""
        ret: List[str] = []
        for key, val in self.__style.items():
            if isinstance(val, bool) and val is True:
                ret.append(key)
        return ret

    def copy(self) -> 'NativeWindowState':
        return NativeWindowState(
            component_id=self.__cid,
            title=self.__title,
            process_id=self.__process_id,
            names=dict(self.__names),
            bordered_rect=self.__bordered_rect.copy(),
            client_rect=self.__client_rect.copy(),
            style=self.__style,
            is_visible=self.__is_visible,
            is_active=self.__is_active,
            is_focused=self.__is_focused
        )

    def __repr__(self) -> str:
        return (
            'NativeWindowState(component_id={0}, title={1}, '
            'process_id={2}, names={3},'
            'bordered_rect={4}, client_rect={5}, style={9}, '
            'is_visible={6}, is_active={7}, is_focused={8})'
        ).format(
            repr(self.__cid), repr(self.__title),
            repr(self.__process_id), repr(self.__names),
            repr(self.__bordered_rect), repr(self.__client_rect),
            repr(self.__is_visible), repr(self.__is_active), repr(self.__is_focused),
            repr(self.__style)
        )


class AllActiveWindowsState:
    """
    All the windows in the system and a high-level view of their state.  This
    overlaps with individual window states.
    """
    __slots__ = ('__windows',)

    def __init__(self, windows: Iterable[NativeWindowState]) -> None:
        self.__windows = tuple(windows)

    @property
    def windows(self) -> Sequence[NativeWindowState]:
        return self.__windows

    def __repr__(self) -> str:
        return 'AllActiveWindowsState({0})'.format(repr(self.__windows))


def set_active_windows_state(bus: EventBus, windows: Iterable[NativeWindowState]) -> None:
    set_state(
        bus, STATE_ID_ACTIVE_WINDOWS,
        AllActiveWindowsState, AllActiveWindowsState(windows)
    )
