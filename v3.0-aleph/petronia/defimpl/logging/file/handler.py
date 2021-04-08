
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
)
from .ident import (
    CONFIG_ID_FILE_LOGGER,
    STATE_ID_FILE_LOGGER,
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
)
from ....core.config_persistence.api import PersistentConfigurationState


class LogHandler:
    """
    Handles the transition of a configuration request on the
    log handler.
    """
    __slots__ = ('_listeners', '_bus', '_raw_config', '_config', '_lock', '_seen_deprecated', '_log_lock')
    _bus: Optional[EventBus]
    _listeners: Dict[str, Tuple[LogLevel, LogHandlerId]]
    _seen_deprecated: Set[str]

    def __init__(self, bus: EventBus, listeners: ListenerSet, config: StateWatch[PersistentConfigurationState]) -> None:
        self._lock = Lock()
        self._log_lock = Lock()
        self._listeners = {}
        self._bus = bus
        config.set_listener(self._on_config_change)
        listeners.add_dispose_callback(self.dispose)
        self._seen_deprecated = set()

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
        # print("DEBUG parsing config {0}".format(state.persistent))
        new_config, errors = parse_config(state.persistent)
        assert isinstance(new_config, FileLoggerConfig)
        for error in errors:
            report_error(self._bus, error)
        # print("DEBUG loaded configuration {0}".format(new_config))

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
                set_log_state(self._bus, STATE_ID_FILE_LOGGER, new_state)

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
            if src_msg not in self._seen_deprecated:
                self._seen_deprecated.add(src_msg)
                self._print("DEPRECTATION WARNING: {0} (reported from {1})".format(
                    msg, src
                ))
        else:
            self._print(self._config.format_message(now, level, src, msg))
        if err:
            self._print(self._config.format_message(
                now, level, src,
                '\n'.join(traceback.format_exception(err.__class__, err, err.__traceback__))
            ))

    def _print(self, msg: str) -> None:
        out_to = self._config.filename
        if out_to == '-':
            with self._log_lock:
                sys.stdout.write(msg + '\n')
                sys.stdout.flush()
        else:
            with self._log_lock:
                with open(self._config.filename, 'a') as f:
                    f.write(msg + '\n')


def startup_file_logger(bus: EventBus, listeners: ListenerSet) -> None:
    config = StateWatch(listeners, CONFIG_ID_FILE_LOGGER, PersistentConfigurationState({}))

    def on_state_change(_val: PersistentConfigurationState) -> None:
        if config.is_set:
            LogHandler(bus, listeners, config)

    config.set_listener(on_state_change)
