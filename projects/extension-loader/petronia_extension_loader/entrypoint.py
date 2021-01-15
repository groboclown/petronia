"""Event streaming entrypoint."""

from typing import Sequence
import traceback
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, RET_OK_NONE
from .event_router import create_router
from .setup import initialize
from .messages import display_message


def entrypoint(args: Sequence[str], inp: BinaryReader, outp: BinaryWriter) -> StdRet[None]:
    """Standardized entrypoint for event stream handling.
    Can be used for the in-memory launcher."""
    print("Starting up extension-loader with arguments {0}".format(args))
    try:
        init_res = initialize(*args)
        if init_res.has_error:
            display_message(init_res)
            return init_res

        router_res = create_router(inp, outp)
        if router_res.has_error:
            display_message(router_res)
            return router_res.forward()

        router_res.result.handle_source()

        print("Extension-loader completed running.")
    except BaseException as err:
        traceback.print_exception(type(err), err, err.__traceback__)
        raise err
    return RET_OK_NONE
