
"""
General utilities for Petronia
"""

from .rwlock import RWLock
from .worker_thread import WorkerThread, stop_all_threads
from .op import (
    in_or,
    optional_key,
    optional_list_key,
)

from .memory import (
    EMPTY_DICT,
    EMPTY_LIST,
    EMPTY_TUPLE,
    STRING_EMPTY_TUPLE,

    T, V, K,

    ValueHolder,
    readonly_dict,
)
