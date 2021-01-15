"""No-Op launcher entrypoint."""
from typing import Sequence
import threading
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, RET_OK_NONE

IS_ALIVE = [False]
LAUNCH_COUNT = [0]
RUNNING_CONDITION = threading.Condition()


def entrypoint(args: Sequence[str], inp: BinaryReader, _outp: BinaryWriter) -> StdRet[None]:
    """No-Op launcher."""
    LAUNCH_COUNT[0] += 1
    run_count = LAUNCH_COUNT[0]
    print(f"No-Op launcher {args} {run_count} started")
    with RUNNING_CONDITION:
        assert not IS_ALIVE[0]
        IS_ALIVE[0] = True
        RUNNING_CONDITION.notify_all()
    # This must stay alive until it's explicitly stopped.  Otherwise, it can trigger
    # a restart.
    res = b'x'
    while len(res) > 0:
        res = inp.read(1)
        print(f"No-Op launcher {args} {run_count}: read [{repr(res)}]")
    print(f"Stopping No-Op launcher {args} {run_count}")
    return RET_OK_NONE


def wait_for_launcher_alive(timeout: float) -> bool:
    """Wait for the entrypoint to be run."""
    with RUNNING_CONDITION:
        return RUNNING_CONDITION.wait_for(is_launcher_alive, timeout=timeout)


def is_launcher_alive() -> bool:
    """Is the entrypoint alive?"""
    with RUNNING_CONDITION:
        return IS_ALIVE[0]


def reset_launcher() -> None:
    """Reset the launcher state, used for test clean up."""
    IS_ALIVE[0] = False
