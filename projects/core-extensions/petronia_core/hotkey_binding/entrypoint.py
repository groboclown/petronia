"""Hotkey Binding Entrypoint."""

from typing import Sequence, Dict, Callable, Any

from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_errors, join_none_results, RET_OK_NONE
from petronia_ext_lib.datastore import register_datastore_update_parsers
from petronia_ext_lib.events import datastore
from petronia_ext_lib.extension_loader import send_register_listeners
from petronia_ext_lib.logging import send_user_error
from petronia_ext_lib.runner import EventRegistryContext
from petronia_ext_lib.runner.lookup import LookupEventRegistryContext
from . import shared_state, bind_handler, native_handler
from .events.ext import hotkey as native_hotkey
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

    # The hotkey binding is still single-threaded, but it requires
    # a more complex event bus handling than what simple provides us.
    context = LookupEventRegistryContext(reader, writer, None, None)

    # A failure from loading the configuration should not stop the extension from
    # starting.
    config_res = shared_state.load_configuration(config)

    res = join_none_results(
        bind_handler.register_bind_handlers(context),
        native_handler.register_native_handlers(
            context, bind_handler.create_on_hotkey_pressed_callback(context),
        ),
        push_config_to_native(context),
    )

    if res.has_error:
        return StdRet.pass_error(join_errors(
            # Report the configuration problems...
            *config_res.error_messages(), *res.error_messages(),
        ))

    if config_res.has_error:
        report_send_receive_problems(
            'hotkey-binding',
            send_user_error(
                context,
                hotkey_state.ConfigurationState.UNIQUE_TARGET_FQN,
                config_res.valid_error,
                'invalid-configuration',
            ),
        )

    context.process_reader(hotkey_state.EXTENSION_NAME)
    return RET_OK_NONE


def push_config_to_native(
        context: EventRegistryContext,
) -> StdRet[None]:
    """Send the current shared state to the native hotkey bind.
    This waits until the native hotkey is live."""
    return join_none_results(
        register_datastore_update_parsers(context),
        send_register_listeners(context, hotkey_state.EXTENSION_NAME, (
            (
                datastore.DataUpdatedEvent.FULL_EVENT_NAME,
                native_hotkey.HotkeyBindingsState.UNIQUE_TARGET_FQN,
            ),
        )),
        # on_init.wait_for_state(
        #     context,
        #     hotkey_state.EXTENSION_NAME + ":initialize",
        #     native_hotkey.HotkeyBindingsState.UNIQUE_TARGET_FQN,
        #     native_hotkey.HotkeyBindingsState.parse_data,
        #     create_bindings_initialize_callback(context),
        # ),
        native_handler.send_set_hotkey_bindings(
            context,
            shared_state.get_master_sequence().sequence_type,
            shared_state.get_master_sequence().sequence,
            shared_state.list_bound_keys(),
            lambda x, y: None,
        ),
    )


def create_bindings_initialize_callback(
        context: EventRegistryContext,
) -> Callable[[StdRet[native_hotkey.HotkeyBindingsState]], None]:
    """Create the callback when the hotkey binding is active."""
    def callback(_value: StdRet[native_hotkey.HotkeyBindingsState]) -> None:
        print("*************************")
        print("*************************")
        print("*************************")
        print("*************************")
        print("*************************")
        print("*************************")
        print("************ HOTKEY BIND SEND CONFIG")
        master_sequence = shared_state.get_master_sequence()
        report_send_receive_problems(
            'hotkey-binding',
            native_handler.send_set_hotkey_bindings(
                context,
                master_sequence.sequence_type, master_sequence.sequence,
                shared_state.list_bound_keys(),
                lambda x, y: None,
            ),
        )
    return callback
