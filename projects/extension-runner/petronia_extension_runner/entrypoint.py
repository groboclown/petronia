"""Event streaming entrypoint."""

from typing import Sequence
import traceback
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, RET_OK_NONE
from .setup import initialize, get_entrypoint_name, get_module_name, get_python_path
from .messages import display_message, low_println
from .importer import get_entrypoint_function


def entrypoint(args: Sequence[str], inp: BinaryReader, outp: BinaryWriter) -> StdRet[None]:
    """Standardized entrypoint for event stream handling.
    Can be used for the in-memory launcher."""
    low_println(f"Starting up extension-runner with arguments {args}")
    try:
        init_res = initialize(*args)
        if init_res.has_error:
            display_message(init_res)
            return init_res.forward()
        ext_args, config = init_res.result

        entrypoint_func_res = get_entrypoint_function(
            get_module_name(),
            get_entrypoint_name(),
            get_python_path(),
        )
        if entrypoint_func_res.has_error:
            display_message(entrypoint_func_res)
            return entrypoint_func_res.forward()

        func_res = entrypoint_func_res.result(
            inp, outp, config, ext_args,
        )
        if isinstance(func_res, StdRet) and func_res.has_error:
            display_message(func_res)
            return func_res

        low_println("Extension-runner completed running.")
    except BaseException as err:  # pylint:disable=broad-except
        traceback.print_exception(type(err), err, err.__traceback__)
        raise err
    return RET_OK_NONE
