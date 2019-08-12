
"""
Definition for components that use a configuration part.
"""

from typing import Dict, Iterable, Union
from ....base.util import T

# Supported persistent types...
_PrimitivePersistType = Union[str, float, bool, None]
_GenericPersistType = Union[
    _PrimitivePersistType,
    Dict[str, T],
    Iterable[T]
]
# FIXME Any way to make this a tree with cycles?
PersistType = Dict[str, _GenericPersistType[
    _GenericPersistType[
        _GenericPersistType[
            _GenericPersistType[
                _GenericPersistType[
                    _GenericPersistType[
                        _GenericPersistType[
                            _GenericPersistType[
                                _PrimitivePersistType
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]
]]


class PersistentConfigurationState:
    """
    A "state" value that contains values that were read from a configuration,
    and that can potentially be written back to configuration.
    """
    __slots__ = ('__persistent',)
    def __init__(self, persistent: PersistType) -> None:
        self.__persistent = persistent

    @property
    def persistent(self) -> PersistType:
        """
        Because of the nature of events, the returned value shouldn't be edited, as that
        will have unexpected consequences.
        """
        return self.__persistent
