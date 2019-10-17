

from ...shell.control.root_layout import root_layout_factory
from ...shell.control.command_handler import command_handler_factory
from ...shell.control.active_portal_manager import active_portal_manager_factory
from ...shell.control.unowned_portal import unowned_portal_factory
from ..logger import logger_factory


def get_base_singleton_factories():
    return [
        logger_factory,
        command_handler_factory,
        root_layout_factory,
        active_portal_manager_factory,
        unowned_portal_factory,
    ]
