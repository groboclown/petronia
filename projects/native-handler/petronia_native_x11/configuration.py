"""Handles configuration."""

from typing import List, Callable, Optional
from petronia_common.util import StdRet
from petronia_ext_lib import datastore
from petronia_ext_lib import runner
from .datastore.petronia_native_x11 import ConfigurationState


class ConfigurationStore:
    """Stores the X11 configuration."""
    __slots__ = ('_cache', '_callbacks')

    def __init__(
            self,
            config: Optional[ConfigurationState],
    ) -> None:
        self._cache = config
        self._callbacks: List[Callable[[Optional[ConfigurationState]], None]] = []

    def get_config(self) -> Optional[ConfigurationState]:
        """Get the configuration.  This should be considered mutable, but any update
        should follow up by calling into on_config_update()."""
        return self._cache

    def add_callback(self, callback: Callable[[Optional[ConfigurationState]], None]) -> None:
        """Add a callback which is invoked when the configuration changes."""
        self._callbacks.append(callback)

    def on_config_update(self, context: runner.EventRegistryContext) -> StdRet[None]:
        """Called when the configuration is updated."""
        for callback in self._callbacks:
            callback(self._cache)
        return self.put_in_datastore(context)

    def put_in_datastore(self, context: runner.EventRegistryContext) -> StdRet[None]:
        """Put the internal configuration state into the datastore."""
        if self._cache is None:
            return datastore.send_delete_data(context, ConfigurationState.UNIQUE_TARGET_FQN)
        return datastore.send_store_data(
            context, ConfigurationState.UNIQUE_TARGET_FQN, self._cache,
        )
