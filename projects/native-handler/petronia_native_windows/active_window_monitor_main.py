"""
Helper tool to probe an active Windows system and discover the Window metadata.
This is intended to be run stand-alone.
"""

from typing import Sequence, List, Callable, Union, Optional
import sys

from petronia_common.event_stream import RawBinaryReader
from petronia_common.util import StdRet, T, RET_OK_NONE
from petronia_ext_lib.events import datastore as datastore_events
from petronia_ext_lib.runner import (
    EventRegistryContext, EventBinaryTarget, EventObjectTarget,
    EventObjectParser,
)
from petronia_ext_lib.runner.registry import EventObject
from petronia_ext_lib.standard.embedded_json_data import embedded_json_data
from petronia_native.common.events.impl import window as window_events
from petronia_native_windows.configuration import ConfigurationStore
from . import setup
from . import message_loop
from . import window_handler
from . import screen


class SinkContext(EventRegistryContext):
    """Just reads in events, does not send anything."""

    __slots__ = ('eof_targets',)

    def __init__(self) -> None:
        self.eof_targets: List[Callable[[], None]] = []

    def stop(self) -> None:
        """Call the EOF targets."""
        for target in self.eof_targets:
            target()

    def send_event(self, source_id: str, target_id: str, event: EventObject) -> StdRet[None]:
        if isinstance(event, window_events.WindowCreatedEvent):
            show_window_data(event.state)
            return RET_OK_NONE
        elif isinstance(event, datastore_events.StoreDataRequestEvent):
            sevt: datastore_events.StoreDataRequestEvent = event
            json_data_res = embedded_json_data(sevt.json)
            if json_data_res.ok:
                json_data = json_data_res.result
                if isinstance(json_data, dict):
                    data_res = window_events.WindowState.parse_data(json_data)
                    # This could fail if it's not a window state data event, which is fine.
                    if data_res.ok:
                        show_window_data(data_res.result)
                        return RET_OK_NONE
        # print(f"Ignoring event from {source_id} -> {target_id}")
        return RET_OK_NONE

    def register_event(self, event_id: str, parser: EventObjectParser) -> StdRet[None]:
        return RET_OK_NONE

    def register_target(
            self, event_id: str, target_id: Optional[str], target: EventObjectTarget[T],
            source_id: Optional[str] = None, timeout: float = -1.0,
    ) -> StdRet[None]:
        return RET_OK_NONE

    def register_binary_target(
            self, event_id: str, target_id: Optional[str],
            target: EventBinaryTarget, source_id: Optional[str] = None,
            timeout: float = -1.0,
    ) -> StdRet[None]:
        return RET_OK_NONE

    def register_eof_target(self, callback: Callable[[], None]) -> StdRet[None]:
        self.eof_targets.append(callback)
        return RET_OK_NONE

    def send_binary_event(
            self, source_id: str, target_id: str, event_id: str,
            data: Union[bytes, bytearray],
    ) -> StdRet[None]:
        return RET_OK_NONE

    def send_binary_event_stream(
            self, source_id: str, target_id: str, event_id: str,
            data_size: int, data: RawBinaryReader,
    ) -> StdRet[None]:
        return RET_OK_NONE


def show_window_data(data: window_events.WindowState) -> None:
    """Print the window data."""
    text = (
        f"Window updated:\n  "
        f"position/size: {data.location.x}x{data.location.y} / "
        f"{data.location.width}x{data.location.height}\n  meta:\n"
    )
    meta_list = sorted([m for m in data.meta], key=lambda m: m.key)
    for meta in meta_list:
        text += f"  {meta.key}: [{meta.value}]\n"
    print(text)


def main(_args: Sequence[str]) -> int:
    """CLI entry method."""
    context = SinkContext()
    config = ConfigurationStore(None)
    screen_monitor = screen.WindowsScreen(context, config)
    win_handler = window_handler.WindowsNativeHandler(screen_monitor.mapper)
    win_handler.register_listeners(context, 'x')
    loop = message_loop.WindowsMessageLoop()
    win_handler.register_messages(loop)
    runner = setup.WindowsRunner(
        loop,
        [win_handler.initialize_system_state],
    )
    runner.start()
    print("Press <enter> or <ctrl-c> to stop")
    try:
        sys.stdin.readline()
        print("Stopping.")
    except KeyboardInterrupt:
        print("Forcing stop.")
    finally:
        context.stop()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
