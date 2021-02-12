"""Event streaming entrypoint."""

from typing import Sequence
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from .setup import initialize, get_entrypoint_name, get_module_name, get_python_path
from .messages import low_println
from .importer import get_entrypoint_function
from .defs import TRANSLATION_CATALOG


def entrypoint(args: Sequence[str], inp: BinaryReader, outp: BinaryWriter) -> StdRet[None]:
    """Standardized entrypoint for event stream handling.
    Can be used for the in-memory launcher."""
    low_println(f"Starting up extension-runner with arguments {args}")
    try:
        init_res = initialize(*args)
        if init_res.has_error:
            return init_res.forward()
        ext_args, config = init_res.result

        entrypoint_func_res = get_entrypoint_function(
            get_module_name(),
            get_entrypoint_name(),
            get_python_path(),
        )
        if entrypoint_func_res.has_error:
            return entrypoint_func_res.forward()

        func_res = entrypoint_func_res.result(
            inp, outp, config, ext_args,
        )

        low_println(f"Extension-runner completed running {get_module_name()}.")
        return func_res
    except BaseException as err:  # pylint:disable=broad-except
        return StdRet.pass_exception(
            TRANSLATION_CATALOG,
            _('Python extension {name} execution encountered an unhandled error'),
            err,
            name=get_module_name(),
        )
