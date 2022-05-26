"""Xcb API usage and interface."""

from typing import List, Any
from .xcb import xcb_native as nat
from .xcb.xcb_atoms import AtomDef


class Freeable:
    """A pointer that might be able to be freed."""
    __slots__ = ('__val',)

    def __init__(self, val: Any) -> None:
        self.__val = val

    def free(self, lib: nat.LibXcb) -> None:
        if self.__val is not None:
            lib.free(self.__val)
            self.__val = None


class XcbApi:
    """Interface with standard XCB stuff."""
    __slots__ = (
        '__lib', '__conn', '__screen', '__visual',
        '__default_depth', '__default_colormap',
        '__cursor_context', '__timestamp', '__atoms',
        '__selection_atom', '__selection_owner_window',
    )

    def __init__(
            self, *,
            lib: nat.LibXcb,
            conn: nat.XcbConnectionP,
            screen: nat.XcbScreenP,
            visual: nat.XcbVisualtypeP,
            default_depth: int,
            default_colormap: int,
            cursor_context: nat.XcbCursorContextP,
            atoms: AtomDef,
            selection_atom: nat.XcbAtom,
            selection_owner_window: nat.XcbWindow,
            timestamp: nat.XcbTimestamp,
            pending_events: List[nat.XcbGenericEventP],
            to_free: List[Freeable],
    ) -> None:
        pass
