
"""
The log handler.
"""

import sys
import time
import traceback
from threading import Lock
from typing import Dict, Set, Tuple, Optional

from .config import (
    FileLoggerConfig,
    parse_config,
    DEFAULT_FORMAT,
    DEFAULT_CONTINUATION_FORMAT,
)
from .ident import (
    TARGET_ID_FILE_LOGGER_CONFIG,
    TARGET_ID_FILE_LOGGER_STATE,
)
from ..configuration import (
    LogState,
    set_log_state,
)
from ....aid.std import (
    EventBus,
    ListenerSet,
    StateWatch,
    LogHandlerId,
    LogLevel,
    add_log_handler,
    remove_log_handler,
    report_error,
    DEPRECATED,
    EMPTY_MAPPING,
)
from ....core.config_persistence.api import PersistentConfigurationState


class LogHandler:
    """
    Handles the transition of a configuration request on the
    log handler.
    """
    __slots__ = ('_listeners', '_bus', '_raw_config', '_config', '_lock',)
    _bus: Optional[EventBus]
    _listeners: Dict[str, Tuple[LogLevel, LogHandlerId]]

    def __init__(self, bus: EventBus, listeners: ListenerSet) -> None:
        self._lock = Lock()
        self._listeners = {}
        self._bus = bus
        self._config = FileLoggerConfig('-', DEFAULT_FORMAT, DEFAULT_CONTINUATION_FORMAT, EMPTY_MAPPING)  # type: ignore
        self._raw_config = StateWatch(listeners, TARGET_ID_FILE_LOGGER_CONFIG, PersistentConfigurationState({}))
        self._raw_config.set_listener(self._on_config_change)
        self._on_config_change(self._raw_config.state)

    def dispose(self) -> None:
        """Dispose of this component.  Completely idempotent."""
        with self._lock:
            for llh in self._listeners.values():
                remove_log_handler(llh[1])
            self._listeners.clear()
            self._bus = None

    def _on_config_change(
            self,
            state: PersistentConfigurationState
    ) -> None:
        new_config, errors = parse_config(state.persistent)
        assert isinstance(new_config, FileLoggerConfig)
        for error in errors:
            report_error(self._bus, error)

        with self._lock:
            # De-register everything that's no longer around or different,
            # and register things that are new or different.
            different = False
            leftover_active_cats = set(self._listeners.keys())
            new_category_levels = new_config.get_category_levels()
            for cat, level in new_category_levels.items():
                if cat in self._listeners:
                    curr_level, listener = self._listeners[cat]
                    if curr_level != level:
                        # Listener changed.
                        remove_log_handler(listener)
                        lid = add_log_handler(level, cat, self._log_message)
                        self._listeners[cat] = (level, lid,)
                        different = True
                        # fall-through to remove the active list item.
                    # else it's the same, so remove from the active list.
                    leftover_active_cats.remove(cat)
                else:
                    # New listener
                    lid = add_log_handler(level, cat, self._log_message)
                    self._listeners[cat] = (level, lid,)
                    different = True
            if leftover_active_cats:
                # There are categories that need to be removed.
                for cat in leftover_active_cats:
                    listener = self._listeners[cat][1]
                    remove_log_handler(listener)
                    del self._listeners[cat]
                different = True

            if different and self._bus:
                self._config = new_config
                new_state = LogState(new_category_levels)
                set_log_state(self._bus, TARGET_ID_FILE_LOGGER_STATE, new_state)

    def _log_message(self, level: LogLevel, src: str, msg: str, err: Optional[BaseException]) -> None:
        """
        File logger.  Includes special deprecated message reporting.
        """
        # Note - this uses "localtime", because that's what matters to a desktop application.
        now = time.localtime()
        if level == DEPRECATED:
            # Deprecated messages are an interesting thing.  We want to report them
            # just once.  Note that we include the source in determining whether to
            # display the deprecated message.
            src_msg = src + msg
            if src_msg not in _SEEN_DEPRECATED:
                _SEEN_DEPRECATED.add(src_msg)
                self._print("DEPRECTATION WARNING: {0} (reported from {1})".format(
                    msg, src
                ))
        else:
            self._print(self._config.format_message(now, level, msg))
        if err:
            self._print(self._config.format_message(
                now, level,
                '\n'.join(traceback.format_exception(err.__class__, err, err.__traceback__))
            ))

    def _print(self, msg: str) -> None:
        with self._lock:
            if self._config.filename == '-':
                sys.stdout.write(msg + '\n')
                sys.stdout.flush()
            else:
                with open(self._config.filename, 'w') as f:
                    f.write(msg + '\n')


_SEEN_DEPRECATED: Set[str] = set()
