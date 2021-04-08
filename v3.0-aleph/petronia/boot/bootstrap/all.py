
"""
The complete bootstrap algorithm.
"""

from ...base import EventBus
from ...base.logging import (
    log, TRACE, DEBUG,
)
from ...core.state.api import set_state
from ...defimpl.configuration.general import (
    STATE_ID_PLATFORM_EXTENSION_CONFIGURATION_STATE,
    PlatformExtensionConfigurationState,
)
from .args import (
    UserArguments,
    cmd_help,
)
from .platform import (
    get_platform_module,
    get_user_platform_module,
    get_platform_discovery_function,
    run_platform_main,
)
from .bus import create_bus
from .core import load_core_extensions
from .managed_queue import create_managed_queue
from .extension_loader import bootstrap_extension_extension
from .halt import bootstrap_halt


def bootstrap_petronia(args: UserArguments) -> EventBus:
    """
    Bootstrap all of Petronia.
    """
    log(DEBUG, bootstrap_petronia, 'Booting petronia.')
    if args.platform:
        log(TRACE, bootstrap_petronia, 'User-defined platform {0}', args.platform)
        platform_module = get_user_platform_module(args.platform)
    else:
        platform_module = get_platform_module()
    log(DEBUG, bootstrap_petronia, 'Using platform {0}', platform_module)
    data = get_platform_discovery_function(platform_module)()
    if args.is_help:
        cmd_help(data.arg_help)

    log(TRACE, bootstrap_petronia, 'Creating managed queue.')
    queue = create_managed_queue(data.event_queue_model)

    log(TRACE, bootstrap_petronia, 'Creating event bus.')
    bus = create_bus(queue.queue_function)
    log(TRACE, bootstrap_petronia, 'Loading core extensions.')
    preloaded_extensions = load_core_extensions(bus)

    log(TRACE, bootstrap_petronia, 'Loading the extension extension.')
    bootstrap_extension_extension(bus, data, args, preloaded_extensions)

    # TODO make timeout configurable.
    log(TRACE, bootstrap_petronia, 'Loading the halt manager.')
    bootstrap_halt(bus, queue, 120.0)

    config_dirs = list(args.config_dirs)
    config_dirs.extend(data.config_dirs)
    log(DEBUG, bootstrap_petronia, 'Recording information about configuration paths {0}', config_dirs)
    set_state(
        bus, STATE_ID_PLATFORM_EXTENSION_CONFIGURATION_STATE, PlatformExtensionConfigurationState,
        PlatformExtensionConfigurationState(config_dirs)
    )

    log(DEBUG, bootstrap_petronia, 'Petronia bootstrap complete.')
    return bus


def run_petronia(bus: EventBus, args: UserArguments) -> int:
    """
    Run the actual Petronia program.
    """
    if args.platform:
        platform_module = get_user_platform_module(args.platform)
    else:
        platform_module = get_platform_module()
    return run_platform_main(bus, platform_module)
