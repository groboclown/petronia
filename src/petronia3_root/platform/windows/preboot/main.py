
import time
from petronia3.system.bus import EventBus
from petronia3.extensions.shutdown.api import send_system_shutdown_request

def run_petronia(bus: EventBus) -> int:
    print("Petronia for Windows has started.")
    print("Press `Control-C` to stop.")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        pass
    send_system_shutdown_request(bus)
    return 0
