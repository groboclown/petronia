"""
Entrypoint pattern for extensions started by extension-runner.
"""

from typing import Dict, Sequence, Any
import threading
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, RET_OK_NONE

STATE = [0]
LAUNCH_COUNT = [0]
RUNNING_CONDITION = threading.Condition()


def extension_entrypoint(
        inp: BinaryReader, outp: BinaryWriter,
        _config: Dict[str, Any], args: Sequence[str],
) -> StdRet[None]:
    """Starts the extension."""
    LAUNCH_COUNT[0] += 1
    run_count = LAUNCH_COUNT[0]
    print(f"memory extension: started {args} {run_count}")
    with RUNNING_CONDITION:
        assert STATE[0] == 0  # nosec
        STATE[0] = 1
        RUNNING_CONDITION.notify_all()
    # This must stay alive until it's explicitly stopped.  Otherwise, it can trigger
    # a restart.
    buff = inp.read(32)
    if len(buff) != 32:  # pragma no cover
        raise Exception(f'should have read 32 bytes; read {len(buff)}')  # pragma no cover
    print(f"memory extension: Sending back the event ({len(buff)} bytes).")
    outp.write(buff)

    with RUNNING_CONDITION:
        assert STATE[0] == 1  # nosec
        STATE[0] = 2
        RUNNING_CONDITION.notify_all()

    # No need to read the rest of the buffer, because this is a memory buffer.

    print(f"memory extension: stopping {args} {run_count}")

    return RET_OK_NONE


def wait_for_extension_started(timeout: float) -> bool:
    """Wait for the entrypoint to be run."""
    with RUNNING_CONDITION:
        return RUNNING_CONDITION.wait_for(is_extension_started, timeout=timeout)


def wait_for_extension_stopped(timeout: float) -> bool:
    """Wait for the entrypoint to be run."""
    with RUNNING_CONDITION:
        return RUNNING_CONDITION.wait_for(is_extension_stopped, timeout=timeout)


def is_extension_started() -> bool:
    """Is the entrypoint alive?"""
    with RUNNING_CONDITION:
        return STATE[0] != 0


def is_extension_running() -> bool:
    """Is the entrypoint alive?"""
    with RUNNING_CONDITION:
        return STATE[0] == 1


def is_extension_stopped() -> bool:
    """Is the entrypoint alive?"""
    with RUNNING_CONDITION:
        return STATE[0] == 2


def reset_extension() -> None:
    """Reset the extension state, used for test clean up."""
    STATE[0] = 0
