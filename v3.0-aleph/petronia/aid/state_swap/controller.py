
"""
Controls state swaps.
"""

from typing import Dict, Callable, Optional
from threading import Lock


class StateSwapController:
    """
    Controls invoking state objects to swap their behavior.
    """
    __slots__ = ('_setups', '_disposers', '_active', '_lock')
    _setups: Dict[str, Callable[[], None]]
    _disposers: Dict[str, Callable[[], None]]
    _active: Optional[str]

    def __init__(self) -> None:
        self._lock = Lock()
        self._setups = {}
        self._disposers = {}
        self._active = None

    def add_state(
            self,
            name: str,
            setup: Callable[[], None],
            dispose: Callable[[], None]
    ) -> None:
        """
        Adds a new state with function to install the event listeners
        (`setup`), and one to remove the event listeners (`dispose`).
        The dispose function must be *idempotent* - calling it multiple times
        must not cause issues.
        """
        with self._lock:
            assert name not in self._setups and name not in self._disposers
            self._setups[name] = setup
            self._disposers[name] = dispose

    def dispose(self) -> None:
        """
        Removes all internal references to the states.  They must properly
        fully dispose themselves.
        """
        with self._lock:
            self._setups = {}
            self._disposers = {}
            self._active = None

    def switch_state(self, new_state: str) -> None:
        """
        Turn off the current state (if any) and set the current state to the
        argument.  If the new state was not added, then a ValueError is
        raised.
        """
        with self._lock:
            if new_state not in self._setups:
                # Should be a validation error.
                raise ValueError('unknown state ' + repr(new_state))

            # Is there a situation where the new state could miss an event?
            if self._active:
                self._disposers[self._active]()
            self._active = new_state
            self._setups[new_state]()
