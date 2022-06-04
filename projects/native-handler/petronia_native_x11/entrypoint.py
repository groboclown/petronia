"""X11 Entrypoint."""

from typing import Sequence, Dict, Any
import threading
import concurrent.futures
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, join_errors
from petronia_ext_lib.runner.lookup import LookupEventRegistryContext
from petronia_ext_lib import logging
from petronia_native.common import user_messages
from .datastore.petronia_native_x11 import (
    ConfigurationState, EXTENSION_NAME,
)
from .configuration import ConfigurationStore
from . import runner, hook_types, wm_runner
from .datastore import petronia_native_x11 as native_state
from .hooks import keyboard_hook, window_hook


def extension_entrypoint(
        reader: BinaryReader,
        writer: BinaryWriter,
        config: Dict[str, Any],
        _args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint."""
    print("Loading X11")
    context = LookupEventRegistryContext(
        reader, writer, None, threading.RLock(),
        concurrent.futures.ThreadPoolExecutor(1),
    )

    # Bad configuration isn't a failure state.
    config_res = parse_config(config)

    phase_runner = get_phase_runner()
    setup_res = runner.start_server(
        context,
        # A bad config doesn't stop us.
        config_res.value or ConfigurationStore(None),
        lambda m: user_messages.display_message(m.debug()),
        phase_runner, get_hook_factories(),
    )

    if setup_res.has_error:
        # ... but report the bad configuration if setup fails.
        return StdRet.pass_error(join_errors(
            *config_res.error_messages(), *setup_res.error_messages(),
        ))
    # Print the config issues if setup fails.
    if config_res.has_error:
        user_messages.low_println(f"X11 Native configuration problem; config = {config}")
        logging.send_user_error(
            context, EXTENSION_NAME + ':configuration', config_res.valid_error,
            'invalid-configuration',
        )
    common_data, hooks = setup_res.result

    try:
        context.process_reader(native_state.EXTENSION_NAME)
    finally:
        return runner.stop_server(common_data, -1, phase_runner, hooks)


def parse_config(config: Dict[str, Any]) -> StdRet[ConfigurationStore]:
    """Parse the configuration dictionary."""
    if not config:
        print("X11 Native configuration is empty.")
        return StdRet.pass_ok(ConfigurationStore(None))
    return ConfigurationState.parse_data(config).map(ConfigurationStore)


def get_phase_runner() -> hook_types.PhaseRunner:
    """Get the phase runner."""
    return wm_runner.WindowManagerPhaseRunner()


def get_hook_factories() -> Sequence[hook_types.HookFactory]:
    """Get all the hook factories that might run."""
    return [
        keyboard_hook.keyboard_factory,
        window_hook.window_factory,
    ]
