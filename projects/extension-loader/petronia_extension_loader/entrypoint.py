"""Event streaming entrypoint."""

from typing import Sequence, Dict, Any
from petronia_ext_lib.runner.main import extension_runner
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet
from .event_router import create_startup_handlers
from .setup import initialize
from .shared_state import ExtLoaderSharedState
from .messages import display_message, low_println, low_traceback
from .handlers import boot_extension_handler


def extension_entrypoint(
        inp: BinaryReader, outp: BinaryWriter,
        _config: Dict[str, Any], args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint for event stream handling.
    Can be used for the in-memory launcher."""
    boot_extension_handler.clear_boot_time_extensions()
    low_println(f"Starting up extension-loader with arguments {args}")
    try:
        init_res = initialize(*args)
        if init_res.has_error:
            display_message(init_res)
            return init_res

        state = ExtLoaderSharedState()
        res = extension_runner(
            args[0],
            inp, outp, state,  *create_startup_handlers(),
        )
        low_println("Extension-loader completed running.")
        return res
    except BaseException as err:  # pragma no cover
        # Encountering this code in unit tests means there's a bug, so code coverage
        # here doesn't make sense.
        low_traceback(err)  # pragma no cover
        raise err  # pragma no cover
