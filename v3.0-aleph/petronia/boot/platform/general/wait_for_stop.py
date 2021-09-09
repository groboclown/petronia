
"""
Implementation to:
    1. Trigger a stop when ctrl-c is pressed.
    2. Trigger a stop when a SIGINT is received.
    3. Trigger sys.exit() when a SIGHUP is received.
    4. Keep the main thread running until a halt signal is received, at
        which point the main thread exits.
This requires a shutdown.api implementation extension to be loaded.
"""


from typing import Callable, Optional
from types import FrameType
import sys
import signal
import time
from ....base import (
    EventBus,
    ParticipantId,
    EventId,
)
from ....core.shutdown.api import (
    send_system_shutdown_request,
    as_system_shutdown_finalize_listener,
    SystemShutdownFinalizeEvent,
    TARGET_ID_SYSTEM_SHUTDOWN,
)


def petronia_wait_for_stop(
        bus: EventBus,
        on_exit: Optional[Callable[[], None]] = None
) -> None:
    stopper = PetroniaWaitForStop(bus, on_exit)
    stopper.wait()


class PetroniaWaitForStop:
    __slots__ = ('__running', '__bus', '__on_exit')

    def __init__(self, bus: EventBus, on_exit: Optional[Callable[[], None]] = None):
        self.__bus = bus
        self.__on_exit = on_exit
        self.__running = True
        # Note: intentionally not saving the listener ID.
        bus.add_listener(
            TARGET_ID_SYSTEM_SHUTDOWN,
            as_system_shutdown_finalize_listener,
            self._final_handler
        )
        signal.signal(signal.SIGINT, self._ctrl_c_handler)
        if hasattr(signal, 'SIGHUP'):
            signal.signal(signal.SIGHUP, self._halt)
        # self.__running_notice = threading.Condition()

    def wait(self) -> None:

        # Does not seem to work on windows.
        # The ctrl-c handler does not work on the wait.
        # There was a Python bug on this back in 2011, but that
        # is marked as closed.
        # with running_notice:
        #     try:
        #         while is_running:
        #             running_notice.wait(60)
        #         print("Completed system shutdown from standard Petronia shutdown.")
        #     except KeyboardInterrupt:
        #         print("Starting forced system shutdown.  This may take a little while.")
        #         send_system_shutdown_request(bus)

        try:
            while self.__running:
                if hasattr(signal, 'pause'):
                    signal.pause()
                else:
                    time.sleep(5)
        except KeyboardInterrupt:
            self.stop()

        # Debug code
        # while True:
        #     time.sleep(5)
        #     print("MAIN waiting for threads to die.  Current thread count = {0}".format(
        #         threading.active_count()
        #     ))
        #     not_me = 0
        #     for t in threading.enumerate():
        #         if t == threading.current_thread():
        #             continue
        #         if t.is_alive():
        #             not_me += 1
        #             print("  - {0} (daemon? {1}".format(
        #                 t.name,
        #                 t.daemon
        #             ))
        #     if not_me <= 0:
        #         break

    def _final_handler(self, _eid: EventId, _tid: ParticipantId, _obj: SystemShutdownFinalizeEvent) -> None:
        if self.__on_exit:
            self.__on_exit()
            self.__on_exit = None
        self.__running = False
        # with running_notice:
        #     running_notice.notify_all()
        print("Sent a wakeup for quit.")

    def _ctrl_c_handler(self, _signal: int, _frame: FrameType) -> None:
        self.stop()

    def stop(self) -> None:
        if self.__running:
            print("Starting forced system shutdown.  This may take a little while.")
            send_system_shutdown_request(self.__bus)

            # Debug Code
            # print("Living threads:")
            # for t in threading.enumerate():
            #     if t == threading.current_thread():
            #         continue
            #     if t.is_alive():
            #         print("  - {0} (daemon? {1}".format(
            #             t.name,
            #             t.daemon
            #         ))

    def _halt(self, _signal: int, _frame: FrameType) -> None:
        if self.__on_exit:
            self.__on_exit()
            self.__on_exit = None
        sys.exit(0)
