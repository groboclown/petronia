
"""
General utilities for Petronia
"""

from .rwlock import RWLock
from .worker_thread import WorkerThread, stop_all_threads
from .op import (
    in_or,
    optional_key,
)