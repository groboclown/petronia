"""Shared state for the portals."""

from typing import List, Sequence, Dict, Optional
from . import tree, state


def clear_data(config: Optional[state.petronia_portal.ConfigurationState] = None) -> None:
    """Initialize the shared state."""
    _ACTIVE_WINDOW_ID[0] = ''
    _FOCUSED_PORTAL_ID[0] = -1
    _ROOT_LAYOUT[0] = create_default_root()
    _CONFIG[0] = config or state.petronia_portal.ConfigurationState([], [])


def layout_root() -> tree.RootContainer:
    """Get the root of the active layout."""
    return _ROOT_LAYOUT[0]


def configuration() -> state.petronia_portal.ConfigurationState:
    """Get the active configuration."""
    return _CONFIG[0]


def get_active_window_id() -> str:
    """Get the active window ID"""
    return _ACTIVE_WINDOW_ID[0]


def set_active_window_id(window_id: str) -> None:
    """Set the active window ID"""
    _ACTIVE_WINDOW_ID[0] = window_id


def get_focused_portal_id() -> int:
    """Get the ID of the focused portal."""
    return _FOCUSED_PORTAL_ID[0]


def set_focused_portal_id(portal_id: int) -> None:
    """Set the focused portal id"""
    _FOCUSED_PORTAL_ID[0] = portal_id


_ACTIVE_WINDOW_ID = ['']
_FOCUSED_PORTAL_ID = [-1]
_ROOT_LAYOUT: List[tree.RootContainer] = [create_default_root()]
_CONFIG = [state.petronia_portal.ConfigurationState([], [])]
