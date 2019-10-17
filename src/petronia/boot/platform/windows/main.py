
import time
from ....base import EventBus
from ....core.shutdown.api import send_system_shutdown_request


def run_petronia(bus: EventBus) -> int:
    print("Petronia for Windows has started.")
    print("Press `Control-C` to stop.")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        pass
    print("Starting system shutdown.  This may take a little while.")
    send_system_shutdown_request(bus)
    return 0
