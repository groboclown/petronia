
"""
Definition for components that use a configuration part.
"""

from ....base.util.simple_type import (
    PersistType,
    readonly_persistent_copy,
)


class PersistentConfigurationState:
    """
    A "state" value that contains values that were read from a configuration,
    and that can potentially be written back to configuration.
    """
    __slots__ = ('__persistent',)

    def __init__(self, persistent: PersistType) -> None:
        self.__persistent = readonly_persistent_copy(persistent)

    @property
    def persistent(self) -> PersistType:
        """
        Because of the nature of events, the returned value shouldn't be edited, as that
        will have unexpected consequences.
        """
        return self.__persistent
