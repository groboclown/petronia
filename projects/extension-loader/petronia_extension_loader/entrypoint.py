"""Event streaming entrypoint."""

from typing import Sequence, Dict, Any
import traceback
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.extension.runner.main import extension_runner
from petronia_common.util import StdRet
from .event_router import create_startup_handlers
from .setup import initialize
from .messages import display_message


def extension_entrypoint(
        inp: BinaryReader, outp: BinaryWriter,
        _config: Dict[str, Any], args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint for event stream handling.
    Can be used for the in-memory launcher."""
    print("Starting up extension-loader with arguments {0}".format(args))
    try:
        init_res = initialize(*args)
        if init_res.has_error:
            display_message(init_res)
            return init_res

        res = extension_runner(
            inp, outp, *create_startup_handlers(),
        )
        print("Extension-loader completed running.")
        return res
    except BaseException as err:
        traceback.print_exception(type(err), err, err.__traceback__)
        raise err
