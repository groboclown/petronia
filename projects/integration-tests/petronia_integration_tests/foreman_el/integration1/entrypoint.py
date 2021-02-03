"""
Entrypoint pattern for extensions started by extension-runner.
"""

from typing import Dict, Sequence, Any
import threading
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, RET_OK_NONE

IS_ALIVE = [False]
LAUNCH_COUNT = [0]
RUNNING_CONDITION = threading.Condition()


def extension_entrypoint(
        inp: BinaryReader, _outp: BinaryWriter,
        config: Dict[str, Any], args: Sequence[str],
) -> StdRet[None]:
    """Starts the extension."""
    LAUNCH_COUNT[0] += 1
    run_count = LAUNCH_COUNT[0]
    print(f"integration-extension1 {args} {run_count} started")
    if 'started-file' in config:
        # This code is run in a separate process from the code-coverage tool,
        # so we can mark it as not covered.
        with open(config['started-file'], 'w') as f:  # pragma no cover
            f.write('started')  # pragma no cover
        print("Extension wrote started file defined in config.")  # pragma no cover
    else:
        with RUNNING_CONDITION:
            assert not IS_ALIVE[0]  # nosec
            IS_ALIVE[0] = True
            RUNNING_CONDITION.notify_all()
    # This must stay alive until it's explicitly stopped.  Otherwise, it can trigger
    # a restart.
    res = b'x'
    while len(res) > 0:
        res = inp.read(1)
        print(f"integration-extension1 {args} {run_count}: read [{repr(res)}]")
    print(f"Stopping integration-extension1 {args} {run_count}")
    return RET_OK_NONE


def wait_for_extension_alive(timeout: float) -> bool:
    """Wait for the entrypoint to be run."""
    with RUNNING_CONDITION:
        return RUNNING_CONDITION.wait_for(is_extension_alive, timeout=timeout)


def is_extension_alive() -> bool:
    """Is the entrypoint alive?"""
    with RUNNING_CONDITION:
        return IS_ALIVE[0]


def reset_extension() -> None:
    """Reset the extension state, used for test clean up."""
    IS_ALIVE[0] = False
