"""Hotkey Binding Entrypoint."""

from typing import Sequence, Dict, Any
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_errors, RET_OK_NONE
from petronia_ext_lib.logging import send_user_error
from petronia_ext_lib.runner.lookup import LookupEventRegistryContext
from . import shared_state, bind_handler, native_handler
from .state import hotkey_binding as hotkey_state
from ..user_messages import report_send_receive_problems


def extension_entrypoint(
        reader: BinaryReader,
        writer: BinaryWriter,
        config: Dict[str, Any],
        _args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint."""
    shared_state.clear_data()

    # A failure from loading the configuration should not stop the extension from
    # starting.
    config_res = shared_state.load_configuration(config)

    # The hotkey binding is still single-threaded, but it requires
    # a more complex event bus handling than what simple provides us.
    context = LookupEventRegistryContext(reader, writer, None, None)

    res2 = bind_handler.register_bind_handlers(context)
    res3 = native_handler.register_native_handlers(
        context, bind_handler.create_on_hotkey_pressed_callback(context),
    )

    if res2.has_error or res3.has_error:
        return StdRet.pass_error(join_errors(
            # Report the configuration problems...
            *config_res.error_messages(), *res2.error_messages(), *res3.error_messages(),
        ))

    if config_res.has_error:
        report_send_receive_problems(
            'hotkey-binding',
            send_user_error(
                context,
                hotkey_state.ConfigurationState.UNIQUE_TARGET_FQN,
                config_res.valid_error,
                'invalid-configuration',
            )
        )

    context.process_reader()
    return RET_OK_NONE
