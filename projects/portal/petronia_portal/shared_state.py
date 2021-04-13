"""Shared state for the portals."""

from typing import List, Optional
from . import tree, state


def clear_data(config: Optional[state.petronia_portal.ConfigurationState] = None) -> None:
    """Initialize the shared state."""
    _FOCUSED_WINDOW_ID[0] = ''
    _ACTIVE_PORTAL_ID[0] = -1
    _ROOT_LAYOUT[0] = tree.OptimizedTileTree()
    _CONFIG[0] = config or state.petronia_portal.ConfigurationState([], [])


def layout_root() -> tree.OptimizedTileTree:
    """Get the root of the active layout."""
    return _ROOT_LAYOUT[0]


def configuration() -> state.petronia_portal.ConfigurationState:
    """Get the active configuration."""
    return _CONFIG[0]


def get_focused_window_id() -> str:
    """Get the focused window ID"""
    return _FOCUSED_WINDOW_ID[0]


def set_focused_window_id(window_id: str) -> None:
    """Set the focused window ID"""
    _FOCUSED_WINDOW_ID[0] = window_id


def get_active_portal_id() -> int:
    """Get the ID of the active portal."""
    return _ACTIVE_PORTAL_ID[0]


def set_active_portal_id(portal_id: int) -> None:
    """Set the active portal id"""
    _ACTIVE_PORTAL_ID[0] = portal_id


_FOCUSED_WINDOW_ID = ['']
_ACTIVE_PORTAL_ID = [-1]
_ROOT_LAYOUT: List[tree.OptimizedTileTree] = [tree.OptimizedTileTree()]
_CONFIG = [state.petronia_portal.ConfigurationState([], [])]
