
from ....base import EventBus
from ..general.wait_for_stop import petronia_wait_for_stop


def run_petronia(bus: EventBus) -> int:
    print("Petronia for Windows has started.")
    print("Press `Control-C` to stop.")

    def on_exit() -> None:
        print("Petronia shut down.")

    petronia_wait_for_stop(bus, on_exit)
    return 0
