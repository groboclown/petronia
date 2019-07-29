
"""
Posix platform main process.
"""

from petronia3.system.bus import EventBus

def run_petronia(bus: EventBus) -> int:
    print("Petronia for Posix environments started.")
    return 0
