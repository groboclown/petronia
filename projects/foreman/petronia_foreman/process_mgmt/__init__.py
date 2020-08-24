
"""
Manages the launching of processes via requests from the extension loader process.

The processes:
    1. Start with the requested permissions.
    2. Stdin is used as the event data writer (from this end), and extra FD 3 is added as a
        pipe for reading event data (from this end).
"""

from .process import ManagedProcess
from .launch import run_launcher
