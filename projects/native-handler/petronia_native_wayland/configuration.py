"""Handles configuration."""

from typing import List, Callable, Optional
from petronia_common.util import StdRet
from petronia_ext_lib import datastore
from petronia_ext_lib import runner
from .datastore.petronia_native_wayland import ConfigurationState, Connection, VirtualScreens


class ConfigurationStore:
    """Stores the X11 configuration."""
    __slots__ = ('_cache', '_callbacks')

    def __init__(
            self,
            config: Optional[ConfigurationState],
    ) -> None:
        # Setup default values.
        self._cache = ConfigurationStore._with_defaults(config)
        self._callbacks: List[Callable[[ConfigurationState], None]] = []

    def get_config(self) -> ConfigurationState:
        """Get the configuration.  This should be considered mutable, but any update
        should follow up by calling into on_config_update()."""
        return self._cache

    def add_callback(self, callback: Callable[[ConfigurationState], None]) -> None:
        """Add a callback which is invoked when the configuration changes."""
        self._callbacks.append(callback)

    def on_config_update(self, context: runner.EventRegistryContext) -> StdRet[None]:
        """Called when the configuration is updated."""
        for callback in self._callbacks:
            callback(self._cache)
        return self.put_in_datastore(context)

    def put_in_datastore(self, context: runner.EventRegistryContext) -> StdRet[None]:
        """Put the internal configuration state into the datastore."""
        # cache is never None here.
        # if self._cache is None:
        #     return datastore.send_delete_data(context, ConfigurationState.UNIQUE_TARGET_FQN)
        return datastore.send_store_data(
            context, ConfigurationState.UNIQUE_TARGET_FQN, self._cache,
        )

    @staticmethod
    def _with_defaults(config: Optional[ConfigurationState]) -> ConfigurationState:
        config = config or ConfigurationState(Connection(None), VirtualScreens([]))
        config.connection = config.connection or Connection(None)
        config.connection.replace_existing_wm = (
            False if config.connection.replace_existing_wm is None
            else config.connection.replace_existing_wm
        )
        return config
