
"""
Definition for components that use a configuration part.
"""

from typing import Dict, Sequence, Union
from ....util.memory import T

# Supported persistent types...
_PrimitivePersistType = Union[str, float, bool, None]
_GenericPersistType = Union[
    _PrimitivePersistType,
    Dict[str, T],
    Sequence[T]
]

# Can't do a recursive type, apparently.
PersistType = _GenericPersistType[
    # Going too deep here has serious performance impact on MyPy.
    _GenericPersistType[
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
    ]
]


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
