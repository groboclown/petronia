
"""
The complete bootstrap algorithm.
"""

from typing import Sequence
from petronia3.system.bus import EventBus
from petronia3.extensions.extensions.api import (
    send_request_load_extension_event
)
from .args import UserArguments
from .platform import (
    get_base_platform_module,
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
    if args.platform:
        platform_module = get_user_platform_module(args.platform)
    else:
        platform_module = get_base_platform_module()
    data = get_platform_discovery_function(platform_module)()

    queue = create_managed_queue(data.event_queue_model)

    bus = create_bus(queue.queue_function)
    preloaded_extensions = load_core_extensions(bus)

    # TODO allow the user or platform to change the extension implementation?
    bootstrap_extension_extension(bus, data, args, preloaded_extensions)

    for name in args.preboot_extensions:
        send_request_load_extension_event(bus, name)

    for name in data.platform_extensions:
        send_request_load_extension_event(bus, name)

    # TODO make timeout configurable.
    bootstrap_halt(bus, queue, 120.0)

    return bus


def run_petronia(bus: EventBus, args: UserArguments) -> int:
    """
    Run the actual Petronia program.
    """
    if args.platform:
        platform_module = get_user_platform_module(args.platform)
    else:
        platform_module = get_base_platform_module()
    return run_platform_main(bus, platform_module)
